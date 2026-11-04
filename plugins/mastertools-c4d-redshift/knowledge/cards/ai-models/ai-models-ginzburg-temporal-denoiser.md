---
id: ai-models-ginzburg-temporal-denoiser
title: Ginzburg Neural Denoiser (MIT, research) is a temporal denoiser: temporal PSNR 43.78 vs OIDN 42.33 on one 36-frame shot, but OIDN wins single frames
domain: ai-models
tags: [ginzburg, temporal denoiser, flicker, oidn, optix, cuda, research]
applies_to: early repo, 9 commits
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://github.com/ginzburg-dev/ginzburg-neural-denoiser, src:research-verticals]
feeds: [PLAN 5b]
conflicts: none
---
Self-reported on one shot: flicker (LF-p95) 0.045% vs OptiX 0.060% vs OIDN 0.054%; single-frame 41.74 dB for OIDN vs 40.02. Flagship weights are private; NVIDIA RTX 40 build.

**Use it:** best lead for temporal denoise; copy its metric set (temporal PSNR, flicker).
