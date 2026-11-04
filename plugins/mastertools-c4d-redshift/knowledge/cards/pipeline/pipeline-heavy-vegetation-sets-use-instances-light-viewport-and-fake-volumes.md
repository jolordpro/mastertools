---
id: pipeline-heavy-vegetation-sets-use-instances-light-viewport-and-fake-volumes
title: For heavy vegetation sets: instances and proxies, a bare-minimum viewport, nothing modelled outside the camera, and faked volumetric light
domain: pipeline
tags: [vegetation, instances, proxies, viewport, sampling, volumetric lights, sss, aov, cube creative, cycles, deep-read]
applies_to: Cycles, Blender 2.7x (2018)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=4R8PduY_vV4, src:yt-transcripts]
feeds: []
conflicts: none
---
Cube Creative [13:32-18:52]. A moss-and-grass set had huge poly and object counts, so instances and proxies were needed early; Cycles' memory use with instances was very good. The viewport showed only the largest grass fans and rough shapes so layout and animation stayed responsive. Do not model anything outside the camera's view. Memory was not the limit; sampling noise was, so the team balanced detail scale against what could be rendered, mindful of close shots. They could not afford physical volumetrics, so they used rigging plus textures on polygons for light shafts that survive large camera moves. Principled shader made subsurface easy. Problem: at that time Cycles could not render custom AOVs without rebuilding the scene for each render layer.

**Use it:** Check list for a heavy-set shot: instances, a light viewport proxy, cull outside the camera, and cheaper volume fakes if sampling is the bottleneck.
