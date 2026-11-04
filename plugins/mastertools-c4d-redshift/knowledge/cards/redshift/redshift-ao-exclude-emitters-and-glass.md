---
id: redshift-ao-exclude-emitters-and-glass
title: Fake AO also darkens lights, flames and glass; exclude them with a Store Color to AOV node set to white on the AO AOV
domain: redshift
tags: [ambient occlusion, store color to aov, emissive, glass, exclusion]
applies_to: Redshift 2024-2025
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [AOV package, shakedown]
conflicts: none
---
AO is a shading trick based on normals, so it adds black to lamps, candle wicks, flames and windows [52:25-53:26]. On each such material, add Store Color to AOV between the texture and output, pick the AO AOV and output white [53:58-56:44]. Hair on cloth can be excluded the same way [57:49]. Adding a new AOV later keeps the layer order in recent After Effects [57:49].

**Use it:** Check for emissive or transparent materials without the exclusion when an AO AOV exists; note that Python support for this node is unreliable.
