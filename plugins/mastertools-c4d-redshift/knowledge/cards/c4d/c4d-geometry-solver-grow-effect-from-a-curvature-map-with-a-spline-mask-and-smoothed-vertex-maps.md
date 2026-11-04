---
id: c4d-geometry-solver-grow-effect-from-a-curvature-map-with-a-spline-mask-and-smoothed-vertex-maps
title: Coral-like grow effect in a C4D geometry solver - Plane vector pushes along normals, driven by random field times curvature, masked by a spline
domain: c4d
tags: [scene-nodes, geometry-solver, curvature, vertex-map, fields, growth, cinema-4d-2025, deep-read]
applies_to: Cinema 4D 2025
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=Iy2FAJbbyrY, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Dominik Ruckli, 2025 [20:35-36:09]. Recipe order:
1. Solve step: a Plane vector moves points along their normal axis (Z) by about 3 to 5; sphere starts small [21:14].
2. Vertex map on the Volume Measure, driven by a Group field instead of building it inside the map [22:16].
3. Random field (noise) plus a curve for contrast as the base [22:48].
4. Volume Measure exports a convex curvature map; feed it back as a field (it is blank on frame 0, so add an initial random deformation to seed it) and boost its contrast with a curve [23:21-25:58].
5. Multiply curvature onto the base noise; the first result was far too strong, so reduce strength [25:58-26:37].
6. A blurry checkered look is fixed by a second vertex map in average mode (10 was too strong, 2 to 4 worked) which the Plane vector reads [27:09-28:44].
7. A circle spline in the Group field (radius mode) is the mask for where growth is allowed; any geometry or spline that works with fields can do it [28:44-31:56].
Tuning is by eye; he warns that numbers have to be re-dialled after each change.

**Use it:** A look-dev route for organic panel or logo growth with no simulation licence needed.
