# SCOUT — Templates: the caps made physical

**Built by: Opus 4.8 · July 19, 2026 · v0.1**

Fixed formats. A deliverable that outgrows its template gets cut back to it.
Every header stamps the model and date.

---

## L1 — Recon note (one page, hard cap)

```
# RECON · [topic] · [date] · model: [stamp]
Question: [the one-line ask]
Tier reason: [why L1, one line]

## Lay of the land
[5–10 short findings, each with (S)/(R)/(I) and a link where (S)]

## What I could not establish
[the empty searches, the paywalls, the ambiguities]

## Escalate?
[NO — sufficient · or YES → L2, with the pre-registered questions drafted]
```

---

## L2 — Evidence sheet (one page per lane)

```
# SHEET · [lane name] · [date] · model: [stamp]
Tests: [pre-registered questions or hypothesis IDs]
Budget: [blocks allotted / used]

## Evidence (≤5 bullets, each dated + linked, ladder rung named)
1. …
2. …
[Five is a cap per lane, not a filter. A lane holding more evidence than the
cap is two lanes — split it, never cut real evidence to fit.]

## Verdicts
[per question: FOR / AGAINST / COMPLICATES — one line why]
[grading state: clean / subagent / self-graded — name which and why]
[conflicts: both readings named, or "none found"]

## Where this is weak
[single-source claims · unverified owned facts · alternative reading]

## Transfer note
[one sentence: what this means outside its own domain]
```

---

## L2 — Source log (append-only, written at read time)

```
| # | Source | URL | Rung | Dated | Read | Used for | Flag |
|---|--------|-----|------|-------|------|----------|------|
| 1 | [name] | [link] | primary-doc | 2026-03 | fetched-full / snippet | [claim IDs] | |
```

Rungs: `primary-doc · primary-human · expert-secondary · quality-press ·
aggregator · seo`. A load-bearing claim resting on `aggregator` or below gets
a Flag and a climb attempt.

**Dated** is the source's own publication or last-updated date, not the date
you read it. Unknown is a legal value and it is itself a flag. Per A2, a
source older than the current product cycle carries **(R)**, not **(S)**, on
any version, price, capability, or personnel claim. **(S-via)** rows name the
intermediary in the Source column: `Reuters via TechCrunch`.

---

## L3 — Field-study charter (before session one)

```
# CHARTER · [program] · [date] · model: [stamp]
## The job — one paragraph
## Definition of done — numbered, testable
## Pre-registered questions / hypothesis board — each with a death condition
## Laws in force — deltas from scout defaults only
## Tiers and budget — blocks per phase
## Human checkpoints — what only the user's eyes confirm
## Kill condition — what ends this program early
```

---

## L3 — PROGRAM-STATE.md (loaded first, updated last, every session)

```
# PROGRAM-STATE · [program] · updated [date] · by [model stamp]

## Rulings (append-only)
[decision · date · one line]

## Board (living)
[hypothesis · current verdict · evidence pointer]

## Blocks
[id · status: not-started / in-progress / done · one line]
Statuses flip. Entries never get deleted.

## Open questions for the user
## Deliverables checklist (paths)
## Mixed-session log
[any session showing a model-switch banner, and what it touched]
```

Session ritual, non-negotiable: **open** = read this file, then the charter,
then run one basic sanity check on the freshest artifact before new work.
**close** = write deltas here, commit if in a repo, state the stop reason.

---

## Report register

All human-facing reports ship in the user's stated writing rules: short lines,
findings ranked, breaks written bigger than confirmations, banned-word list
scrubbed, one em dash per paragraph at most, Next Steps block at the end.
