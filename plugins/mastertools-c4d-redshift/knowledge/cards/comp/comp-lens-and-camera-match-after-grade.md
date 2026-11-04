---
id: comp-lens-and-camera-match-after-grade
title: After colour, match lens and camera: focus and bokeh, chromatic aberration, motion blur at 0.5 shutter, then shot-specific effects
domain: comp
tags: [courtney price, nuke, foundry, depth of field, chromatic aberration, motion blur, shutter, bokeh, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=yl28HkA-qyo, src:yt-transcripts, https://www.youtube.com/watch?v=ETV1VTV0vNg]
feeds: [composition]
conflicts: none
---
Courtney Price's sharpness stage has three sub-parts [31:48-33:55]:
Focal: defocus, ZDefocus or convolve, with a free bokeh-builder gizmo by Kieran Bishop to shape a kernel; add chromatic aberration (the RGB split grows toward the lens edge).
Motion: motion blur on the transform with shutter 0.5 (180 degrees); 0.25 is 90 degrees. Feed the transform into MotionBlur2D to make vectors, then vector blur [32:51].
Contextual: focus pulls, shallow depth, vignetting, anamorphic stretch if the plate has them.
Transfers to broadcast: same checks when a C4D render sits over footage.

**Use it:** Use it as the lens-match checklist after colour: blur, fringing, shutter and vignette all need to match the plate.
