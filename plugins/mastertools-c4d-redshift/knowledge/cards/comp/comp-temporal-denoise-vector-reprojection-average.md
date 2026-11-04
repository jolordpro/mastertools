---
id: comp-temporal-denoise-vector-reprojection-average
title: Spatial denoisers cannot fix flicker between frames; reproject the neighbouring frames with motion vectors and average
domain: comp
tags: [temporal denoise, flicker, motion vector, reprojection, denoise data, davinci resolve, cycles]
applies_to: Blender 4.5/5 (principle general)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=w3HGJ2KuGfo, src:yt-transcripts, https://www.youtube.com/watch?v=yAbuPpbbATA, https://www.youtube.com/watch?v=jyGQIKOPwGA]
feeds: [comp-fix planner, shakedown]
conflicts: none
---
[01:03] OIDN and OptiX work frame by frame, so each frame looks clean but the sequence flickers; glass and god rays make it worse.
[05:46] Method: render with the vector pass, move frames n-1 and n+1 onto frame n with their vectors, average the three (add twice, multiply by a third).
[04:10] Resolve Studio temporal noise reduction does the same with three frames each side; the free version watermarks. Limits: slows and trails moving particles; repeating is possible but the speaker stopped at three passes [10:57].

**Use it:** gives the comp planner a flicker fix and the limits to warn about.
