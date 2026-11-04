---
id: pipeline-estimate-sample-late-frames-render-time
title: On a cloth sim, average 21.3 s per frame hid later frames at 23-28 s, so estimates should sample across the range
domain: pipeline
tags: [render time, estimator, late frames, cloth, frame variance, test frames]
applies_to: Redshift 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PJ3eNgTMNKo, src:yt-transcripts, https://www.youtube.com/watch?v=RCCaQmwxNB4, https://www.youtube.com/watch?v=sh8UhQ1zofg]
feeds: [estimator]
conflicts: none
---
Later frames got heavier as cloth filled the frame and overlapping layers grew [07:17-07:49]; final stretch ran 23-28 s versus 21.3 average over 301 frames [08:00]. GPU use peaked at 94%, temperature 27-51 C [06:13].

**Use it:** Sample first, middle and last frames, and report the spread.
Transcript support: Volkov: iterate on first, middle, last or four to five sample frames and run the full range once they hold (https://www.youtube.com/watch?v=RCCaQmwxNB4 [20:33])
Transcript support: farm estimator samples random frames across the range for the same reason (https://www.youtube.com/watch?v=sh8UhQ1zofg [34:38])
