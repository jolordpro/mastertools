---
id: c4d-2027-sample-field-node
title: The Sample Field node lets any C4D field drive a Scene Nodes tool, for example blending points to a target by field strength
domain: c4d
tags: [scene nodes, sample field, field, modifier, black hole, electric spline, custom tools]
applies_to: C4D 2027.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: []
conflicts: none
---
[01:10:16] Add a Sample Field node, expose the field as an input, and it gives a 0 to 1 value, colour, direction or deactivate output.
Recipe [01:12:50 to 01:20:04]: Nodes Modifier, get/set geometry positions, iterate collection, mix between original and target position by the field value, local position fed from each point. Six nodes give a black-hole effect on any model.
Adding it to an existing tool took three nodes, giving the electric spline modifier full field falloff [01:27:19].

**Use it:** when users ask for field control on a custom tool, point to Sample Field.
