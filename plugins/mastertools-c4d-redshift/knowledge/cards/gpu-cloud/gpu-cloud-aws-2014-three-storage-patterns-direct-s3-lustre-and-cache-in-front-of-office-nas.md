---
id: gpu-cloud-aws-2014-three-storage-patterns-direct-s3-lustre-and-cache-in-front-of-office-nas
title: AWS 2014: three ways to feed cloud render nodes: parallel reads straight from S3, a disposable Lustre, or a cache appliance in front of the office NAS
domain: gpu-cloud
tags: [aws, 2014, storage patterns, s3, lustre, avere, direct connect, nas cache, render nodes, deep-read, gpu-cloud]
applies_to: AWS (2014)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=cm4sPe1nLjU, src:yt-transcripts, https://www.youtube.com/watch?v=fnbRcTeKirw]
feeds: [estimator]
conflicts: none
---
Pattern one: if the render software can read S3 itself, split reads into ranged gets and writes into multi-part uploads; throughput scales with the instance's network until it saturates [07:25-07:56, 38:37-39:08].
Pattern two: a Lustre file system in front of S3 (see the disposable Lustre card) when software needs a normal file system; size storage and metadata nodes to the farm size and bandwidth [38:37-39:41].
Pattern three, hybrid: when the office NAS holds huge files that are slow to move, run Avere vFXT cache appliances in EC2 in front of it over one or more 10 Gb Direct Connect links; several cache nodes can saturate the link [11:34-12:04, 39:41-40:12].
Render clients mount the file system and point the farm manager at its licence server; that is nearly all the node setup [17:16].

**Use it:** the platform's render-node checklist can name the storage pattern per farm and warn when a farm renders from a slow link back to the office.
Transcript support: Azure OpenCue sample puts a cache cluster in front of cheap blob storage for the same reason (https://www.youtube.com/watch?v=fnbRcTeKirw [23:07])
