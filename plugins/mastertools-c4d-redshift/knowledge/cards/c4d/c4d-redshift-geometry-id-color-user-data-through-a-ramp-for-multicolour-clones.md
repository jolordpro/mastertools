---
id: c4d-redshift-geometry-id-color-user-data-through-a-ramp-for-multicolour-clones
title: Colour clones with one material: Color User Data (Geometry ID Color) into a Ramp, with Step interpolation for flat colours and knot width setting each colour's share
domain: c4d
tags: [redshift, color user data, geometry id color, ramp, step interpolation, gradient preset, clones, freeze geometry, deep-read]
applies_to: Redshift in Cinema 4D 2024 (School of Motion, EJ, Apr 2024)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=_6toVWN7NMo, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
EJ (Redshift in C4D 2024; the node editing is as shown on screen) [31:05-36:30]. To make material tweaks fast, tick Freeze Tessellation and Freeze Geometry in the Redshift render settings so only materials update; untick to see geometry change [31:35; 36:30].
In the node editor: Color User Data node with the Geometry ID Color preset gives each clone an ID. Feed it through a Ramp node (the same black-white default shows as grey levels), and plug the ramp into the preset material's colour port feeding its colour mix [32:54-34:27]. Change ramp knots to colours; Step interpolation gives three flat colours, and widening one knot's segment raises its share of the bricks [34:57-35:28]. Gradient presets can be loaded or saved; Distribute Knots spaces them evenly; a noise amount adds randomness [35:28-36:30].

**Use it:** One shared material with controlled colour share across hundreds of clones; widths of ramp segments act as brand-colour ratios.
