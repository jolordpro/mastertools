---
id: lookdev-octane-sampling-patterns-random-vs-blue-noise-and-doubling-samples
title: Path-tracer sampling explained for Octane: grid shows aliasing, random leaves holes, blue-noise-like patterns win; speaker says noise halves when samples double
domain: lookdev
tags: [octane, sampling, blue noise, quasi monte carlo, spp, path tracing, samples per pixel, deep-read]
applies_to: OctaneRender (about 2020); theory applies to any path tracer
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=3ornW8uKJpI, src:yt-transcripts]
feeds: []
conflicts: none
---
SilverwingVFX [02:33-14:46], not a renderer engineer by his own disclaimer. Grid patterns cover evenly but alias; pure random avoids stair-stepping but leaves clumps and holes so more noise; blue-noise or quasi-Monte-Carlo patterns spread samples evenly without a grid, which is what modern renderers use (he thinks Octane uses blue noise early, quasi Monte Carlo later). Each sample can spawn rays: reflection, direct-light, rough-reflection fans, and a hemisphere of diffuse GI rays. At 1 sample per pixel the image has black pixels where rays missed the light. His rule: noise is cut by doubling samples, so 64 to 65 does nothing and you need 128. Caution: standard Monte Carlo noise falls with the square root of samples, so doubling cuts noise by about 30 percent, not half.

**Use it:** Teaching pattern for the coach: judge sampling changes in doublings. Do not state 'half noise' as fact.
