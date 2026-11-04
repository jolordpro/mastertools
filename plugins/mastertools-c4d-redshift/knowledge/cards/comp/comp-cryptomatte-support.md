---
id: comp-cryptomatte-support
title: Cryptomatte is an open spec (Psyop, v1.4.0); Nuke and Fusion use plugins, After Effects relies on third-party tools
domain: comp
tags: [comp, cryptomatte, id matte, nuke, fusion, after effects, renderman, mask]
applies_to: Cryptomatte 1.4.0
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/Psyop/Cryptomatte, https://help.maxon.net/c4d/2026/en-us/Content/html/Cryptomatte.html, https://www.cgchannel.com/2026/07/pixar-releases-renderman-27-3/, src:research-vfx-pipelines, https://www.youtube.com/watch?v=cE-Bbdspu_8, https://www.youtube.com/watch?v=NaCJiquNnYY, https://www.youtube.com/watch?v=aR3yNNGK_sc, https://www.youtube.com/watch?v=Q3ceb1RsseE]
feeds: [PLAN masks]
conflicts: none
---
C4D 2026 help has setup; RenderMan XPU 27.3 has initial support limited to name, path and material layers.
Cryptomatte is a standard AOV request; large bucket sizes can conflict with it (Maxon trainer chapter title, not confirmed).

**Use it:** include Cryptomatte in the AOV package when per-object grading or masks are likely.
Transcript support: Nuke Cryptomatte gizmo is a separate GitHub install (2019); picker add and remove with control-click. (https://www.youtube.com/watch?v=Q3ceb1RsseE [02:13-02:46])
