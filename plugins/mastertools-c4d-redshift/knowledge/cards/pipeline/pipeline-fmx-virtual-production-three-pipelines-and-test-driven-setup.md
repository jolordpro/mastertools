---
id: pipeline-fmx-virtual-production-three-pipelines-and-test-driven-setup
title: "FMX 2014 TD student: virtual production has three pipelines (pre, on-set, post); test small parts first, and camera tracking removed match-moving on 95% of shots"
domain: pipeline
tags: [fmx, technical-director, virtual-production, cryengine, optitrack, student, deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=8tW77BsgtPY, src:yt-transcripts]
feeds: [pipeline design]
conflicts: none
---
First speaker (name garbled in captions; a TD student) set up the pipeline for a 3D short shot with a game engine (CryEngine Sandbox) in live virtual production [02:09-03:45].
Rule: do not have one pipeline but three (pre-production, on set, post) [04:28-05:00]. Method: test-driven, pick small parts of the problem, test them, then go on set, otherwise the complexity cannot be managed [05:00-05:32].
Data flow: mocap system tracks the camera, engine renders from that camera, a live key combines it with the viewfinder image so the director sees the composite on set [06:03-06:36]. Because tracking data existed, match-moving was avoided on 95% of shots, and the same data fed post [07:07-07:38].
Also proposed a handheld app giving every department the camera, engine and key streams plus annotation, fast transmission preferred to reliable [08:08-09:40, 52:50-53:21].
Transfers to live-sports/XR: camera tracking data as the single source for on-air and post.

**Use it:** For any tracked-camera pipeline: split prep, live and post, test each piece alone, and archive the camera data for post.
