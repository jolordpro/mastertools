---
id: c4d-voronoi-slicer-stable-weights-give-loopable-colour
title: A looping sliced-banana effect: give each matrix clone a fixed weight with a Step effector, bring it into a field as a MoGraph object, and colour from a gradient so colours stay stable over the loop
domain: c4d
tags: [voronoi fracture, matrix, step effector, weights, mograph object, gradient, loop, color, motion blur, deep-read]
applies_to: Cinema 4D 2022 (Maxon Ask the Trainer, Apr 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cCCgPVurWjQ, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Trainer (Nosman) [57:52-1:09:21]. Voronoi Fracture reads its source points from a Matrix set to Object mode on a spline; Rate percent sets travel speed (33.333% for a 3 second travel along the line, with a 3 s loop) [58:54-59:56]. Colouring by index flickered because indices change as points change [1:00:28].
Fix: a Step effector on the Matrix affecting Weight gives every clone a unique, stable weight from 0 to 100. In the Voronoi Fracture's fields color, drag the Matrix into the field list and accept the MoGraph object option; only weights come across, no positions or values. Turn on color Remapping, use a gradient preset [1:01:29-1:03:34]. Loop tip: the first and last frames are identical in an absolute loop, so render one frame fewer or trim in comp [1:03:34].
Bonus: linear field on Z plus a Sine preset in the contour curve makes the pieces ripple like a worm; the animation still loops [1:04:36-1:05:39]. Any object (a banana) can replace the cubes; dynamics on it are unstable as topology changes [1:06:13-1:06:43].
Warning at [1:09:21]: this will not motion-blur correctly, since the fragments are not the same object frame to frame.

**Use it:** Looping graphic slices with stable colour; for blur, render with motion blur off and add it in comp.
