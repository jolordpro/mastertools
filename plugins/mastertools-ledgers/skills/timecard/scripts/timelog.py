#!/usr/bin/env python3
"""timecard ledger tool — the arithmetic lives here, not in the model.

Commands:
  init        create the ledger CSV with header
  log-build   record build/rework cost for a task
  log-run     record one run (computes saved_min in code)
  summary     per-task net savings, build cost, payback point
  rows        print recent rows (minimal view: date, user, task, saved)
  check       validate a ledger's health (schema, numerics, injection guards)

Ledger schema (append-only), last column is a schema version tag:
  date,user,task,event,benchmark_min,benchmark_source,runtime_min,
  review_min,saved_min,build_cost_min,notes,schema_version

Notes on honesty & safety:
- Benchmarks are human-supplied. This tool never invents one.
- saved_min is computed here, never typed.
- Negative benchmark / build / review are rejected or clamped, never allowed
  to inflate savings.
- Free-text cells (task, user, notes) starting with = + - @ tab or CR are
  prefixed with an apostrophe so spreadsheets don't execute them as formulas.
"""

import argparse
import csv
import getpass
import os
import sys
from datetime import datetime
from pathlib import Path

SCHEMA_VERSION = "1"
HEADER = [
    "date", "user", "task", "event", "benchmark_min", "benchmark_source",
    "runtime_min", "review_min", "saved_min", "build_cost_min", "notes",
    "schema_version",
]
REQUIRED_READ = {"task", "event", "benchmark_source", "saved_min",
                 "build_cost_min"}
VALID_SOURCES = {"user_stated", "user_timed", "estimated", "none"}
DEFAULT_LEDGER = os.environ.get("TIMECARD_LEDGER", ".ledger/time-savings.csv")

# ------------------------------------------------------------------ helpers

def ledger_path(args):
    return Path(args.ledger)


def now_stamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def default_user():
    try:
        return getpass.getuser() or "unknown"
    except Exception:
        return "unknown"


def fnum(value):
    """Parse a ledger cell to float, or None if blank/none/unparseable."""
    v = (value or "").strip().lower()
    if v in ("", "none", "n/a"):
        return None
    try:
        return float(v)
    except ValueError:
        return None


def safe_text(s):
    """Neutralize spreadsheet formula injection in human-controlled fields."""
    s = "" if s is None else str(s)
    return ("'" + s) if s[:1] in ("=", "+", "-", "@", "\t", "\r") else s


def fmt(minutes):
    sign = "-" if minutes < 0 else ""
    m = abs(minutes)
    # round(m, 1) so 59.99 displays as "1.0h (60.0m)", not "60.0m"
    if round(m, 1) >= 60:
        return f"{sign}{m/60:.1f}h ({sign}{m:.1f}m)"
    return f"{sign}{m:.1f}m"


def ensure_ledger(path):
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    # 'x' mode: cold-start race safe — first writer wins, others fall through.
    try:
        with path.open("x", newline="") as f:
            csv.writer(f).writerow(HEADER)
        print(f"[timecard] created ledger at {path}")
    except FileExistsError:
        pass


def append_row(path, row):
    ensure_ledger(path)
    # Guard the seam check can't cover: rows are written in canonical HEADER
    # order, so appending to a file whose header is reordered or foreign
    # would misalign columns. Refuse rather than corrupt.
    with path.open(newline="") as f:
        first = f.readline().rstrip("\r\n")
    if first == "":
        with path.open("a", newline="") as f:
            csv.writer(f).writerow(HEADER)
    elif first.split(",") != HEADER:
        sys.exit(f"[timecard] ledger {path} header doesn't match schema "
                 f"v{SCHEMA_VERSION} (column order matters — appending would "
                 f"misalign the row). Run `check`, fix the header, or point "
                 f"--ledger / TIMECARD_LEDGER at a fresh file.")
    with path.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=HEADER, extrasaction="ignore")
        w.writerow(row)


def read_rows(path):
    if not path.exists():
        sys.exit(f"[timecard] no ledger at {path} — run `init` first "
                 f"(or set TIMECARD_LEDGER / put --ledger before the command)")
    with path.open(newline="") as f:
        reader = csv.DictReader(f)
        cols = set(reader.fieldnames or [])
        missing = REQUIRED_READ - cols
        if missing:
            print(f"[timecard] warning: ledger {path} is missing expected "
                  f"columns {sorted(missing)} — it may be an older or "
                  f"hand-edited schema. Reading best-effort.", file=sys.stderr)
        return [r for r in reader]


def task_filter(rows, query):
    """Filter rows by task, matching the raw query OR its sanitized form —
    a task logged as '=report' is stored as ''=report' and must still be
    findable by the name the user actually typed."""
    if not query:
        return rows
    accepted = {query, safe_text(query)}
    return [r for r in rows if r.get("task") in accepted]


def norm_task(name):
    """Fold case and separators to catch task-name drift (csv-cleanup vs
    csv_cleanup vs 'CSV cleanup')."""
    return "".join(c for c in (name or "").lower() if c.isalnum())


# ------------------------------------------------------------------ commands

def cmd_init(args):
    path = ledger_path(args)
    if path.exists():
        print(f"[timecard] ledger already exists at {path}")
    else:
        ensure_ledger(path)


def cmd_log_build(args):
    if args.minutes < 0:
        sys.exit("[timecard] build minutes cannot be negative "
                 "(a build that cost negative time is not a thing)")
    row = {k: "" for k in HEADER}
    row.update({
        "date": now_stamp(),
        "user": safe_text(args.user or default_user()),
        "task": safe_text(args.task),
        "event": "build",
        "build_cost_min": f"{args.minutes:.10g}",
        "notes": safe_text(args.notes or ""),
        "schema_version": SCHEMA_VERSION,
    })
    append_row(ledger_path(args), row)
    print(f"[timecard] build logged: task={args.task} "
          f"build_cost={fmt(args.minutes)}")


def cmd_log_run(args):
    if args.benchmark is not None and args.source is None:
        sys.exit("[timecard] --benchmark requires --source "
                 "(user_stated | user_timed | estimated)")
    if args.source is not None and args.benchmark is None:
        sys.exit("[timecard] --source requires --benchmark "
                 "(a provenance claim with no benchmark is meaningless)")
    if args.benchmark is not None and args.benchmark < 0:
        sys.exit("[timecard] benchmark cannot be negative")

    runtime = args.runtime_min
    if runtime is None and args.runtime_sec is not None:
        runtime = args.runtime_sec / 60.0
    if runtime is None:
        sys.exit("[timecard] provide --runtime-min or --runtime-sec")
    clamp_notes = []
    if runtime < 0:
        print("[timecard] warning: negative runtime clamped to 0 "
              "(clock skew?)", file=sys.stderr)
        runtime = 0.0
        clamp_notes.append("runtime-clamped-from-negative")

    review = args.review_min or 0.0
    if review < 0:
        print("[timecard] warning: negative review time clamped to 0",
              file=sys.stderr)
        review = 0.0
        clamp_notes.append("review-clamped-from-negative")

    saved = None
    if args.benchmark is not None:
        saved = args.benchmark - (runtime + review)

    row = {k: "" for k in HEADER}
    row.update({
        "date": now_stamp(),
        "user": safe_text(args.user or default_user()),
        "task": safe_text(args.task),
        "event": "run",
        "benchmark_min": "" if args.benchmark is None else f"{args.benchmark:.10g}",
        "benchmark_source": args.source or "none",
        "runtime_min": f"{runtime:.2f}",
        "review_min": f"{review:.10g}",
        "saved_min": "" if saved is None else f"{saved:.2f}",
        "notes": safe_text("; ".join(filter(None, [args.notes or ""]
                                            + clamp_notes))),
        "schema_version": SCHEMA_VERSION,
    })
    append_row(ledger_path(args), row)

    if saved is None:
        print(f"[timecard] run logged: task={args.task} "
              f"runtime={fmt(runtime)} review={fmt(review)} "
              f"saved=unknown (no benchmark supplied)")
    else:
        print(f"[timecard] run logged: task={args.task} "
              f"runtime={fmt(runtime)} review={fmt(review)} "
              f"saved={fmt(saved)} (benchmark {args.benchmark:g}m, "
              f"{args.source})")


def _row_date(r):
    return r.get("date", "")


def cmd_summary(args):
    rows = task_filter(read_rows(ledger_path(args)), args.task)
    if not rows:
        print("[timecard] no matching rows")
        return

    # task-name drift detection
    seen = {}
    for r in rows:
        seen.setdefault(norm_task(r.get("task")), set()).add(r.get("task"))
    for variants in seen.values():
        if len(variants) > 1:
            print(f"[timecard] warning: these task names look like the same "
                  f"task but won't be grouped: {sorted(variants)}",
                  file=sys.stderr)

    tasks = {}
    for r in rows:
        tasks.setdefault(r.get("task"), []).append(r)

    grand_net = 0.0
    grand_estimated = 0.0
    any_estimated = False

    for task in sorted(tasks, key=lambda t: t or ""):
        trows = sorted(tasks[task], key=_row_date)  # chronological for payback
        builds = [fnum(r.get("build_cost_min")) or 0.0
                  for r in trows if r.get("event") == "build"]
        runs = [r for r in trows if r.get("event") == "run"]

        build_cost = sum(builds)
        verified = [r for r in runs
                    if fnum(r.get("saved_min")) is not None
                    and r.get("benchmark_source") in ("user_stated",
                                                      "user_timed")]
        estimated = [r for r in runs
                     if fnum(r.get("saved_min")) is not None
                     and r.get("benchmark_source") == "estimated"]
        unbenchmarked = [r for r in runs if fnum(r.get("saved_min")) is None]

        gross = sum(fnum(r.get("saved_min")) for r in verified)
        est_gross = sum(fnum(r.get("saved_min")) for r in estimated)
        net = gross - build_cost

        payback = None
        if build_cost > 0 and verified:
            cum = 0.0
            for i, r in enumerate(verified, 1):
                cum += fnum(r.get("saved_min"))
                if cum >= build_cost:
                    payback = i
                    break

        print(f"\n{task}")
        print(f"  runs: {len(runs)} "
              f"({len(verified)} verified, {len(estimated)} estimated, "
              f"{len(unbenchmarked)} unbenchmarked)")
        print(f"  gross saved (verified): {fmt(gross)}")
        print(f"  build cost:             {fmt(build_cost)}")
        print(f"  net saved:              {fmt(net)}")
        if build_cost > 0:
            if payback:
                print(f"  payback:                run {payback} of "
                      f"{len(verified)}")
            else:
                gap = build_cost - gross
                print(f"  payback:                not yet — {fmt(gap)} to go")
        if estimated:
            any_estimated = True
            print(f"  estimated-source rows (excluded from net): "
                  f"{fmt(est_gross)} across {len(estimated)} runs")

        grand_net += net
        grand_estimated += est_gross

    print(f"\n{'-'*52}")
    print(f"TOTAL net saved (verified benchmarks): {fmt(grand_net)}")
    if any_estimated:
        print(f"TOTAL estimated-source (quarantined):  {fmt(grand_estimated)}")


def cmd_rows(args):
    rows = task_filter(read_rows(ledger_path(args)), args.task)
    # --limit 0 (or negative) means "all"; a positive N takes the last N.
    if args.limit and args.limit > 0:
        rows = rows[-args.limit:]
    if not rows:
        print("[timecard] no matching rows")
        return
    def clip(s, w):
        return s if len(s) <= w else s[:w - 1] + "…"
    uw = min(20, max(6, max((len(r.get("user", "")) for r in rows),
                            default=0) + 2))
    tw = min(40, max(12, max((len(r.get("task", "")) for r in rows),
                             default=0) + 2))
    print(f"{'date':<17}{'user':<{uw}}{'task':<{tw}}{'event':<7}"
          f"{'saved':>13}  src")
    for r in rows:
        saved = fnum(r.get("saved_min"))
        if r.get("event") == "build":
            saved_s = f"-{fnum(r.get('build_cost_min')) or 0:.10g}m (build)"
        elif saved is None:
            saved_s = "—"
        else:
            saved_s = f"{saved:+.1f}m"
        print(f"{r.get('date',''):<17}{clip(r.get('user',''), uw):<{uw}}"
              f"{clip(r.get('task',''), tw):<{tw}}{r.get('event',''):<7}"
              f"{saved_s:>13}  {r.get('benchmark_source','')}")


def cmd_check(args):
    path = ledger_path(args)
    if not path.exists():
        sys.exit(f"[timecard] no ledger at {path}")
    with path.open(newline="") as f:
        reader = csv.reader(f)
        header = next(reader, [])
        raw = list(reader)
    problems = []
    if header != HEADER:
        problems.append(f"header differs from expected schema "
                        f"v{SCHEMA_VERSION} (column ORDER matters — appends "
                        f"write canonical order): got {header}")
    idx = {name: header.index(name) for name in header}
    for n, cells in enumerate(raw, start=2):
        if len(cells) != len(header):
            problems.append(f"line {n}: {len(cells)} fields, expected "
                            f"{len(header)}")
            continue
        src = cells[idx["benchmark_source"]] if "benchmark_source" in idx else ""
        if src and src not in VALID_SOURCES:
            problems.append(f"line {n}: unknown benchmark_source '{src}'")
        for field in ("benchmark_min", "runtime_min", "review_min",
                      "saved_min", "build_cost_min"):
            if field in idx:
                val = cells[idx[field]]
                if val and fnum(val) is None:
                    problems.append(f"line {n}: {field}='{val}' not numeric")
        for field in ("task", "user", "notes"):
            if field in idx and cells[idx[field]][:1] in ("=", "+", "-",
                                                           "@", "\t", "\r"):
                problems.append(f"line {n}: {field} starts with a formula "
                                f"character and was NOT neutralized — pre-fix "
                                f"row (opening in a spreadsheet is unsafe)")
    if problems:
        print(f"[timecard] {len(problems)} issue(s) in {path}:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)
    print(f"[timecard] {path}: {len(raw)} rows, schema OK, no issues found")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--ledger", default=DEFAULT_LEDGER,
                   help="ledger path (place BEFORE the command). "
                        "Default: $TIMECARD_LEDGER or .ledger/time-savings.csv")
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init")

    b = sub.add_parser("log-build")
    b.add_argument("--task", required=True)
    b.add_argument("--minutes", type=float, required=True,
                   help="wall-clock minutes the build took (human-supplied)")
    b.add_argument("--user")
    b.add_argument("--notes")

    r = sub.add_parser("log-run")
    r.add_argument("--task", required=True)
    r.add_argument("--benchmark", type=float,
                   help="human-supplied benchmark in minutes; omit if unknown")
    r.add_argument("--source",
                   choices=["user_stated", "user_timed", "estimated"])
    r.add_argument("--runtime-min", type=float)
    r.add_argument("--runtime-sec", type=float)
    r.add_argument("--review-min", type=float, default=0.0)
    r.add_argument("--user")
    r.add_argument("--notes")

    s = sub.add_parser("summary")
    s.add_argument("--task")

    w = sub.add_parser("rows")
    w.add_argument("--task")
    w.add_argument("--limit", type=int, default=20,
                   help="show last N rows; 0 = all")

    c = sub.add_parser("check")

    args = p.parse_args()
    {"init": cmd_init, "log-build": cmd_log_build, "log-run": cmd_log_run,
     "summary": cmd_summary, "rows": cmd_rows, "check": cmd_check}[args.cmd](args)


if __name__ == "__main__":
    main()
