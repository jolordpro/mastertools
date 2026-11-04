---
id: redshift-metal-roughness-range-and-variation-layers
title: Keep metal roughness inside roughly 0.03 to 0.5 and add layered noise variation with the overlay blend
domain: redshift
tags: [polygon division, redshift, metal, roughness, color layer, noise, overlay, variation, deep-read]
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
Above about 0.5 roughness the metal stops reading as reflective; below about 0.03 reflections look fake-sharp unless it is deliberate chrome or polished steel (captions garble the lower number) [09:26-09:56]. His example base was 0.25, with a test at 0.125 [02:13, 10:26].
Variation: a colour-layer node blends several turbulence noises set to Overlay at about 0.25 strength, at three scales (100, 75, 50 in a 200 cm scene unit; scale to real-world units, e.g. 0.5, 0.25, 0.1) [11:28-13:31]. Each layer's amount becomes a slider later.
Even studio-clean product shots need this minimal variation [13:31].

**Use it:** a sanity range for the coach to flag metal roughness outliers; mark as one creator's rule of thumb, not a Redshift limit.
