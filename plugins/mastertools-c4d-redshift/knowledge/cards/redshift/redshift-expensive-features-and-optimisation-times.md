---
id: redshift-expensive-features-and-optimisation-times
title: Displacement, motion blur, depth of field, caustics and refraction cost render time; caustics are the worst; a tuning workshop cut 7:40 to 1:13 at equal quality
domain: redshift
tags: [render time, caustics, optimisation, displacement, motion blur, dof, unified sampling]
applies_to: Redshift 2025
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KnfiJy2ND2o, src:yt-transcripts]
feeds: [advisor, estimator]
conflicts: none
---
The expensive list [1:05:00-1:06:01]; chat agreed caustics are worst. His workshop covered unified sampling, local sampling, GI and trace steps, same quality: 7:40 to 1:13, and about 8 min to just under 4 [1:06:34]. Quality must stay equal [1:06:34].

**Use it:** Order advice by cost: switch off the costly feature first, tune sampling second; verify claims on the scene.
