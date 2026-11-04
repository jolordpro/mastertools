---
id: gpu-cloud-deadline-cloud-service-managed-idle-shutdown-takes-five-minutes-shorten-it
title: Idle Deadline Cloud workers hang on about five minutes before shutting down; Argo Casper measured 5-6 minutes and calls idle time the main cost driver
domain: gpu-cloud
tags: [aws, deadline-cloud, idle, scale-in, cost, argo-casper, deep-read]
applies_to: AWS Deadline Cloud, webinar uploaded 2025-03
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PjafAJ0-6SA, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
After the last task ends, the managed fleet waits roughly five minutes before scaling in; he timed 5 to 6 minutes [21:31, 50:50-51:21].
He says those little idle windows add up on the month's bill and prefers to halve the wait in his own autoscaling rule [21:31-22:04].
Upside: during the window a re-render or the next job reuses the warm instance and skips boot time [51:21-51:51].
His summary: cost starts only when workers are active, idle or rendering, or when data sits in storage [52:23-53:59].

**Use it:** the estimator should add idle minutes per job burst to any cloud estimate, not just render minutes. Matches the existing idle-cost card.
