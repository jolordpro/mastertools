---
id: gpu-cloud-serverless-gpu-prices
title: Serverless GPU rates: Modal L40S $1.95/h, Replicate L40S $3.51/h and idle billed on private models
domain: gpu-cloud
tags: [modal, replicate, runpod serverless, gpu, price, idle billing, l40s, h100]
applies_to: prices as of 2026-10
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://modal.com/pricing, https://replicate.com/pricing, src:research-gaps-deep]
feeds: [PLAN 5b]
conflicts: none
---
Modal: L40S $1.95/h, H100 $3.95, A10 $1.10, RTX PRO 6000 $3.03; $30/month free credit on the Starter plan.
Replicate: L40S $3.51/h, A100 $5.04, H100 $5.49; private models bill idle time too.
RunPod serverless 5090 is $1.79/h.

**Use it:** serverless suits bursty mockup calls; for a steady warm worker, compare against a plain rented 5090.
