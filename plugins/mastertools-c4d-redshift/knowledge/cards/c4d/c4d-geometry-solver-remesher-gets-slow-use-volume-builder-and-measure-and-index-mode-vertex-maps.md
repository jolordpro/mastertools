---
id: c4d-geometry-solver-remesher-gets-slow-use-volume-builder-and-measure-and-index-mode-vertex-maps
title: In a C4D geometry solver the Remesher gets slow as geometry grows; Volume Builder at 5 cm then 2 cm is far faster, and vertex maps use index mode
domain: c4d
tags: [scene-nodes, geometry-solver, volume-builder, remesh, performance, dominik-ruckli, cinema-4d-2025, deep-read]
applies_to: Cinema 4D 2025
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=Iy2FAJbbyrY, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
Dominik Ruckli, 2025.
- A Remesher in the solve step has to raise density each frame as the mesh grows (he tried triangles and about 102 percent density) and is slow [08:34-09:36].
- Replacing it with Volume Builder then Volume Measure was much faster; voxel size 5 cm to start, 2 cm for the final [09:36-10:06, 32:59].
- When vertex maps are read on the same geometry, set the mode to index so no nearest-point search is made [35:03].
- Dial smoothing and strength back after raising resolution, since values that read well at low resolution get too strong [33:30].

**Use it:** The performance rule for any iterating sim: stay in the volume domain, not remeshing.
