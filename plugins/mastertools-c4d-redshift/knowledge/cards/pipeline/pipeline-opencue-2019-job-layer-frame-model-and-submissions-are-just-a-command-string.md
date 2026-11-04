---
id: pipeline-opencue-2019-job-layer-frame-model-and-submissions-are-just-a-command-string
title: OpenCue (SIGGRAPH 2019 BoF): jobs hold layers, layers run a shell command over a frame range, and the server does no per-app translation, so any software can render
domain: pipeline
tags: [opencue, render manager, job layer frame, pyoutline, submission, pre and post process, auto retry, academy software foundation, siggraph 2019, deep-read]
applies_to: OpenCue 2019 (open-sourced early 2019)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=0gXT3sntiFg, src:yt-transcripts]
feeds: [CHECKS, estimator]
conflicts: none
---
Structure: a job contains layers, each layer is a command run against a frame range, and individual frames are the work units [17:39]. Submission builds a command with placeholders (frame number is the main one); nothing is translated on the server and the node receives almost exactly that command, so you need no plug-in to run any software, though host-app plugins (Maya at the time) pre-fill the command [43:23-44:27, 08:34]. The Python layer builds classes that bake to an XML job description, with a higher-level PyOutline library [45:02]. Pre- and post-processes are just extra layers [55:04]. Auto retry is built in; a kill-after-time limit is not [52:25]. A basic submit app builds linear pre-flight, render, comp chains but not a full graph [49:43].

**Use it:** a good model for the platform's own job spec: a few layers (check, render, comp) of plain commands, with frame placeholders, avoids per-app server code.
