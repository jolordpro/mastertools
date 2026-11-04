---
id: pipeline-splat-in-blender-ply-attributes-and-floater-filter
title: A splat .ply imported into Blender is a point cloud with colour (DC0-2) and spherical-harmonic attributes; remove floaters by nearest-neighbour distance
domain: pipeline
tags: [gaussian splatting, ply, blender, geometry nodes, spherical harmonics, floaters, nearest neighbour, deep-read]
applies_to: Blender 3D Gaussian Splatting add-ons
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=ERuRMOVO58Q, src:yt-transcripts]
feeds: [pipeline design]
conflicts: none
---
Spherical harmonics (0 to 3) control how far each splat's colour changes with view angle; 0 is plain and view-independent [07:47]. Imported in Blender, the splat shows as plain points with scale, rotation and DC0, DC1, DC2 as RGB, and rest values for harmonics [12:56][14:31]. Z-up fix: rotate 90 degrees on X [13:27]. Floater filter in geometry nodes: for each point, distance to its nearest neighbour; delete above a threshold (dense areas black, strays bright) [14:31][15:02]. Two add-ons: one imports as points with a shader (fast, can be lit with a point light, works in Cycles, pad scale slightly ~2.1 to close gaps) and a slower one that builds planes facing the camera [16:03][17:34]. Camera trick: build the camera move in Blender, bake it to Alembic, export selection only, and render [19:08].

**Use it:** useful when a splat must go into a DCC for lighting or camera work; note view dependence is lost when converting to points.
