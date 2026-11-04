---
id: comp-aces-dont-bake-view-transform
title: Do not bake the ACES view transform into renders: grade on the unprocessed image, then apply the transform
domain: comp
tags: [aces, view transform, banding, baked, comp, exposure, grade]
applies_to: any (shown with Redshift, After Effects, Fusion)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=vEoIXTbyz6o, src:yt-transcripts, https://www.youtube.com/watch?v=x2sx-P5f-iM]
feeds: [coach, shakedown]
conflicts: none
---
[04:15] A render with the ACES view transform baked in bands quickly when gain is pushed, and shows odd oversaturation. Colour-correcting the raw image and applying ACES on top stays clean (no banding in the forehead test).
[05:19] Corrections look better done before the transform, so the baked output costs flexibility.
[15:12] An exposure change placed after the transform looks bad; before it, it holds up.

**Use it:** flag a baked-in view transform on a delivery that will be graded in comp.
