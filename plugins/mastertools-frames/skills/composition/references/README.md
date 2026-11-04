---
id: readme
title: Composition Library, how to use it
type: reference
aliases: [start here, library guide, how to load]
tags: [meta, setup]
related: [index, evidence-legend, glossary]
evidence: n/a
updated: 2026-10-20
---

# Composition Library

## Quick answer
- A knowledge base on visual composition for photography, design, cinematography, broadcast and motion.
- Built for AI retrieval: one topic per file, same header on every file, evidence tags on every claim.
- Start at `00-index.md`. It routes any question to the right file.

## What is inside
- `science/`: perception research behind composition (placement, balance, Gestalt, attention, clutter, culture).
- `facets/`: one file per building block (light, value, color, depth, line, shape, hierarchy, space, framing...).
- `photography/`, `cinematography/`, `broadcast-motion/`, `design/`: medium-specific grammar.
- `masters/`: how named artists composed, with documented vs retrofitted claims marked.
- `critique/`: rubric, critique protocol, genre checklists, rule-breaking.
- `systems/`: tools, models, datasets, metric recipes and the build architecture for an evaluator app.
- `glossary.md`: every term with synonyms. `sources.md`: master bibliography.

## How each file is built
- YAML header: `id`, `title`, `type`, `aliases`, `tags`, `related`, `evidence`, `updated`.
- `## Quick answer` first: 2 to 4 lines an AI can quote.
- Then fixed sections, in this order when they apply:
  - Definition
  - Mechanism (why it works)
  - Evidence (tagged)
  - Techniques
  - By medium
  - How to measure
  - Failure modes
  - Critique questions
  - Terms
  - Sources
- Cross-links use file ids in backticks, e.g. `balance`.

## Evidence tags (full rules in `01-evidence-legend.md`)
- `[E-strong]` replicated research
- `[E-mixed]` contested, small or single studies
- `[Practice]` professional consensus without experimental proof
- `[Lore]` popular but unsupported or refuted
- `[Unverified]` from standard texts, not checked against the original this pass
- `[Infer]` this library's own reasoning or suggested threshold
- `[Standard]` a published technical standard
- `[Measured]` a number measured in the frame being judged or our own render

## Three ways to use it
1. Claude Project: upload the whole folder as project knowledge. Ask critiques normally.
2. Claude skill: put `00-index.md`, `01-evidence-legend.md`, `critique/protocol.md` and `critique/rubric.md` in the skill body. Keep the rest as reference files the skill reads on demand.
3. Claude Code app: `systems/architecture.md` and `systems/metric-recipes.md` are the build spec. The rubric weights are machine-usable.

## Maintenance rules
- Add a claim only with a tag and a source.
- Upgrade `[Unverified]` to a real tag after checking the primary text.
- Keep one topic per file. Split a file when it passes about 250 lines.
