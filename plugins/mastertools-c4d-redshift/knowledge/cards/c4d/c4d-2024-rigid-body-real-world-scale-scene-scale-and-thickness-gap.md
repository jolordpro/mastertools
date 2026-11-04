---
id: c4d-2024-rigid-body-real-world-scale-scene-scale-and-thickness-gap
title: New-system rigid bodies need real-world scale; set Scene Scale to the average dynamic object size and cut the tag's Thickness on small objects or they hover above the floor
domain: c4d
tags: [rigid body, simulation scene, scene scale, thickness, hover gap, cloner, school of motion, 2024, deep-read]
applies_to: Cinema 4D 2024 rigid body (School of Motion, EJ, Apr 2024)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=_6toVWN7NMo, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
EJ (School of Motion, Cinema 4D 2024 new simulation system) [00:30-05:12]. Model to real-world scale first. Put the Rigid Body tag on the Cloner, not on the child objects, and a Collider tag on the floor [01:32]. The first play may sit on frame 0 while it calculates; more objects, longer wait [02:05]. Extend the document length (90 to 300 frames) so the sim can settle [02:37].
Hover fix: Project settings (Cmd/Ctrl-D), Simulation tab (not the old bullet tab), Scene Scale = the average size of the dynamic objects (his bricks were about 10 cm) [03:39]. On the tag, Thickness is a force-field-like skin to stop intersections; the default 1.5 is too large for 10 cm bricks, so he dropped it to 0.2 and the gap under the objects closed [04:10-05:12]. Also raise friction on the tag and collider to stop sliding [03:08].

**Use it:** Check Scene Scale and Thickness first when objects float on the floor or tunnel in a small-scale sim.
