---
id: gpu-cloud-rtx-pro-6000-price-by-provider
title: RTX PRO 6000 (96 GB) costs $1.50-4.00 per GPU-hour depending on provider
domain: gpu-cloud
tags: [rtx pro 6000, blackwell, 96gb, price, coreweave, modal, aws, runpod]
applies_to: prices as of 2026-10
status: V2
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.runpod.io/pricing, https://docs.coreweave.com/docs/pricing/pricing-instances, https://modal.com/pricing, https://gpucloudprices.pages.dev/gpu/rtx-pro-6000/, src:research-gaps-deep]
feeds: [PLAN 5b]
conflicts: none
---
RunPod $2.49 secure / $1.69 community. CoreWeave $20/h for an 8-GPU node = $2.50 each. Modal $0.000842/s = $3.03/h. AWS g7e one GPU: on-demand $3.36-4.00, spot $1.50-1.70 (tracker, not AWS list).
Vast tracker range $0.80-1.69, median about $1.67, snapshots from different months.

**Use it:** when a scene needs more than 32 GB VRAM, compare these rows; the AWS spot figure is a tracker value, so confirm before quoting.
