---
id: ai-models-ttm-prep-masks-and-preview-after-three-steps
title: TTM prep: mask the subject with SAM 3, remove the stick with an image-edit model, and judge the take after three steps
domain: ai-models
tags: [sam 3, qwen image edit, mask, start frame, end frame, preview, comfyui, ttm]
applies_to: ComfyUI workflow (Dec 2025)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=pUb58eAZ3pc, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
[03:41] Click the subject and right-click the parts that are not it, such as the stick. The mask may flicker without harm [04:12].
[04:12] Clean the start and end frames with an image-edit prompt such as 'remove the wooden stick', adding 'do not change the look of the figure' [04:44].
[06:16] Use both frames for stability. Sampling is in two parts and shows a rough preview after three steps; stop and change seed or prompt if it fails [06:16].

**Use it:** when a user generates motion, show the cheap preview first.
