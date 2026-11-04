---
id: lighting-lumen-emissive-noise-use-tube-lights
title: Many emissive surfaces make Lumen noisy; pair them with real lights and raise GI quality only where cost allows
domain: lighting
tags: [sean gobi, gameloft, unreal fest, lumen, emissive, noise, tube lights, gi quality, deep-read]
applies_to: Unreal Engine 5, Lumen
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=nlbJwMoj1Dg, src:yt-transcripts]
feeds: []
conflicts: none
---
For street and nightclub scenes with lots of emissive meshes, the developers' advice relayed was: do not rely on emissive alone; place tube lights near the emissive so the light does the lifting [37:22-37:54].
A second speaker adds that the post-process global illumination sliders are exponential: raising them improves Lumen crawl and update speed but is costly for games, fine for film or virtual production [39:02-40:37]. A snap camera cut can be given priority in the update rate [31:36-32:06].

**Use it:** real-time context only; the lesson that emissive-only lighting is slow to converge applies to offline engines too.
