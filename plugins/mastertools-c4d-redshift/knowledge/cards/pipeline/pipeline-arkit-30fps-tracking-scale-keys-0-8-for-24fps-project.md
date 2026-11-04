---
id: pipeline-arkit-30fps-tracking-scale-keys-0-8-for-24fps-project
title: iPhone ARKit camera tracking is locked to 30 fps; to match a 24 fps project, scale the keyframes by 0.8 (24 divided by 30)
domain: pipeline
tags: [arkit, jetset, 30 fps, 24 fps, frame rate, keyframe scale, blender, autoshot, camera tracking, deep-read]
applies_to: Lightcraft Jetset, Autoshot, Blender
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=G0zHw0PbQ6A, src:yt-transcripts]
feeds: [CHECKS, pipeline design]
conflicts: none
---
Jetset on the cine rig gives tracking at the footage frame rate (24 here); the iPhone-only version tracks at 30 because ARKit is hard-locked to 30 [10:26][10:57]. Appending a second 30 fps camera into a 24 fps project: it will not play at its own rate, one second of the 30 fps data takes 6 extra frames [10:57][11:28]. Fix: select all keyframes from the first one, scale by 0.8 (24 / 30) so the motion lines up [11:28]. Even then the position can be wrong: he rotated the empty parenting camera and footage by eye until the green screen matched the scan [11:58]. Creator was sponsored by Lightcraft; takes this with the disclosure stated [00:34].

**Use it:** frame-rate mismatch check when importing any tracked or captured animation: confirm source rate before scaling keys.
