---
id: redshift-bucket-size-multi-gpu-straggler
title: With several GPUs, big buckets can leave one card stuck on a hard region while the others sit idle
domain: redshift
tags: [bucket size, multi gpu, straggler, subsurface, transparency, render time]
applies_to: Redshift in C4D (2025 video)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Uk1_Cwi8BUQ, src:yt-transcripts]
feeds: [coach, estimator, redshift]
conflicts: none
---
Scene with one very complex element and simple surroundings: bucket 128 took 53 s because one card chewed on the complex bucket; smaller buckets 39 s [12:08-13:46]. Fewer GPUs or lower resolution changes the answer.
On simple scenes bigger buckets were faster: about 7 s to 4 s [11:38]; a bubble-candy scene went 32 s to 20 s at final resolution while small buckets only helped at low resolution [14:51].
His rule: test sizes; in most cases a large value saves time.

**Use it:** estimator: if the scene has one heavy hotspot (SSS, transparency) and several GPUs, test a smaller bucket; otherwise go big.
