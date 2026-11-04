---
id: gpu-cloud-qumulo-vendor-sizing-hybrid-nodes-hit-80-90-percent-cache-reads-4-node-flash-19gbs-96k-iops
title: Qumulo sizing numbers (vendor, 2022): hybrid nodes served 80-90 percent of reads from flash; 4 all-flash nodes 19 GB/s and 96,000 IOPS
domain: gpu-cloud
tags: [storage, qumulo, nvme, iops, throughput, render-farm, sean-walbridge, deep-read]
applies_to: Qumulo 5.x node families, video uploaded 2022-07
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=XSqzTroN_ec, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Sean Walbridge, vendor numbers, not tests: hybrid (hard-drive plus flash) nodes typically see 80-90 percent cache hits, so reads feel like flash [13:29-14:31].
Four all-flash nodes: 19 GB/s and 96,000 IOPS [20:17-20:48]. Four C192 NVMe-hybrid nodes: about 70,000 IOPS, 14 GB/s cached read, 17.5 GB/s with a fifth node [23:23-24:54]. A 16-node 4 PB cluster of 432 TB boxes: 240,000 IOPS [25:54-26:27].
Smallest usable sizes quoted: 52 TB (own hardware), 68 TB (Supermicro all flash), 80 TB hybrid [19:12-21:20].
Host: IOPS are what people forget to size for in rendering [20:48]. Sean: a 5.1.0 update raised write speed 20-30 percent [21:50].

**Use it:** use only for orders of magnitude when talking about a studio NAS; a freelancer with a few render machines needs a fraction.
