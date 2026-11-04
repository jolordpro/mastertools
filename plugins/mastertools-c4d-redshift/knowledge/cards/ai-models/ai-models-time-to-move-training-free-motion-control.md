---
id: ai-models-time-to-move-training-free-motion-control
title: Time-to-Move (TTM) is training-free and works with any diffusion video model; a control clip sets the motion
domain: ai-models
tags: [ttm, time to move, wan 2.2, video generation, control video, comfyui, dual clock denoising]
applies_to: Wan 2.2 in ComfyUI (Dec 2025)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=pUb58eAZ3pc, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
[00:33] TTM needs no training and plugs into diffusion video models (shown on Wan 2.2; others named). A control video of motion (dragged in AE or Blender, or a physical stick) sets it.
Dual clock denoising [01:04]: low noise where the subject moves so it follows exactly, higher noise elsewhere for a clean background. About 70% of shots worked first time [02:07].

**Use it:** an option for storyboards and animatic motion, not a final-pixel path.
