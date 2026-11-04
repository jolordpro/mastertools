---
id: pipeline-nineb-usd-variants-one-asset-many-geos-and-materials
title: USD variants store several geometries and materials in one asset; link each geometry to its own material or the first alphabetical material is applied to all
domain: pipeline
tags: [nine between, houdini, solaris, usd, variants, nested variants, explore variants, materials, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts, https://www.youtube.com/watch?v=3Z4-9qN0KHg]
feeds: [CHECKS, coach]
conflicts: none
---
Variant sets let one asset hold, say, three geometries (gumdrop, jelly bean, smarty) and three materials; you pick which one in the scene graph, or per instance [57:04-58:38, 1:08:26-1:10:31]. By default a component's material goes onto every geometry, taking the first material in alphabetical order, so all three pieces came out the same until each material was assigned explicitly [1:03:48-1:04:20, 1:11:02-1:12:35].
With nested variants each geometry carries only its own material, so switching geometry switches material too; lights can even be merged in as a variant [1:14:37-1:16:40]. A car with interior, seat and dash variants is his example [1:14:06-1:14:37].

**Use it:** Package team-colour or product variants in one asset instead of copies; verify that every variant has an explicit binding.
