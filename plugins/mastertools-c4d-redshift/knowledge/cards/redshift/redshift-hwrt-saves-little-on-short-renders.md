---
id: redshift-hwrt-saves-little-on-short-renders
title: Hardware ray tracing adds a 5-10 s ramp-up, so it helps heavy instanced scenes more than 20-40 s frames
domain: redshift
tags: [hardware ray tracing, rt cores, m3, instancing, render time, ramp up]
applies_to: Redshift GPU, RTX or Apple M3 and later
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts]
feeds: [redshift, estimator]
conflicts: none
---
Needs RT-core GPUs (RTX, M3+); M1 and M2 lack it [40:08, 42:13]. Expect 5-10 s of ramp-up, so 20-40 s renders see little change [40:39].
Big wins for instanced scenes such as grass on terrain [41:10]. The interior test saved only a couple of seconds on a render of about 1:30 [46:55].

**Use it:** the estimator adds a small fixed startup term when hardware RT is on, and the advisor suggests it mainly for instance-heavy scenes.
