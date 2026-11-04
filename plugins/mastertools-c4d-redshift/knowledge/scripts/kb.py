#!/usr/bin/env python3
"""kb.py: find, index, check and stale for the knowledge base. Stdlib only.

  python3 -I kb.py find <words...> [--all]   cards ranked by word hits (title and tags count triple)
  python3 -I kb.py index                     rebuild INDEX.md from card front matter
  python3 -I kb.py check                     list cards missing required fields; exit 1 if any
  python3 -I kb.py stale [--today YYYY-MM-DD] cards past recheck_by
"""
import datetime
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = ROOT / "cards"
REQUIRED = ["id", "title", "domain", "status", "confidence", "decay", "read", "recheck_by", "sources"]


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


def cards():
    for p in sorted(CARDS.rglob("*.md")):
        meta, body = parse(p)
        yield p, meta, body


def cmd_find(words, show_all=False):
    # split quoted phrases too: find "a b c" used to search for the whole phrase and miss everything
    words = [w.lower() for arg in words for w in arg.split()]
    scored = []
    for p, meta, body in cards():
        head = (meta.get("title", "") + " " + meta.get("tags", "") + " " + meta.get("id", "")).lower()
        rest = body.lower()
        hits = sum(3 * head.count(w) + rest.count(w) for w in words)
        matched = sum(1 for w in words if w in head or w in rest)
        if matched:
            scored.append((matched, hits, p, meta, body))
    scored.sort(key=lambda s: (-s[0], -s[1]))
    if not scored:
        print("Nothing in the knowledge base for: " + " ".join(words))
        return 1
    for matched, hits, p, meta, body in scored[: None if show_all else 8]:
        print(f"{meta.get('id', p.stem)} · {meta.get('status', '?')} · {meta.get('confidence', '?')} · recheck {meta.get('recheck_by', '?')}")
        print(f"  {meta.get('title', '')}")
        first = next((l for l in body.splitlines() if l.strip()), "")
        print(f"  {first[:160]}")
        print(f"  {p.relative_to(ROOT)}  ({matched}/{len(words)} words)")
    return 0


def cmd_index():
    lines = ["# Knowledge base index", "", "One line per card. Rebuilt by `scripts/kb.py index`; don't edit by hand.", ""]
    n = 0
    for p, meta, _ in cards():
        lines.append(f"- [{meta.get('id', p.stem)}]({p.relative_to(ROOT)}) · {meta.get('domain', '?')} · "
                     f"{meta.get('status', '?')} · {meta.get('title', '')} · tags {meta.get('tags', '[]')}")
        n += 1
    (ROOT / "INDEX.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"INDEX.md rebuilt: {n} cards")
    return 0


def cmd_check():
    bad = 0
    ids = {}
    for p, meta, _ in cards():
        missing = [k for k in REQUIRED if not meta.get(k)]
        cid = meta.get("id")
        if cid in ids:
            print(f"{p.relative_to(ROOT)}: duplicate id {cid} (also {ids[cid]})")
            bad += 1
        ids[cid] = p.relative_to(ROOT)
        if missing:
            print(f"{p.relative_to(ROOT)}: missing {', '.join(missing)}")
            bad += 1
        if meta.get("status") not in ("V", "V2", "U"):
            print(f"{p.relative_to(ROOT)}: status must be V, V2 or U")
            bad += 1
    print(f"{len(ids)} cards checked, {bad} problems")
    return 1 if bad else 0


def cmd_stale(today=None):
    today = today or datetime.date.today().isoformat()
    n = 0
    for p, meta, _ in cards():
        due = meta.get("recheck_by", "")
        if due and due < today:
            print(f"{meta.get('id', p.stem)} · due {due} · {meta.get('title', '')}")
            n += 1
    print(f"{n} cards past their re-check date (today {today})")
    return 0


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    cmd, rest = argv[0], argv[1:]
    if cmd == "find" and rest:
        return cmd_find([w for w in rest if w != "--all"], "--all" in rest)
    if cmd == "index":
        return cmd_index()
    if cmd == "check":
        return cmd_check()
    if cmd == "stale":
        today = rest[rest.index("--today") + 1] if "--today" in rest else None
        return cmd_stale(today)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
