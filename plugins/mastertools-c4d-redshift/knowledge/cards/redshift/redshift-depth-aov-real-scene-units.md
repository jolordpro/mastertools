---
id: redshift-depth-aov-real-scene-units
title: Depth AOV now follows real scene units when camera near/far is off
domain: redshift
tags: [depth aov, z depth, scene units, comp]
applies_to: Redshift 2026.2
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ZAom6DvSi3s, src:yt-transcripts, https://www.youtube.com/watch?v=Xh8A767yA1U]
feeds: [comp, redshift]
conflicts: none
---
With use camera file off, depth AOV values match the scene scale (cm, mm), continuing the real-world-units work from the previous release [1:08:54].

**Use it:** comp check: treat depth as scene units; scale the Z-defocus range accordingly.
Transcript support: Second upload, same detail. (https://www.youtube.com/watch?v=Xh8A767yA1U [1:08:56-1:09:29])
