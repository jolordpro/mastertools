---
id: gpu-cloud-zync-2016-preemptible-vms-70-percent-cheaper-24-hour-cap-set-one-frame-per-task
title: Zync (2016): preemptible VMs are about 70% cheaper but can be taken at any time and run at most 24 hours, so use them for short frames and set frames per task to one
domain: gpu-cloud
tags: [zync, preemptible, pvm, google cloud, live migration, frames per task, checkpoint, todd prives, ibc 2016, deep-read]
applies_to: Google Cloud preemptible VMs through Zync, 2016
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=aAjOM-JqnHI, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Standard VMs can run indefinitely and use live migration during maintenance; preemptible VMs are spare capacity, can be taken away if Google needs them, run at most 24 hours and cost around 70% less (less with Zync because licensing is included) [36:18-37:20]. Prives's example for a 64-core Maya + V-Ray machine is about $4 an hour standard against a figure the captions give as '$150', probably $1.50, so the figure is unclear [37:20]. His advice: fine for frames up to about an hour, risky at 3 to 4 hours per frame [37:20-37:52]. A lost task loses everything in it, so set frames per task to 1 so each frame downloads as it finishes [38:55]. Snapshotting partly done renders, for example Arnold, was under consideration [37:52].

**Use it:** adds the numbers (70%, 24 hours, frame-size limit) to the Slayden preemptible habit card; for GPU preemptible nodes check the provider's own limit.
