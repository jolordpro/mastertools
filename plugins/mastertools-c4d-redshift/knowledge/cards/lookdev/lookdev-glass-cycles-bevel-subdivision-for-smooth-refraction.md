---
id: lookdev-glass-cycles-bevel-subdivision-for-smooth-refraction
title: Round glass shapes with bevel and a higher render subdivision level give smooth refraction lines at the same render time
domain: lookdev
tags: [glass, bevel, subdivision, refraction, smooth shading, cycles, polyfjord, deep-read]
applies_to: Blender 3.3 Cycles
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Jwl48psPrxU, src:yt-transcripts]
feeds: []
conflicts: none
---
A default cube became glass with roughness 0, then a bevel and subdivision (4 viewport) with smooth shading made rounded refractions [01:36-02:06]. Raising the render subdivision (up to 6) removed low-poly edges and the second render was slightly faster, under 5 seconds [03:08-03:38]. Lesson: refraction exposes every facet, so the mesh needs more smoothness than it looks like it does. The sphere with a Voronoi displace needed subdivision after displace plus a smooth modifier [07:44-09:47].

**Use it:** When glass looks faceted in refraction, raise the geometry subdivision, not the sampling.
