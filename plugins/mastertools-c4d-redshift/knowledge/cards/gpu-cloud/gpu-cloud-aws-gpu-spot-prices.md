---
id: gpu-cloud-aws-gpu-spot-prices
title: AWS g6e (L40S) spot runs $0.43-0.87/h against about $1.86 on demand
domain: gpu-cloud
tags: [aws, spot, g6e, g7e, l40s, gpu, price]
applies_to: us zones, 2026-10
status: V2
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.devzero.io/instances/aws/g7e.4xlarge, https://compute.doit.com/spot/us-east-1/g6e.xlarge, src:research-gaps-deep, https://www.youtube.com/watch?v=Fl_FdVgp2E0]
feeds: [PLAN 5b]
conflicts: none
---
g6e (L40S) on-demand about $1.86/h; spot $0.43-0.87 in some zones. g7e (RTX PRO 6000 Blackwell), one GPU: on-demand $3.36-4.00, spot $1.50-1.70.
All from third-party trackers, not AWS's own list. Exact spot rates are unverified. AWS is the slowest to set up.

**Use it:** AWS is a fallback for licence-metered work, not a price winner; re-read live spot prices.
Transcript support: Rocket Science VFX ran Redshift on GPU spot via Deadline in 2019 (no prices given) (https://www.youtube.com/watch?v=Fl_FdVgp2E0 [12:50-13:31])
