#!/usr/bin/env python3
"""Show a thread's place in the thread tree, its folder, and the signals used to judge how to resume it.

Usage:
  handoff_tree.py <transcript id | local_ id | title words>   the thread and every thread under it
  handoff_tree.py --active-days N                             every thread active in the last N days, as trees
  handoff_tree.py --tidy                                      move child folders inside their parent's folder
Options: --create (make missing folders), --dir <handoff folder>

Signals per thread: transcript size, compactions, last activity, children, fenced (regulated: nothing copied).
Mode per thread: WRITE (no handoff in its folder yet) or UPDATE (one exists: add a changelog entry, refresh the stale
parts), with the --since value for handoff_extract.py so an update reads only what is new.
"""
import os, shutil, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from handoff_common import (account_label, age, changelog, fenced, find_transcript, folder_for, handoff_dir,  # noqa: E402
                            id_folders, last_handoff, load_threads, read_ids, resolve, subtree, thread_folders)

args = sys.argv[1:]


def opt(name, default=None):
    if name in args:
        i = args.index(name)
        val = args[i + 1] if i + 1 < len(args) else default
        del args[i:i + 2]
        return val
    return default


def flag(name):
    if name in args:
        args.remove(name)
        return True
    return False


root = handoff_dir(opt("--dir"))
create = flag("--create")
tidy = flag("--tidy")
days = opt("--active-days")
threads = load_threads()


def compactions(path):
    n, tail = 0, b""
    with open(path, "rb") as f:
        while chunk := f.read(1 << 22):
            buf = tail + chunk
            n += buf.count(b'"isCompactSummary":true')
            tail = buf[-40:]
            n -= tail.count(b'"isCompactSummary":true')
    return n


def line(tid, depth, known):
    t = threads[tid]
    tr = find_transcript(tid)
    size = f"{os.path.getsize(tr) / 1e6:.1f} MB, {compactions(tr)} compactions" if tr else "transcript not found"
    fence = fenced(t)
    folder = folder_for(root, threads, tid, create, known)
    pad = "  " * depth
    flags = " · ARCHIVED" if t["archived"] else ""
    flags += f" · FENCED ({fence}): nothing copied" if fence else ""
    out = (f"{pad}- {t['title']}{flags}\n{pad}  transcript {tid} · {account_label(t['account'])} · {size} · "
           f"active {age(t['last'])} · {len(t['children'])} children\n"
           f"{pad}  folder: {folder}{'' if os.path.isdir(folder) else ' (not created yet)'}")
    if os.path.isfile(os.path.join(folder, "HANDOFF.md")):
        since = last_handoff(folder, tid)
        entries = changelog(folder)
        shared = len(read_ids(folder)) - 1
        out += (f"\n{pad}  mode: UPDATE · {len(entries)} changelog entries · shared with {shared} other session(s) · "
                + (f"--since {time.strftime('%Y-%m-%dT%H:%M', time.gmtime(since))}Z" if since else "whole transcript is new"))
    else:
        out += f"\n{pad}  mode: WRITE (no HANDOFF.md yet)"
    return out


if tidy:
    # A folder moves only by its original thread's parent. A resumed thread's parent is the resume session,
    # so following it would pull the folder out of place.
    moved = 0
    for path, ids in sorted(thread_folders(root).items(), key=lambda kv: kv[0].count(os.sep)):
        known = id_folders(root)
        path = known.get(ids[0], path)
        t = threads.get(ids[0])
        if not t or t["parent"] not in known:
            continue
        want_parent = known[t["parent"]]
        if os.path.dirname(path) != want_parent and not want_parent.startswith(path + os.sep):
            dest = os.path.join(want_parent, os.path.basename(path))
            if os.path.exists(dest):
                print(f"skip (exists): {dest}")
                continue
            shutil.move(path, dest)
            moved += 1
            print(f"moved: {path}\n   -> {dest}")
    print(f"{moved} folders moved")
    sys.exit(0)

known = id_folders(root)
if days:
    cutoff = time.time() - float(days) * 86400
    active = {tid for tid, t in threads.items() if t["last"] >= cutoff and not t["archived"]}
    # Show each active thread under its highest ancestor, so the tree stays whole.
    tops = set()
    for tid in active:
        top = tid
        while threads[top]["parent"] in threads:
            top = threads[top]["parent"]
        tops.add(top)
    print(f"{len(active)} threads active in the last {days} days, in {len(tops)} trees\n")
    for top in sorted(tops, key=lambda x: -threads[x]["last"]):
        for tid, depth in subtree(threads, top):
            if tid in active or any(c in active for c, _ in subtree(threads, tid)):
                print(line(tid, depth, known))
    sys.exit(0)

if not args:
    sys.exit(__doc__)
tid = resolve(threads, args[0])
if not tid:
    sys.exit(f"No desktop session record matches {args[0]!r}. A thread started outside the desktop app has no tree; use its transcript id with handoff_extract.py.")
t = threads[tid]
if t["parent"] in threads:
    print(f"Parent: {threads[t['parent']]['title']} (transcript {t['parent']})")
elif t["parent_title"]:
    print(f"Parent: {t['parent_title']} (no record on this machine)")
else:
    print("Parent: none (top-level thread)")
for sub, depth in subtree(threads, tid):
    print(line(sub, depth, known))
