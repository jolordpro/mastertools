---
id: ai-models-clef-decision-models-workers-ai
title: Cloudflare Clef (27B) and Clef-flash (9B) are Apache decision models: images in, probabilities out, 64K context, on Workers AI
domain: ai-models
tags: [cloudflare, clef, decision model, workers ai, apache, probabilities, triage]
applies_to: 1 Oct 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://developers.cloudflare.com/changelog/post/2026-10-01-clef-workers-ai/, src:research-frontier-ai]
feeds: [checks tuner M2]
conflicts: none
---
Takes up to four images; fast pass/fail with probabilities. Reinforcement fine-tuning of Clef is by design-partner sign-up. Cloudflare AI Gateway works with Workers AI endpoints.

**Use it:** candidate for per-check flags; user verdicts could tune it.
