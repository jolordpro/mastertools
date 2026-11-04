---
id: lookdev-unreal-scale-uvs-from-center-with-clamp
title: Scale UVs from the centre, and clamp the texture, to shrink a logo without tiling
domain: lookdev
tags: [unreal, material function, uv scale, clamp, logo, patrick-wongbo, deep-read]
applies_to: Unreal Engine 4.25
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=WLdmYnkFoK4, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Wongbo [1:51:00-1:53:04]: the stock scale-UV node scales from the corner, which is rarely wanted. A centre-scale material function (value 1 = unchanged, 2 = half size) plus a clamp node stops the tiling and just stretches the edge pixel, so a logo with padding sits centred and smaller. A box mask node with falloff gives soft edges, a sphere mask does circles [1:54:37]. He calls the centre-scale function the single most useful thing in the stream.

**Use it:** Use as the recipe for logo-on-plate shaders in Unreal.
