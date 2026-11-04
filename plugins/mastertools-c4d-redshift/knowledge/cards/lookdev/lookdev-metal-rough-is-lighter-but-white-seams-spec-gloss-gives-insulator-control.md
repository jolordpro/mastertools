---
id: lookdev-metal-rough-is-lighter-but-white-seams-spec-gloss-gives-insulator-control
title: Metal-rough is lighter on memory (grayscale maps) but can leave white line artifacts at low resolution; spec-gloss gives more reflectivity control but also lets you enter wrong values
domain: lookdev
tags: [pbr, metallic roughness, specular glossiness, normal map, opengl, directx, albedo, manson akram, deep-read]
applies_to: any PBR
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=6lioyniEl_E, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Manson Akram [6:19-7:53]: metal-rough needs albedo, metallic, roughness, normal and height; spec-gloss needs diffuse, specular, glossiness, normal and height. Spec-gloss is heavier because specular is an RGB map; metal-rough is more optimised and more common. Downsides of metal-rough: white-line artifacts at material transition points on low-resolution maps, and less control of insulator reflectivity; if artists don't understand it they can type unrealistic metalness values and break it. Spec-gloss avoids the seam artifacts and offers full-colour reflectance control, but it is easy to enter non-physical reflectance. Reference values he states: non-metals reflect 4 to 5 percent, sRGB 40 to 75 dark; metals 70 to 100 percent, sRGB 180 to 255 [2:41]. OpenGL normal maps have green up and DirectX green down; invert the green channel when the engine disagrees [4:14-4:44]. Roughness is the inverse of glossiness [3:14]. Beginner channel, low confidence.

**Use it:** The scene check can flag a metalness map with grey mid-values and mismatched normal-map convention.
