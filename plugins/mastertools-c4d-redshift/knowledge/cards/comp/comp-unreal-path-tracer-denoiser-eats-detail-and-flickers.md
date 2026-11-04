---
id: comp-unreal-path-tracer-denoiser-eats-detail-and-flickers
title: Faucher's A/B: a 10-sample denoised frame hides roughness and scale detail that a 500-sample frame keeps, and per-frame denoising flickers in animation
domain: comp
tags: [william faucher, unreal, path tracer, denoiser, sample count, temporal, flicker, roughness, deep-read]
applies_to: Unreal 4.27 path tracer
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=X5zVhc5ahl0, src:yt-transcripts]
feeds: [[redshift, shakedown, CHECKS]]
conflicts: none
---
10 samples plus denoiser vs 500 samples plus denoiser looked identical on compressed video but zoomed showed that the denoiser wiped a roughness breakup on a black plastic base, scale detail on a turtle shell and notches on a plank edge [06:53-08:27]. Denoiser is meant mainly for stills; at 100 spatial samples animation flickers because each frame is denoised alone (not temporal) [08:57-09:28]. Temporal samples in the movie render queue help but dark detailed areas still flicker [10:03]. His rule: noise is detail, so he turns the denoiser off in render and denoises later in comp where he controls it [25:00-25:32]. Starting point 16 spatial x 16 temporal. Spatial and temporal multiply: 100 x 5 = 500, 50 x 10 = 500, so decide the sample total first, then split [24:00-24:28]. Matches the existing Redshift-side cards on the denoiser as a finisher.

**Use it:** Review check: zoom to 200% on a roughness or bump-heavy surface before approving a low-sample denoised draft; for animation compare 3 consecutive frames for crawl.
