---
id: lighting-cycles-fast-clean-settings-and-bounce-numbers
title: Fast Cycles test settings: noise threshold 0.1, start at 100 samples, volume bounces 0, transparent bounces about 10
domain: lighting
tags: [cycles, noise threshold, bounces, transparent bounces, denoise, optix, oidn, png, deep-read]
applies_to: Blender 4.5 Cycles
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=EKb5G_Efunw, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
One heavy scene (translucency, transparency, fog) went from 1.5 hours to 1:25 [00:02]. Steps: GPU compute; noise threshold 0.1 (0.01 if you skip denoising); max samples start at 100 and raise only if noisy; OptiX denoise for video, OpenImageDenoise for stills [00:32]. Bounces: volume 0 (never needed), transparent about 10 here, glossy 6, diffuse 5, translucent 8 [01:04]. Failure: transparent bounces at 3 gave dark shadow patches on foliage; 20 removed them [01:04]. Caustics off and fast-GI on when they make no visible difference; motion blur on for video; persistent data only for animation [02:08]. Save PNG, not the default JPEG, at max compression (smaller file, no quality loss) [02:38].

**Use it:** the dark-patches-on-leaves failure is a quick tell for a too-low transparency depth; the same compare-and-trim habit applies to Redshift ray depths.
