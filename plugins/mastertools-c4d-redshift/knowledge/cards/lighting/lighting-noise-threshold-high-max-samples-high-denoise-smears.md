---
id: lighting-noise-threshold-high-max-samples-high-denoise-smears
title: Let a high noise threshold stop easy pixels early while a high max-sample cap reaches the hard ones; denoisers smear, so keep a clean base
domain: lighting
tags: [spencer magnusson, blender, cycles, noise, noise threshold, max samples, sample count pass, denoise, blue noise, adaptive sampling, deep-read]
applies_to: Blender Cycles 5.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=0amlKMClE4s, src:yt-transcripts, https://www.youtube.com/watch?v=kIW648Cfo18, https://www.youtube.com/watch?v=FNiobzflmpA, https://www.youtube.com/watch?v=EKb5G_Efunw]
feeds: [redshift, advisor]
conflicts: none
---
Magnusson [30:30-35:43]: view the sample-count pass; white means max samples, dark means the threshold stopped early. Goal: threshold as high as possible so easy pixels stop, but hard pixels still run to the cap (4096 with 0.05 here). 0.05 to 0.01 is the crisper range. Automatic threshold (0) is 1 over the sample count, clamped at 0.001.
Denoisers smear, so judge the raw result first; one sample giving 30 samples of coverage looked horrible even with denoise. Blue-noise pattern (automatic) helps denoisers [23:20]. Rendering larger then downscaling gives the denoiser more image to work with [35:43].

**Use it:** the cost estimator should not trust a low threshold plus a heavy denoiser; check the sample-count pass.
