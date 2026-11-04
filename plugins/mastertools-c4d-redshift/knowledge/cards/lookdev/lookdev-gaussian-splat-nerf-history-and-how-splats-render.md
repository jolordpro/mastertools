---
id: lookdev-gaussian-splat-nerf-history-and-how-splats-render
title: How splats work: millions of stretchable 3D ellipsoids with view-dependent colour, rendering in real time; NeRF took a day to train until Instant-NGP
domain: lookdev
tags: [gaussian splatting, nerf, instant ngp, ellipsoid, view dependent, real-time, history, education, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=KZqv3Z5rRg8, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Michael Rubloff (radiancefields.com) gives the lineage: NeRF (2020) shoots rays and samples position and view direction to colour and density, but a reconstruction took about 24 hours [05:58] [07:01]. NVIDIA's Instant-NGP (2022) cut this to seconds or minutes [07:32]. 3D Gaussian Splatting (April 2023) is rendered at real-time rates [08:03] [08:34].
His metaphor: Jackson Pollock dripping paint, but with 3D ellipsoids that stretch, layered tens of thousands to millions deep, with view-dependent colour [09:04] [09:34]. Both NeRF and splats follow capture, then structure from motion, then reconstruction [10:35].

**Use it:** Teaching pattern: explain a new technique with a painter's metaphor and a speed-up timeline (24 hours to minutes to real time).
