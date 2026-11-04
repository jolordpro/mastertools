---
id: ai-models-claude-caching-batch-discounts
title: Claude cache reads cost 5% of input on Opus/Sonnet 5.5 (2.5% on Fable 5.1), batch is 50% off, minimum cache block 512 tokens
domain: ai-models
tags: [claude, prompt caching, batch, cache read, fast mode, cost]
applies_to: Claude 5.5 family
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://platform.claude.com/docs/en/models/opus-5-5/overview, https://releasebot.io/updates/anthropic/claude-developer-platform, src:research-frontier-ai]
feeds: [model routing]
conflicts: none
---
Sonnet 5.5 cache read was cut to $0.10 per M on 7 Oct 2026. Fast mode for Opus 5.5 is generally available. Gemini caching on Argon is implicit only.
Other levers listed: cache reads 2.5-10% of input across vendors.

**Use it:** put stable preambles first so the cache hits, and batch anything not interactive.
