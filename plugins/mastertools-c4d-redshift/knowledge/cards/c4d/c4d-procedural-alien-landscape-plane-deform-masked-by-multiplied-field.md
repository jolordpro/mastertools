---
id: c4d-procedural-alien-landscape-plane-deform-masked-by-multiplied-field
title: Block a landscape procedurally: 1000x1000 plane (a million polygons), Plain effector deforming points in Z, a big noise, then mask it by multiplying with a spherical field
domain: c4d
tags: [landscape, plane, plain effector, noise, mask, multiply, subdivision surface, procedural, fields, deep-read]
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
Steps [52:10-56:49]. Plane at 1000x1000 segments is about a million polygons, the most the trainer would go. Plain effector set to deform points with Z offset (50 to 100). Noise (he likes Luka noise, size around 1500) makes the terrain.
Mask: multiplying a gradient field in the field list masks the effect, since the sphere is 0 at its edge and 1 in the middle, so 0 times anything stays 0 [53:11-53:42]. Add another random noise at lower influence for detail.
Workflow to stay fast: block the broad shapes on a low-poly plane, put it under a Subdivision Surface, add a second Plain effector with a small noise for fine detail on the subdivided points, then another subdivision on top (a few million polygons, wait) [54:13-56:18]. Make editable and save a copy when satisfied. Splines in the field list can cut canyons and roads; project them with Shrink Wrap first [56:49].

**Use it:** Background terrain or planet surfaces for a sports open's world-building, iterated cheaply at low subdivision.
