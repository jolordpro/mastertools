---
id: gpu-cloud-aws-thinkbox-2019-spot-interruptions-were-95-percent-finished-jobs-with-a-two-minute-warning
title: AWS (2019): in a 3-month study 95% of spot-instance terminations were users shutting down after finished renders; real interruptions came with a two-minute warning
domain: gpu-cloud
tags: [aws, ec2 spot, interruption, two minute warning, checkpointing, deadline, will macdonald, siggraph 2019, deep-read]
applies_to: AWS EC2 Spot, 2019
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=Fl_FdVgp2E0, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
Spot is the same compute, region and instance types as on-demand; the only difference is it can be taken back, with a two-minute warning [10:21]. MacDonald says AWS studied three months of interruptions and 95% were instances finishing work and being shut down by the user, so only about 5% were real interruptions [11:23]. He says clusters of up to 1 million parallel vCPUs have been run on spot [10:52], and that checkpointing is the obvious render-side mitigation [11:23]. Capacity is diversified by mixing instance types in a spot fleet [12:29].

**Use it:** a vendor statistic from 2019 for CPU-heavy VFX work; do not assume GPU spot behaves the same (compare gpu-cloud-aws-gpu-spot-prices). The check: short chunks mean a lost spot node costs little.
