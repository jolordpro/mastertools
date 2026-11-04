---
id: ai-models-splat-training-shiny-needs-fewer-splats-trees-need-more
title: Splat training tuning: keep the initial splat count for shiny items; for foliage downsample, add splats, lower harmonics
domain: ai-models
tags: [gaussian splat, training, ssim, spherical harmonics, vram, splat count, deep-read]
applies_to: Postshot, Octane
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=QW8ec3qquHA, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Postshot locks cameras and points while training, so data quality matters; research trainers (Nvidia, Nerfstudio-style) can adjust them but gave no gain in his tests [21:38-22:41]. Defaults are usually fine; watch the SSIM curve, where higher is better [22:41-23:13]. For shiny objects limit splats to the initialised amount and use high-resolution images [23:43-24:15]. For detailed scenes like trees, downsample images, fit as many splats as VRAM allows and lower the spherical harmonics degree, which has a large effect on memory [24:47]. Octane was the first renderer with proper splat relighting and shadows [25:19].

**Use it:** reference for any splat-based set element, kept low-confidence (single creator).
