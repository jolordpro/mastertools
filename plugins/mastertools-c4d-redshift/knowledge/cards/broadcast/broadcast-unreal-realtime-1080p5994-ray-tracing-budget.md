---
id: broadcast-unreal-realtime-1080p5994-ray-tracing-budget
title: Real-time budget at 1080p59.94: ray-trace only the floor reflections, keep samples at 1, bake the rest
domain: broadcast
tags: [unreal, ray tracing, performance, reflections, samples per pixel, baked lights, upsampling, deep-read]
applies_to: Unreal Engine 4.27 (concepts carry to UE5)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bcL001ZFHBQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Target 1920x1080 at 59.94 [48:43]. Ray tracing is on in the post-process but off for GI and translucency; the one wanted effect is reflections on a semi-rough floor, where planar reflection and screen-space gave artifacts [49:15-49:45].
Controls exposed live: default 1 sample per pixel and 1 bounce (roughness cut-off 0.45 in the project). Samples per pixel buys the most and costs the most; raised to 16 it smooths noise but is a high GPU cost, so the same setting can be raised for offline renders [49:45-50:47].
Lighting: many small rect lights for streaks, only one light with ray-traced shadows (for a sharp car outline); everything static is baked, except lights inside fans [50:47-51:53].
Temporal upsampling was avoided so 1080p is native and a future 4K would not be a 4x upscale [52:54-53:26]. Profile showed shadow depth, direct and indirect lights, RT reflections, denoise and light post.

**Use it:** Treat as the template for a live-quality budget: choose one hero ray-traced effect.
