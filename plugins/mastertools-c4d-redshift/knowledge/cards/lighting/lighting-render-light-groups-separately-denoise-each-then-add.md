---
id: lighting-render-light-groups-separately-denoise-each-then-add
title: When many overlapping lights fight for a pixel, render light groups (or view layers) separately, denoise each, then add them
domain: lighting
tags: [spencer magnusson, blender, cycles, noise, light groups, view layers, denoise, compositor, overlapping lights, deep-read]
applies_to: Blender Cycles 5.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=0amlKMClE4s, src:yt-transcripts, https://www.youtube.com/watch?v=tB5-Oe7pTUs]
feeds: [comp, redshift]
conflicts: none
---
Magnusson [15:20-18:01], from a Blender Conference talk: lights compete for each pixel in a linear workflow, so group them (cool and warm here), render each, and sum. With denoising data (albedo, normal) per group the composite was cleaner, less splotchy than one-pass denoise, and the check used a subtraction. He notes the scene was deliberately under-sampled.

**Use it:** a light-group noise plan: neon, billboards and window lights as groups, denoised and added in comp.
