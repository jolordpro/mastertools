---
id: redshift-polygon-division-stacked-speedup-chain
title: Stacked speedups on one scene took 1:23 to 15 s per frame, but with a higher threshold plus denoiser doing most of it
domain: redshift
tags: [render time, threshold, denoiser, stacked, bucket, 240 frames, claims]
applies_to: Redshift GPU, Windows
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=AFecCpLTUBI, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Chain: point cloud to brute force 1:23 to 1:01; threshold raised to 0.2 (captions say '01 to .2', probably from 0.01) with denoiser on, 0:21; bucket 256 0:17; bucket 512 0:15 [J 01:10-03:15]. Claimed saving: a 240-frame job from 4 hours to about 40 minutes.
Caveats: quality is not compared beyond the video; the biggest cut is the noisier threshold hidden by denoising.

**Use it:** treat as a ceiling example, not a target; the estimator should price quality loss before accepting a threshold increase.
