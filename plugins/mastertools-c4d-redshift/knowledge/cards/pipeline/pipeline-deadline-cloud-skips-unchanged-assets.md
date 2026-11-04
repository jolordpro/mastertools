---
id: pipeline-deadline-cloud-skips-unchanged-assets
title: Deadline Cloud does not re-upload unchanged asset files, such as a 300 MB HDR
domain: pipeline
tags: [deadline cloud, upload, assets, hdr, sync]
applies_to: AWS Deadline Cloud
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Sz-Bmxj4POU, src:yt-transcripts, https://www.youtube.com/watch?v=Fl_FdVgp2E0]
feeds: [pipeline, estimator]
conflicts: none
---
If a prior job uploaded the file and it did not change, it is skipped [28:06]. The demo scene was 19 MB.

**Use it:** estimator: upload cost applies to first submission only.
Transcript support: Deadline 10 on AWS (2019) already walked scene dependencies and pushed only what the job needed (https://www.youtube.com/watch?v=Fl_FdVgp2E0 [17:09-17:40])
