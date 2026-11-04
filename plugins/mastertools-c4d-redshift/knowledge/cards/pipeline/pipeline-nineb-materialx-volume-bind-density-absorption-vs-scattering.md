---
id: pipeline-nineb-materialx-volume-bind-density-absorption-vs-scattering
title: MaterialX volume: bind the density primvar to the shader or smoke renders as blocks; absorption is extinction-based, scattering is direct colour
domain: pipeline
tags: [nine between, houdini, solaris, usd, volume, smoke, density, absorption, scattering, vdf, deep-read]
applies_to: Houdini 19.5/20 Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=cE-Bbdspu_8, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
A volume shader has a VDF slot (smoke; absorption and scattering) and an EDF slot for emission (fire) [2:13:29-2:14:32]. Without binding density you see the voxel bounds as blocks; plug a geometry-property-value reading density into absorption and scattering, then multiply a colour by density for each [2:15:02-2:17:04].
Absorption removes the colour you set, so a blue absorption reads red; scattering shows the colour you set [2:17:04-2:17:34]. Mask the velocity field to where density exists and drop other fields before export [2:12:27-2:12:57]. The viewport needed restarts when a volume vanished [2:14:32].

**Use it:** Look-dev tip for smoke or fog: colour the scattering, set absorption to the opposite colour, and always drive both by density.
