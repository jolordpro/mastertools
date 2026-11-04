---
id: redshift-openpbr-dispersion-weight-separates-amount-from-abbe
title: Redshift OpenPBR adds a Dispersion Weight, so the Abbe value can stay physical while the weight dials the look in or out
domain: redshift
tags: [openpbr, dispersion, abbe, transmission, glass, deep-read]
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
Test setup: transmission weight 1, metalness 0, specular roughness 0 [06:25]. Dispersion Weight 1 with Abbe 20 gives the dispersion; Abbe 5 makes it stronger [06:25-06:56].
The new weight scales the overall dispersion without touching Abbe. For real-world values set weight 1 and drive the effect with Abbe alone [06:56].
OpenPBR transmission has no extra roughness input; scatter colour is just Scatter and scatter anisotropy is just Anisotropy, same behaviour [05:55].
For broadcast glass this gives an art-directed dial for colour fringing.

**Use it:** Glass look-dev: keep Abbe physical, animate or tune Dispersion Weight for how much fringing the shot can take.
