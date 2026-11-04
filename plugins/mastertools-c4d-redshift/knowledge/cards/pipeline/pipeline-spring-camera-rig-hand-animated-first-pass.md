---
id: pipeline-spring-camera-rig-hand-animated-first-pass
title: Failure: layout camera data would not transfer to the armature camera rig, so the first camera pass was redone by hand
domain: pipeline
tags: [pipeline, camera, layout, rig, coordinates, armature, handoff, failure, deep-read]
applies_to: Blender 2.8
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aR3yNNGK_sc, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Layout used plain cameras with object animation; production used a camera rig driven by actions with different pivots [25:24]. Transferring motion from the layout camera into the rig failed because armature and world coordinates did not match, so most shots were hand-animated for the first camera pass in the anim file [25:24] [25:57].
Cameras in set files also had no good way to stay up to date [19:39].

**Use it:** Warn when a camera is rebuilt as a rig: plan for a manual first pass. Keep layout camera data as reference only.
