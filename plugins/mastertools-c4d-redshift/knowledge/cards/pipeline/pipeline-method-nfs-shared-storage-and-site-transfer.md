---
id: pipeline-method-nfs-shared-storage-and-site-transfer
title: Use shared NFS inside a site, but move work between sites with an async prioritised transfer service, not a mounted network drive
domain: pipeline
tags: [andre prado, method studios, nfs, disk storage, transfer service, multi site, latency, corruption, deep-read]
applies_to: Studio infra
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=HuV0_AbDgYk, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Prado [17:25-19:01]: all workstations and render nodes mount the same NFS so work is shared and visible to the farm. Method's Vancouver NFS cluster was 21 nodes, each with 100 GB RAM and 1.6 TB SSD cache. Disk space is always tight: hundreds of artists create terabytes daily.
Mounting NFS across sites causes latency and corruption problems, so a transfer service submits jobs like the farm does (file path to studio, priority, asynchronous) [18:29]. Software packages sit on NFS too, so no system-level installs [19:01].
The pipeline tools wrap disk management: metadata about files, cleanup, transfers, third-party wrapping.

**Use it:** Remote or multi-site delivery: queue transfers with priority and verify; never edit over WAN mounts.
