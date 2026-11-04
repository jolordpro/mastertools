---
id: ai-models-claude-model-prices-q3-2026
title: Claude API prices per M tokens: Haiku 5.5 $0.10/$0.50, Sonnet 5.5 $2/$10, Opus 5.5 $4/$20, Fable 5.1 $10/$50
domain: ai-models
tags: [claude, anthropic, price, haiku, sonnet, opus, fable, tokens]
applies_to: Claude 5.5 family, Oct 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://platform.claude.com/docs/en/models/opus-5-5/overview, https://www.gradually.ai/en/claude-models/, src:research-frontier-ai]
feeds: [PLAN 3, model routing]
conflicts: none
---
Haiku 5.5 (7 Oct): $0.10 in / $0.50 out up to a 100K prompt, then $0.50 / $2.50; 1M context; built for routing, extraction, sub-agents. Sonnet 5.5 (28 Sep): $2 / $10, 1M context. Opus 5.5 (22 Sep): $4 / $20, 1M context, 128K output. Fable 5.1 (1 Sep): $10 / $50, top tier. Opus 5 (24 Jul): $5 / $25.
Model facts decay fast; re-read the docs before quoting.

**Use it:** plan tiers as Haiku triage, Sonnet work, Opus gate, Fable rare; same API and cache across them.
