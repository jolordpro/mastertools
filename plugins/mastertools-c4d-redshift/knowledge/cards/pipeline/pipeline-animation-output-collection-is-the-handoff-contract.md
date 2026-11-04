---
id: pipeline-animation-output-collection-is-the-handoff-contract
title: The animation file exposes one 'animation output' collection; the lighting file links only that, so anything left out stays behind
domain: pipeline
tags: [nick alberelli, blender studio, kitsu, editorial, collection, link, handoff, animation output, fx, deep-read]
applies_to: Blender
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jiXB5X1S1AI, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Alberelli [17:44-18:45]: a shot builder creates each department's file from Kitsu data. The animation file has an output collection that mirrors what should pass downstream; lighting links that collection. Reference-only objects are left out.
For FX that needs rig info, override the collection to expose more objects [47:09].

**Use it:** define an explicit handoff set per department (a group or take) and keep reference items outside it.
