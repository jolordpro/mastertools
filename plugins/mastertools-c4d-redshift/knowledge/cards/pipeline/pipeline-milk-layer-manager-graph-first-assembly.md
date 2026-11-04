---
id: pipeline-milk-layer-manager-graph-first-assembly
title: Start from the layer graph: a template manifest of the asset, then load only the prims a shot needs
domain: pipeline
tags: [milk vfx, layer manager, usd, assembly, environment, prims, template, deep-read]
applies_to: Houdini Solaris, ShotGrid (Milk VFX, FMX HIVE 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=XfMp13jOSxE, src:yt-transcripts]
feeds: []
conflicts: none
---
Enrico (co-head of VFX, Milk VFX; surname not caught). Instead of pulling a whole heavy asset and pruning downstream, they open the graph to artists as the start of the process [33:20-33:52]. A manifest/template describes the asset graph first; this forces thought about the hundreds or thousands of prims an environment holds [33:52-34:23]. A layer-manager panel mirrors the Solaris graph so primitives can be loaded dynamically, as granular as needed, and small shot-based assemblies get built on demand [34:23-35:57].

**Use it:** Fits shot-specific dressing: pull the few prims a shot needs.
