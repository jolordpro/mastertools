---
id: lookdev-octane-black-glass-backfaces-fixed-by-raising-max-glossy-depth-to-32
title: Black back faces on glass vases came from too-low glossy depth; raising depth to 32 fixed it, with adaptive sampling on
domain: lookdev
tags: [octane, glass, glossy depth, scatter depth, diffuse depth, adaptive sampling, interior, deep-read]
applies_to: Octane for Blender
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NdqK0UJYvYY, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
ArchiVizual: vases showed a black far-side face because max glossy depth was too low; setting glossy, scatter and diffuse depth to 32 made them see-through [27:11]. He turns adaptive sampling on 'otherwise it renders forever' [27:44]. Final 4K took about 20 minutes [31:41]. His camera imager is set to sRGB response with gamma 1 and a LUT added for contrast; colour management sRGB and exposure 0 are checked first [01:14].

**Use it:** same family as the Cycles transparent-bounce failure; when glass shows black, raise the ray depth before changing the material.
