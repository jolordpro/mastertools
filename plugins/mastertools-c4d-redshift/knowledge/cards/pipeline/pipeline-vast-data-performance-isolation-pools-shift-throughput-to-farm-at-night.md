---
id: pipeline-vast-data-performance-isolation-pools-shift-throughput-to-farm-at-night
title: A studio gave artists and the render farm separate compute pools on one storage system and scripted performance to move to the farm at night
domain: pipeline
tags: [vast-data, howard-marks, performance-isolation, qos, render-farm, night-scripts, effects-artist, pipeline, deep-read]
applies_to: Vast (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=lCr3vIKUpwo, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Marks describes a customer that doubled its artists: it made one pool of compute servers for artists and another for the render farm, plus a dedicated pool for a resource library, and ran scripts so that as artists go home, performance shifts from the artist pool to the farm pool [29:36-30:38]. Host Joe: a single effects artist can take down a studio by submitting a heavy job, so FX gets its own robust, segregated configuration so a roto artist does not see a stalled tablet [31:10-31:40]. Isolation lets one data pool serve every stage without separate systems and copy steps [31:40-32:11]. Joe adds that day and night scripts are normal, with the day about 8-10 hours and only about 8 hours of night in crunch, and that the same idea (night mode) applies beyond storage [32:11-32:45]. Vendor and host views, not measured.

**Use it:** when a farm shares storage with artist seats, ask for per-pool or per-queue throttling and a night profile; for a small farm the equivalent is queue priorities and night windows.
