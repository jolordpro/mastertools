#!/usr/bin/env python3
"""Build START-HERE.md in the handoff folder: red flags first, then every thread as a tree, then open decisions.

Usage: handoff_rollup.py [handoff folder]
       handoff_rollup.py --print-dir          print the handoff folder and exit
       handoff_rollup.py --unresumed          list folders with a handoff and no RESUMED.md line, and exit

The folder, first match wins: the argument, $HANDOFF_DIR, the path written in
~/.config/handoff/dir, the folder this script sits in if it holds INDEX.md, ~/.claude/handoffs.

Threads come from folders holding a .thread-id file (HANDOFF.md, SUMMARY.md, AUTO-DIGEST.md or POINTER.md
inside). The tree comes from the desktop app's session records, falling back to folder nesting.
Older single-file handoffs listed in INDEX.md are shown at the end. Safe to rerun; it only rewrites START-HERE.md.

Red flags come from the newest of the folder's last CHANGELOG entry and its SUMMARY.md (one-line
`Red flags: 🔴 a 🔴 b` included). A flag naming a pid or a lock file is re-checked: a dead one is tagged
"(pid gone, checked <time>)" and keeps its level, unless the flag says it is running now; then it moves to
"Checked and gone". A thread whose transcript moved on after its last handoff write, or whose CHANGELOG is newer
than its SUMMARY.md, gets a 🔴 of its own; a CHANGELOG newer than RESUME-PROMPT.md gets a 🟠.
START-HERE passes through the secret redactor.
"""
import glob, os, re, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from handoff_common import (changelog, find_transcript, handoff_dir, load_threads, other_host, redact,  # noqa: E402
                            thread_folders)

args = [a for a in sys.argv[1:] if not a.startswith("--")]
root = handoff_dir(args[0] if args else None)
if "--print-dir" in sys.argv:
    print(root)
    sys.exit(0)
if not os.path.isdir(root):
    sys.exit(f"No handoff folder at {root}")
NOW = time.time()
CHECKED = time.strftime("%H:%M")
FLAGS_LINE = re.compile(r"^\s*[-*]?\s*\**red flags?\**\s*:\**\s*(.*)$", re.I)
PID = re.compile(r"\bpids?\s*:?\s*#?(\d{2,7})\b", re.I)
LOCK = re.compile(r"`?((?:/|~/)[^\s`]*?(?:\.lock|\.pid|LOCK)[^\s`]*)`?")


def parse_flags(text):
    """🔴 lines, including one-line `Red flags: 🔴 a 🔴 b` (split into one flag each)."""
    out = []
    for line in text.splitlines():
        s = line.strip()
        m = FLAGS_LINE.match(s)
        body = m.group(1) if m else (s[2:].strip() if s.startswith("- 🔴") else s if s.startswith("🔴") else "")
        if "🔴" not in body:
            continue
        out += ["🔴 " + part.strip(" ;,·-") for part in body.split("🔴")[1:] if part.strip(" ;,·-")]
    return out


def alive(pid):
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    except OSError:
        return False
    return True


RUNNING_NOW = re.compile(r"\b(running|live|rendering|still up|is up|alive|listening|serving|held|locked)\b", re.I)


def recheck(flag):
    """A flag naming a pid or lock file that no longer exists is tagged "(pid gone, checked <time>)" and keeps its level.
    Only a flag that says the process is running now (or the lock held) moves to "Checked and gone"."""
    pids = [int(p) for p in PID.findall(flag)]
    locks = [os.path.expanduser(l) for l in LOCK.findall(flag)]
    if not pids and not locks:
        return flag, True
    if any(alive(p) for p in pids) or any(os.path.exists(l) for l in locks):
        return flag, True
    tag = f" ({'pid' if pids else 'lock'} gone, checked {CHECKED})"
    if RUNNING_NOW.search(flag):
        return "⚪" + flag[1:] + tag, False
    return flag + tag, True


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


def mtime(path):
    try:
        return os.path.getmtime(path)
    except OSError:
        return 0


if "--unresumed" in sys.argv:
    waiting = [f for f in sorted(thread_folders(root))
               if (os.path.isfile(os.path.join(f, "HANDOFF.md")) or os.path.isfile(os.path.join(f, "SUMMARY.md")))
               and not read(os.path.join(f, "RESUMED.md")).strip()]
    print(f"{len(waiting)} folders with a handoff and no RESUMED.md line:")
    for f in waiting:
        print(f"- {os.path.relpath(f, root)}")
    sys.exit(0)


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
    elif has["POINTER.md"] and read(f["POINTER.md"]).count("Private thread"):
        status = "private: full handoff in its project folder (see POINTER.md), on this machine"
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
    flags = parse_flags(summary + "\n" + section(handoff, r"Transfer check"))
    if entries and entries[-1][0] > max(mtime(f["SUMMARY.md"]), mtime(f["HANDOFF.md"])):
        # The newest changelog entry is newer than the summary: its red-flag line is the current one.
        newest = [l for l in entries[-1][4].splitlines() if FLAGS_LINE.match(l.strip())]
        if newest:
            flags = parse_flags("\n".join(newest))
    if not flags and auto and not handoff:
        mine = auto.split("## Elsewhere on this Mac")[0].split("\n---\n")[0]
        flags = parse_flags(mine)
    flags = [recheck(fl) for fl in flags]
    written = max(mtime(f["HANDOFF.md"]), mtime(f["SUMMARY.md"]), mtime(os.path.join(folder, "CHANGELOG.md")))
    if (has["HANDOFF.md"] or has["SUMMARY.md"]) and not has["POINTER.md"]:
        trs = [t for t in (find_transcript(i) for i in ids) if t]
        newest_tr = max((mtime(t) for t in trs), default=0)
        if newest_tr - written > 3600:
            flags.append((f"🔴 worked past its handoff, {(newest_tr - written) / 3600:.0f} hours: its transcript moved on "
                          f"after the last handoff write; update the handoff or read the transcript tail", True))
        log = mtime(os.path.join(folder, "CHANGELOG.md"))
        # Update mode before 1.13 never refreshed RESUME-PROMPT.md, so an older one is a check, not a red flag.
        for name, mark in (("SUMMARY.md", "🔴"), ("RESUME-PROMPT.md", "🟠")):
            p = os.path.join(folder, name)
            if log and os.path.isfile(p) and log - mtime(p) > 300:
                flags.append((f"{mark} CHANGELOG.md is newer than {name}: refresh {name} before resuming", True))
    host = other_host(folder)
    if host:
        status += f" · 🟠 last written on another Mac ({host[0]}, {host[2]})"
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

red = [(it["title"], fl) for it in items.values() for fl, live in it["flags"] if live and not fl.startswith("🟠")]
check = [(it["title"], fl) for it in items.values() for fl, live in it["flags"] if live and fl.startswith("🟠")]
gone = [(it["title"], fl) for it in items.values() for fl, live in it["flags"] if not live]
out = ["# Start here: handoff roll-up", "",
       f"{len(items)} threads. Resume the top threads first; each one starts its own children.",
       "Rebuild this page any time: `python3 -I handoff_rollup.py`.", "", "## Red flags", ""]
out += [f"- **{t}**: {fl.lstrip('- ').strip()}" for t, fl in red] or ["🟢 None found."]
if check:
    out += ["", "To check:", ""] + [f"- **{t}**: {fl}" for t, fl in check]
if gone:
    out += ["", "Checked and gone (no action):", ""] + [f"- **{t}**: {fl}" for t, fl in gone]
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
open(dest, "w", encoding="utf-8").write(redact("\n".join(out) + "\n"))
print(f"Wrote {dest}: {len(items)} threads, {len(red)} red flags" + (f", {len(legacy)} older files" if legacy else ""))
