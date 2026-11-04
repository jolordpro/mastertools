#!/usr/bin/env python3
"""Build START-HERE.md in the handoff folder: red flags first, then every thread as a tree, then open decisions.

Usage: handoff_rollup.py [handoff folder]
       handoff_rollup.py --print-dir          print the handoff folder and exit

The folder, first match wins: the argument, $HANDOFF_DIR, the path written in
~/.config/handoff/dir, the folder this script sits in if it holds INDEX.md, ~/.claude/handoffs.

Threads come from folders holding a .thread-id file (HANDOFF.md, SUMMARY.md, AUTO-DIGEST.md or POINTER.md
inside). The tree comes from the desktop app's session records, falling back to folder nesting.
Older single-file handoffs listed in INDEX.md are shown at the end. Safe to rerun; it only rewrites START-HERE.md.
"""
import glob, os, re, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from handoff_common import changelog, handoff_dir, load_threads, thread_folders  # noqa: E402

args = [a for a in sys.argv[1:] if a != "--print-dir"]
root = handoff_dir(args[0] if args else None)
if "--print-dir" in sys.argv:
    print(root)
    sys.exit(0)
if not os.path.isdir(root):
    sys.exit(f"No handoff folder at {root}")


def read(path):
    try:
        return open(path, encoding="utf-8").read()
    except OSError:
        return ""


def section(text, pattern):
    m = re.search(rf"^##\s*\d*\.?\s*{pattern}[^\n]*\n(.*?)(?=^##\s|\Z)", text, re.S | re.M | re.I)
    return m.group(1).strip() if m else ""


def when(path):
    return time.strftime("%b %d %H:%M", time.localtime(os.path.getmtime(path)))


records = load_threads()
items = {}
for folder, ids in thread_folders(root).items():
    # One folder can hold a thread and the sessions that resumed it on other accounts. The original thread's
    # record places it in the tree; the newest session's record gives the current title.
    tid = ids[0]
    newest = max((records[i] for i in ids if i in records), key=lambda r: r["last"], default={})
    f = {n: os.path.join(folder, n) for n in ("HANDOFF.md", "SUMMARY.md", "AUTO-DIGEST.md", "POINTER.md")}
    has = {n: os.path.isfile(p) for n, p in f.items()}
    digests = sorted(glob.glob(os.path.join(glob.escape(folder), "AUTO-DIGEST*.md")), key=os.path.getmtime)
    if digests:  # the newest session's backup, when the folder is shared by sessions on more than one account
        f["AUTO-DIGEST.md"], has["AUTO-DIGEST.md"] = digests[-1], True
    handoff, summary, auto = read(f["HANDOFF.md"]), read(f["SUMMARY.md"]), read(f["AUTO-DIGEST.md"])
    rec = records.get(tid, {})
    title = newest.get("title") or rec.get("title") or os.path.basename(folder)
    resumed = read(os.path.join(folder, "RESUMED.md")).strip().splitlines()
    entries = changelog(folder)
    resumed_at = os.path.getmtime(os.path.join(folder, "RESUMED.md")) if resumed else 0
    if entries and entries[-1][0] >= resumed_at - 60:
        when_, acct, _, _, _ = entries[-1]
        status = f"updated {time.strftime('%b %d %H:%M', time.localtime(when_))} on {acct} · {len(entries)} changelog entries"
    elif resumed:
        status = "resumed: " + resumed[-1].lstrip("- ")
    elif has["POINTER.md"]:
        status = "fenced: nothing copied, resume from the local transcript"
    elif has["HANDOFF.md"]:
        status = f"handoff written {when(f['HANDOFF.md'])}"
        if has["AUTO-DIGEST.md"] and os.path.getmtime(f["AUTO-DIGEST.md"]) > os.path.getmtime(f["HANDOFF.md"]) + 3600:
            status += f" · auto-backup newer ({when(f['AUTO-DIGEST.md'])}): work moved on since the handoff"
    elif has["AUTO-DIGEST.md"]:
        status = f"auto-backup only, {when(f['AUTO-DIGEST.md'])}: no handoff written yet"
    else:
        status = "⚪ pending: no handoff or backup yet"
    m = re.search(r"^\s*[-*]?\s*\**Next[^:\n]*:\**\s*(.+)$", summary or section(handoff, r"Where we stopped"), re.M | re.I)
    nxt = m.group(1).strip() if m else ""
    flags = [l.strip() for l in (summary + "\n" + section(handoff, r"Transfer check")).splitlines() if l.strip().startswith(("🔴", "- 🔴"))]
    if not flags and auto and not handoff:
        mine = auto.split("## Elsewhere on this Mac")[0].split("\n---\n")[0]
        flags = [l.strip() for l in mine.splitlines() if l.strip().startswith("🔴")]
    items[tid] = dict(folder=folder, title=title, status=status, next=nxt, flags=flags,
                      decisions=section(handoff, r"Open decisions"), parent=rec.get("parent"))

# Parent: the session record first, then the nearest enclosing thread folder.
by_folder = {v["folder"]: k for k, v in items.items()}
id_of = {i: tid for f, ids in thread_folders(root).items() for i in ids for tid in [ids[0]]}
for it in items.values():
    it["parent"] = id_of.get(it["parent"], it["parent"])
for tid, it in items.items():
    if it["parent"] not in items:
        up, it["parent"] = os.path.dirname(it["folder"]), None
        while up.startswith(root) and up != root:
            if up in by_folder:
                it["parent"] = by_folder[up]
                break
            up = os.path.dirname(up)
children = {}
for tid, it in sorted(items.items(), key=lambda kv: kv[1]["title"].lower()):
    children.setdefault(it["parent"], []).append(tid)

red = [(it["title"], fl) for it in items.values() for fl in it["flags"]]
out = ["# Start here: handoff roll-up", "",
       f"{len(items)} threads. Resume the top threads first; each one starts its own children.",
       "Rebuild this page any time: `python3 -I handoff_rollup.py`.", "", "## Red flags", ""]
out += [f"- **{t}**: {fl.lstrip('- ').strip()}" for t, fl in red] or ["🟢 None found."]
out += ["", "## Threads", ""]


def walk(key, depth):
    for tid in children.get(key, []):
        it = items[tid]
        pad = "  " * depth
        out.append(f"{pad}- **{it['title']}** · {it['status']}")
        if it["next"]:
            out.append(f"{pad}  next: {it['next']}")
        out.append(f"{pad}  folder: `{it['folder']}`")
        walk(tid, depth + 1)


walk(None, 0)

legacy, index = [], os.path.join(root, "INDEX.md")
if os.path.isfile(index):
    seen = set()
    for line in reversed(open(index, encoding="utf-8").read().splitlines()):
        cells = [c.strip() for c in line[2:].split("|")] if line.startswith("- ") else []
        path = next((c for c in cells if c.endswith(".md") and "/" in c), None)
        tid = next((c.split()[1] for c in cells if c.startswith("transcript ")), None)
        if not path or path in seen or (tid and tid in items) or not os.path.isfile(path) or os.path.dirname(path) in by_folder:
            continue
        seen.add(path)
        legacy.append(f"- **{cells[2]}** ({cells[1]}) · {cells[0]}\n  file: `{path}`")
if legacy:
    out += ["", "## Older single-file handoffs", ""] + legacy[::-1]

out += ["", "## Open decisions for the user (from every handoff)", ""]
for it in items.values():
    if it["decisions"]:
        out.append(f"### {it['title']}\n\n{it['decisions']}\n")

dest = os.path.join(root, "START-HERE.md")
open(dest, "w", encoding="utf-8").write("\n".join(out) + "\n")
print(f"Wrote {dest}: {len(items)} threads, {len(red)} red flags" + (f", {len(legacy)} older files" if legacy else ""))
