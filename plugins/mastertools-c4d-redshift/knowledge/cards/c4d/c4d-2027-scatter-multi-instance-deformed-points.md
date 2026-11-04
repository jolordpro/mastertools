---
id: c4d-2027-scatter-multi-instance-deformed-points
title: Scatter (C4D 2027) outputs multi-instances and follows a deformed landscape only with 'use deformed points' on
domain: c4d
tags: [scatter, mograph, instances, deformed points, landscape, distribution, plane deformer]
applies_to: C4D 2027.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: [scene checks, coach]
conflicts: none
---
[11:54] Scatter lives in the MoGraph menu and behaves like a cloner in fast multi-instance mode. It must sit after the object it scatters on.
Default surface scattering acts as if the ground were flat; with a deformer-built landscape switch on the deformed-points option [11:54] or the clones float on the undeformed plane.
Distribution modes: surface grid, spline projection, area weighted (random), UV grid. Viewport can show clones as bounding boxes, points or nothing, but he leaves it on object [13:26].

**Use it:** when a scatter sits on a deformed surface, check the deformed-points flag; floating clones in a draft are the symptom.
