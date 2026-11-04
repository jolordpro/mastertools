---
id: redshift-standard-material-extra-roughness-blurs-refraction-not-surface
title: Redshift 3.5 Standard material: Transmission Extra Roughness blurs only the refraction inside, leaving the surface reflection sharp
domain: redshift
tags: [redshift standard material, transmission, extra roughness, milky glass, ior, weight, waxy plastic, deep-read]
applies_to: Redshift 3.5 / C4D R26 Standard material (2022); newer versions use OpenPBR defaults
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=DmeiTnrqp3I, src:yt-transcripts]
feeds: [lookdev, redshift]
conflicts: none
---
Derek Kirk [02:17-05:20]: transmission weight 1 is fully see-through, lower is more solid, but the waxy look comes from Extra Roughness. IOR is no longer in transmission; it lives under Reflection (no 'link to reflection' tickbox now): 1.1 barely bends, 2 bends hard, 1.5 for glass [02:43-03:46]. Extra Roughness makes the inside cloudy while the surface reflection can stay perfectly smooth, and it blurs the refraction lines, not the reflections [03:46-04:48]. Thin Wall keeps Extra Roughness but greys out the depth and scatter controls, a quick route to thin plastics (IOR about 1.32) [05:50-06:22]. Colour comes from the Transmission colour.

**Use it:** Frosted glass: set Extra Roughness, not surface roughness. The ledger notes 2026 builds default to OpenPBR, so map names may differ.
