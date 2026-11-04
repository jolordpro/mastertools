---
id: pipeline-nineb-materialx-only-subnet-keeps-shaders-portable
title: Build MaterialX shaders in a MaterialX-only subnet: it hides renderer-specific nodes so a mix cannot break the shader elsewhere
domain: pipeline
tags: [nine between, houdini, solaris, usd, materialx, subnet, portability, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
If a VEX node is mixed with MaterialX nodes, the shader breaks in other apps and in Karma XPU [37:19-38:22]. A MaterialX subnet filters the node list to MaterialX nodes only, so only portable nodes can be used [38:22-38:54].
Some SideFX-made nodes (a colour ramp) are marked: they are not in the MaterialX standard, but still write valid MaterialX code, though other apps will not show that node [45:37-46:08].

**Use it:** For a portable look, use only standard MaterialX nodes and note any vendor-only ones in the handoff.
