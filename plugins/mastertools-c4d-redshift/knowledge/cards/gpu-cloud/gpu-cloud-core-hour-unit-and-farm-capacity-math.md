---
id: gpu-cloud-core-hour-unit-and-farm-capacity-math
title: Core hours = cores times hours of a frame; his example 89 machines x 20 cores is about 300,000 core hours a week
domain: gpu-cloud
tags: [core hour, farm capacity, on-prem, render capacity, weekly capacity, queue planning, deep-read]
applies_to: any farm
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=FStbueCu1f8, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Core hour: cores given to a frame times hours it runs. A 20-core machine at 1 h on one frame = 20 core hours; two 10-core frames at 1 h each = 10 each, same 20 for the box [05:13-06:14]. Capacity example: 89 machines x 20 cores, 24/7 = about 300,000 core hours a week [12:24-12:56]. A 365,000 core-hour shot spread over about 3 weeks as roughly 2,000 / 46,000 / 138,000 (the bulk lands in the final week). One shot fits; ten staggered shots over 10 weeks overflow unless the early tests are trimmed [12:56-14:29]. Assumed 4-8 core jobs for animation tests, 8-core for FX sims, 16 for lighting.

**Use it:** Plan farm load as core hours per week and expect the last week of a shot to hold the biggest chunk. GPU farms use GPU-hours; the logic is the same.
