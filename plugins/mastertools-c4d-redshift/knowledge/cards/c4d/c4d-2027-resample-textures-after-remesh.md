---
id: c4d-2027-resample-textures-after-remesh
title: C4D 2027 Create > Resample Textures moves a scan's texture onto a remeshed model and builds new UVs by itself
domain: c4d
tags: [resample textures, remesh, photogrammetry, scan, uv, texture transfer, kiri engine]
applies_to: C4D 2027.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: []
conflicts: none
---
[54:44] Workflow: remesh the scan to about 10% of its polygons, feeding an outline spline as a flow guide for cleaner flow.
[55:45] Resample Textures: choose the source UV tag, the target object, and an output folder. It reprojects UVs itself if none are set and writes a new texture; results were cleaner on seams than the remesher's own transfer. The output folder naming is clunky.
Replaces a hand-baked process that took a 2 h 7 min tutorial [52:10]. Test scan came from a phone app (Kiri Engine).

**Use it:** recommend this for cleaning scanned props before they enter a Redshift scene.
