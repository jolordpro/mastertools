---
id: broadcast-unreal-batch-render-editor-utility-movie-render-queue
title: A small editor utility widget batch-renders graphics per team through the Movie Render Queue scripting plugin
domain: broadcast
tags: [unreal, batch render, movie render queue, editor utility widget, versioning, sequencer scripting, deep-read]
applies_to: Unreal Engine 4.27 (concepts carry to UE5)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bcL001ZFHBQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Enable the Sequencer Scripting plugin to reach the render queue from Blueprint or Python [39:44-40:51]. The widget lets a user choose a graphic and teams (e.g. one match-up per pair); it counts jobs from the arrays, creates one job per entry, sets name, preset, map and output filename from the options, runs the executor, then clears the queue so the same jobs do not re-render [41:22-43:29].

**Use it:** Use as the model for a versioning tool: one pick list, one job per row, queue cleared after.
