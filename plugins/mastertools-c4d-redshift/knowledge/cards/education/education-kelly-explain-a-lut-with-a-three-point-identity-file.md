---
id: education-kelly-explain-a-lut-with-a-three-point-identity-file
title: "Cullen Kelly's teaching trick: make a 3-point identity 1D LUT and read it in a text editor to see what a LUT is"
domain: education
tags: [cullen-kelly, lut, teaching, lattice, identity lut, 1d lut, 3d lut, polish, deep-read]
applies_to: Lattice, any text editor
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster]
feeds: [coach]
conflicts: none
---
Make a 1D LUT with 3 points instead of 4096 in Lattice, save it, open in a text editor: one row per channel with input intervals and output values, identity so out equals in [34:23-35:58]. Then scale up to 5 points, then 100, then 3D (sets of three inputs to three outputs) [36:00-36:29]. Lattice is a technical utility for adapting and prepping LUTs, not a creative tool [33:52-34:23]. A multiplication-table picture explains why in-between values need interpolation [40:39-42:13].

**Use it:** Use the identity-file demo when the coach has to explain LUT interpolation to a newcomer.
