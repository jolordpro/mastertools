#!/usr/bin/env python3
"""Reopen notice: when a thread starts or is reopened, say if another session (often on the other account)
added changelog entries to its handoff folder since this thread last saw them. Runs from the SessionStart hook.

Prints nothing when nothing is new, so it costs no context. Prints at most a few lines when something is.
Reads the hook's JSON on stdin (session_id is the transcript id). Manual run: handoff_notice.py <transcript id>
"""
import json, os, sys, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from handoff_common import changelog, handoff_dir, id_folders, last_handoff  # noqa: E402

SEEN = os.path.join(os.path.expanduser("~"), ".cache", "handoff", "seen")


def main():
    ids = [a for a in sys.argv[1:] if not a.startswith("--")]
    if ids:
        tid = ids[0]
    else:
        try:
            hook = json.load(sys.stdin)
        except ValueError:
            return
        tid = hook.get("session_id", "")
    if not tid:
        return
    folder = id_folders(handoff_dir()).get(tid)
    if not folder:
        return
    stamp = os.path.join(SEEN, tid)
    try:
        marked = float(open(stamp).read().strip() or 0)
    except (OSError, ValueError):
        marked = 0
    seen = max(last_handoff(folder, tid) or 0, marked)
    new = [e for e in changelog(folder) if not tid.startswith(e[3]) and e[0] > seen]
    if not new:
        return
    os.makedirs(SEEN, exist_ok=True)
    open(stamp, "w").write(str(new[-1][0]))  # the newest entry shown, so the next start stays quiet
    accounts = sorted({e[1] for e in new})
    print(f"Handoff notice: {len(new)} newer changelog entr{'y' if len(new) == 1 else 'ies'} from another session "
          f"({', '.join(accounts)}) in this thread's handoff folder since this thread last saw it.")
    print(f"Before acting on old context, read {os.path.join(folder, 'CHANGELOG.md')} from the entry dated "
          f"{time.strftime('%Y-%m-%d %H:%M', time.localtime(new[0][0]))}, then {os.path.join(folder, 'SUMMARY.md')}.")
    print(f"Newest: {new[-1][4].splitlines()[0].lstrip('# ')}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # a notice must never break a session
        sys.stderr.write(f"handoff_notice: {e}\n")
