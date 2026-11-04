---
id: gpu-cloud-qube-azure-low-priority-pool-scaled-2-to-40-nodes-in-5-to-10-minutes-2018
title: Qube 7 on Azure (2018): a pool of dual-GPU NC-series VMs with Redshift and drivers pre-installed scaled from 2 to 40 low-priority nodes in 5 to 10 minutes
domain: gpu-cloud
tags: [qube, azure, pipelinefx, redshift, low priority, dedicated, batch explorer, cloud render farm, nc series, deep-read]
applies_to: Qube 7, Azure Batch pools, Redshift (2018 upload, PipelineFX)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=p50NXgsMGiw, src:yt-transcripts]
feeds: [estimator, pipeline]
conflicts: none
---
Setup shown: Qube supervisor, workers and storage; two Azure pools managed in Batch Explorer or the web portal [00:02-01:05]. Machines: NC12 v2-class dual-GPU VMs (caption says 'nce 12 v2 s', two Tesla P100-class GPUs), single-GPU and four-GPU sizes also exist [01:05, 06:47].
Pool scaled from 2 to 40 nodes; Azure took 5 to 10 minutes depending on load [01:40]. Each node starts as a base image, then application packages add Nvidia drivers, Qube dependencies and scripts, and Redshift [01:40-02:11]. 31 of 40 workers appeared after about three minutes [03:17].
Low-priority nodes chosen because the job is short and the chance of preemption low; choose dedicated nodes for must-deliver or long frames [02:11-02:42]. No prices are given.

**Use it:** cloud estimator: add a 5-10 minute scale-up and note preemption risk; price basis not stated in the video.
