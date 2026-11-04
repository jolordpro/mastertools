---
id: redshift-caustics-diamond-material-and-trace-depth-tradeoffs-16-hour-render
title: Redshift diamond caustics: IOR 2.41, roughness about 0.05-0.3, dispersion 10; lower trace depths cut noisy caustics; his 5M-photon, 0.005-threshold animation took about 16 hours
domain: redshift
tags: [caustics, diamond, ior, trace depth, dispersion, render time, caustics aov, deep-read]
applies_to: Redshift in C4D (2025-26 era)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=BJrUgdVBDts, src:yt-transcripts]
feeds: [redshift, estimator]
conflicts: none
---
Material: transmission on, IOR 2.41 (diamond), roughness 0.05 in the demo, dispersion 10; final material had a roughness map around 22-32% [03:54-04:46, 07:58-08:33]. IOR, roughness and dispersion together change the caustic look [05:19-05:51].
Light that makes the tile-like patterns: a light placed at the diamond's level, with the other light values zeroed and named Caustics Light (his description is loose) [04:46-05:19].
Noise: raise reflection, refraction and light samples (he shows 1,024), raise max samples (32 shown) and lower the threshold [05:51-06:24]. Global-tab trace depths for translucent objects stay high for detail; lowering reflection and refraction depth to 3 and 3 removed noisy patterns [06:24-07:25].
Cost: threshold 0.005 and 5M photons made a roughly 16-hour render; he thinks 1,024 samples, threshold 0.01 and denoising would be under 10 hours. One test frame with the key light took 8 minutes [09:04-10:05].
A Caustics AOV can be lifted or tinted in After Effects; exposure +2 or -2 shown [10:36-11:08].

**Use it:** Estimator: caustics shots are hours, not minutes; budget them with a lower threshold and test trace depth first.
