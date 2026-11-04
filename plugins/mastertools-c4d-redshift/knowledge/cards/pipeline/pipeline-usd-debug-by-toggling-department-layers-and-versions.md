---
id: pipeline-usd-debug-by-toggling-department-layers-and-versions
title: Debug a USD shot by enabling layers one department at a time, then swapping versions of a single layer
domain: pipeline
tags: [pipeline, usd, debugging, layer manager, versions, usdview, department, deep-read]
applies_to: Prism USD layer manager
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CpiumJctktM, src:yt-transcripts]
feeds: [shakedown, CHECKS]
conflicts: none
---
Prism's layer manager lists every department layer and sublayer in the shot container; with all layers off nothing shows [28:52] [29:22]. Order shown: layout gives camera and static assets, animation gives moving characters, effects the simulated pebbles, then sequence lighting (dome) and finally shot lighting for the final image [29:22] [29:54].
You can then switch the version of a single layer, for example the previous camera, to see the effect, and use USD's viewer (usdview) for hierarchy, attributes and material bindings [30:25].

**Use it:** Debug order for any layered scene: add one layer at a time in department order and note where the image goes wrong.
