---
id: redshift-openpbr-metalness-and-specular-weight-split-from-standard
title: In the Redshift OpenPBR material, metalness only decides metal or not and Specular Weight sets the metal's reflection strength; the Standard material behaves the other way
domain: redshift
tags: [openpbr, metalness, specular weight, standard material, plus, deep-read]
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
Standard material: with metalness at 1, changing reflection weight does not change how strong the metal reflection is [04:15]. OpenPBR: metalness at 1 only says the surface is metal, and Specular Weight now controls the metal's reflection intensity [04:15-04:46].
OpenPBR's base layer also fixes the diffuse model to the energy-conserving one (EON-style); the Standard material lets you pick Lambert or the newer model [03:12-03:43].
Speaker: Plus (course sample from the 19-hour Redshift Masterclass). OpenPBR was still in development at the time and parameters could change.

**Use it:** When converting or comparing Standard and OpenPBR metals, check Specular Weight, not reflection weight, before blaming the render.
