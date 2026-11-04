---
id: pipeline-deadline-cloud-farm-queue-fleet-model
title: Deadline Cloud: one farm, queues for projects, fleets of workers assigned to many queues; same-priority jobs run by submit date
domain: pipeline
tags: [deadline cloud, queue, fleet, priority, farm structure]
applies_to: AWS Deadline Cloud (Jan 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Sz-Bmxj4POU, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
A queue per project, team or archive; fleets define worker CPU/memory/OS and can be attached to several queues [21:22-22:27]. Same priority means the earliest submit renders first [25:00]. Conda packages deploy apps on workers; GPU or Linux limits are set in the submit window [25:31-27:03].

**Use it:** design reference for a render queue.
