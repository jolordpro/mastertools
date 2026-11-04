---
id: redshift-toon-watercolor-line-thickness-from-noise-and-facing-ratio-layered-overlay
title: Redshift Toon sketch lines (Greyscalegorilla, 2024): drive line width with a clamped noise multiplied by a facing-ratio, mixed with a color layer in Overlay
domain: redshift
tags: [redshift toon, contour, fresnel, noise, change range, sketch lines, c4d, greyscalegorilla, deep-read]
applies_to: Cinema 4D + Redshift Toon (video May 2024)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=u6j9yrpgRhU, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
Tutorial host (Greyscalegorilla) builds the line first with colour and tone off [03:08-05:13]. Steps: set external thickness (about 10), turn internal off while testing, add a Maxon Noise (Luka type), scale about 30-60, clamp low and high for contrast, feed it through a float Change Range into the external thickness modifier [05:13-07:19]. Second driver: a Fresnel (facing ratio), which makes lines thick on grazing angles and thin where the surface faces the camera; raise the range minimum to about 0.2 so lines never vanish, a marker-pen feel [07:49-09:24]. Combine the two with a Color Layer: noise as base, Fresnel on layer one in Overlay, so the Fresnel amount can be dialled from zero up [09:57-11:32]. Base thickness ended around 14-18 [11:00-13:35].
Angle threshold: larger means fewer crease lines, so he raised it to cut internal lines that would muddy the watercolor [12:02-15:10]; he admits it was done by taste.
He wishes for a light-angle-driven line width node; not available then (his claim).

**Use it:** use noise x facing ratio as the starting recipe for an inked, uneven line; judge by eye at final size.
