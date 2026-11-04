---
id: redshift-2027-procedural-fur-controls
title: Redshift 2027 procedural fur: UV texture maps only (no vertex maps), bend needs gravity above zero, no viewport preview
domain: redshift
tags: [procedural fur, hair, principled hair, density, length, maps, gravity, displacement]
applies_to: Redshift 2027.0 in C4D 2027
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=FmaKhqSITFQ, src:yt-transcripts]
feeds: [redshift, coach]
conflicts: none
---
Created from the Redshift object menu; the fur shows in IPR but not the viewport yet [39:44-40:14]. Controls: surface offset, density, length, thickness, root and taper, bend, curl, and variation for each [40:48-43:52].
Bend needs a gravity setting above zero and gets odd stretching if high [41:48]. Maps are texture maps that need UVs; vertex maps are not supported yet. White is full, black is zero [44:24-45:57].
Shade with Principled Hair; for texture colour plug the map into the albedo input and set albedo mix to 1 [46:59-48:31]. If the base mesh has displacement, put the same map in surface offset [48:31-49:02].

**Use it:** the coach can give fur settings and the UV requirement; a check can flag a fur source with no UVs.
