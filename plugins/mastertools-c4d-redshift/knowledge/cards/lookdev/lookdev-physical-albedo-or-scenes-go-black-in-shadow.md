---
id: lookdev-physical-albedo-or-scenes-go-black-in-shadow
title: Diffuse textures that are too dark look fine in strong light but go black in dim light, so use physically based albedo
domain: lookdev
tags: [sean gobi, gameloft, unreal fest, albedo, diffuse, macbeth chart, physically based, deep-read]
applies_to: Unreal Engine 5
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=nlbJwMoj1Dg, src:yt-transcripts, https://www.youtube.com/watch?v=nUk3Zs91kZU]
feeds: [lookdev]
conflicts: none
---
Reason: surfaces only return the fraction of light their diffuse value allows; lighters complain that characters look good in light and the environment is black in darkness when artists paint under-bright diffuse [07:21-07:51].
He points to a built-in colour-checker overlay in the viewport (backslash key) to check values [07:51-08:22].

**Use it:** extends the albedo ranges card; ask for material values to be fixed before adding lights to compensate.
