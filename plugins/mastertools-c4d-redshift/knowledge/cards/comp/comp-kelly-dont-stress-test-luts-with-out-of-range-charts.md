---
id: comp-kelly-dont-stress-test-luts-with-out-of-range-charts
title: "Cullen Kelly no longer stress-tests LUTs on extreme colour charts; he feeds the contextual input the LUT was designed for"
domain: comp
tags: [cullen-kelly, lut, stress test, testing, show lut design, clipping, polish, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster]
feeds: [comp, shakedown]
conflicts: none
---
Stress-test charts feed values the LUT never expects, which breaks the first rule of LUTs: feed it what it expects [30:15-30:47]. The test can cut both ways: show faults that never matter on real footage, or pass a LUT that fails on a proper image [32:51-33:22]. His standard: every valid colour and luminance value the LUT should receive must give a sensible output, tested with real in-space images; he will only accept LUTs from sources he already trusts, and says building one properly means knowing how to design without needing a stress test [31:17-32:51].

**Use it:** QC a look LUT with in-gamut footage across the full legal range, not with a chart outside the working space.
