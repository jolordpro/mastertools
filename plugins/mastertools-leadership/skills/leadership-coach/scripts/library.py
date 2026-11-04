#!/usr/bin/env python3
"""library.py: front door to the Leadership RAG Library. Stdlib only. Run with python3 -I.

  library.py where          where the library is, its version and page count
  library.py set <folder>   check a folder is the library, then save it as this machine's location
  library.py check          every section pointer (§2.2, § Path K, ...) in the leadership skills
                            must land on a real heading or passage in the page it names

The location comes from $LEADERSHIP_LIBRARY_DIR, else the first line of
~/.config/leadership-library/dir, else the copy bundled with this plugin (library/).
The path is never kept in these skills.
Exit 3 means the library is not reachable on this machine. Exit 1 means `check` found
a pointer that no longer lands.
"""
import json
import os
import pathlib
import re
import sys

CONFIG = pathlib.Path.home() / ".config" / "leadership-library" / "dir"
NOT_REACHABLE = 3
SKILLS = ("leadership-coach", "cascade-diagnostic", "containment-decision",
          "capacity-audit", "judgment-drift-check")
REQUIRED = ("CLAUDE.md", "00_START_HERE.md", "MANIFEST.json")
# skills/leadership-coach/scripts/library.py -> the plugin root holds library/
BUNDLED = pathlib.Path(__file__).resolve().parents[3] / "library"


def problems(root):
    """What makes this folder not the library; empty when it is."""
    missing = [n for n in REQUIRED if not (root / n).is_file()]
    if not (root / "Core_Canonical_Super_Pages").is_dir():
        missing.append("Core_Canonical_Super_Pages/")
    if missing:
        return missing
    try:
        manifest = json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))
        pages = manifest["core_super_pages"]
    except (ValueError, KeyError) as e:
        return [f"MANIFEST.json unreadable ({e})"]
    return [p["file"] for p in pages if not (root / p["file"]).is_file()]


def locate():
    raw = os.environ.get("LEADERSHIP_LIBRARY_DIR", "").strip()
    source = "$LEADERSHIP_LIBRARY_DIR"
    if not raw and CONFIG.is_file():
        lines = CONFIG.read_text(encoding="utf-8").splitlines()
        raw, source = (lines[0].strip() if lines else ""), str(CONFIG)
    if not raw:
        if not problems(BUNDLED):
            return BUNDLED, "the copy bundled with this plugin"
        return None, "not set: no $LEADERSHIP_LIBRARY_DIR, no ~/.config/leadership-library/dir, no bundled copy"
    root = pathlib.Path(raw).expanduser()
    bad = problems(root)
    if bad:
        return None, f"{source} points at {root}, which is missing: {', '.join(bad[:4])}"
    return root, source


def manifest(root):
    return json.loads((root / "MANIFEST.json").read_text(encoding="utf-8"))


def cmd_where():
    root, source = locate()
    if root is None:
        print(f"Leadership library not reachable on this machine ({source}).")
        return NOT_REACHABLE
    m = manifest(root)
    print(root)
    print(f"version {m.get('package_version', '?')}, {len(m['core_super_pages'])} Super Pages "
          f"(from {source})")
    return 0


def cmd_set(folder):
    root = pathlib.Path(folder).expanduser().resolve()
    bad = problems(root)
    if bad:
        print(f"Not the library: {root} is missing {', '.join(bad[:4])}. Nothing saved.")
        return 1
    CONFIG.parent.mkdir(parents=True, exist_ok=True)
    CONFIG.write_text(str(root) + "\n", encoding="utf-8")
    print(f"Saved {root} to {CONFIG}")
    return 0


# ---- check: section pointers -------------------------------------------------------------

HEADING = re.compile(r"^#{1,6}\s+§?(\d+(?:\.\d+)*)\.?(?=\s|$)")
DOC_ID = re.compile(r"\b([A-Z]+(?:-[A-Z]+)?-\d{3})\b")
FILE = re.compile(r"\b((?:\d\d_)?[A-Za-z][A-Za-z_]*\.md)\b")
ALIAS_LINE = re.compile(r"^([A-Z]+)\s*=\s*<REPO>/(\S+\.md)\s*$")
SECTION = re.compile(r"§\s?(\d+(?:\.\d+)*)|§\s*(Path\s+[A-Z])")
OF_DOC = re.compile(r"^\s+of\s+(?:the\s+)?`?([A-Za-z0-9_<>/.-]+?)`?(?=[\s.,;)]|$)")


def headings(path):
    out = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = HEADING.match(line)
        if m:
            out.add(m.group(1))
    return out


class Pages:
    def __init__(self, root):
        self.root = root
        self.ids = {p["id"]: root / p["file"] for p in manifest(root)["core_super_pages"]}
        self._cache = {}

    def by_name(self, token, aliases):
        token = token.replace("<REPO>/", "")
        if token in aliases:
            return self.root / aliases[token]
        if token in self.ids:
            return self.ids[token]
        for base in (self.root, self.root / "Core_Canonical_Super_Pages"):
            if (base / token).is_file():
                return base / token
        return None

    def heads(self, path):
        if path not in self._cache:
            self._cache[path] = headings(path)
        return self._cache[path]


def doc_tokens(text, pages, aliases):
    """(position, page path) for every document named in the text, in order."""
    found = []
    for rx in (DOC_ID, FILE):
        for m in rx.finditer(text):
            p = pages.by_name(m.group(1), aliases)
            if p:
                found.append((m.start(), p))
    for name in aliases:
        for m in re.finditer(r"`%s`|\b%s\b" % (name, name), text):
            found.append((m.start(), pages.root / aliases[name]))
    return sorted(found, key=lambda t: t[0])


def check_skill(skill_md, pages):
    """Broken pointers in one SKILL.md, as 'line N: §x -> page: why' strings."""
    text = skill_md.read_text(encoding="utf-8")
    aliases = {}
    for line in text.splitlines():
        m = ALIAS_LINE.match(line.strip())
        if m:
            aliases[m.group(1)] = m.group(2)
    default = pages.root / next(iter(aliases.values())) if aliases else None
    errors, n = [], 0
    # A paragraph is the unit: a page named earlier in it is what a later bare § points into.
    for para in re.split(r"\n\s*\n", text):
        start = text.index(para)
        docs = doc_tokens(para, pages, aliases)
        for m in SECTION.finditer(para):
            n += 1
            line_no = text.count("\n", 0, start + m.start()) + 1
            label = "§" + (m.group(1) or m.group(2))
            after = OF_DOC.match(para[m.end():])
            before = para[max(0, m.start() - 16):m.start()]
            if re.search(r"Super Page'?s?\s*$", before) and m.group(1):
                targets = list(pages.ids.values())  # "each Super Page's §4": every page
            elif after and pages.by_name(after.group(1), aliases):
                targets = [pages.by_name(after.group(1), aliases)]
            else:
                prior = [p for pos, p in docs if pos < m.start()]
                target = prior[-1] if prior else default
                if target is None:
                    errors.append(f"line {line_no}: {label} names no page")
                    continue
                targets = [target]
            for page in targets:
                if m.group(2):  # § Path K: the passage must exist, not a heading
                    if m.group(2) not in page.read_text(encoding="utf-8"):
                        errors.append(f"line {line_no}: {label} -> {page.name}: not found")
                elif m.group(1) not in pages.heads(page):
                    errors.append(f"line {line_no}: {label} -> {page.name}: no such heading")
    return errors, n


def cmd_check(skills_dir=None):
    root, source = locate()
    if root is None:
        print(f"Leadership library not reachable on this machine ({source}).")
        return NOT_REACHABLE
    skills_dir = pathlib.Path(skills_dir) if skills_dir else pathlib.Path(__file__).resolve().parents[2]
    pages, bad, total = Pages(root), 0, 0
    for name in SKILLS:
        skill_md = skills_dir / name / "SKILL.md"
        if not skill_md.is_file():
            print(f"{name}: SKILL.md missing")
            bad += 1
            continue
        errors, n = check_skill(skill_md, pages)
        total += n
        for e in errors:
            print(f"{name}: {e}")
        bad += len(errors)
    print(f"{total} pointers checked, {bad} broken")
    return 1 if bad else 0


def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv[0] == "where":
        return cmd_where()
    if argv[0] == "set" and len(argv) == 2:
        return cmd_set(argv[1])
    if argv[0] == "check":
        return cmd_check(argv[1] if len(argv) > 1 else None)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
