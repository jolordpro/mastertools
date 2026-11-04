---
id: c4d-2024-rigid-body-collider-polygon-count-and-collision-shape-choices
title: The new rigid body treats vertices like particles: a denser collision mesh is more accurate (add segments to the floor), and Convex Hull with a small geometry accuracy is the efficient shape
domain: c4d
tags: [rigid body, collision shape, convex hull, geometry accuracy, vertices, triangle mesh, draw rigid body shapes, deep-read]
applies_to: Cinema 4D 2024 rigid body (School of Motion, EJ, Apr 2024)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=_6toVWN7NMo, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
EJ [05:12-10:22]. Opposite of the old habit of keeping everything light: because the system is particle-based, a higher polygon count means fewer objects passing through the collider; a floor with too few vertices let bricks intersect until he raised its segments, and that did not slow the sim [05:43-06:44]. Dense bricks (from Volume Builder) were fine because the sim uses a simplified collision shape.
See it: Project settings, Simulation, Draw, tick the rigid body shapes [07:44]. Auto shape is a shrink-wrap that ignores nooks. Options: Box and Sphere (fast), Triangle Mesh (best quality, no settings), Convex Hull with a Geometry Accuracy slider. He prefers Convex Hull with accuracy about 2 or 3 for the bricks, sometimes up to 20 for other objects [08:17-09:51]. Rewind and replay to see changes. For the demo he used Box with accuracy at zero [09:51-10:22].

**Use it:** Pick the cheapest collision shape that matches the silhouette; densify the collider, not the moving objects, when pieces pass through.
