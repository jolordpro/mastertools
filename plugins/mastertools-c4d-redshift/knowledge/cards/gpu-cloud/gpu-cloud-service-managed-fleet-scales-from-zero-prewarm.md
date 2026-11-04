---
id: gpu-cloud-service-managed-fleet-scales-from-zero-prewarm
title: Service-managed Deadline fleets scale from zero; workers come up in minutes, so a demo pre-warmed some, and a Wait & Save fleet attached to every queue only joins when capacity allows
domain: gpu-cloud
tags: [[deadline cloud, service managed fleet, scale to zero, pre-warm, worker startup, wait and save, queue, johannes omen, andy hayes], deep-read]
applies_to: AWS Deadline Cloud
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Sz-Bmxj4POU, src:yt-transcripts, https://www.youtube.com/watch?v=-Ks7SSgeHGg, https://www.youtube.com/watch?v=PjafAJ0-6SA, https://www.youtube.com/watch?v=kyaphnaCDEU]
feeds: [estimator]
conflicts: none
---
Andy Hayes (AWS): a service-managed fleet lets you choose Windows or Linux and CPU or GPU, scales up when a job lands, does the work, then drops back to zero; no machine images or patching [19:20-19:50].
In the live demo some workers were pre-warmed for speed; the fleet then showed a growing state and grew from 5 to 10 to 14 workers in a few minutes [28:38-29:40]. Wait & Save workers would not be expected to start for a short job, but the fleet was attached to all queues and joins as capacity appears [22:27-22:57, 30:14].
For a repeat job submitted later in the day, a few Wait & Save workers joined and cut cost on that run by roughly 20-30%, with the spot fleet still guaranteeing fast turnaround [30:45].

**Use it:** the estimator should model a start-up delay of a few minutes for fresh fleets and treat Wait & Save as a bonus that may or may not join.
Transcript support: Earlier customer view: several fleets on one job, a heavy one for sims and a light one for 2D (https://www.youtube.com/watch?v=-Ks7SSgeHGg [08:28])
Transcript support: start-up up to about 2 minutes, 40 seconds possible with a lean base image (https://www.youtube.com/watch?v=PjafAJ0-6SA [47:41])
Transcript support: tutorial shows the fleet choices: spot vs on-demand, auto-scaling min and max; a max of 10 used to cap spend. (https://www.youtube.com/watch?v=kyaphnaCDEU [06:21-06:52])
