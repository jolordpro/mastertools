---
name: timecard
description: >-
  Honest, clock-based time-savings instrumentation plus a persistent Claude
  Time Savings ledger. The rule that makes it honest: the model never
  generates a number — benchmarks come from the human, actual time comes from
  timestamps, and "time saved" is computed in code. Fire this BY DEFAULT
  whenever creating or modifying any script, automation, workflow, or
  pipeline for the user: instrument it with the standard timekeeping block
  unless the user opts out ("skip timekeeping" / --no-timelog). Never
  instrument hooks, plugin scripts, CI jobs, or scripts whose output another
  program reads. Also use
  whenever the user mentions time saved, time savings, ROI, payback,
  benchmarks, "how much time did that save," "this normally takes me X
  minutes," logging to the time-savings table, or wants a summary of
  accumulated savings across scripts and tasks.
---

# Timecard

Track what Claude actually saves, not what it feels like it saves. The whole
mechanism rests on one split:

- **The benchmark comes from the human.** "This normally takes me 45
  minutes" is a fact the user supplies. Record it; never invent it. No
  benchmark supplied → log `benchmark: none`. Do not estimate.
- **The actual time comes from the clock.** Timestamps at start and end of
  the run. Never a narrated guess.
- **"Time saved" is arithmetic done in code**, never prose written by the
  model. `saved = benchmark − (runtime + review)`. Model judgment touches
  the number nowhere.

If the number comes out negative, it stands. A ledger that only records
wins is marketing, not measurement.

---

## First-time setup (for a new user)

Nothing to install beyond `python3`. On first use, create the ledger and,
if the user wants one combined table across all their scripts, point
`TIMECARD_LEDGER` at an absolute path:

```
python3 scripts/timelog.py init
# optional, in ~/.bashrc or ~/.zshrc:
export TIMECARD_LEDGER="$HOME/.timecard/time-savings.csv"
```

That's it. From there, either let Claude instrument scripts (default) or log
runs by hand with `log-run`. Windows users without WSL/Git Bash: use the
Python timekeeping block, not the bash one.

---

## When this fires

**Default-on:** any time a script, automation, or pipeline is being written
or substantially modified for the user, include the timekeeping block (see
Instrumenting below). This is opt-out, not opt-in.

**Never instrument:** scripts that run without the user at the
keyboard or whose output another program reads. The block prints a
`[timecard]` line, can wait for input and writes a ledger where it runs, so it
would leak into their output or stall them. That means:
- hooks (Claude Code start, stop and tool hooks; git hooks);
- plugin and skill scripts;
- CI jobs, launchd and cron jobs, scheduled tasks;
- scripts whose stdout another script parses or pipes on.

**Opt-out signals — honor any of these, no argument:**
- The user says "skip timekeeping," "no timelog," or equivalent while
  commissioning the work.
- The script is trivial glue (a one-liner, a throwaway) where instrumentation
  would outweigh the script. Use judgment; when in doubt, instrument — the
  block costs a few dozen lines.
- Every instrumented script must itself carry a `--no-timelog` flag and
  respect `TIMECARD=off` in the environment, so the user can silence it
  per-run without editing code. (All runtime flags — `--benchmark`,
  `--review-min`, `--source` — work in both `--flag value` and `--flag=value`
  form.)

**On-request:** the user asks to log a time saving, view the ledger, get a
summary, or record a benchmark for a task.

---

## Instrumenting a script

Read `references/timekeeping-blocks.md` and inline the matching block (bash
or Python) into the script. The blocks are self-contained — no dependency on
this skill being installed wherever the script eventually runs. Requirements
every instrumented script must satisfy:

1. **Benchmark is a declared variable or flag** (`--benchmark 45` or
   `--benchmark=45` — the blocks accept both forms, for this flag and for
   `--review-min` and `--source`), documented as human-supplied. Ships empty
   by default. Empty → the row logs
   `benchmark_source: none` and no saved figure. The script never fills it in
   with a guess, and neither do you when writing the script — if the user
   stated a benchmark in conversation, bake that number in and set
   `benchmark_source` to `user_stated`; otherwise leave it empty and tell the
   user how to set it.
2. **Runtime from timestamps.** Epoch seconds at start and end. The block
   handles it.
3. **Review time is asked for, not assumed.** When running interactively
   (tty), the block prompts "Review minutes (Enter for 0):" before logging.
   Non-interactive runs log `review_min: 0` — real, visible, and the user can
   pass `--review-min N` to correct it.
4. **The saved figure is computed inside the block** and printed as a plain
   line: `[timecard] task=X runtime=Ym saved=Zm (benchmark 45m,
   user_stated)`. No adjectives.
5. **The row appends to the ledger CSV** (schema below). Never overwrite,
   never edit prior rows.
6. **Opt-out plumbing**: `--no-timelog` flag and `TIMECARD=off` env check.

**Build cost:** when you finish building or substantially reworking a script,
log one `build` row recording roughly how long the build took (wall-clock of
the working session — ask the user if unclear; don't guess). Gross savings
without build cost is how people convince themselves automation is free.

---

## The ledger

One CSV per project: `.ledger/time-savings.csv` (sits beside the
Challenger/Shakedown ledger if one exists — same directory, different file,
same philosophy). Override location with the `TIMECARD_LEDGER` env var; a
user who wants one global ledger across projects points that var at a fixed
path.

Schema — header row required, append-only (the last column is a version tag
so future format changes stay detectable):

```
date,user,task,event,benchmark_min,benchmark_source,runtime_min,review_min,saved_min,build_cost_min,notes,schema_version
```

- `event`: `run` or `build`. Build rows fill `build_cost_min` and leave the
  run fields empty; run rows do the reverse.
- `benchmark_source`: `user_stated` | `user_timed` | `estimated` | `none`.
  `estimated` exists only for the rare case the user explicitly asks for an
  estimate — it is quarantined and visibly second-class in every summary.
- `saved_min` is computed, never typed. Blank when benchmark is none.

**In plain chat (no persistent filesystem):** emit the CSV row in a code
block and tell the user to append it to their ledger. Same fallback pattern
as the audit skills.

**Path scope matters.** The default ledger path is relative to the working
directory, so scripts run from different folders write to different ledgers.
For one combined ledger across a user's work, set `TIMECARD_LEDGER` to an
**absolute** path in their shell profile (e.g. `~/.timecard/time-savings.csv`).
Mention this the first time a second script is instrumented for someone.

**Spreadsheet safety.** People open this CSV in Excel or Sheets. Free-text
fields (task, user, notes) are sanitized on write so a value starting with
`= + - @` can't execute as a formula. Every writer — `timelog.py`, both
timekeeping blocks — does this; don't hand-append rows that skip it. `check`
flags any unsanitized row already in a ledger.

---

## Logging manual or interactive work

Interactive Claude sessions ("draft this doc with me") are muddier than
scripts because elapsed time includes the user's prompting and steering — and
honestly should, since that's real cost. Log these only when every input
traces to the human or a clock the human read: the user states the benchmark,
the user states (or timed) the session length. Note `runtime user-stated` in
the notes field. If the user can't say how long it took, don't log it —
a missing row is more honest than a reconstructed one.

---

## Summaries and reporting

Use `scripts/timelog.py` for anything beyond a single row — it does the
arithmetic so the model doesn't. `--ledger PATH` is global and goes **before**
the command (or set `TIMECARD_LEDGER`):

```
python3 scripts/timelog.py [--ledger PATH] init
python3 scripts/timelog.py [--ledger PATH] log-build --task X --minutes N [--user U] [--notes ...]
python3 scripts/timelog.py [--ledger PATH] log-run   --task X --runtime-min R
        [--benchmark N --source user_stated|user_timed|estimated]
        [--review-min V] [--user U] [--notes ...]
python3 scripts/timelog.py [--ledger PATH] summary [--task X]
python3 scripts/timelog.py [--ledger PATH] rows    [--task X] [--limit N]   # limit 0 = all
python3 scripts/timelog.py [--ledger PATH] check                            # validate ledger health
```

`summary` reports, per task: run count, gross saved, build cost, **net**
saved, and the payback point (which run the script paid for itself, or how
far it still has to go). `rows` prints the user's minimal view — date, user,
task, saved — plus source flags.

When presenting results:
- Lead with **net**, not gross. Payback status is part of the headline.
- Negative and not-yet-paid-back numbers are reported at the same volume as
  wins.
- Rows with `benchmark_source: estimated` or `none` are broken out
  separately, never blended into the verified total.
- No editorializing. "Net 340 minutes across 22 runs; paid back at run 8"
  is the sentence. Not "an incredible 340 minutes!"

---

## Anti-patterns (do not do these)

- **Inventing the counterfactual.** The model never supplies "how long this
  would have taken a human." Not even a range. Not even hedged.
- **Narrated runtime.** "This took about 3 minutes" is not a timestamp.
- **Typing the saved figure.** If the arithmetic didn't run in code, the
  number doesn't exist.
- **Zero-cost automation.** Reporting gross savings while the build cost sits
  unlogged.
- **Review-time amnesia.** A 40-second script the user checks for 6 minutes
  did not save the benchmark minus 40 seconds.
- **Win-only ledger.** Suppressing negative rows or quietly reframing them.
- **Blending sources.** `estimated` rows averaged into `user_stated` totals.
- **Silent instrumentation removal.** If the user opted out once, that was
  per-script or per-run, not forever — but never re-add it to a script they
  explicitly stripped it from without asking.
- **Hand-rolled CSV.** Never generate a script that builds ledger rows with
  raw `echo`/string concatenation — commas corrupt columns and raw values in
  `awk`/`eval` are an injection hole. Route writes through the Python writer in
  the timekeeping block, always.
- **Trusting negative or non-numeric inputs.** A negative benchmark, review,
  or build cost inflates savings — the one lie the tool exists to prevent.
  Reject or clamp, never record.

---

## References

- `references/timekeeping-blocks.md` — the self-contained bash and Python
  blocks to inline into generated scripts. Read it whenever instrumenting.
  Bash times the run; both blocks delegate validation and CSV writing to one
  shared, injection-safe Python writer.
- `scripts/timelog.py` — ledger init, logging, summary math, and a `check`
  command that validates a ledger's schema and flags unsafe rows. Runs on
  stdlib Python 3; no installs. The ledger carries a `schema_version` column
  so future format changes stay detectable.
