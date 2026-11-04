---
id: gpu-cloud-deadline-cloud-failed-job-retries-five-times-read-the-task-log-for-a-missing-dependency
title: Deadline Cloud jobs retry five times by default; the task log, not the worker log, shows why (his demo: a self-hosted worker with no conda environment)
domain: gpu-cloud
tags: [aws, deadline-cloud, failure, retries, task-log, hybrid, argo-casper, deep-read]
applies_to: AWS Deadline Cloud, webinar uploaded 2025-03
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PjafAJ0-6SA, src:yt-transcripts]
feeds: [shakedown]
conflicts: none
---
Default is 5 attempts per job; after 5 failures status reads never attempted, which here meant initialization failed [43:27-45:33]. He says raising it rarely helps: if it fails five times it fails a sixth.
Demo cause: his own PC worker lacked the Python conda environment the job bundle needs. The reason appears in the task log in the monitor and in CloudWatch, not in the local worker window [44:30-45:33]. The same job on the managed fleet succeeded first time [49:46-50:50].
Other loop causes he lists: memory limit too low, missing licence on a fresh local node, bad config, storage. Check dashboards, right-size, or change the scale-in rule [58:41-1:00:45].
Workers health-check every 15 seconds [38:31].

**Use it:** in a hybrid farm checklist, verify each local node has the same runtime environments and licences as the cloud image before sending it work.
