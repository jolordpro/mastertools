---
id: gpu-cloud-raw-gpu-vs-farm-price-gap
title: Raw rented GPU time is roughly 9x-20x cheaper than farm card-hour prices
domain: gpu-cloud
tags: [gpu, farm, price gap, margin, compute at cost, shot 8]
applies_to: Oct 2026 prices
status: U
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [src:research-gaps-deep, src:research-render-farms]
feeds: [PLAN 5b, pricing model]
conflicts: none
---
Super Renders Farm sells a 5090 at about $5.17 per card-hour with licence and support. Raw Vast 5090 median $0.57; Salad batch $0.25. That is the 9x-20x gap (researcher's maths).
The gap has to pay for the Redshift licence, preflight, upload, retries, support and margin. The raw compute for Shot 8 is about $3-25; idle time is the usual surprise bill.

**Use it:** a clear price model is compute at cost plus a flat fee; the licence and setup, not the GPU, set the margin.
