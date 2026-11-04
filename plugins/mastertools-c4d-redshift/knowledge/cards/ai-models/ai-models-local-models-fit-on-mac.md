---
id: ai-models-local-models-fit-on-mac
title: Rough Mac fit: 27-31B models on a 128 GB M5 Max, big MoEs on 256-512 GB, one benchmark of 51 tokens/s for a 27B on a 256 GB M5 Ultra
domain: ai-models
tags: [local llm, mac, m5 max, m5 ultra, qwen 3.8, gemma 4, memory, mlx]
applies_to: Oct 2026
status: U
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://github.com/VincentGourbin/gemma-4-swift-mlx/wiki, src:research-frontier-ai]
feeds: [local brain]
conflicts: none
---
Fits 128 GB or a 24 GB+ card: Qwen 3.8 27B, Gemma 4 31B and E4B, Clef-flash 9B, LFM3-VL-2B (exact speeds unverified). Gemma 4 video on MLX: 1 frame/s at 70 tokens per frame via a community Swift port. The 51 tokens/s figure is a single aggregator.

**Use it:** use for planning only, benchmark on the real machine.
