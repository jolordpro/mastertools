---
id: gpu-cloud-sheepit-free-volunteer-farm-with-points-queue-and-no-deadline-promise
title: SheepIt is a free volunteer render farm for Blender: a points queue, no promised wait, frames or tiles split across strangers' machines
domain: gpu-cloud
tags: [sheepit, blender, render farm, volunteer, credits, queue, 2025, deep-read]
applies_to: Blender
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=q7wAwtQFpkI, src:yt-transcripts]
feeds: [[estimator]]
conflicts: none
---
InspirationTuts (2025, secondhand summary of the service): started 2007-08; by mid 2025 it had rendered over 460 million frames across more than 1 million projects [00:33][01:05][02:08]. Jobs are split per frame, or per tile for a still, and sent to volunteer clients that fetch the right Blender version; machines never talk to each other, only to the server [02:39][03:11][03:42][04:13]. Submit through a web form: Blender version, frame range or still, CPU/GPU/both; outputs are deleted after about 9 days [04:43][05:46]. Queue order is by points: roughly 38 points per minute earned when rendering, about 10 per minute spent when others render for you; GPUs earn and spend about 18 times faster than CPUs; your machine renders some of your own frames first by default [06:17][07:20][07:52]. No promised speed or wait, so it is wrong for a tight deadline [07:52][08:22].

**Use it:** the estimator should treat it as "free but unscheduled"; compare paid farms' time math in gpu-cloud-render-farm-time-math-1500-frames-100-nodes. Figures are as said in the narration (V2-like second-hand); decays fast.
