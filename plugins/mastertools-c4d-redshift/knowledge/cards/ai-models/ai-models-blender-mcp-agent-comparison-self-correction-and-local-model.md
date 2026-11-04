---
id: ai-models-blender-mcp-agent-comparison-self-correction-and-local-model
title: In a Blender MCP test, Claude and Codex rendered, checked and corrected their own frames; a local Qwen 3.5 122B 4-bit model on a 128 GB Mac finished a donut in about 8 minutes
domain: ai-models
tags: [blender mcp, claude code, codex, qwen 3.5, lm studio, local model, mcp setup, port 9876, agent self-check, deep-read]
applies_to: Blender MCP, Claude, Codex, LM Studio, MacBook M5 Max (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=TojQChim9mM, src:yt-transcripts]
feeds: [estimator, pipeline design]
conflicts: none
---
Setup: add-on installed from disk, open sidebar, Start MCP server, which listens on port 9876; each agent's config adds a server using command uvx with argument blender-mcp [00:01][00:32][01:03]. Codex: inspects the scene first, renders a hero frame, notices the camera was too tight, measures framing, widens lens, re-renders, cuts back the glaze, rebalances exposure; also tried Hyper3D text-to-3D, generating three candidates and choosing one [02:04][02:35][08:45]. Claude: plan first, subsurface on dough, depth of field at f/3.2, Cycles with AgX; 100+ objects for a belt, 80+ for a dragon, and repositioned lights when chrome blew out the centre [03:05][06:12][09:48]. Local Qwen 3.5 122B MoE, 4-bit, M5 Max 40-core GPU, 128 GB unified memory: donut in about 8 minutes; belt in 5 [03:37][06:42]. The host's scoring is flamboyant and opinion; treat quality claims as low confidence.

**Use it:** for MCP evaluations, judge by whether an agent re-renders and corrects, not by first output; timing notes help size local-model runs.
