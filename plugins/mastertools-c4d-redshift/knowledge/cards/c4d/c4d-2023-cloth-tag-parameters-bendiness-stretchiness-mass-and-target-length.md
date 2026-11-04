---
id: c4d-2023-cloth-tag-parameters-bendiness-stretchiness-mass-and-target-length
title: What each new cloth tag parameter does: bendiness (folding and detail), stretchiness, bounciness, friction, stickiness, thickness, mass (lighter blows harder) and target length (below 100 shrinks, above grows)
domain: c4d
tags: [cloth tag, bendiness, stretchiness, bounciness, stickiness, thickness, mass, target length, growth, deep-read]
applies_to: Cinema 4D 2023 new simulation system, cloth (School of Motion, EJ, Oct 2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dHQWVXWbsEM, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
EJ [10:29-12:31]. Bendiness: high values (he tried 500) let the cloth bend and fold on itself with detail. Stretchiness lets particles relax and stretch. Bounciness: how much particles bounce off each other and the collider. Friction clumps the cloth. Stickiness makes it cling to other dynamic objects. Thickness is a small force-field skin around edges and polygons to stop intersections. Target Length: under 100 the cloth shrinks onto itself, above 100 it grows beyond its start state; keyframing it gives a growing-cloth effect. Mass: lower mass is lighter like paper, so forces push it harder.

**Use it:** A map for tuning: wrinkles from bendiness, drape from mass, growth from target length.
