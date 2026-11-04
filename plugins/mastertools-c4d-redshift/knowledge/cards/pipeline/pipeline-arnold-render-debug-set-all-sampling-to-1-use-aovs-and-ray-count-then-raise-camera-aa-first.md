---
id: pipeline-arnold-render-debug-set-all-sampling-to-1-use-aovs-and-ray-count-then-raise-camera-aa-first
title: Arnold scene optimisation (2021) - set samples and ray depth to 1, read CPU-time and ray-count AOVs, raise AA/SSS/specular, add denoiser and adaptive sampling
domain: pipeline
tags: [arnold, render-time, sampling, aov, adaptive-sampling, denoiser, arvid-schneider, maya, deep-read]
applies_to: Arnold CPU and GPU in Maya (XGen implies Maya; video 2021-07-23) - not Redshift
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=mLMXWCLX4SY, src:yt-transcripts]
feeds: [estimator, shakedown]
conflicts: none
---
Arvid Schneider, uploaded 2021-07-23, part one of an Autodesk webinar.
- Starting point: fur, subsurface, raindrops, DOF; client settings gave 23 min 41 s on his machine [00:00-01:32].
- Cost is the camera AA samples and the per-ray sample groups; sampling multiplies (AA 4 gives 16, other groups squared). Adaptive sampling at max 20 with threshold 0.015 is expensive; he has seen 10 on every depth with matching diffuse and complains of oversampling [01:32-04:11].
- Method: output all AOVs including CPU time and ray count, then set all sampling to 1, depth 1 and adaptive off; the frame renders in 8 s and AOVs show which pass is noisy [04:11-06:46].
- Raise in steps while testing a hard region: camera AA 2 to 4, SSS to 3, diffuse and specular, DOF needs AA 8 (1 min 43 s). Specular indirect to 2 was needed. High camera AA lets other groups drop [06:53-09:22].
- Add the denoiser imager (restart render), AA 2: 44 s [09:53].
- Adaptive sampling back on: max AA 10, min 2, threshold 0.05: 3 min 39 s, about 8 times faster than 23:41; also watch light samples [10:26-12:25].
- Arnold GPU: single camera AA, adaptive minimum about 5, max 60 to 80, threshold 0.25 then 0.05, with denoiser [12:31-15:05].
Settings are scene-specific; the logic is transferable (not Redshift numbers).

**Use it:** Pattern for Redshift sampling tests: collapse to minimum, find the noisy pass, raise one thing at a time.
