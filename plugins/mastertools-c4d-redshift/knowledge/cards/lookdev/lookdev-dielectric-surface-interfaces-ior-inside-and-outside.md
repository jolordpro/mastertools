---
id: lookdev-dielectric-surface-interfaces-ior-inside-and-outside
title: With open surfaces, set each boundary's IOR inside and outside: glass-air 1.5/1.0, liquid-glass 1.333/1.5, liquid-air 1.333/1.0
domain: lookdev
tags: [dielectric, interface, boundary surface, ior inside outside, water glass, surfaces, deep-read]
applies_to: KeyShot dielectric
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Bbj18-933Vg, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
When the model is open surfaces (not enclosed), a solid glass shader fails; use a dielectric per surface with refractive index inside and outside [10:25][10:55]. Outer glass surface: inside 1.5, outside air 1 [11:28]. Liquid-to-glass surface: inside 1.333, outside 1.5 [11:58][12:28]. Liquid-to-air top surface: inside 1.333, outside 1 [12:59][13:31]. Use the same transmission colour for the liquid on both liquid surfaces; darker bottom needed matching the transmission value [14:01]. Both setups give identical results. The surface approach gives more control when straws or ice penetrate; the solid approach saves work if it works [14:32][15:03].

**Use it:** use the interface table when water and glass are separate shells; the same logic applies to Redshift's nested priority.
