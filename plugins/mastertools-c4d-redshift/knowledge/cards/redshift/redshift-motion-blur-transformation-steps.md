---
id: redshift-motion-blur-transformation-steps
title: More linear motion blur steps make trails more accurate but use more memory
domain: redshift
tags: [motion blur, transformation steps, memory, matrices, noise]
applies_to: Redshift 2026-2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Motion+Blur.html.md, https://help.maxon.net/c4d/2027/en-us/Content/_REDSHIFT_/html/Motion+Blur+-+Advanced.html.md, src:research-agency-pipelines, src:research-vfx-pipelines, https://www.youtube.com/watch?v=ehpdzt0JHUc, src:yt-transcripts]
feeds: [advisor]
conflicts: none
---
Linear steps trade accuracy for memory. Fast motion adds noise. Per-object transform matrices live in GPU memory and grow with many instances times many steps.

**Use it:** when memory is tight with many instances, look at blur steps before cutting textures.
Transcript support: Shutter angle controls blur length per frame; 360 hazy, 45 crisp. (https://www.youtube.com/watch?v=ehpdzt0JHUc [01:10])
