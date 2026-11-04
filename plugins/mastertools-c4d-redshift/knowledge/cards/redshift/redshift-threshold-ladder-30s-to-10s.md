---
id: redshift-threshold-ladder-30s-to-10s
title: Raising threshold, lowering min samples and bounces took a mug scene from 30 s to 10 s, and 13 s with denoise looked the same at 400%
domain: redshift
tags: [threshold, render time, denoise, min samples, bounces, a/b compare]
applies_to: Redshift 2026 on Mac
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts]
feeds: [coach, estimator, redshift]
conflicts: none
---
Steps [1:04:07-1:09:50]: default with denoise 30 s; denoise off 24 s; higher threshold + lower min + fewer bounces 18 s; threshold up again 14 s; threshold 0.2 about 10 s.
Then low settings with denoise on cost about 3 s more (about 13 s). A/B in Picture Viewer (right-click set A, set B) at 400% showed no visible difference on a still; he calls it about half the time.
Quoted numbers are from one scene with unfinished UVs.

**Use it:** coach: show the stepwise ladder; always A/B at 400% before accepting a cheaper setting.
