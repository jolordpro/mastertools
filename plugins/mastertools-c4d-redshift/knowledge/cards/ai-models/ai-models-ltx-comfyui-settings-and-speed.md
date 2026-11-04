---
id: ai-models-ltx-comfyui-settings-and-speed
title: LTX 2.3 render settings seen: resolution divisible by 64, middle guide frame at 0.75 strength, FP8 plus distilled LoRA, 330 frames in about 1:50 on an RTX 5090
domain: ai-models
tags: [ai render, ltx, comfyui, rtx 5090, nvfp4, gguf, upscale, settings, mickmumpitz, deep-read]
applies_to: LTX 2.3, ComfyUI, RTX (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=7J7hi-Hxpac, src:yt-transcripts]
feeds: []
conflicts: none
---
Mickmumpitz [12:25-18:29]. Resolution must be divisible by 64 or it errors; the demo ran lower and could go to full HD or 2K. Frame load cap = sequence length (go lower for tests). Up to three reference frames can sit anywhere in the clip; a middle frame was set true at the frame it was made from, strength 0.75. Driving-video strength: lower frees the model and makes the prompt matter more, but on complex motion it breaks the animation. Models: full FP8 with a distilled LoRA on a 5090 (32 GB); NVFP4 (50-series only) claimed about 3x faster than full precision with little loss; GGUF for older or low-VRAM cards. A 330-frame shot took about 1:50 on the 5090; the author tests on a 4070 and 4090 without GGUF. NVIDIA RTX video super resolution in ComfyUI upscales to 4K in seconds and was run on every shot. Change the seed to get a slightly different take.

**Use it:** Cost and time inputs for any AI render step: seconds per shot are minutes, VRAM class decides the model variant, and upscaling is a separate cheap pass.
