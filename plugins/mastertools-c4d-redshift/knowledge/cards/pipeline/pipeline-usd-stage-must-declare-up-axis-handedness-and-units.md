---
id: pipeline-usd-stage-must-declare-up-axis-handedness-and-units
title: A USD file carries its own up axis, handedness and unit scale; set them or the receiving app will read the scene wrong
domain: pipeline
tags: [usd, openusd, up axis, handedness, meters per unit, coordinate system, interchange, deep-read]
applies_to: OpenUSD
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=_N--2xOXEN0, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
The creator (a game shader developer, not a vendor) says USD defaults to Z-up right-handed. Gate correction (from our knowledge of the USD spec, not re-checked today): USD's fallback up axis is Y, geometry is right-handed by default, and Z-up is a per-stage setting many apps write, so declare it rather than trusting a default. He contrasts this with Unity is Y-up left-handed; USD lets the author set the up axis, an orientation (left-handed) attribute, and default units so one unit equals one metre, and the app converts on import [06:49-07:52].
A mesh is vertices plus index lists for the triangles, face counts, and a bounding box used to skip off-screen objects [07:52-08:55]. USD has a built-in PBR surface material that works across apps, and the Unity import hot-reloaded when the file was re-saved [08:55-10:28]. The whole procedural plane took about 30 lines of Python [10:28]. Per the speaker the format cannot yet describe rigs [02:38]. Other points: USD is also an ecosystem (Hydra viewer, Python API, physics API) [05:14]; Godot lacked support at the time [14:06].

**Use it:** in a hand-off check for exchanging scenes between C4D, Blender and an engine, compare up axis, handedness and units on both sides.
