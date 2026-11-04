---
id: pipeline-houdini-mesh-cross-dissolve-erode-by-uv-with-thresholds-synced-between-sim-and-geometry
title: Mesh cross-dissolve in Houdini: erode two shapes with the same UV threshold in sim and in geometry, play one in reverse, and point deform per connected piece rather than remeshing
domain: pipeline
tags: [tim-bolland, man-vs-machine, houdini, grains, constraints, uv, point deform, cross dissolve, deep-read]
applies_to: Houdini grains/DOPs
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=JCUks81cBtw, src:yt-transcripts]
feeds: []
conflicts: none
---
Idea: a swirling orb of materials erodes away; the glasses run the same simulation setup eroding to nothing; play the glasses footage in reverse, like a cross dissolve done with meshes [27:42-29:17]. Setup: separate parts by material attribute with connectivity, make UVs, delete points by a UV x threshold that wipes over time; randomly stretch or offset the UVs per island, which shifts timing island by island [31:26-33:07]. The threshold must be synced between the geometry and the simulation so point deform keeps a one-to-one point match with nothing missing [33:07-33:37]. Grain sim: noise attraction to a middle point, curl noise at two scales, animated pull and push; constraints start attached and pop after a time, and a stretched rest length on border constraints gives the initial burst [29:48-34:45]. Run point deform inside a for loop per connected piece, because it keeps original UVs and works better than remeshing [35:20]. The pop effect was accidental and made the film [30:22].

**Use it:** A method card for transitions made of geometry; the sync-threshold rule applies to any sim-plus-geo workflow.
