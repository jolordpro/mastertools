---
id: lighting-expanse-gray-ball-difference-heat-map-to-match-the-first-light
title: Expanse's first lighting step is matching the gray ball, checked with a Copernicus node that shows plate-vs-CG difference as a per-channel heat map
domain: lighting
tags: [lighting, expanse, gray ball, houdini, copernicus, match, plate, deep-read]
applies_to: Houdini Copernicus
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
First lighting step for plate work: match the gray ball so the initial light match is good [40:19]. A custom node uses Copernicus to compute the difference between the plate's gray ball and the CG gray ball, showing a heat map per colour channel in the viewport [40:19-40:51]. Their own words: a perfect match is hard, but the node helps get closer; the target after tweaking is a mostly flat map [40:51].

**Use it:** Turn "looks about right" into a number check by differencing the reference ball against the CG ball per channel.
