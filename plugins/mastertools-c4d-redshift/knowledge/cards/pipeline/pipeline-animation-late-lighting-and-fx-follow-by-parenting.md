---
id: pipeline-animation-late-lighting-and-fx-follow-by-parenting
title: Parent FX and lights to rig anchors so late animation changes still carry the effects; separate files let departments work out of order
domain: pipeline
tags: [cody winchester, dylan goo, dillongoo studios, blender conference 2024, parenting, lighting, fx, late changes, empties, link, deep-read]
applies_to: Blender
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aDsyNfISVLA, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Goo and Winchester [50:44-54:00]: lighting and FX files link the animation file but do not wait on it; an FX like an explosion needs no final animation. Empties are parented to the rig and effects to the empties; face and hair lights are parented to the head. Animation files may get fixes right to the end, with separate cleanup passes for clipping late in the project.
Quality check is constant playblasts on the shared timeline.

**Use it:** build FX and light rigs from anchors on the animation so a re-time or pose fix does not force a rebuild.
