---
id: lookdev-pbr-maps-colour-space-ranges-and-common-mistakes
title: PBR maps: only colour and emission are colour data; metal, roughness, normal, height, AO and alpha are non-colour, and colour maps must have no baked shadows
domain: lookdev
tags: [pbr, albedo, roughness, metalness, normal map, height map, ambient occlusion, non-color, texture setup, deep-read]
applies_to: any renderer (shown in Blender)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=T2K6WXdifGA, src:yt-transcripts, https://www.youtube.com/watch?v=Qml8EakEAQ4, https://www.youtube.com/watch?v=6lioyniEl_E, https://www.youtube.com/watch?v=08CqyBVkpeU]
feeds: [lookdev, CHECKS]
conflicts: none
---
Beginner-channel summary (Graffin). Colour map: base colour only, no baked shadows or reflections, wired to the colour input [01:05]. Metallic: mostly black or white because a surface is usually metal or not; at 1 almost all albedo is lost and it mirrors the environment [01:35][02:06]. Roughness: 0 (mirror) to 1 (rubber-like, diffuse reflections) [02:06][02:37]. Normal map: fake depth cheaply, purple RGB-direction data, wired through a normal-map node, strength usually lowered [03:08][07:16]. Height map: black low, white high, looks like roughness so do not mix them up; real displacement quality is limited by mesh density and costs render time [04:10][04:41]. Alpha masks opacity, emission is an RGB map for self-lit parts [05:12][05:42]. Set colour space to non-colour on every data map [02:06][03:38]. AO is multiplied over colour, not connected automatically [06:44]. Displacement strength default of 1 is too strong [07:16].

**Use it:** a short material import checklist for CHECKS: colour space per map, strength defaults, no baked light in albedo.
Transcript support: Redshift version: colour maps sRGB, data maps Raw; a greyscale map's black is 0 and white is 1 for the slider it drives. (https://www.youtube.com/watch?v=08CqyBVkpeU [03:08-04:11])
