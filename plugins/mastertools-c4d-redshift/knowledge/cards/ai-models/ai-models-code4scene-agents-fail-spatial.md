---
id: ai-models-code4scene-agents-fail-spatial
title: Code4Scene: frontier agents mismatched 20.6% of spatial requirements and 35.8% of correct edits also changed other things
domain: ai-models
tags: [code4scene, 3d agent, unreal, spatial, benchmark, scene edit, held-out]
applies_to: Sep 2026
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://arxiv.org/html/2609.36777v1, src:research-frontier-ai]
feeds: [agent door, eval design]
conflicts: none
---
Tested on Unreal. Agents named: Qwen 3.8 27B, Gemma 4 31B, GLM-5.3 Flash, DeepSeek V4.1 Flash. The benchmark keeps a private held-out half of cases to stop overfitting.

**Use it:** measured checks, not an LLM, are the safety net; copy the private held-out half for our own eval.
