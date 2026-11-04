---
id: gpu-cloud-irender-8x4090-360-frame-redshift-benchmark-78-minutes
title: iRender vendor benchmark (Aug 2026): 360 frames of a C4D + Redshift fluid/particle scene at 1080p took 1 h 18 min on 8 RTX 4090, about 71 credits
domain: gpu-cloud
tags: [irender, rtx 4090, 8 gpu, redshift, cloud workstation, benchmark, billing, deep-read]
applies_to: iRender 9S machine: 8x RTX 4090 24 GB, Threadripper Pro 5975WX, 256 GB RAM (Aug 2026)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=EuUroqBPANo, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Vendor video, so best case. Redshift 1920x1080, 360 frames: 360 of 360 in 1:18:13, late frames about 14-15 s each; all eight GPUs sat at 97-100 percent [01:39-03:24]. Usage 1 h 21 min, about 71 IR (credits) because billing runs while the machine is on and stops when you shut it down [03:24]. Output 360 files, about 890 MB. Drives: C system, X software, Y output, Z input; only Y and Z are persistent, C is kept for the next session but not for long-term storage [03:00-03:24]. Gateway choice affects latency, not render speed [00:32]. A March 2023 iRender video on 6x RTX 4090 reports a total of 1 h 20 min 8 s for a scene whose frame count it never states, so it gives no per-frame rate [9mcDxU9P2Hs 03:09].

**Use it:** Rental-workstation cost = hours on x hourly rate; move frames to Y and shut down before sleeping. See existing iRender cards for the rate.
