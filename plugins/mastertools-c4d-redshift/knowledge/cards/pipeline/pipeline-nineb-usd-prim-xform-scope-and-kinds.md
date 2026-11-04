---
id: pipeline-nineb-usd-prim-xform-scope-and-kinds
title: In USD a 'prim' is any scene element; xform is a movable parent, scope a non-moving one (materials), and kinds tag component (finished asset), assembly and group
domain: pipeline
tags: [nine between, houdini, solaris, usd, prim, xform, scope, kind, component, assembly, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Primitive means any element, not 'basic geometry': light, camera, mesh and so on, each with a type [26:32-27:34, 37:24-37:55]. Xform is a null-like parent that can move children; scope is a parent that never needs to move, so materials sit under scopes [27:34-28:05, 38:25-38:56].
Kinds: a component is one composed, finished asset (a door); an assembly is components combined (a house or workstation); a group is any arbitrary related set (all lights, all trees) [28:05-29:38, 43:38-45:12].
Unique node names become unique prim names [39:58-40:30].

**Use it:** Vocabulary for the coach when reviewing a USD hierarchy and for naming assets in a handoff.
