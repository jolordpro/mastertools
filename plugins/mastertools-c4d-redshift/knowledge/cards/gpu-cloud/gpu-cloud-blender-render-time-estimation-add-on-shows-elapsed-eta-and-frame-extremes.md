---
id: gpu-cloud-blender-render-time-estimation-add-on-shows-elapsed-eta-and-frame-extremes
title: A paid Blender add-on (about 6 dollars, Blender 2.82/2.9 era) shows elapsed time, estimated end and average, shortest and longest frame, and works best on animations
domain: gpu-cloud
tags: [blender, render time estimation, add-on, eta, cycles, eevee, animation, deep-read]
applies_to: Blender 2.82 and 2.9 (about 2020)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=H3KurpOBE24, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Short Blender tip [00:34-04:42]. Price about 6 dollars; installs from Preferences, Install add-on, then tick the box [00:34]. The panel in the render window shows start time, elapsed time, estimated end, rate of the frames, shortest and longest frame, and average per frame, and can export the data [01:06-01:36]. It works with Cycles or Eevee. The speaker finds it good on animation and not good on single images [02:07]. In his demo (Suzanne moving, frames 1-250) it ran at roughly 3 seconds a frame with a finish about 13 minutes out; the caption's other numbers (40 seconds, 14 minutes, 40 minutes) are inconsistent, so do not rely on them [04:09-04:42].

**Use it:** Confirms the pattern behind the estimator: take the average of a few real frames and multiply, then track longest and shortest. Product name not given in the captions.
