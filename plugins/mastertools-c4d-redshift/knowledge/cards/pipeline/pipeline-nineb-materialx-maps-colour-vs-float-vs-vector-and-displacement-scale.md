---
id: pipeline-nineb-materialx-maps-colour-vs-float-vs-vector-and-displacement-scale
title: MaterialX texture slots: colour for base colour, float for roughness and height, vector3 plus a normal-map node for normals; displacement needs a scale (0.01 in his door)
domain: pipeline
tags: [nine between, houdini, solaris, usd, materialx, textures, normal map, displacement, quixel, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS, redshift]
conflicts: none
---
Set the image node's type by what it is: colour for base colour, float for single-channel maps like roughness and height, and vector3 (not colour) for a normal map, fed through a normal-map node [1:40:58-1:42:30]. Height into displacement blows the shape out until the scale is set (0.01 there) [1:42:30-1:43:01].
For Quixel Megascans he used a remap (0..1 to -0.5..0.5) and cut gain by 0.75 to make displacement behave; he says he is not sure why [1:43:01-1:44:02].
Strong subsurface can hide the normal map; reduce it or add displacement [1:44:34-1:45:05].

**Use it:** A texture-import checklist: data maps are not colour; set displacement scale and midpoint on first test render. Applies to Redshift displacement nodes the same way.
