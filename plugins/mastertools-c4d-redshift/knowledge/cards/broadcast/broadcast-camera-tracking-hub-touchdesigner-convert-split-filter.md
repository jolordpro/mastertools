---
id: broadcast-camera-tracking-hub-touchdesigner-convert-split-filter
title: Normalise broadcast camera tracking in TouchDesigner: convert between protocols, split one source to several engines, and filter before the render engine
domain: broadcast
tags: [camera tracking, touchdesigner, protocols, stype, mo-sys, encam, filter, live link hub, broadcast ar, girraphic, deep-read]
applies_to: Unreal Engine, TouchDesigner (2025)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=2DoF-oYNQgU, src:yt-transcripts, https://www.youtube.com/watch?v=cE3jw6MO9kw]
feeds: []
conflicts: none
---
Girraphic [07:25-10:28]. Broadcast incumbents have a box that combines all tracking sources, standardises and redistributes them; Unreal's Live Link Hub aims at animation and mocap, not broadcast AR. Many standards exist (a 1990s one, plus Stype, Mo-Sys, Encam formats; speaker names them aloud, captions are rough). TouchDesigner has input nodes for each protocol, output nodes, and a filter node, so data can be converted, split (a serial-port camera head went through a serial-to-Ethernet converter, then was split to several Unreal engines), and smoothed (simple filters or a Kalman-type filter) before it reaches any render engine, rather than inside each engine.

**Use it:** A tracked-camera check should confirm one protocol, one filter and one fan-out point, with the filter outside the render engines.
Transcript support: stadium AR uses Stype mechanical tracking per camera, with one render engine fed per tracked camera (https://www.youtube.com/watch?v=cE3jw6MO9kw [55:39])
