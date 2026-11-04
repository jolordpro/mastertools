# Report

Shared by challenger, shakedown and stress-test. Edit in `core/`, never in a copy.

## Order

1. **Plain verdict, five lines max**, first. The reader must see the two
   findings that matter before anything else.
2. The skill's own sections (calibration, coverage map, findings as work
   orders, and the rest each skill defines).
3. **Run next**, one line, last: the next review in the chain, or "none:
   0 Highs" when the stop rule is met.

Stress Test's tool lane keeps its full 12-part structure. Its part 1 is the
verdict and its Next steps part carries the run-next line.

## The review chain

- **Plans:** challenger → claim check → shakedown on the revision → the human
  approves.
- **Builds:** shakedown and stress-test → fixes → re-check only what was
  fixed.
- **Stop rule:** a pass with 0 Highs, or the human says ship.

## Where the report goes

- Where artifacts exist, fill `assets/report-page.html` (replace the
  `/*REVIEW_DATA*/null` placeholder with the report as JSON: skill, tool,
  date, tier, verdict, works, coverage {deep, skimmed, not, skipped}, findings,
  clean, questions, fix_sequence, next_steps, run_next, ledger), publish it as
  an artifact, and lead the chat reply with the verdict. Sections with no data
  hide themselves; personas and break points are for stress-test's tool lane.
- Otherwise write Markdown with the same order.

## Prose check

Before anything reaches the human, check the report's prose against the
human's stated writing rules (banned words, dash limits, table width). Where
scripts can run: `python3 references/core/assets/prose_check.py REPORT.md`
(rules from `~/.config/mastertools/prose-rules.txt`, else `assets/prose-rules.txt`).
Elsewhere, check by hand against the same rules. Fix what fails; never ship a
report that breaks the reader's own rules.
