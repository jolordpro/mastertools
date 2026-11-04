---
id: gpu-cloud-farm-priority-tiers-cap-nodes-garagefarm-low-15-ranch-medium-80-priority-cannot-change-after-start
title: Farm priority tiers cap node count (GarageFarm Low 15 nodes, RANCH Medium 80) and GarageFarm will not change a running job's priority
domain: gpu-cloud
tags: [garagefarm, ranch, priority, nodes, queue, render farm, deep-read]
applies_to: GarageFarm and RANCH Computing (Dec 2025 test)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=mK3nXETuNII, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
GarageFarm offers Low, Medium and High priority; Low allowed a maximum of 15 nodes for the job [03:31-04:05]. RANCH Medium priority allowed up to 80 nodes [06:21-06:46].
Tip given: if a job sits in the queue, raise priority to move it up. But a job started at Low cannot be changed; the screen showed High while it still ran at Low [04:05].
Fox Renderfarm and iRender had no priority tiers [00:32-01:02].

**Use it:** Pick the tier when submitting; plan for the node cap when estimating wall-clock time.
