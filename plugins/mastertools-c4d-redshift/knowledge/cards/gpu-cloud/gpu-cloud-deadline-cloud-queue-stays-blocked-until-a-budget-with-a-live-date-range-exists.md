---
id: gpu-cloud-deadline-cloud-queue-stays-blocked-until-a-budget-with-a-live-date-range-exists
title: AWS Deadline Cloud: a queue set to require a budget stays blocked until a budget with an active date range is attached
domain: gpu-cloud
tags: [aws, deadline-cloud, budget, queue, argo-casper, deep-read]
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
Argo Casper (devops, webinar on Deadline Cloud): if the queue is created with the budget requirement, no job can run until a budget is attached to that queue [05:00-06:33, 13:56-14:28].
Demo budget was 333 dollars; the default window is 3 months, he shortened it to 1 month, and a wrong start/end date left the queue still showing blocked [15:00-17:40].
After fixing it the status took several more minutes to clear; he says AWS settings are never instant but under about a minute [18:17], and in the demo it was longer [31:43].
Two limit actions exist: stop new jobs after the running ones finish (soft), or stop everything now (hard). He sets both [16:04-17:09].

**Use it:** check the budget's date window first when a fresh queue says blocked, then wait a few minutes before debugging other things.
