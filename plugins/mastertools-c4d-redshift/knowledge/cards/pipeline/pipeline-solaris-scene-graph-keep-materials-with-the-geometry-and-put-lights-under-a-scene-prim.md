---
id: pipeline-solaris-scene-graph-keep-materials-with-the-geometry-and-put-lights-under-a-scene-prim
title: Solaris scene organisation habit: one scene prim holding geometry (with its materials inside), cameras and lights, so an object can move to another scene with its materials
domain: pipeline
tags: [solaris, scene graph, usd, primitive path, organisation, materials, deep-read]
applies_to: Houdini 18.0 Solaris, 2020
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=lidw4rllGV4, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
The scene graph panel is the outliner: a Scene root, then geometry, cameras and lights [21:51-22:53]. Materials sit inside each geometry's collect so the object can be moved to another scene and bring them [22:22].
New lights land at the root; setting the light's primitive path with /scene/ puts them under the scene prim ('/' is the node name token) [22:53-23:23].
He urges a fixed layout and following the studio's own convention if one exists [21:51].

**Use it:** Matches the USD layout practice in the KB; adopt one fixed prim layout per project.
