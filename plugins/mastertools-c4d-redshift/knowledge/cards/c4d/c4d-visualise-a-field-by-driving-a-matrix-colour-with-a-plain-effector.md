---
id: c4d-visualise-a-field-by-driving-a-matrix-colour-with-a-plain-effector
title: To see what a field does, put a matrix under a Plain effector that uses only Color from the field; turn Remapping on or the color option will not appear
domain: c4d
tags: [fields, visualise, plain effector, matrix, color remap, vertex map, debugging, deep-read]
applies_to: Cinema 4D 2022 (Maxon Ask the Trainer, Apr 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cCCgPVurWjQ, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Trainer's debugging habit [49:02-50:35]: make a matrix, treat it as a blank sheet, add a Plain effector with everything off except Color, and drop the field (spline, spherical, whatever) in. Color shows up only when the field's Remapping is on; some lists default it off, so no remap means no color. Set the matrix color to red or similar and the result reads like a vertex map: ones high, zeros low. Then switch the field layer between Along and Radius to see its influence.
The trainer found the display looked inverted at first (black stood for the maximum); captions are unclear on that detail, so judge with a known field first.

**Use it:** Before blaming a deformer, look at the field alone as a colour map to check its range and falloff.
