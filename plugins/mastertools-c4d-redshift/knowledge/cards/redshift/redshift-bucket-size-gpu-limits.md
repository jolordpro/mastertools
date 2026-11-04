---
id: redshift-bucket-size-gpu-limits
title: Maxon advice: avoid bucket 64 on a GPU and 512 with several GPUs; default 128; one GPU got faster as buckets grew
domain: redshift
tags: [bucket size, gpu, multi gpu, vram, render time]
applies_to: Redshift in C4D (2023 video)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=uKRqHwVr0F4, src:yt-transcripts]
feeds: [coach, estimator, redshift]
conflicts: none
---
Maxon says 64 underuses the GPU and 512 is wrong with multiple GPUs [11:28]. One-GPU test: 128 = 8.4 s, bigger = 7.6 s, 512 = 7.2 s [12:04].
Bigger buckets need more VRAM, so keep 128 if the card is tight.

**Use it:** estimator: log bucket size next to render time per machine; coach: default 128, test one step up on single-GPU machines.
