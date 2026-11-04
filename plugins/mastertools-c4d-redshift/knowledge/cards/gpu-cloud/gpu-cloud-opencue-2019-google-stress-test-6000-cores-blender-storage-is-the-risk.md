---
id: gpu-cloud-opencue-2019-google-stress-test-6000-cores-blender-storage-is-the-risk
title: Google solution architects stress-tested OpenCue with Blender at 6,000 cores and thousands of simultaneous tasks; they say storage and network design, not the queue, is where trouble appears
domain: gpu-cloud
tags: [opencue, google cloud, blender, stress test, storage, nfs, latency, siggraph 2019, deep-read]
applies_to: OpenCue on Google Cloud, 2019
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=0gXT3sntiFg, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
Brennan Doyle (Google solution architect) says Google ran Blender jobs through OpenCue with 6,000+ cores at once (instances of a few to 16 vCPUs), with many tiny jobs and a few huge ones, thousands of tasks at a time; it needed a few small efficiency fixes then coped [26:57-29:03]. Both Sony and Google say the file filers and network, not the scheduler or latency to the queue, are the main concern; open Cue itself does not touch file storage [25:55-26:26, 27:28-28:00]. Google published scene files and an example deployment on its site [29:03]. The queue data keeps history in separate tables so scheduling stays fast [31:09].

**Use it:** another data point that the render manager scales and the bottleneck is storage throughput; budget the shared file system first when sizing a farm.
