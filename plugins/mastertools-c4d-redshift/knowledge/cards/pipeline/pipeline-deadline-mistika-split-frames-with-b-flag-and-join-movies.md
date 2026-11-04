---
id: pipeline-deadline-mistika-split-frames-with-b-flag-and-join-movies
title: Mistika Workflows on Deadline: the farm parameter -b sets frames per machine, and a Join Movies node merges the segments
domain: pipeline
tags: [mistika, deadline, render farm, frames per machine, join movies, prores, deep-read]
applies_to: Mistika Workflows with Deadline
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=drO16Y4dcRo, src:yt-transcripts, https://www.youtube.com/watch?v=gqpVdX8k2xU]
feeds: []
conflicts: none
---
SGO's tutorial: in Preferences, Render Farm, pick Deadline and check the paths; Deadline Monitor and Worker must be running [00:09]. On a transcoding node turn on the render farm option and put -b 100 in Farm params to write 100 frames per machine [00:40]. A 145-frame clip gave two movies, frames 0-99 and 100-144, and a Join Movies node merges them into one 145-frame file [01:43]. With several workers on both node and queue, one Deadline job per worker appears [02:15].

**Use it:** shows the chunk-then-join pattern for post transcodes; check the last chunk is the remainder, not a duplicate.
Transcript support: different SGO tutorial on Mistika Workflows: watch-folder start, per-department colour-space versions; same product family (https://www.youtube.com/watch?v=gqpVdX8k2xU [00:09])
