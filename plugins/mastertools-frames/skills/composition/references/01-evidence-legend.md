---
id: evidence-legend
title: Evidence tags and how to weigh them
type: reference
aliases: [evidence tags, confidence levels, tag legend, SAYS vs INFER]
tags: [meta, evidence, epistemics]
related: [index, myths-evidence, rubric, protocol]
evidence: n/a
updated: 2026-10-31
---

# Evidence legend

## Quick answer
- Every claim carries one tag. Weight critique by tag: hard-score `[E-strong]`, advise on `[Practice]`, mention `[Lore]` only as a note.
- `SAYS:` marks what a source states. `[Infer]` marks this library's reasoning.

## Tags
- `[E-strong]`: replicated across studies, methods or labs.
- `[E-mixed]`: contested, small samples, single studies, or effects that depend on image type.
- `[Practice]`: strong professional consensus (schools, masters, standards bodies) without experimental proof.
- `[Lore]`: widely repeated, but unsupported or refuted in controlled tests.
- `[Unverified]`: drawn from canonical texts or common knowledge, not checked against the primary source this pass. Treat as `[Practice]` until checked.
- `[Infer]`: this library's reasoning, or a starting threshold chosen for software. Not a research finding.
- `[Standard]`: a published technical standard (EBU, SMPTE, W3C).
- `[Measured]`: a number measured in the frame being judged or in our own render (a `look.py` or `value_plan.py` metric, or a test render). Name the metric and the frame (`subject ΔL* 9, F1`). True for that frame only.
- `[A (user)]`: the user's own note, ruling or chosen reference. Outranks every other tag, and a measured number never overrides it. Never relabel the user's words as research or practice.

## Markers
- `SAYS:` paraphrase or short quote of the source.
- `DOC:` documented by the artist, studio or a primary record.
- `RETRO:` analysis applied after the fact by others.

## How to use tags in a critique
- Scores: only mechanisms with `[E-strong]` or `[Standard]` support may move a score by more than 1 point.
- Advice: `[Practice]` items become suggestions with a reason.
- Never penalize work for missing a `[Lore]` rule (thirds, golden spiral).
- When two tags conflict, state both and the context that decides.

## Measurements
- The number is `[Measured]`. What it means takes the tag of the rule or threshold it is checked against. Most `look.py` thresholds are `[Infer]`; contrast ratios are `[Standard]`.
- So `[Measured]` alone never moves a score by more than 1 point. Measured against a `[Standard]` or `[E-strong]` rule, it may.
- A pattern measured in one frame or project is `[Infer]` until it holds in others, then `[Practice]`. It never becomes `[E-strong]` from our own frames.

## Across skills
The same evidence carries these labels in the sibling skills. When a note cites one, translate it; never mix systems in one note.

| Kind of evidence | composition | elevate | redshift |
|---|---|---|---|
| Primary source or published standard, read in full | `[E-strong]`, `[Standard]` | V | `[V]` (dated Maxon page) |
| Derived from a primary fact | `[Infer]` (reasoning from a tagged source) | D | `[D]` |
| Measured in our own render or frame | `[Measured]` | M | none yet |
| Practitioner or teaching practice | `[Practice]`; `[Unverified]` until checked | P | `[P]` |
| Contested or single-study research | `[E-mixed]` | P (say "mixed") | none |
| Test range or starting threshold | `[Infer]` (software thresholds) | T | `[T]` |
| Art direction, or the user's call | `[A (user)]` for the user's words; an unapproved look has no tag | A, A (user) | `[A]` |
| Popular but refuted | `[Lore]` | none (don't cite) | none |
| Asserted, then failed checking | none | none | `[R]` (never use) |

## Known limits of the research base
- Most lab studies use Western university students and simple stimuli. Effects on complex artworks tend to be smaller.
- Aesthetic datasets encode crowd taste (photo contests, web users), not broadcast design taste.
- Image statistics describe art. They do not prove the statistics cause beauty.
- Benchmark numbers for AI models come mostly from the authors' own papers, often preprints.
