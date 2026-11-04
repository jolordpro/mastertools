# Timekeeping blocks

Self-contained blocks to inline into scripts you generate. They must run
anywhere the script runs — no dependency on the timecard skill being installed
there. The **only** runtime requirement is `python3`, which is used for the
one job bash must not do by hand: writing CSV. (Hand-rolled `echo` CSV corrupts
on any comma and `awk` on a raw benchmark value is a code-injection hole — both
are avoided by routing the write through Python.)

Design rules, non-negotiable:
- Benchmark is human-supplied or absent. Never pre-fill a guess.
- Runtime from timestamps; `saved` computed in code, never narrated.
- Negative benchmark/review is rejected or clamped — savings never inflate.
- Free-text fields (task, user, notes) that begin with `= + - @` tab or CR are
  prefixed with `'` so spreadsheets don't run them as formulas.
- Appends to the ledger; never rewrites it. If the existing ledger's header
  doesn't match the schema below (column order matters), the block refuses to
  append and prints the row instead — a misaligned row is corruption, a
  printed row is recoverable.
- Runtime flags accept **both** `--flag=value` and `--flag value` forms:
  `--benchmark`, `--review-min`, `--source` (user_stated | user_timed), and
  `--no-timelog`. `TIMECARD=off` in the environment also disables logging.

Schema (last column is a version tag so future changes stay detectable):

```
date,user,task,event,benchmark_min,benchmark_source,runtime_min,review_min,saved_min,build_cost_min,notes,schema_version
```

**Twin note:** the safe-writer logic below is duplicated across the bash block,
the Python block, and `scripts/timelog.py`. If you change validation or the
schema, change all three together — divergence between them is the exact bug
class this design exists to prevent. Known intentional asymmetries: bash
measures wall-clock (`date +%s`, so negative deltas are clamped and noted),
Python measures monotonic time (negative impossible); on a header-mismatched
ledger `timelog.py` refuses before writing, while the blocks refuse *and print
the row* so an end-of-run refusal never loses data.

---

## Bash

Bash only measures time and (optionally) asks for review minutes. Everything
that must be correct — validation, the arithmetic, safe CSV writing — happens
in the embedded Python. Put SETUP at the top, LOG at the end.

```bash
# ═══ timecard SETUP ═══ (opt out: --no-timelog, or TIMECARD=off)
TC_TASK="my-task-name"          # stable kebab-case name; groups runs in the ledger
TC_BENCHMARK=""                 # HUMAN-SUPPLIED minutes, e.g. "45". Empty = no estimate is made.
TC_SOURCE="user_stated"         # user_stated | user_timed (only used if benchmark set)
TC_LEDGER="${TIMECARD_LEDGER:-.ledger/time-savings.csv}"
TC_ON=1; TC_REVIEW=""; TC_PREV=""
for arg in "$@"; do
  case "$TC_PREV" in
    benchmark)  TC_BENCHMARK="$arg"; TC_PREV=""; continue ;;
    review-min) TC_REVIEW="$arg";    TC_PREV=""; continue ;;
    source)     TC_SOURCE="$arg";    TC_PREV=""; continue ;;
  esac
  case "$arg" in
    --no-timelog)     TC_ON=0 ;;
    --benchmark=*)    TC_BENCHMARK="${arg#*=}" ;;
    --review-min=*)   TC_REVIEW="${arg#*=}" ;;
    --source=*)       TC_SOURCE="${arg#*=}" ;;
    --benchmark)      TC_PREV="benchmark" ;;
    --review-min)     TC_PREV="review-min" ;;
    --source)         TC_PREV="source" ;;
  esac
done
[ -n "$TC_PREV" ] && echo "[timecard] --$TC_PREV needs a value; ignoring" >&2
[ "${TIMECARD:-on}" = "off" ] && TC_ON=0
TC_START=$(date +%s)

# ... script body ...

# ═══ timecard LOG ═══
if [ "$TC_ON" = "1" ]; then
  TC_END=$(date +%s)
  TC_RUNTIME_SEC=$((TC_END - TC_START))
  if [ -z "$TC_REVIEW" ] && [ -t 0 ]; then
    printf "[timecard] Review minutes (Enter for 0): "
    read -r TC_REVIEW
  fi
  TC_REVIEW="${TC_REVIEW:-0}"
  TIMECARD_LEDGER="$TC_LEDGER" python3 - \
    "$TC_TASK" "$TC_BENCHMARK" "$TC_SOURCE" "$TC_RUNTIME_SEC" "$TC_REVIEW" "${USER:-}" <<'PY'
import csv, os, sys, getpass
from datetime import datetime
task, benchmark, source, runtime_sec, review, user = (sys.argv[1:7] + [""]*6)[:6]
HEADER = ["date","user","task","event","benchmark_min","benchmark_source",
          "runtime_min","review_min","saved_min","build_cost_min","notes","schema_version"]
def num(s):
    s = (s or "").strip()
    if s == "" or s.lower() in ("none","n/a"): return None
    try: return float(s)
    except ValueError: return None
def safe(s):
    s = "" if s is None else str(s)
    return ("'"+s) if s[:1] in ("=","+","-","@","\t","\r") else s
notes = ""
rt = num(runtime_sec)
if rt is not None and rt < 0:
    print("[timecard] negative runtime clamped to 0 (clock skew?)", file=sys.stderr)
    notes = "runtime-clamped-from-negative"
runtime = max(0.0, (rt or 0.0)/60.0)
b = num(benchmark)
if benchmark.strip() and b is None:
    print(f"[timecard] --benchmark={benchmark!r} is not a number; ignoring",
          file=sys.stderr)
if b is not None and b < 0:
    print("[timecard] benchmark < 0 ignored", file=sys.stderr); b = None
v = num(review); v = 0.0 if (v is None or v < 0) else v
if b is not None and source not in ("user_stated","user_timed"):
    print(f"[timecard] --source={source!r} invalid (user_stated|user_timed); "
          f"using user_stated", file=sys.stderr)
    source = "user_stated"
src = source if b is not None else "none"
saved = None if b is None else b-(runtime+v)
try: user = user or getpass.getuser() or "unknown"
except Exception: user = "unknown"
ledger = os.environ.get("TIMECARD_LEDGER", ".ledger/time-savings.csv")
os.makedirs(os.path.dirname(ledger) or ".", exist_ok=True)
row = [datetime.now().strftime("%Y-%m-%d %H:%M"), safe(user), safe(task),
       "run", "" if b is None else f"{b:.10g}", src, f"{runtime:.2f}",
       f"{v:.10g}", "" if saved is None else f"{saved:.2f}", "", safe(notes), "1"]
try:
    f = open(ledger, "x", newline=""); new = True          # cold-start race safe
except FileExistsError:
    f = open(ledger, "a", newline=""); new = False
if not new:
    with open(ledger, newline="") as rf:
        first = rf.readline().rstrip("\r\n")
    if first == "":
        new = True                                          # adopt an empty file
    elif first.split(",") != HEADER:
        f.close()
        print("[timecard] ledger header differs from schema v1 — row NOT "
              "appended (run timelog.py check). Row was:", file=sys.stderr)
        csv.writer(sys.stdout).writerow(row)
        sys.exit(0)
with f:
    w = csv.writer(f)
    if new: w.writerow(HEADER)
    w.writerow(row)
if saved is None:
    print(f"[timecard] task={task} runtime={runtime:.2f}m review={v:g}m "
          f"saved=unknown (no benchmark set — pass --benchmark=N)")
else:
    print(f"[timecard] task={task} runtime={runtime:.2f}m review={v:g}m "
          f"saved={saved:.2f}m (benchmark {b:g}m, {src})")
PY
fi
```

---

## Python

A normal Python program. The `_tc_write` logic inside `tc_log()` is the shared
safe writer; `tc_log()` measures runtime and calls it.

```python
# ═══ timecard ═══ (opt out: --no-timelog, or TIMECARD=off)
import csv, getpass, os, sys, time
from datetime import datetime
from pathlib import Path

TC_TASK = "my-task-name"       # stable kebab-case name; groups runs in the ledger
TC_BENCHMARK = None            # HUMAN-SUPPLIED minutes, e.g. 45. None = no estimate is made.
TC_SOURCE = "user_stated"      # user_stated | user_timed (only used if benchmark set)
TC_LEDGER = Path(os.environ.get("TIMECARD_LEDGER", ".ledger/time-savings.csv"))
_TC_HEADER = ["date","user","task","event","benchmark_min","benchmark_source",
              "runtime_min","review_min","saved_min","build_cost_min","notes","schema_version"]

def _tc_num(s):
    s = str(s).strip() if s is not None else ""
    if s == "" or s.lower() in ("none","n/a"): return None
    try: return float(s)
    except ValueError: return None

def _tc_safe(s):
    s = "" if s is None else str(s)
    return ("'"+s) if s[:1] in ("=","+","-","@","\t","\r") else s

def _tc_user():
    try: return getpass.getuser() or "unknown"
    except Exception: return "unknown"

def _tc_flag(name, cast=str):
    """Accepts --name=value and --name value."""
    argv = sys.argv[1:]
    for i, a in enumerate(argv):
        raw = None
        if a.startswith(f"--{name}="):
            raw = a.split("=", 1)[1]
        elif a == f"--{name}":
            if i + 1 >= len(argv):
                print(f"[timecard] --{name} needs a value; ignoring",
                      file=sys.stderr)
                return None
            raw = argv[i + 1]
        if raw is not None:
            try: return cast(raw)
            except (ValueError, TypeError):
                print(f"[timecard] --{name}={raw!r} is not valid; ignoring",
                      file=sys.stderr)
                return None
    return None

TC_ON = ("--no-timelog" not in sys.argv) and (os.environ.get("TIMECARD","on") != "off")
_bench_flag = _tc_flag("benchmark", float)
if _bench_flag is not None:
    TC_BENCHMARK = _bench_flag
_src_flag = _tc_flag("source")
if _src_flag is not None:
    if _src_flag in ("user_stated", "user_timed"):
        TC_SOURCE = _src_flag
    else:
        print(f"[timecard] --source={_src_flag!r} invalid "
              f"(user_stated|user_timed); keeping {TC_SOURCE}", file=sys.stderr)
_tc_start = time.monotonic()

def tc_log(review_min=None):
    """Call once, at successful completion."""
    if not TC_ON:
        return
    runtime = max(0.0, (time.monotonic() - _tc_start) / 60.0)
    if review_min is None:
        review_min = _tc_flag("review-min", float)
    if review_min is None:
        if sys.stdin.isatty():
            try:
                raw = input("[timecard] Review minutes (Enter for 0): ").strip()
            except EOFError:
                raw = ""                       # Ctrl-D = "no review time"
            review_min = _tc_num(raw) or 0.0
        else:
            review_min = 0.0
    if review_min < 0:
        review_min = 0.0
    b = TC_BENCHMARK
    if b is not None and b < 0:
        print("[timecard] benchmark < 0 ignored", file=sys.stderr); b = None
    src = TC_SOURCE if b is not None else "none"
    saved = None if b is None else b - (runtime + review_min)
    TC_LEDGER.parent.mkdir(parents=True, exist_ok=True)
    row = [datetime.now().strftime("%Y-%m-%d %H:%M"), _tc_safe(_tc_user()),
           _tc_safe(TC_TASK), "run", "" if b is None else f"{b:.10g}", src,
           f"{runtime:.2f}", f"{review_min:.10g}",
           "" if saved is None else f"{saved:.2f}", "", "", "1"]
    try:
        f = TC_LEDGER.open("x", newline=""); new = True     # cold-start race safe
    except FileExistsError:
        f = TC_LEDGER.open("a", newline=""); new = False
    if not new:
        with TC_LEDGER.open(newline="") as rf:
            first = rf.readline().rstrip("\r\n")
        if first == "":
            new = True                                       # adopt an empty file
        elif first.split(",") != _TC_HEADER:
            f.close()
            print("[timecard] ledger header differs from schema v1 — row NOT "
                  "appended (run timelog.py check). Row was:", file=sys.stderr)
            csv.writer(sys.stdout).writerow(row)
            return
    with f:
        w = csv.writer(f)
        if new: w.writerow(_TC_HEADER)
        w.writerow(row)
    if saved is None:
        print(f"[timecard] task={TC_TASK} runtime={runtime:.2f}m "
              f"review={review_min:g}m saved=unknown (no benchmark set — "
              f"pass --benchmark=N)")
    else:
        print(f"[timecard] task={TC_TASK} runtime={runtime:.2f}m "
              f"review={review_min:g}m saved={saved:.2f}m "
              f"(benchmark {b:g}m, {src})")

# ... script body ...
# tc_log()   # call at the end of main()
```

---

## Placement notes

- **Task naming:** stable, kebab-case, one name per script (`nhl-logo-patch`,
  `csv-cleanup`). Renaming a task orphans its history; `summary` warns when two
  names look like the same task, but it can't merge them for you.
- **Ledger location for multiple scripts:** the default path is *relative to
  the working directory*, so running scripts from different folders scatters
  ledgers. For one combined ledger, set `TIMECARD_LEDGER` to an **absolute**
  path (e.g. `~/.timecard/time-savings.csv`) in the user's shell profile.
- **Runtime source override:** a user who timed themselves can pass
  `--source user_timed` at run time; anything else falls back to the baked-in
  `TC_SOURCE` with a warning. `estimated` is deliberately not settable from
  the blocks — an estimate is a conversation with the ledger tool, not a flag.
- **Failed runs:** default is to log nothing — a crashed run saved nothing and
  its partial runtime is noise. Put the LOG block after the work, not in a
  trap, unless the user wants failures tracked (log them with `saved` blank,
  `notes=failed`).
- **Build rows:** the blocks log runs only. Log build cost once via
  `timelog.py log-build` when the script is finished; the wall-clock comes from
  the human.
- **Windows:** the bash block is POSIX shell — it runs in WSL/Git Bash/macOS/
  Linux, not `cmd.exe` or PowerShell. On native Windows, use the Python block.
- **Don't stack loggers:** if the user already has a homegrown timing block,
  migrate it to this schema or leave it — never run two logging systems into
  one file.
