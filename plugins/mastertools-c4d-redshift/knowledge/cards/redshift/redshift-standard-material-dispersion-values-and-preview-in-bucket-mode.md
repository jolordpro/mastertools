---
id: redshift-standard-material-dispersion-values-and-preview-in-bucket-mode
title: Redshift 3.5 Standard material dispersion: useful values are about 1-10, it needs sharp angles, and shows poorly in IPR so check in bucket mode
domain: redshift
tags: [dispersion, abbe, chromatic, prism, gemstone, ipr, bucket, redshift standard material, deep-read]
applies_to: Redshift 3.5 / C4D R26 Standard material (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=DmeiTnrqp3I, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
Derek Kirk [11:37-13:43]: dispersion splits light like a prism. He says typical values run 0-60 (he says 64 is roughly water); stay near 1-10 to see it clearly, 2 as an example. It does not show well in the IPR, so use bucket rendering. It depends on shape: hard facets show it, curved balls barely. Look up real dispersion values for gemstones. Extra Roughness can blur the rainbow into a cloudy crystal. Unclear from the captions whether higher numbers mean more or less dispersion; he implies lower is stronger, so verify in the shader.

**Use it:** Use hard-edged geometry and bucket mode when judging dispersion.
