---
id: redshift-hdr-exr-clamping-post-settings
title: For a grade-able HDR EXR turn off Redshift's colour management, LUT, colour controls and exposure; bloom, flare and streak can stay
domain: redshift
tags: [post effects, color management, lut, exposure, clamp, exr, bloom]
applies_to: Redshift in C4D (2021), 16-bit float EXR
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=7uY4-bPvRKs, src:yt-transcripts]
feeds: [redshift, CHECKS, comp-fix planner]
conflicts: none
---
A render saved with the view transform on has it baked like a LUT and clamped at 1, so exposure in comp can only grey or blow out the highlights even in an EXR [16:14-17:16].
Uncheck Redshift Post Effects, Color Management and render linear; the trade is that the view looks blown out in the render view [14:43-15:44].
Zak says LUT, colour controls and exposure also clamp, but bloom, flare and streak do not [37:38-38:57]. 16-bit float with a zip compression kept the data [15:44-16:14].

**Use it:** a pre-submit check can flag colour management, LUT or exposure enabled in Redshift post when the output is meant for comp.
