---
id: pipeline-context-playblast-with-neighbour-shots-and-burned-in-metadata
title: Context playblasts join the previous and next shots in one MP4, and burned-in shot and frame data keeps feedback exact
domain: pipeline
tags: [cody winchester, dylan goo, dillongoo studios, blender conference 2024, playblast, burned-in metadata, feedback, ffmpeg, frame number, context, deep-read]
applies_to: Blender, ffmpeg
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aDsyNfISVLA, src:yt-transcripts]
feeds: [CHECKS, motion-critique]
conflicts: none
---
Winchester [21:49-22:51, 40:49-41:51]: a context operator finds the MP4s of the neighbouring shots from the pipeline and joins them with ffmpeg so a shot can be judged in its place. Publish playblast pushes a shot and uploads an MP4 to the edit timeline.
Burn metadata (name, frame) onto the MP4; without it reviewers ask which shot and frame. With frame numbers, notes become 'frame 1045, delay it to 1055'.
Bulk playblast of a whole project in solid or preview view is used near the end when renders are too slow [28:19-29:18].

**Use it:** every review clip should carry name, version and frame; add neighbour shots when timing matters.
