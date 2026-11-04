---
id: redshift-light-samples-before-global
title: Raise light samples before global samples when noise comes from lighting
domain: redshift
tags: [light samples, global samples, noise, greyscalegorilla, speed]
applies_to: Redshift
status: V2
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://greyscalegorilla.com/blog/tips-faster-redshift-renders-c4d, src:research-gaps-deep, https://www.youtube.com/watch?v=ZsqM8QHZ0pQ, src:yt-transcripts, https://www.youtube.com/watch?v=Q5AZ7Xlh2I4, https://www.youtube.com/watch?v=kwFwyzjXsdM]
feeds: [advisor]
conflicts: none
---
Greyscalegorilla warns that raising global samples slows renders more than raising the light's own samples. Taken from a complaint-themes list, not from the page itself.

**Use it:** pair with the per-ray override card: fix the noisy effect, not the whole frame.
Transcript support: Greyscalegorilla: raise light and GI samples first, global last, in powers of two. (https://www.youtube.com/watch?v=ZsqM8QHZ0pQ [06:13])
Transcript support: Dome and area-light samples raised first for shadow noise; Shadows AOV always looks dirtier than Beauty (https://www.youtube.com/watch?v=Q5AZ7Xlh2I4 [04:22-06:30])
Transcript support: dial light samples in powers of two; a large area light needed 256 to 1024 in his scene (https://www.youtube.com/watch?v=kwFwyzjXsdM [02:05-03:48])
