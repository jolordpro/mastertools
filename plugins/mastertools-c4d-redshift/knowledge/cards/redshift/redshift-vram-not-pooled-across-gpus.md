---
id: redshift-vram-not-pooled-across-gpus
title: VRAM does not add across GPUs: four 32 GB cards are four 32 GB budgets
domain: redshift
tags: [vram, multi gpu, memory, rtx 5090]
applies_to: Redshift on multi-GPU
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=u5eoWCQvegI, src:yt-transcripts]
feeds: [estimator, CHECKS, redshift]
conflicts: none
---
iRender (vendor): each GPU holds its own copy of the scene, so four 32 GB cards do not make 128 GB. Plan the scene around one card [02:08-02:43]. History panel logs each frame's render time to find heavy frames.

**Use it:** estimator and VRAM check: compare scene memory to one card, not the sum.
