---
id: c4d-object-profiler-find-slow-objects
title: Object Profiler (Window menu) ranks objects by share of calculation time, so the slow one can be swapped
domain: c4d
tags: [object profiler, performance, viewport, slow scene, c4d]
applies_to: Cinema 4D 2025
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=wsF5c_UnE40, src:yt-transcripts]
feeds: [advisor, estimator]
conflicts: none
---
Open it from the Window menu; set it to All Frames and percent for a running average [04:23]. In his demos a target effector took 25% of calc time, a Thicken generator 65%, a capsule Extrude 80%. Swapping to the old Cloth Surface (with thickness) cut that to about 5%, roughly 60% faster overall [07:00]. Ctrl-click turns a hierarchy off; selection syncs with the Object Manager. It measures scene calculation, not render time.

**Use it:** When a draft or viewport is slow, rank objects by percent and suggest a swap for the top one before blaming the GPU.
