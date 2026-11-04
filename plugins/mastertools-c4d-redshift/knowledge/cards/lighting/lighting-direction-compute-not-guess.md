---
id: lighting-direction-compute-not-guess
title: Light direction is the weakest thing for vision models (best 53%), so compute it from the scene instead
domain: lighting
tags: [lighting, direction, side, back, top, edge, underlight, vlm, labels]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://arxiv.org/html/2505.15145v1, https://arxiv.org/html/2506.21356v2, src:research-production-pipelines]
feeds: [PLAN Phase 1 computed shot labels]
conflicts: none
---
CineTechBench splits lighting into intensity, quality and direction; direction was hardest (best commercial model 53%).
Label words used by the datasets: side, back, top, edge, under; side light, backlight, silhouette, high or low contrast, hard or soft light.
From the scene: key direction versus camera, hard or soft from light size over distance, high or low key from the ratio and histogram.

**Use it:** label shots with the datasets' words computed from lights and camera, so the critic and coach use the same vocabulary.
