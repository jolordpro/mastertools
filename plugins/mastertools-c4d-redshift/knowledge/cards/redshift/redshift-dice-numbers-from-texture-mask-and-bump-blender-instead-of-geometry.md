---
id: redshift-dice-numbers-from-texture-mask-and-bump-blender-instead-of-geometry
title: Keep dice geometry low: numbers come from a mask texture used as blend colour on an off-white layer, plus a height map in a bump blender
domain: redshift
tags: [dice, mask, bump blender, layer color, off white, substance painter, low poly, jon jags nee, deep-read]
applies_to: C4D + Redshift (2022 upload, Jon Jags Nee)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=eKG2QSWJYYM, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
Substance Painter maps (normal, metalness, height) are dragged into the node editor; he declines copying them into the project to avoid duplicates [08:54-09:55]. A second material set to about 95 percent white goes into material blender layer 2, additive, with the metalness map as the blend colour so it shows only where the numbers are [10:27-11:31]. Pure white is avoided as a rule of thumb.
For depth he used bump rather than displacement: height into a bump node, a second bump node with the normal, both into a bump blender in additive mode, bump weight 1, then the blender into the bump input; the effect stays subtle by design [12:02-13:37]. Reason: low topology for animation and many dice in later projects [08:54, 13:37].

**Use it:** replace small modelled detail with mask-and-bump layers when scenes will be instanced many times.
