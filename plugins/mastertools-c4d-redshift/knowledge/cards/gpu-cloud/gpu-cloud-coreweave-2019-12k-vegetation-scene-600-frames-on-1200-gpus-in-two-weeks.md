---
id: gpu-cloud-coreweave-2019-12k-vegetation-scene-600-frames-on-1200-gpus-in-two-weeks
title: A 12K, 600-frame, vegetation-heavy Blender scene (12-20 h per frame locally) was done on 1,200 GPUs in two weeks, said to be half a year on rental machines
domain: gpu-cloud
tags: [coreweave, blender, scale, 12k, case-study, marco, deep-read]
applies_to: CoreWeave Concierge, Blender Conference talk uploaded 2019-10
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=sh8UhQ1zofg, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
A customer came with a 12K projection piece of 600 frames full of leaves and trees, too big for the one-click tier [07:27-08:29].
On their own machines a frame took about 12 to 20 hours; on 1,200 GPUs the job finished in two weeks, against an estimated six months on the customer's rental capacity [08:00-08:29].
This pushed them to build the larger tier. Vendor-reported figure, one customer.

**Use it:** hours per frame times frames divided by GPUs is the first back-of-envelope; the 12-20 h example shows why heavy scenes belong on a farm tier.
