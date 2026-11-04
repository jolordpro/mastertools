---
id: redshift-metal-bump-tiny-height-with-grey-base
title: Metal bump height should be very small, built from mid-grey layers so wear detail goes both ways
domain: redshift
tags: [polygon division, redshift, metal, bump, pockmarks, waviness, voronoi, deep-read]
applies_to: Cinema 4D 2024, Redshift
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-lpj38Cql4c, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
Bump scale on most metals is tiny, he sometimes uses about 0.05 (spoken as 'O five'); do not hesitate to pull it down [15:06-15:36].
Layers must be built on 50% grey because bump pushes up and down from the mid value [16:08]. Waviness: very low-amplitude noise at about 40 to 50 scale, around 0.25 amount [16:40]. Pockmarks: a voronoi-type noise with one octave, high clip raised to separate holes, amount around 0.01 for soft metals like gold [17:11-18:44].
Nicks use a triangular-shaped noise at about 2.5, masked to corners [18:44-19:48].

**Use it:** quick starting numbers for a believable metal bump; adjust for object scale.
