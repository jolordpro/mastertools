---
id: c4d-2024-rigid-body-follow-position-turbulence-swarm-recoil-and-initial-state
title: A swarm effect: gravity 0, Follow Position and Rotation at 1 for tight or 0.5 for loose, turbulence on top, Recoil for springiness and Set Initial State to start mid-motion
domain: c4d
tags: [rigid body, follow position, follow rotation, recoil, damping, turbulence, set initial state, swarm, cloner, deep-read]
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
EJ [24:42-31:05]. Scene gravity to 0 (default is -981). Force tab: Follow Position and Follow Rotation at 1/1 makes dynamic copies track a vibrating cloner exactly; add a Turbulence force and strengths up and it becomes a swarm that follows a keyframed cloner [25:01-27:07]. At 0.5/0.5 it follows loosely; a second copy of the setup with a different random seed makes two swarms interact [27:07].
Damping inside the follow settings: 3 makes everything slow like water or oil [28:09]. Recoil (new) at 2 gives springy overlapping movement; negative values (such as -2.4) smooth the blend instead [28:40-29:43]. Field forces now work on rigid bodies too [29:43].
If the mid-motion look is wanted from frame 0, Dynamics tab, Set Initial State bakes that frame-zero arrangement, then more motion can follow [30:15-30:46].

**Use it:** Swarm and particle-stream motion graphics with controllable paths, cheaper than a particle system.
