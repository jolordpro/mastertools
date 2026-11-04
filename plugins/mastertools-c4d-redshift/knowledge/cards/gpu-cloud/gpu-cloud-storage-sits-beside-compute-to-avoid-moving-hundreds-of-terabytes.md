---
id: gpu-cloud-storage-sits-beside-compute-to-avoid-moving-hundreds-of-terabytes
title: Cloud pipelines work when storage lives next to the compute; moving hundreds of terabytes for each render does not
domain: gpu-cloud
tags: [storage, egress, data transfer, file system, nvme, hdd, triple replicated, coreweave, spire, cloud native, deep-read]
applies_to: any cloud pipeline
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=aJTLc7qQ1G0, https://www.youtube.com/watch?v=me25mlhgERI, https://www.youtube.com/watch?v=_5tXiMbpKw0, src:yt-transcripts]
feeds: []
conflicts: none
---
Spire/CoreWeave [24:07-26:44, SP]: two tiers, NVMe (very high IOPS, used for workstations and mounted into containers) and HDD for bulk; data triple replicated; capacity can grow as a show grows, so no buying a storage server for a new show. Feldman: copying hundreds of terabytes to the cloud for a render is not practical, so keep storage where all other resources can reach it quickly. Textures read often belong on the fast tier [25:42].
CoreWeave 2021 [03:45-05:22, CW]: AWS S3 plus egress fees and slow transfer make a full pipeline there expensive, so the half-way design (cloud desktops over NFS to on-prem storage) is poor. Kember 2015 [04:14, KE]: cloud rendering is a heavy storage problem as much as compute; sims competing with renders for file I/O make renders stall on a farm not built for it.

**Use it:** when pricing a cloud move, include where the scene and caches sit, and what moving them costs in time and egress, before comparing GPU-hour prices.
