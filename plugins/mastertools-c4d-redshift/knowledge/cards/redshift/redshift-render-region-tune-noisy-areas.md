---
id: redshift-render-region-tune-noisy-areas
title: Tune noise with a render region on the worst spot instead of re-rendering the whole frame
domain: redshift
tags: [render region, iPR, noise, shadows, reflection]
applies_to: Redshift in C4D
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=G43QVR1TqXg, https://www.youtube.com/watch?v=uKRqHwVr0F4, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
Hit R (or Shift+drag in Render View) to draw a movable box [08:51, RT; 03:12, RF]. Zoom to the shadow-heavy mouth or the reflective floor, change a setting, render, move the box, compare.
Typical noise hot spots: reflections and shadows first [04:11, RT].

**Use it:** coach: suggest a region on the noisiest 10% of the frame when the user is tuning sampling.
