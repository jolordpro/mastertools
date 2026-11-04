---
id: redshift-metal-ior-edge-tint-presets-per-metal
title: Use per-metal edge-tint and IOR values from a measured database instead of picking a swatch colour
domain: redshift
tags: [polygon division, redshift, metal, ior to metal tints, edge tint, gold, copper, preset, deep-read]
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
A utility node (IOR to metal tints, under Utility > Conversion) takes two colour triples: the IOR and the absorption/edge tint. It outputs a face colour and an edge colour that change with viewing angle, so gold, copper, chrome and iron show tint shifts at grazing angles that a flat colour cannot [01:20-05:20].
Values come from a refractive-index database for metals (he points to the 3D data for artists section of a public site and a spreadsheet he shares); six numbers per metal, saved as presets named after the metal [05:20-07:54].
Lower IOR numbers push the edge tint further in; with the edge tint wired in, the plain IOR slot has no effect [03:46, 08:25]. Metalness is set to 1 [03:14].
Check lights first: the base colour swatch compared with the shader ball should show brightness is sensible, no blown highlights, before judging a metal [01:20-02:13].

**Use it:** for product-accurate metals, store a preset library and avoid hand-picked colours; verify the node name against the installed Redshift before citing it.
