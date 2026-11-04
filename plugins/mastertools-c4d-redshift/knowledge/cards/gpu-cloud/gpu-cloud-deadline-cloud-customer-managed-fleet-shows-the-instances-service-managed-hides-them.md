---
id: gpu-cloud-deadline-cloud-customer-managed-fleet-shows-the-instances-service-managed-hides-them
title: AWS Deadline Cloud: pick a customer-managed fleet if you want to see and stop the EC2 instances; service-managed hides them and just bills
domain: gpu-cloud
tags: [aws, deadline-cloud, fleet, service-managed, customer-managed, argo-casper, deep-read]
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
Argo Casper prefers customer-managed fleets because the autoscaling groups and instances show up in the normal AWS console where he can stop or delete them; with service-managed they do not appear and you only see the bill [07:04-07:36].
Fleet creation form asks for OS (Linux used), 64-bit not Arm, vCPU range (up to 16), memory range (8-24 GB); for GPU nodes he allowed up to 2 accelerators and 12 GB GPU memory, and AWS picks matching instance types [08:07-09:41].
A fleet and queue take about 10-20 seconds to appear and a few more moments to be usable [06:00, 12:21].

