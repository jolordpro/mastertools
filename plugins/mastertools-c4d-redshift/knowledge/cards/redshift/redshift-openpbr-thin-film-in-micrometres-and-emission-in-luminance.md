---
id: redshift-openpbr-thin-film-in-micrometres-and-emission-in-luminance
title: Redshift OpenPBR thin film thickness is a 0-1 micrometre slider with its own weight, and emission uses a Luminance amount instead of a weight
domain: redshift
tags: [openpbr, thin film, emission, luminance, thickness, noise, deep-read]
applies_to: Redshift 2025.2.1-2025.4.2, C4D
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ieWk4U63EBw, src:yt-transcripts]
feeds: [redshift, lookdev]
conflicts: none
---
Standard material thin film thickness ran from 0 to 1,000 and beyond (nanometres); OpenPBR uses micrometres, a slider from 0 to 1 [14:33].
Because the range is small, a noise shader can plug straight into thickness with no Change Range node [14:33-15:03].
Thin film has a new Weight that sets how much it contributes; the test used specular IOR 1 and thin film weight 1 [14:02-14:33].
Emission has a Luminance amount, in nits, in place of the Standard shader's weight [15:03].

**Use it:** Iridescent or emissive broadcast surfaces: expect different numbers than a Standard material, and wire noise to thickness directly.
