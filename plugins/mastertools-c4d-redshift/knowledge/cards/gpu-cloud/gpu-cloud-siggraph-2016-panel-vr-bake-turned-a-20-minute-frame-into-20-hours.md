---
id: gpu-cloud-siggraph-2016-panel-vr-bake-turned-a-20-minute-frame-into-20-hours
title: Kevin Bailey: baking the movie-quality World Trade Center rooftop for VR turned 20-minute film frames into 20-hour bakes
domain: gpu-cloud
tags: [vr, baking, 360, render time, atomic fiction, the walk, siggraph 2016, deep-read]
applies_to: VR bake of film assets, 2016
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=hIxnygxsdmc, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
For the VR piece after The Walk, Atomic Fiction made a low-res version of the rooftop and baked the high-fidelity lighting into it. Frames that took 20 minutes to render for the film took 20 hours to bake because the result must hold from every angle [17:47-18:19]. Bailey uses this to say VR that lives up to 'reality' needs far more compute; the Microsoft panelist adds that 4K/360 raises storage by petabytes [16:43].

**Use it:** use as a ratio when sizing 360, light-bake or multi-angle jobs: all-angle results can cost about 60 times a single-camera frame (20 hours vs 20 minutes) in this one example.
