---
id: comp-luts-for-colour-management-are-approximations-made-for-portable-monitors
title: A LUT stores a simplified conversion so a portable monitor can run it live; CSTs and ACES transforms are the exact maths and a better tool for the grade
domain: comp
tags: [team-2-films, lut, color management, set monitoring, cst, aces transform, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=w0ubDSzEEYg, src:yt-transcripts]
feeds: [[post-composite, shakedown]]
conflicts: none
---
Team 2 Films: LUTs trade accuracy for convenience, which suits on-set viewing; not all are made well and titles or notes may not describe what they do [07:52][08:23][08:54]. CST or ACES transforms do the real mathematical transformation with refining controls, but need setup per clip (templates help) [08:54][09:24]. With LUT workflows, primary corrections are often made camera-referred (before the LUT) and secondaries display-referred (after it) because of the LUT's limits, but grading tools react differently per space, so a grade made in LogC does not transfer to a clip in RED's space [11:27][11:58]. Scenario view: using a LUT is acceptable; remember each camera space needs its own vetted LUT [21:51].

**Use it:** a rule for dailies and look files: use LUTs for monitoring, and base the delivered grade on transforms.
