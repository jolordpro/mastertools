---
id: gpu-cloud-deadline-cloud-2024-console-setup-order-and-failure-points
title: AWS Deadline Cloud (2024) console setup order: Identity Center first, then monitor, farm, queue (with an S3 bucket), fleet
domain: gpu-cloud
tags: [aws, deadline cloud, identity center, monitor, farm, queue, fleet, s3, cloudformation, setup, deep-read]
applies_to: AWS Deadline Cloud console, mid-2024 (service-managed fleet)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=kyaphnaCDEU, https://www.youtube.com/watch?v=LZ-VaD5MZTk, src:yt-transcripts]
feeds: []
conflicts: none
---
Two tutorials (Apr and Jul 2024). Order: IAM Identity Center must be enabled before the wizard works; it manages users and groups and can link to Active Directory [02:07-03:08, D1]. Then name the monitor (the dashboard URL is the key output) and pick a region, which cannot be changed later [03:43, D1; 04:43, D2]. Farm, then a group and user, then a queue (creates an S3 bucket for job files and a least-privilege role) [05:16-05:49, D1], then a fleet [06:21]. Wizard builds it via CloudFormation, reversible by deletion [07:54, D1]. Regions in April 2024: US Virginia, Ohio, Oregon; Singapore, Tokyo, Sydney; Frankfurt; Ireland [03:39, D2].
Service-managed fleets come ready-made (2024: Maya, Nuke, Blender, Houdini/Karma, plus Arnold and KeyShot per AWS); customer-managed means building your own worker images, mounting file shares [00:03-01:04, D1]. Monitor has a web view for checking jobs remotely [01:04].

**Use it:** setup runbook skeleton; verify the supported-renderer list today because it was fresh in 2024.
