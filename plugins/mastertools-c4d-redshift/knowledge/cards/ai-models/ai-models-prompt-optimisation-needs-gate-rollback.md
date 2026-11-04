---
id: ai-models-prompt-optimisation-needs-gate-rollback
title: A practitioner write-up says small models fail at prompt optimisation and a gate plus rollback makes the loop safe
domain: ai-models
tags: [prompt optimisation, gepa, rollback, gate, skillopt, self evolving agents]
applies_to: 2026
status: V2
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://dev.to/studiomeyer_io/self-evolving-ai-agents-the-optimizer-is-the-easy-part-3i84, https://arxiv.org/pdf/2605.23904, src:research-frontier-ai]
feeds: [M4 advisor]
conflicts: none
---
Secondary source. Skill-library optimisation papers (SkillOpt, SkillEvo, SAGE) report only authors' own results.

**Use it:** never let an optimiser change live rules without a held-out check and a way back.
