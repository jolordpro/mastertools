---
id: lookdev-nested-dielectric-solids-overlap-liquid-and-different-ior
title: Nested dielectric by solids: the liquid solid must overlap the glass wall (no air gap) and the two must have different IOR or they merge
domain: lookdev
tags: [nested dielectric, overlapping solids, water in glass, liquid shader, ior, no air gap, deep-read]
applies_to: KeyShot solid glass and liquid
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Bbj18-933Vg, src:yt-transcripts, https://www.youtube.com/watch?v=9yZCElLDRH4]
feeds: [redshift, lookdev]
conflicts: none
---
Model each as a closed solid; the liquid body pokes into the glass wall all around so no air layer exists between them [06:46][07:18]. Glass uses a solid glass shader at default IOR 1.5 [07:48]. Liquid with the same 1.5 IOR looks like one block of glass because the renderer cannot tell the surfaces apart; set water to 1.333 [08:51][09:23]. Colour: very dark colour at first looks black, then lighten the liquid colour nearly to white and add a little tint [09:23]. Liquid touching the wall appears to reach the very edge due to refraction, as with milk [08:20]. Redshift uses its own priority system for the same job, so check ledger.

**Use it:** a checklist for water-in-glass: overlap, distinct IORs, and a light liquid colour.
Transcript support: Coincident faces between glass and liquid confuse the ray tracer and give a patchwork; a gap of a fraction of a millimetre fixes it (Fusion's renderer, same principle). (https://www.youtube.com/watch?v=9yZCElLDRH4 [00:42-04:18])
