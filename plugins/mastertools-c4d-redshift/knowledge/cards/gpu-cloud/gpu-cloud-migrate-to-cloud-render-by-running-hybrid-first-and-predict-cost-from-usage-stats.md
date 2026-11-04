---
id: gpu-cloud-migrate-to-cloud-render-by-running-hybrid-first-and-predict-cost-from-usage-stats
title: Argo Casper's migration advice: set the cloud farm up beside the local one, move jobs over when the team is trained; forecast cost from usage stats plus the AWS calculator
domain: gpu-cloud
tags: [aws, hybrid, migration, cost-prediction, deadline-cloud, argo-casper, deep-read]
applies_to: AWS Deadline Cloud, webinar uploaded 2025-03
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PjafAJ0-6SA, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
There is no good way to predict cloud cost up front; watch real usage, take the usage statistics Deadline gives (managed or not), then feed them into the AWS calculator for an estimate. If usage is stable it works as a quote basis [55:31-56:34].
Best path from a fully local farm: build the cloud queues and fleets in parallel (hybrid), let artists submit when trained, and only go fully cloud after it has proven itself; he says his team did it this way [57:06-58:09].
Ideal cloud use: extra power on top of the existing farm, submitted by farm and queue IDs [53:59-54:30]. Most DCC apps have direct submitters, so the terminal step is rarely needed [54:30-55:00].

**Use it:** the platform's first cloud step should be an overflow queue beside the local farm, with cost forecast from the first week's usage numbers.
