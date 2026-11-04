---
id: lookdev-glass-hard-edge-is-the-ground-refraction
title: A hard line inside a glass object may be the refraction of the ground plane edge; scale the plane up
domain: lookdev
tags: [glass, refraction, ground plane, hard edge, troubleshooting, polyfjord, deep-read]
applies_to: Blender Cycles
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Jwl48psPrxU, src:yt-transcripts]
feeds: []
conflicts: none
---
The sharp edge in the glass was the ground plane's boundary refracted through it [04:08-04:39]. Scaling the plane to 800 meters gave a smooth edge. A light's specks are fixed by enlarging the light radius to 1 m, which also smooths the highlights [05:10-05:41].

**Use it:** Glass debug tip: before changing the shader, ask what each hard line is refracting.
