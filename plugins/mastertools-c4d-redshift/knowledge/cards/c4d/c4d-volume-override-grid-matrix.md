---
id: c4d-volume-override-grid-matrix
title: Volume Builder has an Override Grid Matrix: a null moves, rotates or non-uniformly scales the voxel grid without moving the object
domain: c4d
tags: [volume builder, volume mesher, voxel, override grid matrix, null]
applies_to: Cinema 4D 2025
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=wsF5c_UnE40, src:yt-transcripts, https://www.youtube.com/watch?v=2yaRgwWYoDg]
feeds: []
conflicts: none
---
Meshes from a Volume Builder depend on where the object sits in the voxel grid, so moving the object changes the topology (a letter hole can close or connect) [56:12]. Feeding a null into the override lets the grid move instead; scaling one axis makes the mesh denser on that axis [57:13].

**Use it:** If a volume mesh changes when an object moves, check this override before blaming the settings.
Transcript support: Volume Builder voxel size 1 then Volume Mesher with adaptive reduces polygon count when converting text to a Pyro container (https://www.youtube.com/watch?v=2yaRgwWYoDg [01:45])
