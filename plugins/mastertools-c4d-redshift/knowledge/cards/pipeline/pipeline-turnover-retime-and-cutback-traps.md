---
id: pipeline-turnover-retime-and-cutback-traps
title: Shots with re-speeds or cutbacks break the automatic handle method, so roll out the handles by hand
domain: pipeline
tags: [jack the avid assistant, retime, re-speed, cutback, decompose, handles, sub clip, overlap, deep-read]
applies_to: Avid Media Composer (principles apply to any editor)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=MoR7ncjN9Ds, src:yt-transcripts]
feeds: []
conflicts: none
---
On a re-speed shot (filmed at 120 fps, played back slower), automatic handle creation adds frames before the speed change; the vendor applies the speed first and would run out of real handles [20:50, 21:22].
Fix: roll the trim out by 8 frames each side with the re-speed in place, then match-frame head and tail from the unspeeded media and sub-clip that [21:53].
Cutbacks (two effects shots returning to the same take) can overlap in their handle ranges so the tool merges or duplicates them; run the tool in two passes [22:56, 23:27].
Check names and lengths after the run; they should line up with the cut [23:57].

**Use it:** Flag retimed and repeated-source shots as special cases in a handoff checklist and verify handle length against the post-retime frame count.
