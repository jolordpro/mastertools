---
id: pipeline-nineb-usd-point-instancer-vs-instanceable-reference
title: Instancing keeps one copy in memory; switch to instanceable references only when individual copies need different variants
domain: pipeline
tags: [nine between, houdini, solaris, usd, instancing, memory, point instancer, layout, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [CHECKS, redshift]
conflicts: none
---
Instancing loads an asset once and copies it to points; each point can vary by normal, scale and orientation, and memory stays low [1:17:41-1:18:43, 1:25:59-1:26:30]. A layout node opens with one gumdrop asset inside though many are scattered.
If you must change a variant on single copies, change the method to instanceable reference: each copy is then editable, at a memory cost; he says use plain instances where possible [1:26:30-1:27:31].
Two routes: a layout node with an asset gallery (place or lasso-fill, with coverage and min/max radius) or an instancer node, which he finds more controllable [1:18:43-1:19:45, 1:23:21-1:24:55].

**Use it:** Decide per crowd or kit-bash whether copies need individual edits; if not, keep instances to hold Redshift memory down (see redshift-matrices-memory-growth).
