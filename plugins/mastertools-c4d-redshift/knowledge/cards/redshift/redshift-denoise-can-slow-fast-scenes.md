---
id: redshift-denoise-can-slow-fast-scenes
title: On a simple, fast scene the denoiser can cost more time than it saves
domain: redshift
tags: [denoise, render time, simple scene, overhead]
applies_to: Redshift 2026
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts]
feeds: [coach, estimator, redshift]
conflicts: none
---
Same mug scene: 24 s without denoise and 30 s with it, so about 6 s added [1:04:37-1:05:08]. If the scene is not noisy (no glass, little SSS), skip denoise.

**Use it:** coach: warn that denoise is not free; estimator should add denoise time for fast scenes.
