---
id: pipeline-method-render-farm-numbers-and-job-model
title: A farm job holds tasks with requirements (RAM, priority) and dependencies, and artist machines join the farm overnight
domain: pipeline
tags: [andre prado, method studios, render farm, render node, job dependencies, ram requirements, frame time, deep-read]
applies_to: Studio farm, 2018
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=HuV0_AbDgYk, src:yt-transcripts]
feeds: [estimator, pipeline plan]
conflicts: none
---
Prado [13:36-16:55]: jobs have tasks plus requirements, e.g. an image sequence needing 50 GB RAM at high priority. The manager dispatches each frame to a node with enough cores and RAM (his example: at least 2 cores and 4 GB). Dependencies chain jobs, e.g. encode a QuickTime only after the render finishes. Custom tools show live memory/CPU and preview frames and support block, unblock, requeue, fail [15:18-15:51].
Scale at the time: about 1500 nodes, 50 cores and 100 GB each, bare metal, quoted as 56 thousand cores and 150 TB RAM (his figures do not multiply exactly) [16:55]. A Netflix 4K water and creature show had frames of roughly 125 hours each on one machine, so a 2000-frame shot would take decades on a single machine; artists resubmit many times a day [16:24]. Artist workstations are absorbed by the farm after they log off [19:32].

**Use it:** Estimator: express costs as frame-hours and RAM requirement per frame.
