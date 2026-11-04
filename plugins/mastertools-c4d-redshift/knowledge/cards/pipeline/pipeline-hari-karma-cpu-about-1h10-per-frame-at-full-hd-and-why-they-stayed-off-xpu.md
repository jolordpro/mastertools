---
id: pipeline-hari-karma-cpu-about-1h10-per-frame-at-full-hd-and-why-they-stayed-off-xpu
title: Hari reports rendering a TV series on Karma CPU in full HD at about 1h10 per frame with displacement, refraction and GI, preferring its stability to XPU speed
domain: pipeline
tags: [flavien-rojon, hari, karma, karma cpu, xpu, render time, denoising, lpe, cryptomatte, deep-read]
applies_to: Houdini Karma CPU (2026)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=Dd1eYWpgpkw, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Two productions on Karma; they call it performant, robust, stable and well integrated with Solaris [24:18-24:51]. Statistics over all shots: 1h10 per frame, full HD, with displacement, refraction and global illumination, not brute force [24:51]. Denoising quality is superb if sampling is set right [25:22]. The LPE system gave cryptomattes in refraction, which they had failed to get for years [25:22]. Problems turned out to be user errors, not Karma; motion blur, groom and fur all work [25:53]. Chose CPU because XPU was not production-ready when they started; staying meant buying CPUs not GPUs and gave stability [31:28-32:31]. Number heard from a whisper transcript; check before quoting as exact.

**Use it:** Cost reference for CPU-based series rendering and an argument for stability over speed. Related: pipeline-union-splat-crowd-render-cost-and-camera-distance.
