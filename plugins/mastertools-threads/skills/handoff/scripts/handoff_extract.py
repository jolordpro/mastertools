#!/usr/bin/env python3
"""Distill a Claude Code transcript (.jsonl) into a handoff digest.

Usage: handoff_extract.py <transcript.jsonl | cli-session-id> [--summaries N] [--since 2026-10-28T19:40Z] [--out FILE]

--since keeps only what happened after that time (UTC), for a handoff update. handoff_tree.py prints the value.

Prints, in order:
  1. Stats (size, dates, compactions)
  2. Every message the thread received, tagged [USER] or by the session that sent it
     (system notes and tool output removed)
  3. The newest N compaction summaries in full (default 2); older ones listed by date and size
  4. Files written or edited, artifacts published, sessions started, git commits
"""
import json, re, sys, glob, os, argparse
from collections import OrderedDict

INJECTED = re.compile(r"<(system-reminder|task-notification|side-sessions-event|local-command-stdout|"
                      r"local-command-caveat|command-name|command-message|command-args|ci-monitor-event)"
                      r"[^>]*>.*?</\1>", re.S)
SKIP_PREFIXES = ("Base directory for this skill", "[Image:",
                 "This session is being continued", "Caveat:")


CHILD_NOTE = re.compile(r'The session "([^"]+)" you started \(local_[^)]*\) finished a turn\. It reported[^:]*:\s*"(.{0,600}?)"(?:\s|$|\.)', re.S)
SHELL_WRITE = re.compile(r"(^|[;&|]\s*)(patch|cp|mv|rsync|ditto|tee|mkdir|unzip|zip|ln|touch|python3?|node|bash|sh|\./\S+)\s|open\([^)]*['\"][wa]b?['\"]|write_text\(|sed\s+-i|(?<![<>0-9&])>{1,2}\s*[\"'~/A-Za-z$]")


GIT_COMMIT = re.compile(r"(^|[;&|(]\s*|\n\s*)git(\s+-C\s+(\"[^\"]*\"|'[^']*'|\S+))?\s+commit\b")
HEREDOC = re.compile(r"<<-?\s*(['\"]?)(\w+)\1[^\n]*\n(.*?)\n\s*\2\b", re.S)


def recent_files(folder, since, depth=3, limit=4000):
    """Files under folder (a few levels deep) modified after `since`, newest first, as paths relative to folder."""
    out, seen = [], 0
    if not os.path.isdir(folder):
        return out
    base = folder.rstrip(os.sep).count(os.sep)
    for dirpath, dirnames, files in os.walk(folder):
        dirnames[:] = [x for x in dirnames if not x.startswith(".") and x not in ("node_modules", "__pycache__")]
        if dirpath.count(os.sep) - base >= depth:
            dirnames[:] = []
        for f in files:
            seen += 1
            if seen > limit:
                return [x for _, x in sorted(out, reverse=True)]
            fp = os.path.join(dirpath, f)
            try:
                mt = os.path.getmtime(fp)
            except OSError:
                continue
            if mt > since:
                out.append((mt, os.path.relpath(fp, folder)))
    return [x for _, x in sorted(out, reverse=True)]


def strip_heredocs(cmd):
    """Return the command with heredoc bodies removed, plus the bodies, so text inside a heredoc isn't read as shell."""
    bodies = [m.group(3) for m in HEREDOC.finditer(cmd)]
    return HEREDOC.sub("<<HEREDOC", cmd), bodies


TEMP = ("/private/tmp", "/tmp", "/var/folders", "$S", "$P", "$B")


def find_transcript(arg):
    if os.path.exists(arg):
        return arg
    hits = glob.glob(os.path.expanduser(f"~/.claude/projects/*/{arg}.jsonl"))
    if not hits:
        sys.exit(f"No transcript found for {arg}")
    return hits[0]


def text_of(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text")
    return ""


def is_tool_result(content):
    return isinstance(content, list) and any(isinstance(b, dict) and b.get("type") == "tool_result" for b in content)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcript")
    ap.add_argument("--summaries", type=int, default=2)
    ap.add_argument("--out")
    ap.add_argument("--since", help="UTC time, e.g. 2026-10-28T19:40Z: keep only what happened after it")
    a = ap.parse_args()
    since = a.since.rstrip("Z") if a.since else None
    path = find_transcript(a.transcript)

    inbox, summaries, written, artifacts, sessions, commits, shell_writes, denials = [], [], OrderedDict(), OrderedDict(), [], [], [], []
    seen = set()
    pending_sessions = {}  # tool_use id -> index in sessions
    shell_files = OrderedDict()  # path -> last ts
    first = last = None
    for line in open(path, encoding="utf-8", errors="replace"):
        try:
            r = json.loads(line)
        except ValueError:
            continue
        uid = r.get("uuid")
        if uid:
            if uid in seen:  # compaction re-emits kept messages with the same uuid
                continue
            seen.add(uid)
        ts = r.get("timestamp")
        if since and ts and ts[:len(since)] < since:
            continue
        if ts:
            first = first or ts
            last = ts
        msg = r.get("message") or {}
        content = msg.get("content")
        if r.get("isCompactSummary"):
            summaries.append((ts, text_of(content)))
            continue
        if r.get("type") == "user" and is_tool_result(content):
            for b in content:
                t = b.get("content") if isinstance(b, dict) else None
                t = t if isinstance(t, str) else text_of(t)
                tid = b.get("tool_use_id") if isinstance(b, dict) else None
                if tid in pending_sessions and b.get("is_error"):
                    i = pending_sessions.pop(tid)
                    sessions[i] = (sessions[i][0], sessions[i][1], "this start was REFUSED; it may have started later another way")
                if b.get("is_error") and re.search(r"denied|not allowed|permission", t or "", re.I):
                    denials.append((ts, (t or "")[:200].replace("\n", " ")))
        peer = (r.get("origin") or {}).get("kind") == "peer"
        if r.get("type") == "user" and not is_tool_result(content) and (peer or not r.get("isMeta")):
            raw = text_of(content)
            for name, said in CHILD_NOTE.findall(raw):  # reports from sessions this thread started arrive inside system notes
                inbox.append((ts, f"[FROM SESSION '{name}' (not the user)] reported: {said}"))
            t = INJECTED.sub("", raw).strip()
            if t and not t.startswith(SKIP_PREFIXES):
                m = re.search(r'<cross-session-message[^>]*name="([^"]*)"', t)
                if m:
                    who = f"FROM SESSION '{m.group(1)}' (not the user)"
                elif not inbox and t.startswith("Background (from the session"):
                    who = "BRIEF FROM PARENT SESSION (not the user)"
                else:
                    who = "USER"
                inbox.append((ts, f"[{who}] {t}"))
        if r.get("type") == "assistant" and isinstance(content, list):
            for b in content:
                if not isinstance(b, dict) or b.get("type") != "tool_use":
                    continue
                name, inp = b.get("name", ""), b.get("input") or {}
                if name in ("Write", "Edit", "NotebookEdit") and inp.get("file_path"):
                    written[os.path.normpath(inp["file_path"])] = ts
                elif name == "Artifact" and inp.get("action", "publish") == "publish" and not inp.get("asset"):
                    key = inp.get("url") or inp.get("file_path") or inp.get("type_url")
                    if key:
                        artifacts[key] = ts
                elif name.endswith("start_session"):
                    pending_sessions[b.get("id")] = len(sessions)
                    sessions.append((ts, inp.get("title", "") or inp.get("proposal_id", ""), inp.get("initiation", "")))
                elif name == "Bash":
                    cmd = inp.get("command", "")
                    shell, bodies = strip_heredocs(cmd)
                    if GIT_COMMIT.search(shell):
                        m = re.search(r'-m\s+["\'](.{0,120})', shell)
                        if m:
                            msg = m.group(1)
                        elif re.search(r"-F\s+-", shell) and bodies:
                            msg = bodies[0].strip().splitlines()[0][:120] if bodies[0].strip() else "(empty message)"
                        else:
                            msg = "(message from a file or editor)"
                        commits.append((ts, msg))
                    elif SHELL_WRITE.search(cmd) or "<<" in cmd:
                        m = re.search(r'cd\s+("([^"]+)"|\'([^\']+)\'|(\S+))', shell)
                        d = (m.group(2) or m.group(3) or m.group(4)).rstrip(";&") if m else None
                        if d and "$" in d:
                            d = None  # a shell variable, not a real folder
                        if d and not d.startswith(TEMP):
                            shell_writes.append((ts, d))
                        found = re.findall(r'["\']([^"\'\n]{1,200}\.[A-Za-z0-9]{1,6})["\']', cmd) + re.findall(r'()>>?\s*([^\s;&|"\']+\.[A-Za-z0-9]{1,6})(?=[\s;&|)]|$)|()>>?\s*([~/][^\s;&|"\'$]+)', shell)
                        for lit in found:
                            lit = lit if isinstance(lit, str) else next((x for x in lit if x), "")
                            if "$" in lit or lit.startswith("/dev/"):
                                continue
                            lit = os.path.expanduser(lit)
                            full = lit if lit.startswith("/") else (os.path.join(d, lit) if d else None)
                            if full and not full.startswith(TEMP):
                                full = os.path.normpath(full)
                                if full in written:
                                    written[full] = ts  # later shell edit of a file also edited with Edit/Write
                                else:
                                    shell_files[full] = ts

    out = []
    p = out.append
    p(f"# Transcript digest\n\n- File: {path}\n- Size: {os.path.getsize(path)/1e6:.1f} MB\n"
      f"- From {first} to {last}" + (f" (only what came after {a.since})" if since else "") + f"\n- Compactions: {len(summaries)}\n"
      f"- Messages in: {len(inbox)} ({sum(1 for _, t in inbox if t.startswith('[USER]'))} from the user, the rest from other sessions)\n")
    p("## Messages in (verbatim; long ones trimmed to 1500 chars). Only [USER] lines are the user's words.\n")
    for ts, t in inbox:
        p(f"**{ts}**\n{t[:1500]}{' …[trimmed]' if len(t) > 1500 else ''}\n")
    p(f"## Compaction summaries\n")
    older = summaries[:-a.summaries] if a.summaries else summaries
    for ts, t in older:
        p(f"- {ts}: {len(t)} chars (not shown; rerun with --summaries {len(summaries)} or grep the transcript)")
    for ts, t in summaries[-a.summaries:] if a.summaries else []:
        p(f"\n### Summary at {ts}\n\n{t}\n")
    p("## Files written or edited (last touch)\n")
    for f, ts in written.items():
        flag = "" if os.path.exists(f) else "  (MISSING now)"
        if f.startswith(("/private/tmp", "/tmp", "/var/folders")):
            flag += "  (TEMP: copy into the project before handoff)"
        p(f"- {ts[:16] if ts else ''} {f}{flag}")
    p("\n## Artifacts published (account-bound)\n")
    for k, ts in artifacts.items():
        flag = "  (TEMP source: copy into the project)" if k.startswith(("/private/tmp", "/tmp")) else ""
        p(f"- {ts[:16] if ts else ''} {k}{flag}")
    p("\n## Sessions started\n")
    for ts, title, init in sessions:
        p(f"- {ts[:16] if ts else ''} {title} ({init})")
    start = first and __import__("datetime").datetime.fromisoformat(first.replace("Z", "+00:00")).timestamp()
    p("\n## Folders where shell commands or scripts ran, with files changed since this thread started. The list above misses these\n")
    folders = OrderedDict()
    for ts, d in shell_writes:
        n, _ = folders.get(d, (0, ts))
        folders[d] = (n + 1, ts)
    for d, (n, ts) in folders.items():
        changed = recent_files(os.path.expanduser(d), start) if start else []
        if changed:
            more = f" (+{len(changed) - 8} more)" if len(changed) > 8 else ""
            p(f"- last {ts[:16] if ts else ''} · {n} commands · {d}\n  changed: " + ", ".join(changed[:8]) + more)
    p("\n## Files named in those shell commands and changed on disk since this thread started\n")
    for f, ts in shell_files.items():
        try:
            if os.path.isfile(f) and (not start or os.path.getmtime(f) >= start):
                p(f"- {ts[:16] if ts else ''} {f}")
        except OSError:
            pass
    p("\n## Permission denials and refused actions\n")
    for ts, t in denials:
        p(f"- {ts[:16] if ts else ''} {t}")
    p("\n## Git commits\n")
    for ts, m in commits:
        p(f"- {ts[:16] if ts else ''} {m}")
    text = "\n".join(out)
    if a.out:
        open(a.out, "w").write(text)
        print(f"Wrote {a.out} ({len(text)} chars, ~{len(text)//4} tokens)")
    else:
        print(text)


if __name__ == "__main__":
    main()
