---
id: gpu-cloud-ec2-spot-fleet-request-by-vcpu-and-memory-range-lists-43-matching-types
title: EC2 spot request by vCPU and memory range instead of one instance type: his 2-4 vCPU, 2-8 GB request matched 43 types and showed a 64 percent saving
domain: gpu-cloud
tags: [aws, ec2, spot-fleet, launch-template, rahul-wagh, deep-read]
applies_to: AWS EC2 console, video uploaded 2024-07
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=b6oPVrDvV8E, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Rahul Wagh (AWS tutorial channel, a web hosting demo, not rendering) recommends creating a launch template first so the same recipe can start spot and on-demand machines [05:12-05:43].
In the spot request he sets target capacity (4 here) and gives ranges, 2 to 4 vCPU and 2 to 8 GB, so any matching type can fill the request; the console listed 43 matching types and a strong fleet-strength rating [16:33-18:41].
The summary screen showed 64 percent savings against on-demand [18:41-19:12]. Four instances reached running within a minute or so, health checks still initialising [20:13-21:16].
He narrows by family (for example C5) if needed [18:09].

**Use it:** a flexible range gives spot more places to find capacity; for render nodes add a GPU filter and a memory floor equal to the scene's RAM.
