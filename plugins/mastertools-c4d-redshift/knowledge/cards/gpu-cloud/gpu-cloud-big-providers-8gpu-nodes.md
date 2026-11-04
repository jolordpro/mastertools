---
id: gpu-cloud-big-providers-8gpu-nodes
title: CoreWeave sells only 8-GPU nodes, Lambda has no 5090 or L40S, Paperspace is not a price play
domain: gpu-cloud
tags: [coreweave, lambda, paperspace, digitalocean, gpu, nodes, price]
applies_to: prices as of 2026-10
status: V2
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://docs.coreweave.com/docs/pricing/pricing-instances, https://lambda.ai/pricing, https://gpu-cost.pages.dev/provider/paperspace/, src:research-gaps-deep]
feeds: [PLAN 5b]
conflicts: none
---
CoreWeave: L40S $18/h per 8-GPU node ($2.25 each), RTX PRO 6000 $20/h per node ($2.50 each); too big for one-frame jobs.
Lambda: A6000 $1.09, H100 PCIe $3.29, H100 SXM $3.99-4.29, B200 $6.69-6.99; no L40S, PRO 6000 or 5090 on its page.
Paperspace/DigitalOcean: RTX 6000 Ada and L40S about $1.57, A6000 $1.89 (legacy), no spot.

**Use it:** skip these for per-frame render jobs; they only matter if a big multi-GPU box is wanted.
