---
id: c4d-scatter-density-patches-plane-effector-scale-minus-one-with-random-field-or-polygon-selection
title: C4D scatter patches: scale all instances to -1 with a Plane effector, then bring them back with a Random Field (or use a polygon selection driven by the field)
domain: c4d
tags: [c4d, mograph, field, plane effector, random field, polygon selection, scatter, grass, stepan hka, deep-read]
applies_to: Cinema 4D (video Dec 2023)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=0GD6OeiB6dk, src:yt-transcripts]
feeds: [c4d]
conflicts: none
---
Method [22:30-24:38, 34:50-36:12]: add a Plane effector to the Matrix, turn position off, uniform scale on, value -1 (1 minus 1 is zero, so nothing shows); drop a Random Field in, tune its remap and noise scale to get grass patches. A second Matrix covering the rest of the same landscape (copy the effector, invert the field) failed for him; inversion did not behave as expected and he asks viewers for the fix [26:42-28:50]. Alternative: build a polygon selection tag on the procedural landscape driven by a Random Field and scatter onto that selection [34:50-36:12]. Gradient colour on instances: Color User Data (MoGraph colour) in the grass material plus a Plane effector using a Linear Field for the gradient [29:21-32:32]. Speaker flaw: his invert route did not work; use with a test first.

**Use it:** if invert misbehaves, use a second field with a remap instead of inverting.
