---
id: ai-models-regional-prompts-master-prompt-seed-and-video-interpolation
title: A master prompt plus per-mask regional prompts, a fixed seed for similar re-renders, and rendering only every second frame then interpolating to 24 fps
domain: ai-models
tags: [regional prompt, master prompt, seed, animatediff, rife interpolation, ip adapter, comfyui, ai render, deep-read]
applies_to: ComfyUI, SDXL, AnimateDiff-style motion model
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=mu3JEfx3PHM, src:yt-transcripts]
feeds: [challenger]
conflicts: none
---
Master prompt (style and light) is added to every region; regional prompts per colour mask; a shared negative prompt [05:08][05:39]. Adding rain to the master updates all regions, with puddles added to the ground prompt only [06:42]. The model understands the whole image so light direction and shadows stay coherent [07:46]. Changing composition in 3D and re-running with the same seed and prompts gives a similar image, which suits concept art or storyboards [08:18]. For animation: load the pass sequences, cap frame count, select every second frame and interpolate back to 24 fps with a RIFE-type node [08:50][09:21]. Limits: the early motion model was trained on 8 frames, so background weirdness remains; an IP adapter guided by a textured render improves consistency but makes it more of a filter [11:31][12:03]. Camera-heavy shots with tentacles were hard [09:58].

**Use it:** estimator note: AI restyle pipelines render cheap passes then generate every second frame; fast decay, retest.
