---
id: pipeline-moonray-design-no-house-style-keep-lanes-busy
title: MoonRay's design brief: support non-physical looks as well as realism, avoid restricting artists, and keep every core and vector lane busy
domain: pipeline
tags: [[moonray, renderer design, non-physical, stylised, data oriented, simd, vector lanes, house style, dreamworks, bill ballew], deep-read]
applies_to: MoonRay
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=fQUnq6drevw, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
DreamWorks has no house style, so the renderer must span hyper-textured photoreal worlds to heavily illustrated hand-drawn looks, including non-physical reality that ray tracers are usually bad at, without losing speed [03:55-04:56]. The studio also works on five to six films at once, so efficiency across all compute mattered [03:36-03:55].
Core design: data-oriented (every byte matters, thin interfaces, no redundant data structures) to keep all lanes of all cores busy; path tracing is not trivially vectorisable, which was the main engineering challenge [04:56-05:29, 07:32-08:03]. A layered shader library (Moonshine) supplies the material range, and Arras the distributed compute [05:29-06:01].

**Use it:** when the coach explains why stylised looks need extra work in a physical renderer, this is the case in point.
