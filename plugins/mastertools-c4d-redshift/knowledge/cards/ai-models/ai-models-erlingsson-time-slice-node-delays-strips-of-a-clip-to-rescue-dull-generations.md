---
id: ai-models-erlingsson-time-slice-node-delays-strips-of-a-clip-to-rescue-dull-generations
title: "Erlingsson's time-slice node cuts a video into strips at any angle and delays each by a set number of frames, a cheap glitch pass for flat generations"
domain: ai-models
tags: [ingi erlingsson, comfyui, time slice, slit scan, video effect, glitch, scale slice, nodes, polish, ingi-erlingsson, deep-read]
applies_to: ComfyUI
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=4xS4LOn3CTE, src:yt-transcripts, src:polish-roster]
feeds: []
conflicts: none
---
He describes the effect as slit-scan: slice the clip into a number of slices (vertical, horizontal or any angle) and offset each by a number of frames, one or two or more [51:00-51:31]. Parameters can be randomised, or reversed with negative numbers; two nodes can be chained at opposing angles to get squares instead of lines [51:31-52:01]. A dual node mixes two videos (fire and ice) [53:06].
It uses almost no GPU and is nearly instant [11:46]. His use: when a piece is 'okay but no soul', run it through this and it often comes alive [52:01-53:36].
A sibling 'scale slice' enlarges the middle instead of offsetting; set the slice count near the pixel count and it gives a very smooth warp [53:36-54:07].

**Use it:** Keep a slit-scan style delay pass in the toolbox for rescuing flat motion; test with slice counts from a handful up to near pixel count.
