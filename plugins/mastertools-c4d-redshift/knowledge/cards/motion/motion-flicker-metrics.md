---
id: motion-flicker-metrics
title: Flicker metrics: VBench temporal flicker (mean change between frames) needs a smoothness check; warping error fails when flow is wrong; FVD is poor
domain: motion
tags: [motion, flicker, temporal, vbench, warping error, fvd, motion vectors, temporal consistency]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://arxiv.org/pdf/2508.00144, src:research-verticals]
feeds: [PLAN step 1.5 motion check, motion check]
conflicts: none
---
Pair flicker with a motion-smoothness check so real motion is not punished.
Redshift writes exact motion vectors, so warping with them removes the flow error (proposal).
Merged from `ai-models-flicker-metrics-vbench-warping`: Pair VBench flicker with a motion-smoothness check so real motion is not punished. Warping error is weak when flow is wrong or the frame is blurred. Redshift writes exact motion vectors, which would remove flow error (unverified).

**Use it:** check flicker on the draft by warping with the motion-vector pass, then diff.
