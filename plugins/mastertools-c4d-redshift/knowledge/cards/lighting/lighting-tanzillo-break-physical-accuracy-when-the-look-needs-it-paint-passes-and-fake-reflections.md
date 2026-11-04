---
id: lighting-tanzillo-break-physical-accuracy-when-the-look-needs-it-paint-passes-and-fake-reflections
title: Mike Tanzillo: lighters break physical accuracy to get the look, and a painter's eye beats a photographer's for it
domain: lighting
tags: [mike-tanzillo, photorealism, art direction, passes, reflections, light linking, renderman, deep-read]
applies_to: RenderMan and V-Ray as discussed (2020)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=yDcjIk7L-0Y, src:yt-transcripts]
feeds: [elevate, redshift]
conflicts: none
---
Tanzillo says his studio chose RenderMan partly because creative control matters more than accurate ray-traced bounces on an abstract film [33:17-33:49]. A photoreal-leaning studio (captioned 'Wetty'; probably Weta, unverified) discouraged or blocked light linking, and artists still worked round it [33:49]. A painting background helps more than a photography one because lighters paint with light and must control bounces, not simulate them [34:51].
Photoreal and real are different: the eye sees deeper into shadows than film does, so an art director may want lifted shadows; treat photoreal as one style (blown highlights, crushed blacks) among others [35:55-36:57].
His own habit: he plans a perfect shader setup, then ends up breaking it with separate render layers; on a mirror-material one-off he renders a separate pass, paints in the reflections he wants and colour-corrects, and finished faster than a colleague who was calculating the reflection falloff exactly [37:29-39:03]. He says he would not repeat that on a film that must be physically accurate.
Transfers to Redshift/C4D: a reflection or glow pass graded in comp is a legitimate fix when the brief is look, not physics.

**Use it:** When a look fights the physics, the coach should suggest a pass plus grade before more render time; keep physical accuracy only when the brief demands it.
