#!/usr/bin/env python3
"""Auto-backup: refresh a thread's AUTO-DIGEST.md after a turn. Runs from an async Stop hook and uses no plan usage.

Off unless ~/.config/handoff/auto exists (create it to opt in on a machine).
Reads the hook's JSON on stdin (session_id is the transcript id). Throttled to once per 30 minutes per thread.
Skips threads without a desktop session record and transcripts under 150 KB.
A fenced (regulated) thread gets only POINTER.md: nothing from its transcript is copied.
A private thread (`private: <term>` in the fence file) keeps its backup in its project folder
(<project>/.handoff-private/<title>/); the handoff folder gets only POINTER.md.
Every file written passes through the secret redactor (handoff_common.redact).

Manual run: handoff_auto.py <transcript id> [--force]
"""
import json, os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from handoff_common import (CONFIG, fenced, find_transcript, folder_for, handoff_dir, load_threads, pointer_text,  # noqa: E402
                            host_name, private, private_folder, private_leftovers, read_ids, redact, stamp_host)

THROTTLE = 30 * 60
MIN_BYTES = 150_000
STAMPS = os.path.join(os.path.expanduser("~"), ".cache", "handoff", "stamps")


def main():
    force = "--force" in sys.argv
    ids = [a for a in sys.argv[1:] if not a.startswith("--")]
    if ids:
        tid, cwd = ids[0], ""
    else:
        try:
            hook = json.load(sys.stdin)
        except ValueError:
            return
        tid, cwd = hook.get("session_id", ""), hook.get("cwd", "")
    if not tid or not (force or os.path.exists(os.path.join(CONFIG, "auto"))):
        return
    os.makedirs(STAMPS, exist_ok=True)
    stamp = os.path.join(STAMPS, tid)
    if not force and os.path.exists(stamp) and time.time() - os.path.getmtime(stamp) < THROTTLE:
        return
    transcript = find_transcript(tid)
    if not transcript or (not force and os.path.getsize(transcript) < MIN_BYTES):
        return
    threads = load_threads()
    t = threads.get(tid)
    if not t:
        return
    open(stamp, "w").close()  # claim this run before the slow part, so overlapping hooks skip
    root = handoff_dir()
    folder = folder_for(root, threads, tid)
    # A folder shared with sessions that resumed it keeps one backup per session, so two accounts never overwrite each other.
    digest_name = "AUTO-DIGEST.md" if read_ids(folder)[:1] == [tid] else f"AUTO-DIGEST-{tid[:8]}.md"
    fence = fenced(t, [cwd])
    secret = None if fence else private(t, [cwd])
    if fence or secret:
        local = private_folder(t, create=True) if secret else None
        warning = private_leftovers(folder, local) if secret else None  # private: warn only, never delete or move
        if warning:
            sys.stderr.write(f"handoff_auto: {warning}\n")
        if fence:
            p = os.path.join(folder, digest_name)
            if os.path.exists(p):
                os.remove(p)
        write(os.path.join(folder, "POINTER.md"), pointer_text(t, transcript, fence or secret, local, warning))
        stamp_host(folder, root)
        if not secret:
            return
        folder = local
    digest = run([sys.executable, "-I", os.path.join(HERE, "handoff_extract.py"), transcript], 240)
    written = re.search(r"^## Files written.*?\n(.*?)(?=^## )", digest, re.S | re.M)
    dirs = []
    for p in re.findall(r"(/[^\n`]+)", written.group(1) if written else ""):
        d = os.path.dirname(p.strip())
        if d not in dirs and not d.startswith(("/private/tmp", "/tmp")):
            dirs.append(d)
    live = run([sys.executable, "-I", os.path.join(HERE, "handoff_live.py"), "--no-apps", "--thread", tid,
                "--paths", *(dirs[:12] or [cwd or t["cwd"]])], 60)
    parent = threads.get(t["parent"], {}).get("title") if t["parent"] else t.get("parent_title")
    head = (f"# Auto-backup: {t['title']}\n\n"
            f"Made by a script after a turn, with no model involved. A handoff written by the thread itself (HANDOFF.md), "
            f"when present, is the better source.\n\n"
            f"- Updated: {time.strftime('%Y-%m-%d %H:%M')}\n- Transcript: `{transcript}`\n- Transcript id: {tid}\n"
            f"- Written on: {host_name()} · handoff home `{root}`\n"
            f"- Desktop session: {t['local']} (reference only)\n- Parent: {parent or 'none'}\n- Folder it works in: `{t['cwd']}`\n\n")
    write(os.path.join(folder, digest_name), head + live.strip() + "\n\n---\n\n" + digest)
    stamp_host(folder, root)


def run(cmd, timeout):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, errors="replace", timeout=timeout).stdout
    except (OSError, subprocess.TimeoutExpired) as e:
        return f"(could not run {os.path.basename(cmd[2])}: {e})\n"


def write(path, text):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(redact(text))
    os.replace(tmp, path)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # a backup must never break a session
        sys.stderr.write(f"handoff_auto: {e}\n")
