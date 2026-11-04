---
id: pipeline-deadline-cloud-open-standard-custom-submitters-extra-steps
title: Deadline Cloud is an open job standard: studios can keep their own submit tools, add non-render steps such as AI upscaling, and commercial farms usually cannot
domain: pipeline
tags: [[deadline cloud, open standard, custom submitter, plugins, render farm comparison, ai upscaling, pipeline, johannes omen, omen digital studio], deep-read]
applies_to: AWS Deadline Cloud
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Sz-Bmxj4POU, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Johannes Omen (render-pipeline integrator) compared Deadline Cloud with commercial render farms: it has an open standard, so a studio can build or customise submitters and keep its existing pipeline tools, whereas the commercial farms ship their own closed applications and do not accept plugins added to the renderer [13:37-14:40].
Because any extra step can be part of the job, he sees it as a platform rather than only a render queue: for example an AI upscaling step after render, or any other task that can run on AWS or elsewhere [17:14-17:45].
A first engagement typically starts with a short demo, a compatibility check of DCC plugins and conda packages, then an AWS-funded proof of concept of about two to four weeks and optional ongoing support [16:12-17:14].

**Use it:** supports building the render platform around a job queue with custom submit steps and post-render tasks (comp prep, upscaling, QC) as first-class job steps.
