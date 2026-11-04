---
id: gpu-cloud-irender-2x4090-300-hd-frames-33-95-s-per-frame-15-points-per-hour
title: iRender's own benchmark (Jul 2026): server 4S with 2x RTX 4090 rendered 300 Full HD Redshift frames at about 33.95 s per frame; 15 points per hour
domain: gpu-cloud
tags: [irender, rtx 4090, redshift, benchmark, points, per hour, cloud workstation, deep-read]
applies_to: iRender GPU server 4S, Cinema 4D + Redshift, video 2026-07-28
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=RsG8DYWmlM8, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Machine: AMD Threadripper Pro, 2x RTX 4090 (24 GB each), 256 GB RAM, 2 TB NVMe, Windows 10, 15 points per hour; booking 3-hour blocks saves 10%; first top-up shown with a 100% bonus (promotions change) [01:09-01:44, 08:57-09:31].
Boot under 2 minutes; licences activated through iRender's licence manager, and the licence must be disconnected before leaving [02:15-03:00, 07:49].
Scene: 1920x1080, 30 fps, 300 frames, threshold 0.005, default bucket and system settings; Redshift split work across both GPUs without setup [03:00-04:43]. Result 33.95 s per frame average [09:31]. Our arithmetic (not stated): 300 x 33.95 s is about 2.8 hours of machine time, so about 3 hours billed.
Marketing video from the vendor; point-to-dollar rate not given.

**Use it:** Hourly cloud estimate: frames x seconds per frame / 3,600 x hourly rate, then round up to the booking block.
