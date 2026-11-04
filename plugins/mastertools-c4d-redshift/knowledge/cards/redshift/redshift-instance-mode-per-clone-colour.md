---
id: redshift-instance-mode-per-clone-colour
title: Per-clone colour in Redshift needs a Color User Data node, and multi-instance mode returns one colour for all clones
domain: redshift
tags: [mograph, cloner, color user data, multi instance, geometry id, clone colour, ramp]
applies_to: Redshift, C4D (R20 to 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=t9hy0YCq0I8, https://www.youtube.com/watch?v=ZsqM8QHZ0pQ, src:yt-transcripts]
feeds: [shakedown, coach]
conflicts: none
---
Plug a Color User Data node (attribute MoGraph Color) into diffuse so fields and effectors recolour clones [H 01:35-03:07]. With a Cloner in Multi-Instance mode, a Geometry ID colour gives a single result; switch the instance mode away from multi-instance for per-clone data (the captions do not name the mode clearly) [A 1:17:37-1:18:40]. A ramp remaps the ID to colours and feeds the colour inputs [1:18:40].
Instances give faster scenes; the per-clone mode makes the file heavier [1:18:40].

**Use it:** scene check: cloner with multi-instance mode and a clone-colour dependent material; the coach explains the instance-mode switch.
