---
id: gpu-cloud-conductor-2019-budget-ladder-email-at-4000-pause-at-4500-kill-at-5000
title: Mac Moore (Conductor, 2019): set cost limits per job, for a $5,000 shot email at $4,000, pause pending work at $4,500, kill everything at $5,000
domain: gpu-cloud
tags: [conductor, mac moore, cost limit, budget alert, pause, kill, cloud rendering, one node per frame, siggraph 2019, deep-read]
applies_to: Conductor on AWS/GCP, 2019
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Fl_FdVgp2E0, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
Moore's example: a shot bid at $5,000 gets a warning email at $4,000, a pause of pending work that would add spend at $4,500, and a kill at $5,000, after which the producer and production company decide on more budget or the shot quality so far [30:49-31:51]. Conductor's one-to-one rule: a 1,000-frame shot launches 1,000 nodes (EC2 or spot) [29:44]. Usage charts from one customer reached over 100,000 simultaneous cores, with cost returning to zero as the chart falls [30:17].

**Use it:** build exactly this ladder into the cost estimator: warn at 80%, pause new chunks at 90%, stop at 100% of the quoted budget.
