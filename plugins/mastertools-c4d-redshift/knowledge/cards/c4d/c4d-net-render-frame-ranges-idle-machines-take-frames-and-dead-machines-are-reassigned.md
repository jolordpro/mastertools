---
id: c4d-net-render-frame-ranges-idle-machines-take-frames-and-dead-machines-are-reassigned
title: Legacy C4D Net Render splits frames into contiguous ranges per machine, an idle machine takes frames from others, and frames from a lost machine are re-assigned
domain: c4d
tags: [net render, frame ranges, work sharing, image sequence, save project with assets, mac, pc, deep-read]
applies_to: Cinema 4D R13-era Net Render (video 2011)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=09hP2XAi0Rk, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
With three clients and 90 frames each got a range (0-30, 31-60, 61-90); a machine that finishes first pulls frames from the others' ranges [10:28-11:31, 13:04].
If a machine crashes or is stopped, the server moves its frames to another machine [00:36, 12:33].
Render as an image sequence (IM sequences), not a movie, so single frames can go to different machines [07:22].
First Save Project (with Assets) so textures sit in a tex folder beside the scene [07:53-08:23].
Mixed Mac and PC: keep names under 32 characters, no special characters or spaces (use underscores), and use image sequences for movie textures rather than QuickTime or AVI [20:21-20:53].

**Use it:** Same rules still hold for any farm: contiguous chunks, image sequences, collected assets, safe file names.
