---
id: pipeline-usd-scope-vs-xform-prims
title: USD scope prims hold no transform; xform prims do, so cameras sit under xform and render settings under scope
domain: pipeline
tags: [usd, scope, xform, hierarchy, camera, deep-read]
applies_to: USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hBYSHFRnFlo, src:yt-transcripts]
feeds: []
conflicts: none
---
The two simplest prim types are scope and xform, both only organizing children [20:43-21:13]. A scope stores no transformation, so render settings sit under a scope. An xform can carry a transform, so a camera is parented under one because it will move [21:13-21:46].

**Use it:** Use scope for pure folders (lights, materials, render settings) and xform when the group has to move as a unit.
