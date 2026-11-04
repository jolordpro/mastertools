---
id: ai-models-wan-vace-forward-and-reverse-clips-stitched-from-a-middle-frame
title: Make a transformation shot by editing a mid-frame and growing video both ways from it
domain: ai-models
tags: [wan vace, video model, transformation, reverse, stitch, flux kontext, reference frame, deep-read]
applies_to: Wan 2.1 VACE
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=o5ZqrVNoeiI, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
They picked one frame from the middle of the take where he is already a zombie, edited it with Flux Kontext, then generated two Wan VACE videos from that frame; the first was reversed to run into the frame, and the two were stitched in DaVinci Resolve [15:04-15:34]. Final colour grading hid imperfections, and After Effects kept crashing at the comp stage [15:34].

**Use it:** a generative-video pattern: lock a keyframe, generate outward in both directions, then hide seams in the grade.
