#!/usr/bin/env python3
"""Find live work an account switch could lose: renders and encodes, dev servers, busy terminals,
unsaved documents, and uncommitted git work.

Usage: handoff_live.py [--thread ID] [--paths DIR ...] [--all] [--no-apps]
  --thread   this thread's transcript id. A process started from that Claude session is this thread's.
  --paths    folders this thread works in. Matching processes and repos are marked as this thread's.
  --all      count other threads' items as red too (for the top thread or a whole-Mac check).
  --no-apps  skip asking open apps about unsaved documents (AppleScript). The auto-backup uses this.

The key check: a process whose parent chain runs through a Claude process was started from a Claude
session (for example a background render). It can die when that session, the app, or the account goes away.
Ownership needs evidence: the launching transcript (--resume/--session-id in the process chain) or the process
working folder inside --paths, or a --paths folder named in its command line. Without any, a process or app is
"owner unknown": 🟠 under the headline, to check by hand, not 🔴.
Online-only files (Dropbox placeholders) in --paths show as 🟠 with a count: searches there can come back empty.
Lines starting with 🔴 need action before switching. ⚪ lines are fine or only informational.
"""
import os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from handoff_common import redact  # noqa: E402

args = sys.argv[1:]
no_apps = "--no-apps" in args
explicit_all = "--all" in args
paths = []
named = set()  # --paths as given, before symlinks resolve, to match command lines
thread = args[args.index("--thread") + 1] if "--thread" in args and args.index("--thread") + 1 < len(args) else None
if "--paths" in args:
    i = args.index("--paths") + 1
    while i < len(args) and not args[i].startswith("--"):
        paths.append(os.path.realpath(os.path.expanduser(args[i])))
        named.add(os.path.expanduser(args[i]).rstrip(os.sep))
        i += 1

RENDER = re.compile(r"c4dpy|Cinema 4D|/Commandline|redshiftCmdLine|aerender|After Effects|Media Encoder|ffmpeg|"
                    r"/blender|Premiere Pro|hython|/Nuke|DaVinci Resolve|Compressor|HandBrake", re.I)
SERVER = re.compile(r"\b(vite|next dev|next-server|webpack|astro|wrangler|http\.server|uvicorn|gunicorn|flask|"
                    r"rails server|npm run (dev|start|serve)|pnpm (dev|start)|yarn (dev|start)|bun (dev|run))\b", re.I)
CLAUDE = re.compile(r"/claude(\s|$)|claude-code/|Claude\.app/|Claude Helper", re.I)
TERM_APP = re.compile(r"Terminal\.app|iTerm|Warp\.app|Ghostty|kitty|Alacritty|WezTerm", re.I)
SHELL = re.compile(r"^-?(zsh|bash|fish|sh|login)(\s|$)|/(zsh|bash|fish|sh|login)(\s|$)")
DOC_APPS = ("TextEdit", "Pages", "Keynote", "Numbers", "Photoshop", "Illustrator", "InDesign")
OPAQUE_APPS = ("After Effects", "Cinema 4D", "Premiere Pro", "Blender", "DaVinci Resolve", "Final Cut Pro", "Audition")


def run(cmd, timeout=10):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, errors="replace", timeout=timeout).stdout
    except (OSError, subprocess.TimeoutExpired):
        return ""


procs = {}
for ln in run(["ps", "-axo", "pid=,ppid=,etime=,args="]).splitlines():
    m = re.match(r"\s*(\d+)\s+(\d+)\s+(\S+)\s+(.*)", ln)
    if m:
        procs[int(m.group(1))] = dict(ppid=int(m.group(2)), etime=m.group(3), args=m.group(4))
me = os.getpid()


def chain(pid):
    seen, out = set(), []
    while pid in procs and pid not in seen and pid > 1:
        seen.add(pid)
        pid = procs[pid]["ppid"]
        if pid in procs:
            out.append(pid)
    return out


def under_claude(pid):
    return any(CLAUDE.search(procs[a]["args"]) for a in chain(pid))


OWNER = re.compile(r"--(?:resume|session-id)[ =]([0-9a-f-]{36})")


def owner(pid):
    """The transcript id of the Claude session a process was started from, if any. Stops at the nearest Claude
    process: one with no id means owner unknown, never the id of a session further up (nested runs)."""
    for a in [pid, *chain(pid)]:
        m = OWNER.search(procs[a]["args"]) if a in procs else None
        if m:
            return m.group(1)
        if a in procs and CLAUDE.search(procs[a]["args"]):
            return None
    return None


def cwd(pid):
    out = run(["lsof", "-a", "-d", "cwd", "-p", str(pid), "-Fn"], 5)
    return next((l[1:] for l in out.splitlines() if l.startswith("n")), "")


def inside(where):
    where = os.path.realpath(where) if where else ""
    return bool(where) and any(where == p or where.startswith(p.rstrip(os.sep) + os.sep) for p in paths)


def mine(where, pid=None, text=""):
    """True or False with evidence (launching transcript, then working folder, then a --paths folder named in the
    command line), else None: owner unknown."""
    who = owner(pid) if pid is not None else None
    if who and thread:
        return who == thread
    if inside(where) or any(p and p in text for p in set(paths) | named):
        return True
    return False if who else None


def short(a, n=110):
    return a if len(a) <= n else a[:n] + "…"


red, info, elsewhere, warn = [], [], [], []
own = set(chain(me)) | {me}
scope_all = "--all" in args or not (paths or thread)


def report(line, is_mine, is_red):
    """Red counts only this thread's items, unless --all or no --paths were given. is_mine None means no evidence
    of an owner: 🟠 "owner unknown", listed under the headline to check by hand, unless --all asked for every item as red."""
    if is_red and (is_mine or (scope_all and (is_mine is not None or explicit_all or not (paths or thread)))):
        red.append("🔴 " + line)
    elif is_red and is_mine is None:
        warn.append("🟠 Check by hand, owner unknown (no launching transcript, working folder or path ties it to this thread). " + line)
    elif is_red:
        elsewhere.append("🟠 " + line)
    else:
        info.append("⚪ " + line)


# 1. Renders, encodes and dev servers. Report only the top of each matching process chain.
hits = {}
for pid, p in sorted(procs.items()):
    if pid in own or "handoff_live" in p["args"] or p["args"].startswith(("ps ", "lsof ")):
        continue
    kind = "render/encode" if RENDER.search(p["args"]) else "dev server" if SERVER.search(p["args"]) else None
    if kind and not re.search(r"\.app/Contents/(Frameworks|Helpers|PlugIns|XPCServices)/|crashpad", p["args"]):
        hits[pid] = kind
reported = set()
for pid, kind in hits.items():
    if any(a in hits for a in chain(pid)):
        continue  # its parent already matched; one line per job
    p = procs[pid]
    kids = [k for k in hits if pid in chain(k)]
    reported.update([pid, *kids])
    where = cwd(pid) or next((cwd(k) for k in kids), "")
    is_mine = mine(where, pid, p["args"])
    desc = f"{kind}, pid {pid}, running {p['etime']}: {short(p['args'])}" + (f" (in {where})" if where else "")
    if under_claude(pid):
        report(f"Started from a Claude session, so it can die at the switch. Let it finish, or relaunch it on its own. {desc}", is_mine, True)
    elif is_mine:
        report(f"Runs on its own and survives the switch. {desc}", True, False)

# 2. Listening ports from Claude-started processes not already reported, one line per process
ports, pid = {}, None
for ln in run(["lsof", "-nP", "-iTCP", "-sTCP:LISTEN", "-Fpn"], 8).splitlines():
    if ln.startswith("p"):
        pid = int(ln[1:])
    elif ln.startswith("n") and pid in procs and pid not in own:
        ports.setdefault(pid, []).append(ln[1:].split(":")[-1])
for pid, plist in ports.items():
    if pid in reported or any(a in reported for a in chain(pid)) or CLAUDE.search(procs[pid]["args"]) or not under_claude(pid):
        continue
    where = cwd(pid)
    report(f"Server on port {', '.join(sorted(set(plist)))} was started from a Claude session (pid {pid}): {short(procs[pid]['args'], 80)}"
           + (f" (in {where})" if where else ""), mine(where, pid, procs[pid]["args"]), True)

# 3. Busy terminals in terminal apps (Terminal, iTerm and others). Claude's own terminal panel is checked by the skill
# with its terminal tools, because its shells can't be told apart from Claude's tool calls here.
for pid, p in procs.items():
    parent = procs.get(p["ppid"])
    if pid in own or pid in reported or not parent or not SHELL.search(parent["args"]) or SHELL.search(p["args"]):
        continue
    anc = chain(pid)
    if any(CLAUDE.search(procs[a]["args"]) for a in anc) or not any(TERM_APP.search(procs[a]["args"]) for a in anc):
        continue
    where = cwd(pid)
    report(f"Busy terminal, pid {pid}, running {p['etime']}: {short(p['args'])}" + (f" (in {where})" if where else "")
           + ". Closing that terminal window stops it.", mine(where, None, p["args"]), False)

# 4. Open documents with unsaved changes
apps = {}
for p in procs.values():
    m = re.search(r"/([^/]+)\.app/Contents/MacOS/", p["args"])
    if m and ".app/Contents/MacOS/" in p["args"] and "/Contents/Frameworks/" not in p["args"]:
        apps.setdefault(m.group(1), True)
if no_apps:
    info.append("⚪ Unsaved documents not checked (auto-backup skips the app questions).")
else:
    for name in sorted(apps):
        if any(k in name for k in DOC_APPS):
            script = f'tell application "{name}" to get name of every document whose modified is true'
            try:
                r = subprocess.run(["osascript", "-e", script], capture_output=True, text=True, errors="replace", timeout=8)
            except subprocess.TimeoutExpired:
                info.append(f"⚪ {name} is open; it didn't answer in 8 seconds (a macOS permission prompt may be waiting). Check it by hand.")
                continue
            if r.returncode != 0:
                info.append(f"⚪ {name} is open; couldn't ask it about unsaved documents ({short(r.stderr.strip(), 70)}). Check by hand.")
            elif r.stdout.strip():
                report(f"Unsaved in {name}: {r.stdout.strip()}", None, True)
        elif any(k in name for k in OPAQUE_APPS):
            report(f"{name} is open. It can't report unsaved changes, so save in it by hand.", None, True)

# 5. Online-only files (Dropbox placeholders) in this thread's folders: reads and searches there can come back empty.
SF_DATALESS = 0x40000000


def placeholder(fp, st):
    if getattr(st, "st_flags", 0) & SF_DATALESS or (st.st_size > 0 and getattr(st, "st_blocks", 1) == 0):
        return True
    if st.st_size == 0 and "Dropbox" in fp:
        return True
    try:
        return "com.dropbox.placeholder" in os.listxattr(fp)
    except (AttributeError, OSError):
        return _xattr_has(fp)


def _xattr_has(fp):
    """macOS has no os.listxattr; ask libc instead."""
    try:
        import ctypes
        libc = ctypes.CDLL(None, use_errno=True)
        return libc.getxattr(fp.encode(), b"com.dropbox.placeholder", None, 0, 0, 0x0001) >= 0
    except (OSError, AttributeError):
        return False


for p in paths:
    count, seen, base = 0, 0, p.rstrip(os.sep).count(os.sep)
    for d, dirs, files in os.walk(p):
        dirs[:] = [x for x in dirs if not x.startswith(".") and x not in ("node_modules", "__pycache__")]
        if d.count(os.sep) - base >= 4:
            dirs[:] = []
        for f in files:
            seen += 1
            fp = os.path.join(d, f)
            try:
                st = os.lstat(fp)
            except OSError:
                continue
            if not f.startswith(".") and placeholder(fp, st):
                count += 1
        if seen > 20000:
            break
    if count:
        warn.append(f"🟠 {count} online-only files in {p} (Dropbox placeholders). Searches and reads there can come back "
                    f"empty; make the folder available offline before trusting a \"not found\".")

# 6. Git work in this thread's repos
repos = []
for p in paths:
    top = run(["git", "-C", p, "rev-parse", "--show-toplevel"], 5).strip()
    if top and top not in repos:
        repos.append(top)
for top in repos:
    dirty = len(run(["git", "-C", top, "status", "--porcelain"]).splitlines())
    branch = run(["git", "-C", top, "branch", "--show-current"]).strip() or "detached"
    unpushed = run(["git", "-C", top, "log", "--branches", "--not", "--remotes", "--oneline"]).splitlines()
    if dirty:
        red.append(f"🔴 {dirty} uncommitted files in {top} (branch {branch}). Commit or note them.")
    if unpushed:
        red.append(f"🔴 {len(unpushed)} commits in {top} aren't on any remote. Push or note them.")
    if not dirty and not unpushed:
        info.append(f"⚪ {top} (branch {branch}) is clean and pushed.")

out = [f"# Live check: {len(red)} red" + ("" if scope_all else f" for this thread, {len(elsewhere)} elsewhere on this Mac") + "\n",
       "\n".join(red) if red else "🟢 Nothing found that the switch would lose" + (f" · {len(warn)} to check by hand" if warn else ".")]
if warn:
    out.append("\n" + "\n".join(warn))
if info:
    out.append("\n" + "\n".join(info))
if elsewhere:
    out.append("\n## Elsewhere on this Mac (other threads' work)\n\n" + "\n".join(elsewhere))
print(redact("\n".join(out)))
