#!/usr/bin/env python3
"""cgk.py: front door to the CG knowledge base. Stdlib only. Run with python3 -I.

  cgk.py where                     where the knowledge base is, and its card counts
  cgk.py find <words...> [--all]   search (hands off to the base's own kb.py)
  cgk.py show <card-id...>         print whole cards
  cgk.py grade <card-id...>        evidence grade per card: EVIDENCE, TO-VERIFY or MISSING
  cgk.py grade --strict <ids...>   same, exit 1 unless every card is EVIDENCE
  cgk.py feeds                     the names cards list in `feeds:` (skills, checks, plan steps), with counts
  cgk.py feeds <name> [--all]      cards that feed that skill or check, by domain, with status·confidence

The location comes from $CG_KNOWLEDGE_DIR, else the first line of
~/.config/cg-knowledge/dir, else the cards bundled with this plugin at
${CLAUDE_PLUGIN_ROOT}/knowledge/. The path is never kept in this skill.
Exit 3 means the knowledge base is not reachable on this machine.
"""
import datetime
import os
import pathlib
import re
import subprocess
import sys

CONFIG = pathlib.Path.home() / ".config" / "cg-knowledge" / "dir"
NOT_REACHABLE = 3


def bundled():
    """The plugin's bundled knowledge folder: ${CLAUDE_PLUGIN_ROOT}/knowledge/.
    When the variable isn't set, the plugin root is found from this file
    (<plugin>/skills/cg-knowledge/scripts/cgk.py)."""
    plugin = os.environ.get("CLAUDE_PLUGIN_ROOT", "").strip()
    base = pathlib.Path(plugin).expanduser() if plugin else pathlib.Path(__file__).resolve().parents[3]
    return base / "knowledge"


def locate():
    raw = os.environ.get("CG_KNOWLEDGE_DIR", "").strip()
    source = "$CG_KNOWLEDGE_DIR"
    if not raw and CONFIG.is_file():
        lines = CONFIG.read_text(encoding="utf-8").splitlines()
        raw, source = (lines[0].strip() if lines else ""), str(CONFIG)
    if not raw:
        root = bundled()
        if (root / "scripts" / "kb.py").is_file() and (root / "cards").is_dir():
            return root, "the plugin's bundled knowledge"
        return None, f"not set: no $CG_KNOWLEDGE_DIR, no ~/.config/cg-knowledge/dir, and no bundled cards at {root}"
    root = pathlib.Path(raw).expanduser()
    if not (root / "scripts" / "kb.py").is_file() or not (root / "cards").is_dir():
        return None, f"{source} points at {root}, which has no scripts/kb.py and cards/"
    return root, source


def parse(path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta, m.group(2)


def card_path(root, cid):
    # ids are lowercase words and hyphens; anything else (a pasted list, a glob) is not a card
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]*", cid):
        return None
    hits = sorted((root / "cards").glob(f"*/{cid}.md"))
    return hits[0] if hits else None


def grade(meta, today):
    """EVIDENCE only for a full read (V) at medium or high confidence, in date, with no open conflict."""
    why = []
    if meta.get("status") != "V":
        why.append(f"status {meta.get('status', '?')} (summary or inference, not a full read)")
    if meta.get("confidence") not in ("medium", "high"):
        why.append(f"confidence {meta.get('confidence', '?')}")
    due = meta.get("recheck_by", "")
    if due and due < today:
        why.append(f"past recheck_by {due}")
    conflict = meta.get("conflicts", "none")
    if not conflict.startswith("none"):
        why.append(f"conflicts: {conflict}")
    return ("EVIDENCE", "") if not why else ("TO-VERIFY", "; ".join(why))


def feed_key(name):
    """'polish coach', 'Polish-Coach' and 'polish_coach' are one name."""
    return re.sub(r"[\s_-]+", "-", name.strip().strip("'\"").lower())


def feeds_of(meta):
    raw = meta.get("feeds", "").strip().strip("[]")
    return {feed_key(x) for x in raw.split(",") if x.strip()}


def main(argv):
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__)
        return 2
    root, source = locate()
    if root is None:
        print(f"Knowledge base not reachable on this machine ({source}).")
        print("Carry on without it, and say so once. Don't search the disk for it.")
        return NOT_REACHABLE
    cmd, rest = argv[0], argv[1:]

    if cmd == "where":
        counts = {}
        for p in (root / "cards").rglob("*.md"):
            st = parse(p)[0].get("status", "?")
            counts[st] = counts.get(st, 0) + 1
        total = sum(counts.values())
        print(f"{root}  (from {source})")
        print(f"{total} cards: " + ", ".join(f"{counts[k]} {k}" for k in sorted(counts)))
        return 0

    if cmd == "find" and rest:
        return subprocess.call([sys.executable, "-I", str(root / "scripts" / "kb.py"), "find", *rest])

    if cmd == "show" and rest:
        missing = 0
        for cid in rest:
            p = card_path(root, cid)
            if p is None:
                print(f"{cid}: no such card")
                missing += 1
                continue
            print(f"=== {p.relative_to(root)}")
            print(p.read_text(encoding="utf-8").rstrip())
            print()
        return 1 if missing else 0

    if cmd == "grade":
        strict = "--strict" in rest
        ids = [w for w in rest if w != "--strict"]
        if not ids:
            print(__doc__)
            return 2
        today = datetime.date.today().isoformat()
        all_ok = True
        for cid in ids:
            p = card_path(root, cid)
            if p is None:
                print(f"MISSING    {cid}")
                all_ok = False
                continue
            meta = parse(p)[0]
            verdict, why = grade(meta, today)
            all_ok = all_ok and verdict == "EVIDENCE"
            tag = f"{meta.get('status', '?')}·{meta.get('confidence', '?')}"
            print(f"{verdict:<10} {cid}  [{tag}]" + (f"  {why}" if why else ""))
        return 1 if (strict and not all_ok) else 0

    if cmd == "feeds":
        show_all = "--all" in rest
        names = [w for w in rest if w != "--all"]
        cards = [(p, parse(p)[0]) for p in sorted((root / "cards").rglob("*.md"))]
        if not names:
            counts = {}
            for _, meta in cards:
                for f in feeds_of(meta):
                    counts[f] = counts.get(f, 0) + 1
            for f, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[: None if show_all else 40]:
                print(f"{n:>6}  {f}")
            return 0
        want = feed_key(" ".join(names))
        hits = [(p, m) for p, m in cards if want in feeds_of(m)]
        if not hits:
            print(f"no card lists '{want}' in feeds. Run `cgk.py feeds` for the names in use.")
            return 1
        by_domain = {}
        for p, m in hits:
            by_domain.setdefault(p.parent.name, []).append((p, m))
        print(f"{len(hits)} cards feed '{want}': " + ", ".join(f"{d} {len(v)}" for d, v in sorted(by_domain.items(), key=lambda kv: -len(kv[1]))))
        if show_all:
            for d, rows in sorted(by_domain.items()):
                for p, m in rows:
                    print(f"  {p.stem}  [{m.get('status', '?')}·{m.get('confidence', '?')}]")
        else:
            print("Add --all to list them, or search inside them with `cgk.py find <words>`.")
        return 0

    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
