---
id: pipeline-fast-hat-films-dummy-frame-count-clip-for-vfx-shots
title: Make editorial frame counts reliable by rendering one long black clip counting from 1 and pasting it over each VFX shot, with a second count track for dissolves
domain: pipeline
tags: [fast hat films, editorial, vfx count, frame count, avid, timecode burn, vfx numbers, dissolve overlap, deep-read]
applies_to: Avid Media Composer (method general)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=iuPgX-24TU0, src:yt-transcripts]
feeds: [[shakedown, CHECKS]]
conflicts: none
---
Fast Hat Films (editor, series part 3 of 5, low). Problem: a timecode-burn effect on top of a stack of tracks reads the wrong layer for composite temp effects [00:33-01:35]. Method: new dummy sequence, black generator clip, burn effect set to frames, local count starting at 1, positioned bottom right where the VFX number sits; mix down to one video file counting to roughly 11,000, far past any shot length; on a "VFX count" track paste that clip over each VFX shot in/out so the count starts at 1 on the shot's first frame (his example shot counted to 204); crop it to the corner [01:35-04:44]. Dissolves between two VFX shots overlap, so add a second count track and stack two counts; he says three, four or five tracks are fine [05:49-06:49]. Order of tracks: VFX notes, then count tracks. It is tedious and usually an assistant's job, so diligence matters [04:44].

**Use it:** Turnover rule for comp and motion hand-offs: shot handles and frame counts come from a generated counter, not a live effect; call out overlaps.
