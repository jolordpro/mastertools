---
id: broadcast-capacity-sort-priority-one-modifier-for-2d-stacking
title: One translucent sort-priority modifier on the top null lets 2D layers share the zero plane and stack in layer order
domain: broadcast
tags: [translucent sort priority, 2d layers, z fighting, layer order, sort mode, motion design, deep-read]
applies_to: Unreal Engine 5.6 / 5.7 motion design
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=YiMh6bEebIs, src:yt-transcripts]
feeds: []
conflicts: none
---
Mixed 2D and 3D scenes would otherwise need each 2D plane offset by something like 0.1 in space to avoid fighting [56:08]. A single translucent sort priority modifier at the top of the content null puts everything on the zero plane and orders by layer [1:00:51]. Default sort mode is bottom-first on top, matching render order in many broadcast tools; Photoshop-style top-first can be chosen instead [1:01:21-1:01:51]. A typical graphic needs just one [58:14]. Capacity said getting this right was the first hard part [1:48:17].

**Use it:** If a real-time or C4D 2D layout shows order flicker, solve with one stacking rule, not per-layer offsets.
