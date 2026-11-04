---
id: c4d-2027-nodes-effector-snap-to-spline
title: A Nodes Effector can snap clones to the nearest point on a resampled spline, and two inverted copies crossfade between shapes
domain: c4d
tags: [nodes effector, snap to spline, closest point, resample spline, morph text, mograph, bullet]
applies_to: C4D 2027.0
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: []
conflicts: none
---
[01:39:42] Brute-force build: resample the spline by step (about 1), find the closest spline point for each clone, set that as the clone's offset. Set the closest-point minimum distance very large or far clones stay put [01:44:56].
Fields give it falloff. A second copy with the field inverted and a second text spline makes clones glide from one word to another [01:50:05]; Bullet follow-position of 10 and no sleep makes it dynamic [01:51:37].
Clone matrix is not corrected for the spline moving; a Connect object bakes curved splines [01:49:34]. He is not a nodes expert.

**Use it:** a source for morph-text rigs where clones travel instead of crossfading.
