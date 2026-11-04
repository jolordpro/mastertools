---
id: gpu-cloud-deadline-cloud-autoscaling-group-start-min-and-desired-at-zero-mix-two-gpu-instance-types
title: Autoscaling group for render nodes: start min and desired at 0, raise the max only when needed, list two instance sizes with equal weight
domain: gpu-cloud
tags: [aws, autoscaling, ec2, g4, spot, argo-casper, deep-read]
applies_to: AWS EC2 Auto Scaling for Deadline Cloud, webinar uploaded 2025-03
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PjafAJ0-6SA, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Argo Casper builds an auto scaling template from a Blender server image, adds two accelerated instances from the G4 family (T4/RTX or AMD variants), each with weight 1 so they rotate evenly [23:16-25:25].
Minimum and desired capacity are set to 0 so nothing bills while configuring; he raises the max to 10 afterwards, or raises desired only if a deadline needs instant capacity [29:07-31:12].
No load balancer or VPC needed for a render-only group; lifecycle notifications and tags are skipped because a dead node is just replaced [28:35, 30:11].
He says choose the lowest price instance and optimise later; he has seen only one genuine hardware crash [27:30-28:35].

**Use it:** for a self-built cloud farm plan, default every group to min 0 and desired 0, and keep two interchangeable instance types so spot shortages in one do not stall the queue.
