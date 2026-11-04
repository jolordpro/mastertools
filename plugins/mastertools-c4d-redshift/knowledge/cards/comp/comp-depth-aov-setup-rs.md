---
id: comp-depth-aov-setup-rs
title: Redshift depth AOV: use Center Sample filter, set range with camera near/far clip, and remap the huge values in comp
domain: comp
tags: [depth, z depth, aov, center sample, clipping, normalize, comp]
applies_to: Redshift in C4D 2024, After Effects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts, https://www.youtube.com/watch?v=xwD_UPqbmCU, https://www.youtube.com/watch?v=ARykOD6lG3c]
feeds: [comp-fix planner, CHECKS]
conflicts: [comp-dof-in-post-by-default-in-camera-for-glass-and-extreme-depth]
---
Depth pass settings: direct output, filter type Center Sample for non-antialiased depth, use camera near and far clipping to set the range [1:03:26-1:04:31].
Values are distance in scene units (cm): a pixel 3 m away holds 3000, so the image looks white until black and white points are set; view it raw, not through the display transform [1:12:23-1:13:30].
The depth cannot see through glass, and the camera clip planes are tied to the near and far range; the trainer asks Redshift to decouple them [1:05:01-1:05:32].

**Use it:** a depth-for-comp check validates filter, clip range and that the pass is not display-transformed.
Transcript contradicts: Chad (2018) recalls Min Depth as the depth AOV filter for post DOF; card says Center Sample. Both agree: no anti-aliasing. Low confidence, ledger decides (https://www.youtube.com/watch?v=ARykOD6lG3c [13:35-14:07])
