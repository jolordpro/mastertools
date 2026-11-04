---
id: redshift-path-tracing-from-camera-and-ray-sorting-explained-disney
title: Path tracing starts rays at the camera so only visible light paths are computed, and Disney's renderer sorts rays into batches by direction to render faster
domain: redshift
tags: [path tracing, ray sorting, ray batching, bounces, hyperion, disney, global illumination, render theory, deep-read]
applies_to: Disney Hyperion explainer
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=frLwRLS_ZR0, src:yt-transcripts]
feeds: [coach, estimator]
conflicts: none
---
Explainer from Disney Animation. A film frame can involve billions of ray calculations [04:01]. Path tracing reverses the real process: rays go out of the camera, hit surfaces and continue to the light, so no work is spent on paths the camera never sees [04:33]. Each bounce is a surface hit with a new direction decided by the surface appearance (smooth versus jagged, marble versus granite) [02:58][05:08]. Natural looks (shadows, translucency) need a ray to bounce roughly five to ten times or more [06:14]. Efficiency by ray sorting: rays with similar directions are batched together for each bounce, like doing ten maths problems at a time, which cuts the overhead of switching tasks [06:44][07:47][08:19]. Mapping to Redshift is not stated; it is an explainer for general audiences, so treat Redshift links as inference.

**Use it:** coach explanation for why depth and bounce counts cost time, and why coherent rays render faster.
