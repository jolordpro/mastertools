# Ledger

Shared by challenger, shakedown and stress-test. Edit in `core/`, never in a copy.

One file per project, `.ledger/ledger.md`, read and written by every review
skill. It keeps reviews from becoming a nag and gives delta runs an anchor.
In chat, where no project files exist, emit the ledger block at the end of
the report and tell the human to paste it into the next run.

## Prefixes

| Prefix | Written by |
|---|---|
| `L-` | challenger |
| `SD-` | shakedown |
| `ST-` | stress-test (the pack goes in the source field) |
| `FT-` | Field Test, stress-test's older name; read only |

Read every prefix; write only your own. Continue numbering from the highest
existing ID of your prefix; never restart.

## Run line

Open each run's append with one:

```
- RUN · 2026-10-14 · shakedown · full · tier: Standard · anchor: a1b2c3d (git)
```

For non-git work the anchor is a version and date (`v12 · 2026-10-14`).

## Coverage line

Each run also writes one machine-readable line:

```
- COVER · <run-id> · deep: <paths or section headings> · skimmed: <…> · not: <…>
```

`<run-id>` is `<date> <skill> <anchor>` from the run line. List items are
separated by commas; paths are relative to the project root.

## Entries

Append-only. Supersede an entry by citing its ID; never edit it away.

```
- SD-014 · 2026-10-14 · shakedown · High · Traced · "CR/LF injection in export filename header" · open · at: api/export.js:47
```

Fields: id · date · source (skill, plus pack for ST-) · severity (or type, for
Enhancements) · confidence · one-line summary · status · `at:` location (a file
path with optional `:line`, or for documents a section heading). Optional:
finding type. `at:` is what lets misses be found; always write it.

**Statuses:** `open` · `fixed` · `accepted-risk` · `deferred` · `closed` ·
`clean` (a repeat run found the area clean).

## Rules on every run

- Read the whole ledger first.
- Honor `accepted-risk` and `deferred` from any skill: don't re-report them
  unless severity changed under the current milestone, and then say what
  changed.
- Re-check `fixed` items that sit in this run's deep-coverage zone.
- Update statuses with new entries, never edits.

## Misses

A **MISS** entry records a defect an earlier review should have caught:

```
- MISS · 2026-10-14 · SD-021 · in deep: area of 2026-10-02 shakedown a1b2c3d · src/sync.js
```

`scripts/ledger_miss.py` writes these automatically: a later finding whose
location matches an earlier run's `deep:` area (same file path, or for
documents the same section heading). Anyone may add one by hand. Each miss
becomes an item in that skill's "what first passes miss" list and a new test
case.
