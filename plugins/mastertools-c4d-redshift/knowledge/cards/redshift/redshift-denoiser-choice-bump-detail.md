---
id: redshift-denoiser-choice-bump-detail
title: Optix smooths bump and fine texture more than Altus Dual; use Altus Dual for detail and Optix for clean reflective floors
domain: redshift
tags: [denoise, optix, altus, bump, detail, oidn]
applies_to: Redshift 3.x in C4D
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=G43QVR1TqXg, https://www.youtube.com/watch?v=uKRqHwVr0F4, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
The denoiser can read small bump detail as noise [09:53, RT]. Optix is fastest and smooths bump the most. Altus Dual keeps more texture but takes longer. Optix/OIDN fast with some detail loss; Altus methods slower and sharper [07:18, RF].
Denoise helps most on reflections, shadows, GI, fog and depth-of-field bokeh [10:24, RT].

**Use it:** coach: if a normal or bump map looks smeared after denoise, switch to Altus Dual or lower the threshold before adding samples.
