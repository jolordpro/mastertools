---
id: redshift-toon-maxon-noise-varies-contour-thickness-and-opacity-via-change-range
title: Redshift Toon material: Maxon Noise through Change Range into contour thickness and opacity gives a messy-ink line; negative range minimum opens gaps
domain: redshift
tags: [redshift toon, contour, thickness modifier, opacity, change range, maxon noise, ink, helloluxx, camera map, deep-read]
applies_to: C4D + Redshift 2 toon material (2024 upload, helloluxx)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=3Z6Td_LTpH0, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
Tim from helloluxx: set contour thickness 25 external, 20 then 15 internal, angle threshold down to 10 [02:06-02:38]. Maxon Noise (type Luka) into the thickness modifier, with a Change Range node so the same noise can feed external and internal [02:38-04:10]. Noise scale 5 worked.
In Change Range, new-range minimum -0.15 makes holes in the line and maximum 1.2 makes it thicker; opacity gets its own Change Range, 0.6 to 1.2, so the line varies in density [04:10-05:42].
Paper look: a camera map node with a paper photo into the toon map, then a colour correct saturation almost grey; reflection weight 0 and the two tone maps deleted [00:32-02:06]. Input source object ties noise to the object; world fixes it in space [03:08].

**Use it:** hand-drawn line feel for graphics; ledger-free craft, tune values per scene scale.
