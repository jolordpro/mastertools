#!/usr/bin/env python3
"""aerun.py: the after-effects-engineering skill's one default runner for AE scripts.
Call it from the skill's scripts/ folder; never copy it into a project.

Skill copy of a QC-frozen project runner. Source sha256 a29cd534 (a29cd5341e4d72ff082f4092373e73015ae28b67f5f7ecca2c0760dd607b2408),
QC freeze FREEZE_render v2 b941ea8aa0c04258. Changes from that source, nothing else:
* qc_gate.py lookup: the skill's own scripts/qc_gate.py (next to this file) first, then AE_QC_GATE, then GATE_GLOBS.
* AE Beta Sentry glob pinned to the 27.0 folder (it matched 26.0 and 27.0).
* No project paths or names: kit folders come from AERUN_KITS ("name=/abs/dir;name2=/abs/dir2"), the kit name from AERUN_KIT,
  the ES3 lint from AE_ES3LINT (else es3lint.sh next to this file; missing: refused); logs keep to /tmp/aerun_logs/aerun_<app>.

    python3 aerun.py --app 2026|beta <tool.jsx> [KEY=VALUE ...] [--wait DIR:N] [--timeout SEC] [--lockwait SEC] [--nogate]
    python3 aerun.py --gateinfo                (the lint gate's path and sha; exit 1 when it is missing)

Changes from the kit copy:
* --app picks the AE. 2026 and 2025 share the bundle id com.adobe.AfterEffects.application, so the AppleScript
  targets the app by its full path, never by id. Beta: com.adobe.AfterEffectsBeta.application by path too.
* One lock per app: /tmp/ae_busy_2026.lock, /tmp/ae_busy_beta.lock.
* Logs: /tmp/ae_<app>_<stem>.txt when the tool uses %LOG% (else /tmp/ae_<stem>.txt as before).
* Exit status (QC, Oct 30): 0 = the log exists and has no line starting "ERR " (H.run writes those); 1 = no log, a
  script error, lint or gate refusal. A LOG= given by the caller is the log read back.
* Slot file (house rule, QC Oct 30): a lane's whole slot, not just one call. /tmp/ae_slot_2026 holds one line,
  owner TAB start TAB expected end (HH:MM, local) TAB note. Take it before the first call of a slot, free it after the last:
      python3 aerun.py --slot take A 30 "wrapper probe"     (owner A, 30 min; refuses if another owner holds it)
      python3 aerun.py --slot free A
      python3 aerun.py --slot show
  Every 2026 call names its lane (--lane A, or AE_LANE=A in the environment) and stops (exit 4) if another lane owns the
  slot. No slot file: the call runs (a warning is printed). The per-call lock stays as it was.
Dialog-proofing (QC dialog-proofing ruling 6cec5ce8, Nov 1). Exit codes add 5 (AE not running) and 6 (dialog):
* D2: never launches AE. Before anything is sent, the app's exact binary must be running (pgrep -f on the full path, anchored);
  else "AE NOT RUNNING" and exit 5, nothing sent. The AppleScript also asks "is running" before its tell, so an AE that quit
  after the check is not relaunched either.
* D9: no call within 10 s of AE's launch (the call waits out the rest of the 10 s).
* D4 (G3): AE's Sentry breadcrumbs (the newest SentryIO-db/*.run, __sentry-breadcrumb1 and 2) are scanned for Up_DlgShow /
  AEErrorDialog entries before the send (since AE_G3_SINCE when preflight set it, else since that moment, which proves the
  breadcrumbs readable) and after it (since the call started, or AE_G3_SINCE when earlier). A hit prints "DIALOG <UTC> <text>", writes the stop flag (/tmp/ae_dialog_<app>.stop, with AE's pid)
  and exits 6; while the flag names the running AE's pid, every later call exits 6 and sends nothing (a relaunched AE, another
  pid, clears it). Breadcrumbs that cannot be read count as a hit (fail closed).
* D5: osascript's exit status is checked (non-zero: exit 1); the log must end with H.run's END line (house 1.6), else exit 1, even
  when the log has other lines.
  python3 aerun.py --app 2026|beta --running            exit 0 when that AE runs, 5 when not (sends nothing)
  python3 aerun.py --app 2026|beta --dialogs SINCE      G3 scan only: SINCE is a UTC time (2026-11-01T20:36:36Z) or "launch";
                                                        exit 0 none, 6 a dialog (or breadcrumbs unreadable)
  python3 aerun.py --utcnow                             the UTC time in G3's format
Test hook (stubs only, launchers unset it): AERUN_TEST=<dir> moves the lock, slot, stop flag, logs, filled script and Sentry folder
into <dir> and takes pgrep, ps and osascript from <dir>/bin only (missing: refused), so a stub never reaches the real AE.
"""

import os, re, subprocess, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
KITS = dict(kv.split("=", 1) for kv in os.environ.get("AERUN_KITS", "").split(";") if "=" in kv)   # name -> absolute tools dir
GATE_GLOBS = ("~/.claude/skills/ae-extendscript/scripts/qc_gate.py", "~/.claude/skills/synced/*/ae-extendscript/scripts/qc_gate.py")


def find_gate():
    """The house lint gate (QC, Oct 30: the old fixed path did not exist, so every runner passed --nogate and the gate never
    ran). The skill's own qc_gate.py next to this file comes first; then AE_QC_GATE names it outright and must exist; else the newest match of GATE_GLOBS. None when nothing is found:
    the caller then refuses to run. Never skipped silently."""
    import glob
    own = os.path.join(HERE, "qc_gate.py")
    if os.path.isfile(own): return own
    env = os.environ.get("AE_QC_GATE")
    if env: return env if os.path.isfile(env) else None
    hits = [h for g in GATE_GLOBS for h in glob.glob(os.path.expanduser(g)) if os.path.isfile(h)]
    return max(hits, key=os.path.getmtime) if hits else None


def gate_info():
    """--gateinfo: prints the gate's path and sha (first 16), exit 0; GATE MISSING and exit 1 when none is found."""
    import hashlib
    g = find_gate()
    if not g: print("QC GATE MISSING (AE_QC_GATE=%s; globs %s): nothing may run" % (os.environ.get("AE_QC_GATE", ""), ", ".join(GATE_GLOBS))); return 1
    print("QC GATE %s %s" % (hashlib.sha256(open(g, "rb").read()).hexdigest()[:16], g)); return 0
APPS = {"2026": "/Applications/Adobe After Effects 2026/Adobe After Effects 2026.app",
        "beta": "/Applications/Adobe After Effects (Beta)/Adobe After Effects (Beta).app"}
BINS = {"2026": "After Effects", "beta": "After Effects (Beta)"}        # Contents/MacOS/<name>: the process pgrep must find
SENTRY = {"2026": "~/Library/Caches/Adobe/After Effects/26.0/SentryIO-db",         # globs; the newest *.run under them is AE's live
          "beta": "~/Library/Caches/Adobe/After Effects (Beta)/27.0/SentryIO-db"}      # session (one .run folder per launch)
TEST = os.environ.get("AERUN_TEST")                                    # stubs only (see the docstring)
TMP = TEST if TEST else "/tmp"
LOCK = TMP + "/ae_busy_2026.lock"
LOGS = (TEST + "/aerun_logs") if TEST else "/tmp/aerun_logs"
SLOT = TMP + "/ae_slot_2026"
READY_S = 10                                                           # D9: no call within 10 s of AE's launch


def binpath(name):
    """pgrep, ps, osascript: the system's own by absolute path; under AERUN_TEST only <dir>/bin/<name> (never the real one)."""
    if TEST:
        t = os.path.join(TEST, "bin", name)
        if not os.path.isfile(t): raise SystemExit("AERUN_TEST: no stub %s in %s/bin: refused" % (name, TEST))
        return t
    return {"pgrep": "/usr/bin/pgrep", "ps": "/bin/ps", "osascript": "/usr/bin/osascript"}[name]


def ae_pid(app):
    """D2: the pid of this app's AE (its exact binary, args allowed), or None. pgrep -f with an anchored pattern: AE 2025 and
    Beta also run a binary called After Effects, so the full path is matched."""
    pat = "^" + re.escape(APPS[app] + "/Contents/MacOS/" + BINS[app]) + "( |$)"
    r = subprocess.run([binpath("pgrep"), "-f", pat], capture_output=True, text=True)
    pids = [int(x) for x in r.stdout.split() if x.strip().isdigit()]
    return min(pids) if r.returncode == 0 and pids else None


def ae_age(pid):
    """seconds since the AE process started (ps etime: [[dd-]hh:]mm:ss), or None."""
    r = subprocess.run([binpath("ps"), "-o", "etime=", "-p", str(pid)], capture_output=True, text=True)
    t = r.stdout.strip()
    if r.returncode != 0 or not t: return None
    d, _, t = t.rpartition("-"); parts = [int(x) for x in t.split(":")]
    while len(parts) < 3: parts.insert(0, 0)
    return (int(d) if d else 0) * 86400 + parts[0] * 3600 + parts[1] * 60 + parts[2]


def utcnow():
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + ".%06dZ" % int((time.time() % 1) * 1e6)


# ---------------------------------------------------------------- G3: the dialog detector (D4)
def _mp(b, i):
    """one MessagePack object at b[i]: (value, next index). The subset Sentry native writes; raises on anything else."""
    c = b[i]; i += 1
    if c <= 0x7f: return c, i
    if c >= 0xe0: return c - 0x100, i
    if 0x80 <= c <= 0x8f: return _mpmap(b, i, c & 0x0f)
    if 0x90 <= c <= 0x9f: return _mparr(b, i, c & 0x0f)
    if 0xa0 <= c <= 0xbf: n = c & 0x1f; return b[i:i + n].decode("utf-8", "replace"), i + n
    if c == 0xc0: return None, i
    if c == 0xc2: return False, i
    if c == 0xc3: return True, i
    W = {0xd9: 1, 0xda: 2, 0xdb: 4, 0xc4: 1, 0xc5: 2, 0xc6: 4}
    if c in W:
        n = int.from_bytes(b[i:i + W[c]], "big"); i += W[c]; v = b[i:i + n]
        return (v.decode("utf-8", "replace") if c >= 0xd9 else bytes(v)), i + n
    if c in (0xcc, 0xcd, 0xce, 0xcf): n = {0xcc: 1, 0xcd: 2, 0xce: 4, 0xcf: 8}[c]; return int.from_bytes(b[i:i + n], "big"), i + n
    if c in (0xd0, 0xd1, 0xd2, 0xd3): n = {0xd0: 1, 0xd1: 2, 0xd2: 4, 0xd3: 8}[c]; return int.from_bytes(b[i:i + n], "big", signed=True), i + n
    if c == 0xca: import struct; return struct.unpack(">f", b[i:i + 4])[0], i + 4
    if c == 0xcb: import struct; return struct.unpack(">d", b[i:i + 8])[0], i + 8
    if c == 0xdc: return _mparr(b, i + 2, int.from_bytes(b[i:i + 2], "big"))
    if c == 0xdd: return _mparr(b, i + 4, int.from_bytes(b[i:i + 4], "big"))
    if c == 0xde: return _mpmap(b, i + 2, int.from_bytes(b[i:i + 2], "big"))
    if c == 0xdf: return _mpmap(b, i + 4, int.from_bytes(b[i:i + 4], "big"))
    raise ValueError("msgpack byte 0x%02x" % c)


def _mparr(b, i, n):
    out = []
    for _ in range(n): v, i = _mp(b, i); out.append(v)
    return out, i


def _mpmap(b, i, n):
    out = {}
    for _ in range(n): k, i = _mp(b, i); v, i = _mp(b, i); out[k] = v
    return out, i


def crumbs(path):
    """every breadcrumb map in one __sentry-breadcrumb file (a run of MessagePack maps). A part it cannot decode is skipped
    to the next "timestamp" key; the count of skipped parts is returned too."""
    b = open(path, "rb").read(); i, out, bad = 0, [], 0
    while i < len(b):
        try:
            v, j = _mp(b, i)
            if isinstance(v, dict): out.append(v)
            i = j
        except Exception:
            bad += 1; k = b.find(b"\xa9timestamp", i + 1)
            if k < 0: break
            i = k - 1
    return out, bad


def sentry_run(app):
    """AE's live session: the newest SentryIO-db/*.run folder that has a sibling <name>.run.lock (aerender leaves lockless
    empty .run folders, Nov 2), else the newest *.run folder; and its session start (UTC string or None)."""
    import glob, json
    root = (TEST + "/sentry") if TEST else os.path.expanduser(SENTRY[app])
    runs = [d for d in glob.glob(os.path.join(root, "*.run")) if os.path.isdir(d)]
    if not runs: return None, None
    locked = [d for d in runs if os.path.exists(d + ".lock")]
    d = max(locked or runs, key=os.path.getmtime)
    try: st = json.load(open(os.path.join(d, "session.json"))).get("started")
    except Exception: st = None
    return d, st


def utc_s(t):
    """an ISO UTC time (2026-11-01T20:36:37.805041Z, fraction and Z optional) as epoch seconds; None when it is not one."""
    import calendar
    m = re.match(r"^(\d{4})-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)(\.\d+)?Z?$", str(t).strip())
    if not m: return None
    return calendar.timegm(tuple(int(x) for x in m.groups()[:6])) + (float(m.group(7)) if m.group(7) else 0.0)


def dialogs(app, since):
    """G3: (hits, problem). hits: [(UTC timestamp, text)] for Up_DlgShow* messages or AEErrorDialog entries later than since
    (an ISO UTC string; "launch" = the session's start, or every entry when it has none). problem: a reason the scan could not be
    trusted (no Sentry folder, no breadcrumb file, undecodable data), which callers treat as a hit."""
    d, started = sentry_run(app)
    if not d: return [], "no SentryIO-db/*.run folder for AE %s (breadcrumbs unreadable)" % app
    if since == "launch": since = started or "1970-01-01T00:00:00Z"
    t_since = utc_s(since)
    if t_since is None: return [], "SINCE %r is not a UTC time" % since
    hits, files, bad = [], 0, 0
    for n in ("__sentry-breadcrumb1", "__sentry-breadcrumb2"):
        p = os.path.join(d, n)
        if not os.path.isfile(p): continue
        files += 1
        try: cs, k = crumbs(p)
        except OSError as e: return [], "cannot read %s: %s" % (p, e)
        bad += k
        for c in cs:
            ts, msg, cat = str(c.get("timestamp", "")), str(c.get("message", "")), str(c.get("category", ""))
            if not (msg.startswith("Up_DlgShow") or cat == "AEErrorDialog"): continue
            t = utc_s(ts)
            if t is None: bad += 1; continue                                   # a dialog with no readable time: untrusted
            if t <= t_since: continue
            data = c.get("data") if isinstance(c.get("data"), dict) else {}
            hits.append((ts, "%s %s: %s" % (cat, msg, str(data.get("message", "")).replace("\n", " ")[:300])))
    if not files: return [], "no __sentry-breadcrumb file in %s" % d
    if bad: return hits, "%d undecodable part(s) in %s" % (bad, d)
    return sorted(hits), None


def flagfile(app):
    return "%s/ae_dialog_%s.stop" % (TMP, app)


def flag_set(app, pid, why):
    open(flagfile(app), "w").write("%s\t%s\t%s\n" % (pid, utcnow(), why))


def flag_held(app, pid):
    """the stop flag's text while it names this AE's pid; a flag left by an AE that has since quit is removed (the user relaunched it)."""
    try: f = open(flagfile(app)).read().strip().split("\t")
    except FileNotFoundError: return None
    if pid is not None and f and f[0] == str(pid): return " ".join(f)
    try: os.remove(flagfile(app))
    except OSError: pass
    return None


def g3(app, pid, since, when):
    """scan; on a hit or an untrusted scan: print, set the stop flag, return False."""
    hits, problem = dialogs(app, since)
    for ts, txt in hits: print("DIALOG %s %s" % (ts, txt))
    if hits or problem:
        why = "G3 %s: %s" % (when, problem or ("%d dialog(s) since %s, first %s" % (len(hits), since, hits[0][1])))
        print("G3 STOP " + why + " (exit 6; nothing more is sent to AE %s)" % app); flag_set(app, pid, why); return False
    return True


def g3_cmd(app, since):
    """--dialogs SINCE: scan only (no flag written)."""
    hits, problem = dialogs(app, since)
    for ts, txt in hits: print("DIALOG %s %s" % (ts, txt))
    if problem: print("G3 UNREADABLE " + problem)
    if hits or problem: return 6
    print("G3 clean since %s" % since); return 0


def slot_read():
    try: f = open(SLOT).read().strip().split("\t")
    except FileNotFoundError: return None
    return dict(zip(("owner", "start", "end", "note"), f + [""] * (4 - len(f))))


def slot_cmd(a):
    """--slot take OWNER MIN [note] | free OWNER | show"""
    s = slot_read()
    if a[0] == "show": print("free" if s is None else "%(owner)s since %(start)s, until about %(end)s: %(note)s" % s); return 0
    if a[0] == "take":
        owner, mins, note = a[1], int(a[2]), " ".join(a[3:])
        if s is not None and s["owner"] != owner:
            print("SLOT HELD by %(owner)s since %(start)s, until about %(end)s (%(note)s): not taken" % s); return 4
        open(SLOT, "w").write("%s\t%s\t%s\t%s\n" % (owner, time.strftime("%H:%M"), time.strftime("%H:%M", time.localtime(time.time() + 60 * mins)), note))
        print("slot taken: " + open(SLOT).read().strip()); return 0
    if a[0] == "free":
        if s is None: print("slot already free"); return 0
        if s["owner"] != a[1]: print("SLOT HELD by %(owner)s, not %%s: not freed" % s % a[1]); return 4
        os.remove(SLOT); print("slot freed"); return 0
    print(slot_cmd.__doc__); return 2

def _alive(pid):
    try: os.kill(pid, 0); return True
    except ProcessLookupError: return False
    except PermissionError: return True

def lock(tool, wait):
    t0 = time.time(); said = False
    while True:
        try:
            fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(fd, ("%d\t%s\t%s\n" % (os.getpid(), tool, time.strftime("%H:%M:%S"))).encode()); os.close(fd); return True
        except FileExistsError:
            try: pid, who, when = open(LOCK).read().strip().split("\t")[:3]; pid = int(pid)
            except Exception: pid, who, when = -1, "?", "?"
            if pid > 0 and not _alive(pid):
                os.remove(LOCK); continue                       # stale: its runner died
            if time.time() - t0 > wait:
                print("AE BUSY — %s (pid %s, since %s) still holds %s; gave up after %d s" % (who, pid, when, LOCK, wait)); return False
            if not said: print("waiting for AE: %s (pid %s, since %s)" % (who, pid, when)); said = True
            time.sleep(1)

def unlock():
    try:
        if open(LOCK).read().split("\t")[0] == str(os.getpid()): os.remove(LOCK)
    except Exception: pass

def main(argv):
    args = argv[1:]
    if not args: print(__doc__); return 2
    if args[0] == "--slot": return slot_cmd(args[1:])
    if args[0] == "--gateinfo": return gate_info()
    if args[0] == "--utcnow": print(utcnow()); return 0
    if len(args) >= 3 and args[0] == "--app" and args[1] in APPS and args[2] in ("--running", "--dialogs"):
        if args[2] == "--running":
            pid = ae_pid(args[1])
            print("AE %s running, pid %s" % (args[1], pid) if pid else "AE NOT RUNNING (%s): nothing sent" % args[1]); return 0 if pid else 5
        if len(args) != 4: print("--dialogs needs SINCE (UTC time or launch)"); return 2
        return g3_cmd(args[1], args[3])
    global LOCK
    subs, wait, timeout, lockwait, gate, kit, tool, app = {}, None, 120, 600, True, os.environ.get("AERUN_KIT", ""), None, None
    lane = os.environ.get("AE_LANE")
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--wait": wait = args[i + 1]; i += 2; continue
        if a == "--timeout": timeout = int(args[i + 1]); i += 2; continue
        if a == "--lockwait": lockwait = int(args[i + 1]); i += 2; continue
        if a == "--nogate": gate = False; i += 1; continue
        if a == "--app": app = args[i + 1]; i += 2; continue
        if a == "--lane": lane = args[i + 1]; i += 2; continue
        if tool is None and a.startswith("KIT="): kit = a[4:]; i += 1; continue
        if tool is None and "=" not in a: tool = a; i += 1; continue
        k, v = a.split("=", 1); subs[k] = v; i += 1
    if tool is None: print("no tool given"); return 2
    if app not in APPS: print("--app 2026 or --app beta is required"); return 2
    LOCK = "%s/ae_busy_%s.lock" % (TMP, app)
    if app == "2026":
        s = slot_read()
        if s is None: print("note: no slot file (%s); take one with --slot take <lane> <min>" % SLOT)
        elif s["owner"] != lane:
            print("SLOT HELD by %(owner)s since %(start)s, until about %(end)s (%(note)s)" % s + "; this call is lane %s: not run" % lane); return 4
    src = tool if os.path.isabs(tool) else os.path.abspath(tool)
    if not os.path.exists(src) and kit in KITS: src = os.path.join(ROOT, KITS[kit], tool)
    if not os.path.exists(src): print("no such tool: " + tool + (" (KIT=" + kit + ")" if kit else "")); return 2
    if not kit:
        for k, d in KITS.items():
            if os.path.dirname(d) in src: kit = k
    stem = os.path.splitext(os.path.basename(src))[0]; log = TMP + "/ae_" + app + "_" + stem + ".txt"
    js = open(src, encoding="utf-8").read()
    js = re.sub(r"(?m)^[ \t]*//#inline[ \t]+(.+?)[ \t]*$",
                lambda m: open(os.path.normpath(os.path.join(os.path.dirname(src), m.group(1).strip())), encoding="utf-8").read(), js)
    if "%LOG%" in js and "LOG" not in subs: subs["LOG"] = log
    if "%LOG%" in js: log = subs["LOG"]                      # a caller's LOG= is the log read back (QC, Oct 30: reading the
                                                              # default path made every LOG= call exit 1, so runners ignored it)
    for k, v in subs.items(): js = js.replace("%" + k + "%", v)
    left = sorted(set(re.findall(r"%([A-Z][A-Z0-9_]+)%", js)))
    if left: print("unfilled placeholders:", ", ".join(left)); return 2
    run = TMP + "/aerun_" + app + "_" + stem + ".jsx"
    open(run, "w", encoding="utf-8").write(js)
    # the filled-in script is what AE runs: lint it again, so a value pasted into a string can't reach AE as a syntax error
    # (Oct 29: a JSON value with quotes broke a string literal and left AE on a modal dialog)
    LINT = os.environ.get("AE_ES3LINT") or os.path.join(HERE, "es3lint.sh")
    if not os.path.isfile(LINT): print("ES3 LINT MISSING (%s; set AE_ES3LINT) — not run" % LINT); return 1
    lo = subprocess.run(["bash", LINT, run], capture_output=True, text=True)
    if "ALL CLEAN" not in lo.stdout + lo.stderr:
        print(lo.stdout[-1500:] + lo.stderr[-500:]); print("LINT FAILED on the filled script — not run"); return 1
    if not gate: print("WARNING: --nogate: the house lint gate is skipped for this call (QC C3: runners must not pass it)")
    if gate:
        GATE = find_gate()
        if not GATE: gate_info(); print("QC gate MISSING — not run"); return 1
        g = subprocess.run([sys.executable, GATE, run], capture_output=True, text=True)
        if g.returncode != 0: print(g.stdout); print("QC gate FAILED — not run"); return 1
    # D2: AE must already run (never launched from here); D4: no stop flag for this AE and, inside a preflight run, no dialog since
    # its begin; D9: not within READY_S of AE's launch. All before the lock and before anything is sent.
    pid = ae_pid(app)
    if not pid: print("AE NOT RUNNING (%s): nothing sent (exit 5)" % app); return 5
    held = flag_held(app, pid)
    if held: print("G3 STOP FLAG %s: %s (exit 6; nothing sent: clear AE, then relaunch it)" % (flagfile(app), held)); return 6
    since = os.environ.get("AE_G3_SINCE", "")
    if not g3(app, pid, since or utcnow(), "before %s" % stem): return 6   # also proves the breadcrumbs readable before a send
    age = ae_age(pid)
    if age is None: print("AE %s pid %d: launch time unreadable: nothing sent (exit 5)" % (app, pid)); return 5
    if age < READY_S: print("AE %s launched %d s ago: waiting %d s (D9)" % (app, age, READY_S - age)); time.sleep(READY_S - age)
    if not lock(stem, lockwait): return 3
    t0 = utcnow()
    try:
        if os.path.exists(log): os.remove(log)
        # "is running" first: a tell to an AE that is not running would launch it (D2); this script then only answers NOT RUNNING
        apple = ['if application "%s" is running then' % APPS[app],
                 'with timeout of %d seconds' % timeout,
                 'tell application "%s" to DoScriptFile POSIX file "%s"' % (APPS[app], run), 'end timeout',
                 'return "SENT"', 'else', 'return "NOT RUNNING"', 'end if']
        cmd = ["perl", "-e", "alarm %d; exec @ARGV" % (timeout + 10), binpath("osascript")]
        for line in apple: cmd += ["-e", line]
        osa = subprocess.run(cmd, capture_output=True, text=True)
        if osa.stdout.strip() == "NOT RUNNING": print("AE NOT RUNNING (%s) at the send: nothing sent (exit 5)" % app); return 5
        if wait:
            d, n = wait.rsplit(":", 1); n = int(n)
            for _ in range(timeout):
                if os.path.isdir(d) and len([f for f in os.listdir(d) if not f.startswith(".")]) >= n: break
                time.sleep(1)
            time.sleep(0.5)
    finally:
        unlock()
    # D4: the dialog scan after the call, since it started (or since preflight's begin when that is earlier)
    if not g3(app, pid, min(t0, since) if since else t0, "after %s" % stem): return 6
    # D5: osascript's own exit status (perl's alarm kill, an AppleScript error) fails the call whatever the log says
    if osa.returncode != 0:
        print("OSASCRIPT rc %d: %s (exit 1)" % (osa.returncode, (osa.stderr or osa.stdout).strip()[-300:])); return 1
    if os.path.exists(log):
        txt = open(log, encoding="utf-8").read().replace("\r\n", "\n").replace("\r", "\n"); print(txt)
        try:
            ad = os.path.join(LOGS, "aerun_" + app); os.makedirs(ad, exist_ok=True)
            open(os.path.join(ad, time.strftime("%Y%m%d-%H%M%S_") + stem + ".txt"), "w", encoding="utf-8").write(txt)
        except Exception: pass
        err = [l for l in txt.split("\n") if l.startswith("ERR ")]
        if err: print("SCRIPT ERROR (%d ERR line(s) in %s): exit 1" % (len(err), log)); return 1
        last = [l for l in txt.split("\n") if l.strip()][-1:]
        if not last or not last[0].startswith("END"):
            print("NO END LINE in %s (last line %r): the script did not finish through H.run: exit 1" % (log, last[0][:120] if last else "")); return 1
        return 0
    print("NO LOG (" + log + ") — script did not run. Check AE for an open modal dialog."); return 1

if __name__ == "__main__":
    sys.exit(main(sys.argv))
