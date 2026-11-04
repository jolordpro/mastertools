---
id: ai-models-claude-dreams-memory-cleanup
title: Anthropic Dreams (research preview) reads up to 100 past sessions plus a memory store and writes a cleaned new store
domain: ai-models
tags: [claude, dreams, memory store, managed agents, research preview]
applies_to: research preview, Oct 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://platform.claude.com/docs/en/managed-agents/dreams, src:research-frontier-ai]
feeds: [advisor memory]
conflicts: none
---
The input store is never touched, output is a merged, cleaned store, billed at normal token rates. Review before use. Not zero-data-retention eligible.

**Use it:** a possible per-studio taste memory with no weights; keep a human review step.
