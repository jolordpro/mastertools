---
id: gpu-cloud-aws-2014-keep-manager-and-licence-server-up-and-tear-down-the-render-clients
title: AWS 2014: build the farm as separate templates (licence server, farm manager, client clusters); tear down only the clients between jobs
domain: gpu-cloud
tags: [aws, 2014, deadline, flexlm, troposphere, cloudformation, infrastructure as code, render clients, deep-read, gpu-cloud]
applies_to: AWS, Deadline, FlexLM, Arnold (2014)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=cm4sPe1nLjU, src:yt-transcripts, https://www.youtube.com/watch?v=_5tXiMbpKw0]
feeds: [coach]
conflicts: none
---
Gerald's design: the licence server, render manager and each client cluster are separate CloudFormation stacks built from Python (troposphere), with one function making an auto-scaling group per node tier from a config file for instance types, min and max size, and a shared security group [12:38-17:16].
Node boot script only mounts the file system, points Deadline at the installers, and points it at the licence server [17:16-17:52]. Render and compositing clusters scale separately [15:11-15:41].
When the job ends, tear the clients down but keep the manager and licence server for job history and ease of reuse [15:11].
The speaker said this setup would have taken months before cloud tooling [17:16].

**Use it:** a cloud-farm advisor should treat the licence server and job history as the persistent part and the worker nodes as disposable; check that a farm keeps job logs after tear-down.
Transcript support: Kember (2015): when far from a data centre build a cloud file server, sort cloud licensing, then add render VMs and a queue. (https://www.youtube.com/watch?v=_5tXiMbpKw0 [07:53-08:24])
