---
id: gpu-cloud-coreweave-2019-one-frame-across-many-gpus-needs-identical-gpu-models
title: CoreWeave 2019: pooling GPUs across servers on one frame only works if every GPU is the same model, so the farm ran one card type
domain: gpu-cloud
tags: [coreweave, blender, gpu-pooling, virtualization, parallel-frames, marco, deep-read]
applies_to: CoreWeave Kubic, Blender Conference talk uploaded 2019-10
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=sh8UhQ1zofg, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Marco claims their GPU virtualisation can put 22, 48 or 150 GPUs on a single frame even across servers, while parallel rendering runs other frames on other GPU groups, up to about 100 frames at a time [18:04-19:36].
He says the key requirement is the same GPU model everywhere, otherwise it fails [26:48-27:18].
More GPUs did not cost more (same price, faster result), so the 2.5 release dropped the GPU-count field and let an algorithm choose [19:06-20:07].
Vendor claim, Blender Cycles era; not tested here.

**Use it:** do not assume pooling like this for Redshift; it renders per frame per GPU, so more speed for one frame means a faster card or Redshift's multi-GPU on one box.
