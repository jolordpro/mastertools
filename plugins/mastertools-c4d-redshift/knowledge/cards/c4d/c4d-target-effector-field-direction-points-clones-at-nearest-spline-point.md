---
id: c4d-target-effector-field-direction-points-clones-at-nearest-spline-point
title: Make clones aim at the nearest point of a spline: Target effector in Field Direction mode, spline in the field list with values off and distance mode Radius
domain: c4d
tags: [target effector, field direction, spline field, radius, along, aim, cloner, deep-read]
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
Steps [43:15-48:30]: (1) Target effector, switch target mode from Object Target to Field Direction. (2) Add a field to its Fields tab; a spherical field points everything at its centre. (3) Drop in a spline, untick the Values option and keep Direction only, which is the trap the trainer fell into often. (4) On the spline field change distance mode from Along to Radius and raise the radius; now each arrow aims at the closest point and follows if a spline point is moved.
To show only nearby arrows: Plain effector, same spline field in Radius mode, Position off, Uniform Scale on at -1, Invert in the field's Remapping [46:52-48:00]. Groups can combine several splines, a spline plus a torus field, and so on [48:00-48:32].
Direction rule [50:35-51:38]: each clone's Z axis points from lower toward higher field value, so a plain gradient is what defines the direction.

**Use it:** Flow arrows or particles that bend toward a path in a lower third or map graphic, without keyframes.
