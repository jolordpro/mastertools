---
id: gpu-cloud-nab25-deadline-cloud-queue-budgets-asset-cache-and-simple-permissions
title: AWS Deadline Cloud lets you cap spend per queue or fleet with warnings or a hard stop, and assets uploaded once are cached for other artists; AWS staff's description
domain: gpu-cloud
tags: [deadline-cloud, budgets, queues, asset-cache, permissions, aws, vendor-claim, gpu-cloud, deep-read]
applies_to: AWS Deadline Cloud (March 2025)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=-Ks7SSgeHGg, src:yt-transcripts, https://www.youtube.com/watch?v=Fl_FdVgp2E0, https://www.youtube.com/watch?v=PjafAJ0-6SA]
feeds: [estimator, CHECKS]
conflicts: none
---
From the Q&A, answered by Sonagra and AWS people [18:44-21:19]: management feels like running Deadline 10 on-prem (jobs, priorities), except you can split queues and fleets and give people or jobs different priorities. Fleet setup is a few clicks and can be done by a producer once they know what they are scaling. Assets are cached in the cloud, so a second artist's submission recognises files already there and uploads only what is new. Permissions start simple and can be tightened. Budgets can be set per queue or fleet, so a team or artist cannot pass a limit; flags and warnings appear as you near it, or rendering can stop the moment the budget is hit [20:47-21:19]. The service had launched only weeks before (service launch in early 2025, per the host intro [00:39]). Panelists also say security worries are mostly gone with clients [17:11-17:43].

**Use it:** make the farm budget a per-queue number with a warn level and a hard stop, mirroring this, in any cost estimator or farm policy.
Transcript support: Conductor's 2019 email/pause/kill thresholds are an earlier form of queue budget caps (https://www.youtube.com/watch?v=Fl_FdVgp2E0 [30:49-31:51])
Transcript support: independent hands-on description of queue budgets with limit actions (https://www.youtube.com/watch?v=PjafAJ0-6SA [14:28])
