---
id: redshift-metal-corner-nicks-by-curvature-mask
title: Mask corner nicks with a curvature node whose radius is driven by noise, and scale nick amount to metal hardness
domain: redshift
tags: [polygon division, redshift, metal, curvature, edge wear, nicks, hardness, deep-read]
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
Curvature (convex = edges, concave = crevices) is the mask for nicks; noise feeds its radius through a change-range node so the damage is broken up; sample quality raised to 32; bias lowered slightly to hide triangle shapes [19:48-22:59].
Hardness logic: soft gold gets pockmarks and nicks; steel fewer; tungsten carbide almost none. He cuts the nick amount to about a tenth or less for hard metals [13:31-14:34, 23:01-23:31].
Stack bigger and smaller noises on the mask for a less repetitive pattern [22:59].

**Use it:** wear should follow the material's hardness; flag uniform heavy scratches on hard metals in review.
