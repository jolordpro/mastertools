---
id: gpu-cloud-nab25-right-size-fleets-per-task-type-sim-fleet-vs-2d-fleet
title: On an on-prem farm every machine must suit the heaviest job; cloud fleets can be sized per task, with a bigger fleet for sims and a small one for 2D
domain: gpu-cloud
tags: [deadline-cloud, fleet, right-sizing, sonagra, farm-planning, cost-prediction, gpu-cloud, deep-read]
applies_to: AWS Deadline Cloud
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-Ks7SSgeHGg, src:yt-transcripts, https://www.youtube.com/watch?v=hIxnygxsdmc]
feeds: [estimator]
conflicts: none
---
Andrew Sonagra [08:28-09:31]: an on-prem farm is built for the most expensive computation, because the same machines run heavy simulations and light comps; with Deadline Cloud you can run several fleets on one job, a more powerful one for simulations and a simpler one for 2D rendering, which makes budgeting and prediction more accurate. Sonagra adds [13:36-15:09] that the first jobs involve learning what the instance sizes are and how fast they run; after that a feedback loop forms: for this type of bid, these are the fleets needed, and recurring projects get better expense estimates. If a job runs slowly, add a faster fleet immediately [14:39-15:09]. Chaos's Phillip Miller says that with highly scalable renderers the cost to go wider is flat: it is faster if you divide the job by 100 [06:21-06:53] (vendor claim).

**Use it:** in the estimator, price task types separately (sim, 3D render, 2D comp) with their own node type, instead of one blended node price.
Transcript support: 2016 panelist: cloud allocation is per-task sizing, unlike on-prem packing (https://www.youtube.com/watch?v=hIxnygxsdmc [28:15-28:46])
