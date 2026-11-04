---
id: c4d-safe-frame-matte-plane-child-of-camera
title: Custom safe frame: a rectangle for the crop and a holed luminance plane, both children of an active camera
domain: c4d
tags: [safe frames, social crop, 9x16, camera child, matte, luminance plane, viewport guide]
applies_to: C4D 2026 (Maxon QuickTip 246)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KCZN2neNUNE, src:yt-transcripts]
feeds: [CHECKS, safe-area helper]
conflicts: c4d-safe-frames-spline-tip
---
[03:13] Make a rectangle at the crop aspect (any equal ratio), parent it to the active camera (the default camera does not work), zero coordinates, move it into the frustum, switch off render.
[05:17] Dim outside the crop with a plane parented to the camera, holed in the middle, using a classic material with luminance plus transparency (refraction 1) and a display tag with no lines.
[07:20] Save the group as a null for reuse. Title and action safe are percentages of resolution, so a square or 9:16 safe frame needs this.

**Use it:** use for one-render, multiple-crop deliveries.
