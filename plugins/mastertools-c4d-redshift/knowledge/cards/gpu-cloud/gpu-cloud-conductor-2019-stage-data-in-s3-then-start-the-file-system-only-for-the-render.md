---
id: gpu-cloud-conductor-2019-stage-data-in-s3-then-start-the-file-system-only-for-the-render
title: Mac Moore (Conductor, 2019): do not start cloud nodes early like feeding a parking meter; hold data in cheap S3, then bring up fast storage and nodes only for the render and spin down
domain: gpu-cloud
tags: [conductor, mac moore, just in time, fsx for lustre, aws batch, s3, idle cost, siggraph 2019, deep-read]
applies_to: Conductor on AWS, 2019
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Fl_FdVgp2E0, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
Moore says studios used to light up 200 extra nodes and leave them running for months, which is no better than renting hardware [31:51-32:23]. Cost is the area under the usage curve, so the aim is to shrink the spikes [32:23]. His method: upload to inexpensive S3, prepare everything, bring up an FSx for Lustre file system with AWS Batch for the thousands of nodes only when ready, then spin down and send results back to S3 for download [33:25-33:57]. Customers also now ask for reads and writes direct to S3 buckets instead of POSIX paths [37:06-37:36].

**Use it:** idle time is the avoidable cost: the estimator should charge nodes from the first frame to the last and show prep and teardown separately.
