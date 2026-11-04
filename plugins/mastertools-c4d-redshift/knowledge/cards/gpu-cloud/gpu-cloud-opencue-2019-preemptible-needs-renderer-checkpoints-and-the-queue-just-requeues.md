---
id: gpu-cloud-opencue-2019-preemptible-needs-renderer-checkpoints-and-the-queue-just-requeues
title: Sony's use of preemptible cloud nodes (2019): about a quarter of the price, 24-hour auto reboot handled by an Arnold build that checkpoints on a 30-second warning; the queue only drops the node and reruns the task
domain: gpu-cloud
tags: [preemptible, checkpoint, arnold, sony imageworks, opencue, autoscaling, google cloud, siggraph 2019, deep-read]
applies_to: Sony Imageworks with Google preemptible VMs, 2019
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=0gXT3sntiFg, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
Preemptible nodes cost about a quarter of the normal price and reboot at 24 hours as well as when preempted; Sony handled this in its own Arnold build, which writes periodic checkpoints and resumes elsewhere, given about 30 seconds' notice [21:19-21:50]. The queue itself does nothing special: a preempted node is flagged quickly and removed from the pool, its tasks fail and are requeued, and software with checkpoints resumes [24:23]. Scaling was driven by outside scripts that raised the cloud allocation when production expected a busy render night (for example 8,000 to 10,000 or 15,000 cores); that logic is not in OpenCue yet [22:33-23:52]. Cloud nodes can reuse names or IPs and are handled [54:32].

**Use it:** preemptible GPU nodes are only cheap if a lost frame is small: render by frame chunks and keep checkpointable or short work there. Compare gpu-cloud-zync-2016-preemptible-vms-70-percent-cheaper-24-hour-cap-set-one-frame-per-task.
