---
id: redshift-motion-blur-noise-fixed-only-by-unified-sampling-min-max
title: Redshift (S22 era): there is no motion-blur sample override, so clean blur by raising Unified Sampling max; threshold 0.003 first, then 128 to 512
domain: redshift
tags: [motion blur, unified sampling, max samples, threshold, sampling overrides, noise, render region, deep-read]
applies_to: Redshift 3.x in C4D S22 (2020)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=tsx8Isq6m-s, https://www.youtube.com/watch?v=kwFwyzjXsdM, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Derek Kirk [04:22-07:54]: he wishes motion blur had an override like lights and volumes, but it does not; the only control is Unified Sampling. Steps in his test: threshold to 0.003 (he does this almost always), then max samples up in multiples (16, 32, 64, 128, 256, 512); 128 looked close to acceptable, 512 clean; use a render region to judge. Blur noise lasts one frame so it reads cleaner in motion. Keep sample overrides for other effects so they do not lose their own counts. Maxon's Houdini tutorial agrees: motion blur and depth of field can only be cleaned from Unified Sampling [kwFwyzjXsdM 10:08-10:39]. The ledger agrees that DOF or motion blur need at least 8-16 min and possibly 256+ max.

**Use it:** Coach: noisy motion blur or DOF means raise max samples (and min 8-16), not light overrides.
