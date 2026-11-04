---
id: gpu-cloud-sony-worldwide-studios-aws-deadline-redshift-4k60-12x-faster
title: Sony Worldwide Studios moved 4K60 C4D + Redshift motion graphics to AWS Deadline spot GPUs and rendered 12 times faster than its on-prem farm
domain: gpu-cloud
tags: [sony, playstation, aws, deadline, rfdk, cdk, spot, redshift, p3, g4, usage-based licensing, deep-read]
applies_to: C4D + Redshift on Windows Server 2019, Deadline, AWS (2020 talk)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=kACWEs-XJcI, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Asghar and Andy Taylor (Sony Worldwide Studios IT), AWS re:Invent 2020. The creative-services team needed 4K 60 motion graphics for a press event and the on-prem farm filled up [02:37-03:39]. They stood up a Deadline farm as code (AWS CDK plus the Render Farm Deployment Kit, 5 Python stacks, about 5 commands up and 5 to tear down) and rendered 12x faster than on-prem [04:10-06:48]. Workers were Windows 2019 on spot p3 and g4 instances; p3.16xlarge gives 8 V100s, nearly 41,000 CUDA cores, and Redshift tops out at 8 GPUs, so the per-minute licence is fully used [12:03-13:34]. Licences (C4D and Redshift) were bought usage-based, charged per frame only while the GPU renders [16:23-17:41]. One run: 20 p3.16xlarge = 160 V100s for a 600-frame job [19:14-19:45]. p3 for production, g4 for cheap test frames and low-res [19:14].

**Use it:** Pattern for a studio cloud burst: pay-per-minute licences plus 8-GPU spot boxes, g4-class for tests, scripted up and down. Prices not given in the talk; do not quote a cost from it.
