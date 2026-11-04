---
id: redshift-triplanar-float-scale-bump-strength-and-ramp-linear-for-remap
title: Drive triplanar scale from one float, tune bump strength small (negative flips it), and set the ramp to linear before remapping roughness
domain: redshift
tags: [triplanar, float, bump, ramp, interpolation, roughness remap, color space, lionel, maxon, deep-read]
applies_to: Redshift 3.x in C4D R26 (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=TonSU8Ljm5c, src:yt-transcripts]
feeds: [lookdev, redshift, coach]
conflicts: none
---
Ctrl-click a socket to expose it, then one Math float drives all three triplanar scale axes, enough when you want the same everywhere; scale 3 as a taste choice [47:15-49:15].
Bump strength: 0.1 was far too strong on a cast-iron map, and a negative value flipped the relief direction [49:48-50:53].
Ramp default is smooth interpolation; set it linear at both ends for a remap, otherwise the mapping behaves oddly [52:25-52:57]. Raising the dark end to about 15 to 20 percent stopped the roughness being too shiny, and a rougher surface makes the bump read better [53:58-54:29]. Auto colour space can now be trusted for greyscale maps [51:24].
Socket colour rule he uses: yellow to yellow, purple vector to vector.

**Use it:** coach: remap tips for roughness maps; pairs with the imperfection-map remap card.
