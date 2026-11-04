---
id: gpu-cloud-deadline-wait-save-multiregion
title: AWS Deadline Cloud 'wait and save' fleets start at $0.006 per vCPU-hour; spot is cheaper than on demand; multi-region lets idle regions run others' jobs
domain: gpu-cloud
tags: [deadline cloud, wait and save, spot, vcpu hour, multi-region, follow the sun]
applies_to: AWS Deadline Cloud (May 2026), CPU prices
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=5qY4LFDbNnE, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Three regions, each with its own farm, queues and fleets; spot and wait-and-save fleets [02:38-03:11].
Wait-and-save prices start as low as $0.006 per vCPU-hour; studios can send jobs to a region whose artists have gone home [03:11]. This is vCPU pricing, not GPU.

**Use it:** a cost dial can include a slower cheaper lane, but not with these CPU numbers for Redshift GPU.
