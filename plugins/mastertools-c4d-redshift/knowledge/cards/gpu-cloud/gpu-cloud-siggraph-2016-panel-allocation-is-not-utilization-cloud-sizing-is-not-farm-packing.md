---
id: gpu-cloud-siggraph-2016-panel-allocation-is-not-utilization-cloud-sizing-is-not-farm-packing
title: A panelist: on-prem tuning packs machines for throughput, cloud tuning picks the right size per task, and allocated machines are not the same as machines doing useful work
domain: gpu-cloud
tags: [allocation, utilization, right sizing, throughput, scheduling, siggraph 2016, cloud cost, deep-read]
applies_to: cloud rendering in general, 2016 panel
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hIxnygxsdmc, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
One panelist (the captions do not name the voice; context points to the Shotgun/Autodesk architect Phil Peterson) says that on a local farm you pack the resources you own as tightly as possible for best throughput, while in the cloud you allocate the most suitable size for each job [28:15]. People who compare costs often treat allocation as if it were utilization: you can allocate lots of machines and not use them, or keep machines fully busy on nothing useful, so the real measure is throughput [28:46]. Most studios still think about scheduling only in the on-prem way [28:46].

**Use it:** when the platform quotes a cost, report idle and boot time as cost of allocation, and test render settings on small frames before widening. See gpu-cloud-hidden-costs-idle-boot-rerender.
