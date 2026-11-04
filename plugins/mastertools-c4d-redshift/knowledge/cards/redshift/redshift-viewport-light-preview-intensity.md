---
id: redshift-viewport-light-preview-intensity
title: If lights blow out in Gouraud viewport shading, lower Preview Intensity on each light or switch to Quick Shading
domain: redshift
tags: [Chad, Greyscalegorilla, viewport, Gouraud shading, preview intensity, lights, deep-read]
applies_to: Cinema 4D + Redshift
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=le17-h6tUD0, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Chad: the viewport in Gouraud shading can show lights burnt out. On each light, Preview in the Object tab has an illumination adjustment; he sets 0.2 to 0.7, and the lower fill a bit less [39:35-40:31].
If the viewport lighting does not matter, switch the display to Quick Shading instead.
This only changes the viewport, not the render.

**Use it:** Coach: a blown-out viewport is a display problem, not a lighting fault; fix preview intensity before touching real light values.
