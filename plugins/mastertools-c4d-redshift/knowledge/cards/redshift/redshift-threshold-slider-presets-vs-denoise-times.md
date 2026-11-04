---
id: redshift-threshold-slider-presets-vs-denoise-times
title: One threshold slider with the denoiser took a test frame from 5:39 to 6 s, and the A/B looked nearly identical
domain: redshift
tags: [automatic sampling, threshold, denoise, optix, render time, presets]
applies_to: Redshift 3.x in C4D (2022 video)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=G43QVR1TqXg, src:yt-transcripts, https://www.youtube.com/watch?v=RpiCCLHjlWQ]
feeds: [coach, estimator, redshift]
conflicts: none
---
CG Shortcuts, one test scene, automatic sampling on. Very High preset = threshold 0.001 (lowest): 5 min 39 s. Low preset = 0.1. Threshold 1 = 4 s but very noisy [03:41].
Add OptiX denoise: 12 s. Set bucket denoise overhead to 0 (denoise once at the end): 6 s. A/B snapshot vs the 5:39 render looked extremely close [06:14].
If it is not close enough, lower the threshold step by step; Low would land near 20 s.

Ledger agrees: §2 "Low 0.100 / Medium 0.010 / High 0.005 / Very High 0.001".

**Use it:** coach can offer the ladder: raise threshold, denoise, overhead 0, then A/B against the slow render before accepting it. Numbers are one scene only.
Transcript support: Maxon trainers use Low to Medium bucket quality plus denoise on simple motion graphics and avoid denoise on fine textures, volumes and transparency (https://www.youtube.com/watch?v=RpiCCLHjlWQ [2:05:53-2:07:57])
