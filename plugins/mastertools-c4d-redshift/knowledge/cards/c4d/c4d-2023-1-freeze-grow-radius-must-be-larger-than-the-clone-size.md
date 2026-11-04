---
id: c4d-2023-1-freeze-grow-radius-must-be-larger-than-the-clone-size
title: Freeze in Grow mode spreads a field's selection only if its radius is just larger than the clone spacing or size (200 failed, 201 worked)
domain: c4d
tags: [mitch scott, behind the button, freeze, grow, field modifier layer, radius, cloner, aov, cinema 4d 2023.1, deep-read]
applies_to: Cinema 4D 2023.1 (video uploaded 2023-03)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=tQbqZzk7Kc0, src:yt-transcripts]
feeds: [motion-critique]
conflicts: none
---
Setup: cloner, plane effector, one spherical field sitting in the middle, Freeze layer added [03:41-04:44]. Freeze modes: Max, Min, Average and Grow; Grow is the useful one [04:13].
Grow pushes anything already caught by the field to full strength, even clones only lightly inside the edge, and then spreads outward over time [04:44-05:16].
The spread distance is the Radius. Clones were 200 cm; a radius of 200 did nothing and 201 worked [05:16-05:46]. Rule: set it a hair above the object size or spacing.
Warning: Freeze stops animation, so be careful with an animated field [03:41-04:13].
He suggests the colour output as a custom AOV (he mentions a Redshift video) to recolour or glow a growing region in comp [05:16-05:46].
Limit: the growth shape follows the source field's shape, with less control than a linear field [05:46-06:17].

**Use it:** for a spread/infection reveal, use Grow with radius slightly over clone size; if nothing spreads, bump the radius by one unit before debugging anything else.
