#!/usr/bin/env python3
"""Move older single-file handoffs (<project>--<thread>.md at the handoff folder's root, listed in INDEX.md)
into thread folders: <title>/HANDOFF.md, with a matching <project>--<thread>/ folder moved to <title>/files/.
Paths inside every moved handoff are rewritten, and a new INDEX.md line is appended for each.

Usage: handoff_migrate.py [--dir <handoff folder>] [--dry-run]
Safe to rerun: a flat file written again later replaces the folder's HANDOFF.md if it is newer.
"""
import os, shutil, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from handoff_common import folder_for, handoff_dir, id_folders, load_threads, thread_folders  # noqa: E402

args = sys.argv[1:]
dry = "--dry-run" in args
root = handoff_dir(args[args.index("--dir") + 1] if "--dir" in args else None)
index = os.path.join(root, "INDEX.md")
if not os.path.isfile(index):
    sys.exit(f"No INDEX.md in {root}")

threads = load_threads()
latest = {}  # transcript id -> (cells, path); a later line wins
for line in open(index, encoding="utf-8"):
    if not line.startswith("- "):
        continue
    cells = [c.strip() for c in line[2:].split("|")]
    path = next((c for c in cells if c.endswith(".md") and "/" in c), None)
    tid = next((c.split()[1] for c in cells if c.startswith("transcript ") and len(c.split()) > 1), None)
    if not tid:  # early lines named the desktop session (local_…) instead
        local = next((c for c in cells if c.startswith("local_")), None)
        tid = next((t["id"] for t in threads.values() if local and t["local"] == local), None)
    if path and tid:
        latest[tid] = (cells, path)

known = id_folders(root)
moves = []
for tid, (cells, path) in latest.items():
    flat = path if os.path.isfile(path) and os.path.dirname(path) == root else None
    if not flat:
        continue
    folder = folder_for(root, threads, tid, create=not dry, _known=known)
    dest = os.path.join(folder, "HANDOFF.md")
    if os.path.isfile(dest) and os.path.getmtime(dest) >= os.path.getmtime(flat):
        print(f"skip, folder copy is newer: {os.path.basename(flat)}")
        continue
    stem_dir = flat[:-3]
    moves.append((tid, cells, flat, dest, stem_dir if os.path.isdir(stem_dir) else None, folder))

renames = []
for tid, cells, flat, dest, stem_dir, folder in moves:
    renames.append((flat, dest))
    if stem_dir:
        renames.append((stem_dir, os.path.join(folder, "files")))

for tid, cells, flat, dest, stem_dir, folder in moves:
    print(f"{os.path.basename(flat)}\n  -> {os.path.relpath(dest, root)}" + (f"\n  + {os.path.basename(stem_dir)}/ -> files/" if stem_dir else ""))
    if dry:
        continue
    os.makedirs(folder, exist_ok=True)
    shutil.move(flat, dest)
    if stem_dir:
        target = os.path.join(folder, "files")
        if os.path.isdir(target):
            for name in os.listdir(stem_dir):
                shutil.move(os.path.join(stem_dir, name), os.path.join(target, name))
            os.rmdir(stem_dir)
        else:
            shutil.move(stem_dir, target)

if not dry and moves:
    # Rewrite old paths in every handoff file now in a thread folder (children and parents point at each other).
    for folder in thread_folders(root):
        for dirpath, _, files in os.walk(folder):
            for name in files:
                if not name.endswith(".md"):
                    continue
                p = os.path.join(dirpath, name)
                text = open(p, encoding="utf-8").read()
                new = text
                for old, nw in sorted(renames, key=lambda r: -len(r[0])):
                    new = new.replace(old, nw)
                if new != text:
                    open(p, "w", encoding="utf-8").write(new)
    with open(index, "a", encoding="utf-8") as f:
        for tid, cells, flat, dest, stem_dir, folder in moves:
            rest = [c if c != flat else dest for c in cells[1:]]
            f.write(f"- {time.strftime('%Y-%m-%d')} | " + " | ".join(rest) + " | moved into a thread folder\n")
print(f"{len(moves)} handoffs {'would move' if dry else 'moved'}")
