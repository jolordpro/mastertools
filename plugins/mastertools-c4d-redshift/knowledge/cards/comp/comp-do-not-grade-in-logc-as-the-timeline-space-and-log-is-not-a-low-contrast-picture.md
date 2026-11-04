---
id: comp-do-not-grade-in-logc-as-the-timeline-space-and-log-is-not-a-low-contrast-picture
title: Two habits to avoid: LogC as the timeline colour space (it is narrower than Rec 2020 and RED gamut) and normalizing log by adding contrast and saturation
domain: comp
tags: [team-2-films, log, logc, timeline color space, bottleneck, normalize, contrast, deep-read]
applies_to: DaVinci Resolve
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=w0ubDSzEEYg, src:yt-transcripts]
feeds: [[post-composite]]
conflicts: none
---
LogC as the working space feels familiar to colourists used to camera-referred grading, but it bottlenecks the pipeline because wider spaces exist and it was designed for capture [21:21][21:51]. Normalizing log by hand with contrast and saturation is allowed if you like the result, but log is cleverly designed to extract the most from a sensor, not a "flat" picture, and an unmanaged log image on Rec 709 was never the grade's starting point [20:51][21:21]. Some log spaces (Cineon-style, LogC) take this treatment better than others [20:51].

**Use it:** shakedown warning for footage workflows: confirm the timeline space is a scene space, not a camera space.
