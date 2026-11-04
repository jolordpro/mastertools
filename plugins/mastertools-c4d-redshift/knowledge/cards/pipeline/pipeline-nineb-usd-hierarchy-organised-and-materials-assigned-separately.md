---
id: pipeline-nineb-usd-hierarchy-organised-and-materials-assigned-separately
title: Build the stage in organised branches (geo, cameras, lights, materials) and assign materials by path, rather than importing everything in bulk
domain: pipeline
tags: [nine between, houdini, solaris, usd, scene graph, assign material, hierarchy, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS, shakedown]
conflicts: none
---
A bulk 'import all' scene import works but gives a flat, unorganised stage with little control [33:48-35:21]. Better: import geometry under /Geo, cameras and lights separately, materials in their own scope, then assign by dragging prim to material [39:27-43:38].
Assigning to a parent applies to everything inside; assign to the mesh itself to stay safe. If two assignments conflict the later one wins [43:08, 1:40:27].
Keeping materials on a side stream and assigning later lets another artist supply them [54:29-55:31]. A disabled prim keeps a marker (red dot) showing a viewport override [35:21-35:51].

**Use it:** A scene check: look for stage branches by type and explicit material bindings, not one big pile.
