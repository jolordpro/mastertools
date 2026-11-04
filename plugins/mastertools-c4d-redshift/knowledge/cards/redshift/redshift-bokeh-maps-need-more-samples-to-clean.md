---
id: redshift-bokeh-maps-need-more-samples-to-clean
title: Bokeh image maps take many samples to clean, especially tiny out-of-focus lights, so lower the threshold
domain: redshift
tags: [redshift, bokeh, samples, threshold, noise, polish, greyscalegorilla, deep-read]
applies_to: C4D + Redshift (2022)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aWkfAAJgiJ0, src:yt-transcripts, src:polish-roster, https://www.youtube.com/watch?v=LcxjkHFS-2k]
feeds: [redshift, estimator]
conflicts: none
---
He warns that it takes a lot of samples to clean up bokeh, particularly very out-of-focus points of light in the background; with Unified Sampling you need to reduce the threshold [05:13]. Tests were run in bucket mode to see the final cleanup [04:57-05:13].

**Use it:** Pair a bokeh map preset with a lower adaptive threshold and higher max samples; check the render-time estimate. Consistent with the Redshift ledger on DOF sampling (neutral).
Transcript support: Chad's bokeh shot: min 64, max 512, then glossy and light overrides replaced with 8 and bounces cut to 2 to keep time down (https://www.youtube.com/watch?v=LcxjkHFS-2k [45:38-49:45])
