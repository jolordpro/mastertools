---
id: pipeline-nineb-usd-layers-explicit-save-paths-per-department
title: Give each USD layer an explicit save path (geo, lights, cameras, instances) and merge as separate layers; implicit layers get flattened and are hard to control
domain: pipeline
tags: [nine between, houdini, solaris, usd, layers, sublayer, configure layer, explicit save, department, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts, https://www.youtube.com/watch?v=XUsleR7wJhk]
feeds: [CHECKS, coach]
conflicts: none
---
By default Solaris saves layers implicitly. A configure-layer node sets an explicit save path (e.g. main_geo.usd, lights.usd, cameras.usd), the merge node must be set to separate layers, and the final scene file is just a sublayer list (written as .usda to read it) [2:39:46-2:44:26, 2:41:52-2:42:53].
Layers can reference assets; when the referenced asset changes, the layer picks up the change on load [2:44:58-2:45:59]. Each layer can be loaded alone, so lights, cameras and geometry owners work separately and are assembled in a master file [2:45:59-2:47:32].
Goal: avoid implicit saves so you know where everything goes; any implicit ones are flattened into one [2:42:53-2:43:54].

**Use it:** A USD handoff rule: one layer per department with a fixed name, and a master file that only lists sublayers.
Transcript support: second walkthrough: Start New Layer per department with a node-name-based save path; defaults can be set with make current value default (https://www.youtube.com/watch?v=XUsleR7wJhk [04:48])
