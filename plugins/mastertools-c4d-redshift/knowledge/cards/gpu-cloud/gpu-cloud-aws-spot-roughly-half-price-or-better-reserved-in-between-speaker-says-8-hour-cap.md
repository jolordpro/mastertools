---
id: gpu-cloud-aws-spot-roughly-half-price-or-better-reserved-in-between-speaker-says-8-hour-cap
title: Argo Casper on EC2 pricing tiers: spot is cheapest (he says at least 50 percent below on-demand, up to 90), reserved sits between; he quotes an 8-hour spot limit
domain: gpu-cloud
tags: [aws, spot, on-demand, reserved, argo-casper, ledger-check, deep-read]
applies_to: AWS EC2, webinar uploaded 2025-03
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PjafAJ0-6SA, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Order he gives: on-demand most expensive, reserved (one-year commitment) in the middle, spot cheapest [25:25-26:27].
Spot savings swing, so he budgets at least 50 percent off, up to 90 [25:25-25:56].
He says spot can run at most 8 hours before it is taken back; a single frame or layer rarely needs that long, and longer single tasks are fragile anyway [26:27-26:58]. I could not confirm the 8-hour figure from the video; treat as the speaker's claim.
Render frames are short, so spot is the default for him.

**Use it:** use only as a rule of thumb; check current AWS spot terms before the estimator prints a spot discount. Chunk long frames so none runs for hours.
