---
id: pipeline-splat-shiny-objects-need-full-sphere-coverage
title: Matte objects tolerate a handheld pass; shiny ones need every viewing angle or they show heavy artifacts
domain: pipeline
tags: [gaussian splat, coverage, shiny, turntable, drone, trees, light field, deep-read]
applies_to: Gaussian splat capture
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=QW8ec3qquHA, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Matte scans forgive gaps, so handheld at changing heights and angles is quickest [06:33]. Shiny objects fail where coverage is missing because the trainer cannot interpolate between glare angles; think of it as a light field and cover the full sphere [06:33-07:06, 10:42].
For complex shiny items he uses a mechanical (not motorised, which is slower and for smaller objects only) dual-axis turntable that keeps track of covered angles, then fills gaps handheld [08:08-09:40, 11:12]. For trees, a drone flight pre-planned (he built a Houdini tool using satellite lidar), since abrupt manual flight breaks reconstruction and yields no splats [12:45-13:49].

**Use it:** coach note for any scan: log which angles were covered; shiny surfaces are the failure case.
