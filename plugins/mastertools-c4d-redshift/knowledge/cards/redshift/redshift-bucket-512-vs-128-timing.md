---
id: redshift-bucket-512-vs-128-timing
title: Maxon's quick tip: bucket size 512 instead of default 128 cut one frame from 3:24 to 2:02 with an identical look
domain: redshift
tags: [bucket size, render time, gpu ram, bucket order, system tab]
applies_to: Redshift in C4D 2023, one frame, machine in the video description
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=wnJGABcUCh0, src:yt-transcripts, https://www.youtube.com/watch?v=HlQhMbjrM6M]
feeds: [estimator, redshift]
conflicts: none
---
Bucket size is under Render Settings, System; default 128 [00:32].
On one frame 128 took 3 min 24 s and 512 took 2 min 2 s, which looked identical; result depends on GPU and RAM, so it is one machine only [00:32].

**Use it:** the draft run should test 128/256/512 on the actual machine and log the winner; the estimator should not assume this 40 percent saving.
Transcript support: School of Motion: dual 3090, 128 to 512 saved 22 s per frame, about 40 percent, scene and VRAM dependent (https://www.youtube.com/watch?v=HlQhMbjrM6M [09:08-10:00])
