---
id: redshift-toon-decals-dots-and-dirt-layered-with-color-layer-blend-modes
title: Toon decals from PBR textures via a stepped ramp, a toon pattern dot node at multiply, and noise-masked dirt, all layered in a Color Layer node
domain: redshift
tags: [redshift toon, color layer, ramp stepped, decals, dot pattern, dirt, perlin, multiply, casey gu, deep-read]
applies_to: C4D + Redshift toon shader (2024 upload, Casey Gu)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=LWavn-Io1_o, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
Turn the bought PBR decal texture into pure black and white with a ramp set to stepped and adjust the white point [05:26-06:27]. Mix with the grain in a Color Layer (Photoshop-like): blend subtract, output into exposure [06:27-07:00].
Comic dots: the toon pattern node plugged to the base tone map covers the model; add it as a layer with multiply, size 0.4, giving cyan dots in the white areas [06:59-08:00].
Dirt: Perlin Maxon Noise with contrast, scale and low clip, masked by a second larger noise via multiply so dirt shows in white regions only; then the layer goes to the base tone map [08:00-09:39]. The final scene used separate materials per part [09:39].

