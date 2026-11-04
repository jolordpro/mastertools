---
id: redshift-openpbr-sample-controls-and-subsurface-mode-moved-to-advanced-tab
title: In the Redshift OpenPBR material, subsurface mode and the reflection, transmission, coat and fuzz sample counts live on the Redshift Advanced tab
domain: redshift
tags: [openpbr, advanced tab, samples, subsurface, material, deep-read]
applies_to: Redshift 2025.2.1-2025.4.2, C4D
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ieWk4U63EBw, src:yt-transcripts]
feeds: [redshift]
conflicts: none
---
In the node editor the main OpenPBR node hides subsurface mode, samples and include mode that the Standard material shows [07:27].
They are on the material's Redshift Advanced tab, in the matching sections; the reflection, transmission, coat and fuzz samples are there too [07:27-08:02].
Subsurface inputs otherwise match: weight, colour, radius, radius scale (was Scale), anisotropy [07:15-07:27].

**Use it:** A per-material sample check must read the Advanced tab for OpenPBR materials.
