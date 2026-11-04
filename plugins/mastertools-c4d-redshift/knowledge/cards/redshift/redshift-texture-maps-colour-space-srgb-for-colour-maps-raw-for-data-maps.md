---
id: redshift-texture-maps-colour-space-srgb-for-colour-maps-raw-for-data-maps
title: Redshift (C4D): set colour maps to sRGB and data maps (metalness, roughness, normal) to Raw, because those maps are read as numbers, not colours
domain: redshift
tags: [redshift, texture maps, colour space, srgb, raw, metalness, roughness, maxon, deep-read]
applies_to: Redshift in Cinema 4D (Maxon training, version not stated)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=08CqyBVkpeU, src:yt-transcripts]
feeds: [lookdev, CHECKS, redshift]
conflicts: none
---
Maxon Training Team quick tip [02:50-04:42]. Before wiring the nodes, fix the colour space on each texture node: base colour map sRGB, anything that is not colour (metalness, roughness, normal and similar) Raw, because they are used as unit values [03:08]. A greyscale map is data: 100 percent black is 0, 100 percent white is 1, and in between are slider values, so a metalness map drives the 0-1 metalness slider per pixel [03:39-04:11]. Roughness connects to reflection roughness the same way [04:11]. Once a map is connected the original attribute can no longer be edited [03:39]. Maxon also notes the same process applies from the Shader Graph, and the order of nodes in the editor does not matter [02:05-02:36].

**Use it:** A CHECKS item: any non-colour map left on sRGB is a silent error. Check against the redshift skill ledger before wiring it into a rule; this is the vendor trainer's tip.
