---
id: redshift-gsg-default-scene-sampling
title: Greyscalegorilla Chad's default scene: auto sampling off, high threshold, min 4, light samples 512, brute force 1024 rays
domain: redshift
tags: [default scene, sampling, brute force, bounces, light samples, greyscalegorilla]
applies_to: Redshift 2026 on Mac
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts, https://www.youtube.com/watch?v=MuVzbVhMUvI]
feeds: [redshift, coach]
conflicts: none
---
From the Behind the Render episode, still at 1920x1920 [59:58-1:01:34]: auto sampling off, threshold high (noisy first pass), min low (4 suggested), max medium, light override 512, brute force rays 1024, GI bounces sometimes 8 (he admits 4 vs 8 is nearly the same), trace depth down to 0 when no glass.
He sees these as a starting point for stills with denoise, and adjusts per shot.

**Use it:** advisor: a reference default for a fast look-dev scene; compare a user's settings with it, not as a requirement.
Transcript support: Another starting set from Chad (2017): IPR 64, 256 max/16 min unified, dome 1024, GI rays 512, brute force + irradiance point cloud 3 bounces. (https://www.youtube.com/watch?v=MuVzbVhMUvI [15:09-22:56])
