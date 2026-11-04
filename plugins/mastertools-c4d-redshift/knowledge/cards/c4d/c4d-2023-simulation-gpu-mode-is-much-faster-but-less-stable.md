---
id: c4d-2023-simulation-gpu-mode-is-much-faster-but-less-stable
title: The 2023 particle-based simulation system can run on GPU or CPU (Project settings, Simulation); GPU is far faster but can be less stable
domain: c4d
tags: [simulation, gpu, cpu, project settings, particle based, cloth, stability, deep-read]
applies_to: Cinema 4D 2023 new simulation system (School of Motion, EJ, Oct 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dHQWVXWbsEM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
EJ [03:42-04:44]. New simulation settings live in the Simulation tab of Project settings (old Bullet settings and the expert tab are in the Bullet tab). A switch chooses CPU or GPU; he says GPU makes a long wait instant, but GPU can be less stable. The system is particle-based, which is why it is fast and a base for later fire, smoke or liquid solvers (he hints at an upcoming Maxon teaser) [04:12-05:16]. The old dynamics could explode polygons; the new one is much steadier [03:11].

**Use it:** Draft on GPU, but if a sim glitches, test the same scene on CPU before blaming the setup. Also cache before farm (see the cache card).
