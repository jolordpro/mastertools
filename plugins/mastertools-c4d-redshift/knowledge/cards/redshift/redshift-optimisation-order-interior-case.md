---
id: redshift-optimisation-order-interior-case
title: Worked interior case: 7:40 at Medium came down to about 1:20 by tuning sampling, GI engine, trace depth and hardware RT in order
domain: redshift
tags: [render time, optimisation, workflow, interior, case study, 7:40, 1:20, irradiance point cloud]
applies_to: Redshift GPU, M3 Max, 1024x1280 stills
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts]
feeds: [estimator, coach, redshift]
conflicts: none
---
Method: bracket first with Basic mode Low (1:10, too noisy) and Medium (7:40) [17:26, 44:16]. Then in order: manual sampling (min 16, max 512, threshold 0.01), local overrides, GI brute-force rays, secondary GI to irradiance point cloud (3:36 to 1:48), trace depths to 3, hardware RT (a couple of seconds), bucket 512 (about 9 s) [26:55, 36:54, 46:55, 50:41]. Result 1:20 to 1:29, near identical [56:21].
A first manual try cut to 1:06 but was too noisy; fixing noise took it to about 3 minutes before the GI change [27:25, 31:36].
The speaker stresses it is scene-dependent, and a few seconds matter on 20-minute frames [51:07].

**Use it:** the advisor should present tuning as an ordered list with measured before and after, never a promised percentage; the estimator can use the bracketing runs as its timing anchor.
