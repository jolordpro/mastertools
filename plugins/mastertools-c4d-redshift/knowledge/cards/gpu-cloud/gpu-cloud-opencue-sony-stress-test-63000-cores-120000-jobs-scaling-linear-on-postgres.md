---
id: gpu-cloud-opencue-sony-stress-test-63000-cores-120000-jobs-scaling-linear-on-postgres
title: OpenCue stress test at Sony Pictures Imageworks (2020): 120,000 short jobs, 63,000 running at once, load grew linearly
domain: gpu-cloud
tags: [opencue, imageworks, postgres, scheduler, stress-test, diego, deep-read]
applies_to: OpenCue 0.4.55, ASWF Open Source Day 2020
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=fnbRcTeKirw, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Diego (Imageworks) tested Postgres in place of Oracle before production: jobs of one to two minutes (simulation), ramped from 5 jobs up to 120,000, with about 63,000 render-host cores free so the whole farm could be booked [16:14-18:53].
Server side: several VMs with 12 GB RAM each behind a load balancer; database on two bare-metal 16-core, 90 GB machines in master/standby, only one taking load [17:17-17:49].
At the biggest run memory use was about 18 percent on the servers and 21 percent on the database; the response curve stayed linear, so the scheduler did not become the bottleneck [18:22-19:25].
Ben Dynes: the Oracle to Postgres move went smoothly; they first needed support contracts, backups and monitoring in place [09:19-11:27].

**Use it:** cite as a ceiling check: a scheduler server is unlikely to be the limit for any single-artist or small-studio farm.
