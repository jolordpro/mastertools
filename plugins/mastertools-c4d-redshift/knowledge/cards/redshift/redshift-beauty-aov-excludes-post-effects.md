---
id: redshift-beauty-aov-excludes-post-effects
title: The Beauty AOV is the final image without post effects (bloom, glare), while the main JPEG has them baked in
domain: redshift
tags: [beauty aov, post effects, bloom, glare, streaks, baked sRGB, exr raw]
applies_to: Redshift 2024, ACES
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [comp-fix planner, CHECKS 5]
conflicts: none
---
Beauty excludes bloom and streaks, so it looks flatter than the render view [12:01, 30:00]. Post effects must be rebuilt in comp [30:32]. The main image JPEG is baked to sRGB; the EXR AOV is raw when the ACES colour workflow is set up in C4D [26:23-27:26]. Cryptomatte is a separate output [25:19].

**Use it:** In the comp plan, add bloom and glare as an explicit step; note that raw EXR is the expected state under ACES.
