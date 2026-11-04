---
id: redshift-bump-node-input-map-type-height-field-vs-tangent-normal-and-height-scale
title: The Redshift Bump node handles height maps and normal maps: set Input Map Type to Height Field or Tangent Space Normal, then tune Height Scale
domain: redshift
tags: [maxon, bump node, normal map, height field, tangent space, height scale, deep-read]
applies_to: Redshift 3.5 in Cinema 4D R26 (2022)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=RpiCCLHjlWQ, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
There is no bump toggle on the Redshift material as in C4D; add a Bump node and feed its output into the material's bump input [1:14:15-1:14:45, 1:36:48-1:37:18]. Input Map Type has three options: Height Field for greyscale bump maps, Tangent Space Normal (the usual one) and Object Space Normal for normal maps [1:37:49-1:38:19]. The separate normal map node is described as a legacy node.
Height Scale: 1 is quite strong; she used 0.2 and compared it to the 20 percent default of a C4D bump channel [1:38:51-1:39:21].

**Use it:** Check list: right input type for the map, and height scale below 1 for subtle detail.
