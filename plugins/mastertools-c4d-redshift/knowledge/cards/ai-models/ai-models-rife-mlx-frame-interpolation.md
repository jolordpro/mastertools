---
id: ai-models-rife-mlx-frame-interpolation
title: RIFE 4.25 MLX port runs natively on Apple Silicon (MIT); M1 manages only 576p at 48 fps live via MoltenVK
domain: ai-models
tags: [rife, frame interpolation, mlx, apple silicon, moltenvk, venhance, mps]
applies_to: RIFE 4.25
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://huggingface.co/mlx-community/RIFE-4.25, https://svp-team.com/wiki/RIFE_AI_interpolation, src:research-verticals, https://www.youtube.com/watch?v=nFR0ZXwaD4o]
feeds: [interpolation rung]
conflicts: none
---
venhance (PyTorch MPS) self-reports about 51 ms per 720p frame for rife-v4.7 on an M5. A third-party video shows a C4D grey render taken through AI video then NVIDIA ComfyUI steps: 24 to 48 fps, HDR, upscale to 4K.

**Use it:** RIFE is usable on the Mac; score interpolated frames against real ones.
