---
id: gpu-cloud-runpod-prices
title: RunPod lists an RTX 5090 at $1.19/h secure and $0.69/h community, 4090 at $0.89 and $0.34
domain: gpu-cloud
tags: [runpod, gpu, price, 5090, 4090, l40s, h100, serverless]
applies_to: prices as of 2026-10
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.runpod.io/pricing, src:research-gaps-deep]
feeds: [PLAN 5b, ladder prices.json]
conflicts: none
---
Per GPU-hour, secure / community: RTX 4090 $0.89 / $0.34; RTX 5090 $1.19 / $0.69; RTX PRO 6000 $2.49 / $1.69; L40S $1.09 / $0.79; RTX A6000 $0.59 / $0.33; H100 PCIe $2.89 / $1.99.
Serverless: 5090 $1.79, 4090 $1.34, RTX 6000 Pro $3.49, H100 $5.39. Network volume $0.07/GB-month under 1 TB.

**Use it:** load these into prices.json; secure tier is the safer default for a paid job, community for retryable draft frames.
