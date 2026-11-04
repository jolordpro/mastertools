---
id: gpu-cloud-stacking-small-machines-has-overhead-and-diminishing-returns
title: Adding render nodes never multiplies speed: network overhead, admin and a flattening curve cut the gain
domain: gpu-cloud
tags: [render farm, scaling, overhead, network, mac mini, single frame, diminishing returns, switch ports, deep-read]
applies_to: Blender Cycles, Apple M1 era (2022)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NktbQIDHvAA, src:yt-transcripts, https://www.youtube.com/watch?v=1Gtp3BjlTjY]
feeds: [estimator]
conflicts: none
---
James (not a vendor) reasons from Blender Open Data scores (M1 GPU about 212, M1 Ultra about 1043, higher is better, so about five minis match one Ultra before overhead) [04:11-05:16]. Overhead comes from moving data over the network and from software support [05:49]. Extra costs per node: power, space, cabling, a switch with enough ports (home routers often have four) [06:20-07:22], upkeep and updates on every machine [20:00].
For a single frame, going from 1 to 2 machines nearly halves the time, then each added machine saves less while cost keeps rising, a knee in the curve [17:52-18:54]. For animation, extra nodes help until nodes exceed frames (250 nodes for 250 frames, the 251st is idle) [18:22].
Prices and scores are 2022 and Australian; only the shape of the argument is lasting.

**Use it:** the estimator should not assume linear farm speed-up; model a per-node overhead and cap useful nodes at frames in the job.
Transcript support: first frame on a second node is slow because the project is transferred; Sony adds CPU start-up per frame [kACWEs-XJcI 18:12] (https://www.youtube.com/watch?v=1Gtp3BjlTjY [15:37-16:38])
