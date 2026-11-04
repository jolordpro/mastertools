---
id: gpu-cloud-salad-prices
title: Salad RTX 5090 costs $0.25/h on the batch tier up to $0.60/h on high; new prices start 1 Nov 2026
domain: gpu-cloud
tags: [salad, gpu, price, 5090, 4090, batch, interruptible]
applies_to: Salad prices from 2026-11-01
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://salad.com/pricing, src:research-gaps-deep]
feeds: [PLAN 5b, ladder prices.json]
conflicts: none
---
RTX 5090 32 GB: $0.60 high, $0.483 medium, $0.367 low, $0.250 batch per hour. RTX 4090 24 GB: $0.44, $0.347, $0.253, $0.160.
Billed per second; image download and container start are free; CPU and RAM are included. No L40S, A6000, PRO 6000 or H100 listed.
Batch is cheapest and most interruptible; medium and low can be bumped by higher bids; about 30 min minimum run.

**Use it:** use batch only for frames that can simply be retried; price tables must carry the 1 Nov date.
