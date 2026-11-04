---
id: ai-models-vllm-mlx-image-cache-speedup
title: vllm-mlx shows a 28x speedup for repeated image queries (21.7 s to under 1 s), which is a cache effect
domain: ai-models
tags: [vllm-mlx, mlx, vlm, image cache, apple silicon, qwen-vl, critic]
applies_to: arXiv 2601.19139
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://arxiv.org/html/2601.19139, src:research-gaps-deep]
feeds: [critic on Mac]
conflicts: none
---
No clean image-prefill number for Qwen-VL on an M4 Max was found.

**Use it:** a Mac is fine for the VLM critic when the same image is asked about several times.
