---
id: lighting-kohlmann-extreme-noise-threshold-plus-double-resolution-trick
title: Kohlmann's claim: noise threshold far above normal with the same samples, plus double resolution, took a frame from 23 minutes to 1-2 minutes
domain: lighting
tags: [blender, cycles, noise threshold, resolution, render time, david kohlmann, deep-read]
applies_to: Blender Cycles (2023)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=FNiobzflmpA, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
David Kohlmann reports [00:33-02:37]: frames at the default threshold 0.01 and 4096 samples took about 23 minutes; threshold 0.02 with fewer samples about 6-7 minutes, with artifacts in dark areas; 2048 samples about 12 minutes. A typo of 0.25 instead of 0.025 rendered in about a minute with an acceptable but slightly darker, blurrier look; 1.0 was similar. Doubling the render resolution at that threshold and samples brought the detail back at about 2 minutes. He cannot explain why and calls it an accidental find. Disagrees in degree with the Blender Guru card, which suggests only 0.03 and warns of splotchy shadows when higher.

**Use it:** Treat as a single-creator test to try on a draft frame, not a recommended final setting; compare against a normal render before using it.
