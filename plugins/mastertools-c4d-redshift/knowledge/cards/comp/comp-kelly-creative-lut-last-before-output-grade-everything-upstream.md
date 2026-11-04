---
id: comp-kelly-creative-lut-last-before-output-grade-everything-upstream
title: "Cullen Kelly puts the look LUT last, just before the output transform, and does all grading upstream of it"
domain: comp
tags: [cullen-kelly, lut, node order, output transform, look, color management, polish, deep-read]
applies_to: DaVinci Resolve, any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=dSYTWErq0Vw, src:yt-transcripts, src:polish-roster]
feeds: [comp, coach]
conflicts: none
---
With a creative LUT and sound colour management, the look goes as the very last thing before the display/output transform [26:36-27:06]. Asked what grading to do after the LUT or after the display transform, his answer (a viewer gave it first) is none [28:08-29:13]. The only thing that belongs at the tail is a display adaptation such as a web-viewing transform for YouTube, which is not grading. All grading is done upstream at clip level, so the LUT acts as the glue over everything.

**Use it:** Node order rule for comp and finishing: grade, then look LUT, then output transform; nothing creative after the look.
