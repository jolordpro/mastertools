---
id: pipeline-splat-sfm-reconstruction-tools-and-image-counts
title: Reconstruction (camera solve plus point cloud) is the skeleton for splats; its quality caps the result
domain: pipeline
tags: [structure from motion, colmap, glomap, realitycapture, metashape, postshot, point cloud, image count, deep-read]
applies_to: Postshot, COLMAP, RealityCapture, Metashape
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=QW8ec3qquHA, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Postshot (paid, end-to-end) does its own structure from motion, reliable but very slow above about 500 images and with a sparse point cloud [14:22-15:56]. Alternatives: COLMAP (open source, CUDA build can be awkward) with GLOMAP for global speed-up; RealityCapture (free, strong on hard surfaces); Agisoft Metashape (paid, fastest on thousands of images, trial used) [16:28-19:32].
A simple object rarely needs more than 1500 images; pre-filter longer footage (for example every second frame in Nuke) and put frames in an images folder; align, then export in COLMAP-compatible format [20:03-21:38]. Intricate items may need over 1000 images [17:29-18:00]. A bad reconstruction usually traces back to an out-of-focus capture frame [18:31].

**Use it:** the tool list is the lead; the lasting rule is to check capture focus and cap image counts before solving.
