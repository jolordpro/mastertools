---
id: c4d-2027-scatter-seed-bump-all-at-once
title: All scatters in a scene can be re-rolled together by typing x+1 in their seed fields while keeping every rule
domain: c4d
tags: [scatter, seed, random seed, object manager filter, layout, variation]
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
[51:08] Use the object manager filter to show only scatter objects, select them all, and enter x+1 in the distribution seed field to add one to each seed.
The layout changes, the rules (water plants in water, trees away from water) stay.
Variation colour (hue, saturation, value ranges) feeds the display colour, which a Redshift material can read through user colour data [18:05].

**Use it:** a fast 'give me another layout' step for set dressing, and a reminder that scatter colour needs a user colour data node to show in a render.
