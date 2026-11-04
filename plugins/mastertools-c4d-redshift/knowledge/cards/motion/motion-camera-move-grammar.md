---
id: motion-camera-move-grammar
title: Read camera move type exactly from the keyframes: 16 named moves, and flag accidents (dolly zoom, stray roll, dead-stop ease, push-in too short)
domain: motion
tags: [motion, camera, move, dolly zoom, push in, pan, tilt, roll, keyframes, shotbench]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://arxiv.org/html/2506.21356v2, https://arxiv.org/abs/2504.15376, src:research-production-pipelines, https://www.youtube.com/watch?v=IiyBo-qLDeM]
feeds: [PLAN Phase 1 computed shot labels]
conflicts: none
---
ShotBench move list: push in, pull out, boom up/down, pan left/right, tilt up/down, zoom in/out, static, move left/right, arc, camera roll, dolly zoom.
Movement was the weakest dimension for most vision models, and CameraBench reports weak geometric motion, so compute it.

**Use it:** name the move from the camera track and flag unintended roll, dolly zoom and dead stops.
