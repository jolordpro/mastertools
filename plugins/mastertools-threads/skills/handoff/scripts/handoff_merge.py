#!/usr/bin/env python3
"""Merge duplicate thread folders into the folders they continue.

Before 1.4.1 a thread resumed on another account got a new folder (often under the resume session's folder)
instead of sharing the old one. This finds each such duplicate and plans a merge into the original:
  - a top folder whose thread is named in an older folder's RESUMED.md merges into that older folder;
  - its child folders merge into the original's child with the same resume link or the same title,
    or, as a guess to confirm, the only original child whose title starts with the same words;
  - anything with no match moves in as a new child.
Files never overwrite: a name already in the original gets the session id added (AUTO-DIGEST-1a2b3c4d.md).

Usage: handoff_merge.py [--dir <handoff folder>]                 show the plan only
       handoff_merge.py --apply [--skip "<folder>" ...]           back up the handoff folder, then merge
"""
import os, re, shutil, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from handoff_common import (ID_FILE, add_id, handoff_dir, load_threads, read_ids, resume_links,  # noqa: E402
                            thread_folders)

args = sys.argv[1:]
apply = "--apply" in args
skips = [args[i + 1] for i, a in enumerate(args) if a == "--skip" and i + 1 < len(args)]
root = handoff_dir(args[args.index("--dir") + 1] if "--dir" in args else None)
threads = load_threads()
folders = thread_folders(root)
links = resume_links(root, threads)


def kids(folder):
    return [os.path.join(folder, d) for d in sorted(os.listdir(folder))
            if os.path.isfile(os.path.join(folder, d, ID_FILE))]


def stem(name):
    return re.split(r"\s*[-:·(]\s*", name.lower(), maxsplit=1)[0].strip()


plan = []  # (duplicate folder, target folder, how)


def match_children(dup, target):
    taken = set()
    for c in kids(dup):
        ids, name = read_ids(c), os.path.basename(c)
        options = [t for t in kids(target) if t not in taken]
        hit = next((links[i] for i in ids if links.get(i) in options), None)
        how = "resume link"
        if not hit:
            hit = next((t for t in options if os.path.basename(t) == name), None)
            how = "same title"
        if not hit:
            same = [t for t in options if stem(os.path.basename(t)) == stem(name)]
            hit, how = (same[0], "GUESS: title starts the same") if len(same) == 1 else (None, "")
        if hit:
            taken.add(hit)
            plan.append((c, hit, how))
            match_children(c, hit)
        else:
            plan.append((c, os.path.join(target, name), "moves in as a new child"))


for folder, ids in sorted(folders.items()):
    target = links.get(ids[0])
    if target and target != folder and not folder.startswith(target + os.sep) and not any(
            folder.startswith(d + os.sep) for d, _, _ in plan):
        plan.append((folder, target, "resume link"))
        match_children(folder, target)

plan = [p for p in plan if not any(p[0] == s or p[0].startswith(s + os.sep) or os.path.basename(p[0]) == s for s in skips)]
rel = lambda p: os.path.relpath(p, root)  # noqa: E731
if not plan:
    sys.exit("No duplicate folders found.")
for dup, target, how in plan:
    print(f"- {rel(dup)}\n    -> {rel(target)}  ({how})")
if not apply:
    print(f"\n{len(plan)} folders. Nothing moved. Rerun with --apply (and --skip \"<folder name>\" for any to leave alone).")
    sys.exit(0)

backup = f"{root.rstrip(os.sep)}-backup-{time.strftime('%Y%m%d-%H%M')}"
shutil.copytree(root, backup)
log = [f"# Folder merge {time.strftime('%Y-%m-%d %H:%M')}", "", f"Backup of the whole folder first: `{backup}`", ""]
for dup, target, how in plan:  # parents come before their children, so each child lands in a merged parent
    if not os.path.isdir(dup):
        continue
    if how == "moves in as a new child":
        shutil.move(dup, target)
        log.append(f"- moved `{rel(dup)}` -> `{rel(target)}` (new child)")
        continue
    for tid in read_ids(dup):
        add_id(target, tid)
    origin = read_ids(dup)[0][:8]
    for name in sorted(os.listdir(dup)):
        src = os.path.join(dup, name)
        if name == ID_FILE or os.path.isdir(src) and os.path.isfile(os.path.join(src, ID_FILE)):
            continue  # child thread folders are handled by their own plan line
        dest = os.path.join(target, name)
        if os.path.exists(dest):
            base, ext = os.path.splitext(name)
            dest = os.path.join(target, f"{base}-{origin}{ext}")
        shutil.move(src, dest)
    log.append(f"- merged `{rel(dup)}` -> `{rel(target)}` ({how})")
for dup, _, _ in reversed(plan):  # remove emptied duplicates, deepest first
    if os.path.isdir(dup) and set(os.listdir(dup)) <= {ID_FILE, ".DS_Store"} and not kids(dup):
        shutil.rmtree(dup)
open(os.path.join(root, f"MERGE-LOG-{time.strftime('%Y%m%d-%H%M')}.md"), "w", encoding="utf-8").write("\n".join(log) + "\n")
print(f"\nMerged {len(plan)} folders. Backup: {backup}")
