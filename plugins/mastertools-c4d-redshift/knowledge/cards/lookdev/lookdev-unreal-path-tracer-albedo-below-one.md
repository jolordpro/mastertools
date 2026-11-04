---
id: lookdev-unreal-path-tracer-albedo-below-one
title: Keep white base colour or albedo at 0.8 or lower: nothing real is 1.0, and the lower value cuts render time and improves the result
domain: lookdev
tags: [william faucher, unreal, path tracer, albedo, base color, render time, interior, deep-read]
applies_to: Unreal 4.27 (principle is general)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=X5zVhc5ahl0, src:yt-transcripts]
feeds: [[redshift, lookdev]]
conflicts: none
---
William Faucher (Unreal VFX artist, single creator; low confidence on the render-time claim) [22:24-22:55]: for bright interior materials keep albedo under 1, around 0.8. Even fresh snow is not 1. He says this both shortens renders and gives a better image, a "win-win". Related card for physical ranges: lookdev-albedo-nonmetal-metal-ranges.

**Use it:** Scene check: flag diffuse or base colour above 0.8 on a white wall or paper surface as a likely overbright source of noise and burnt GI.
