---
id: comp-kelly-tetrahedral-interpolation-keeps-neutrals-neutral
title: "Cullen Kelly: choose tetrahedral over trilinear LUT interpolation because it keeps achromatic neutrals from drifting"
domain: comp
tags: [cullen-kelly, lut, tetrahedral, trilinear, interpolation, neutrals, polish, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster]
feeds: [comp, redshift]
conflicts: none
---
Both schemes estimate output for values between a LUT's sample points. Tetrahedral is better: it keeps neutrals (equal R, G and B) free of colour bias, and he says it is also more efficient and more accurate [46:23-47:56]. His short rule: go with tetrahedral. He promised a link to the 3D geometry write-up (not captured).

**Use it:** If an app lets you pick interpolation for a 3D LUT, set tetrahedral.
