---
id: redshift-displacement-clay-tessellation-test
title: Judge displacement in clay mode, start with a fixed subdivision of 2-3 and a scale far below the default (0.01-0.02)
domain: redshift
tags: [displacement, tessellation, subdivisions, clay mode, rs object tag, scale]
applies_to: Redshift RS object tag, C4D (2023)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=le17-h6tUD0, src:yt-transcripts]
feeds: [lookdev, coach]
conflicts: none
---
Add an RS Object tag, enable tessellation and displacement; the default scale is far too large [29:37-30:09].
Use clay mode to see geometry, a non-screen-space (fixed) subdivision, and lower until the effect still reads: 3 then 2 then maybe 1 [30:39-31:41].
Scale went 0.05 then 0.02 then 0.01 for wood grain [31:11-35:18]. Screen-space adaptive is an option later.

**Use it:** displacement advice in the coach should give these ranges for fine materials, not the default.
