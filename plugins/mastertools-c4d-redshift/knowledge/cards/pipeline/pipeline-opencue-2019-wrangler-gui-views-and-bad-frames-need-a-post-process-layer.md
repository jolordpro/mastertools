---
id: pipeline-opencue-2019-wrangler-gui-views-and-bad-frames-need-a-post-process-layer
title: OpenCue (2019): the GUI has artist and wrangler views with plug-in panels and log search; black or bad frames are not caught automatically, so add a post layer that checks and requeues
domain: pipeline
tags: [opencue, wrangler, bad frames, black frames, log streaming, post process, python api, siggraph 2019, deep-read]
applies_to: OpenCue 2019
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=0gXT3sntiFg, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Asked about frames that come out black (a Blender complaint), the answer was that nothing is built in; add a post-process layer that checks outputs and uses the Python API to resubmit or retry frames [39:04-39:34]. The GUI has an artist view and a render-wrangler view with tools to drill into where things are slow or wrong, and each panel is a small plug-in [41:48-42:50]. The log panel streams the selected task with a basic text search; no regex alerts [52:55]. Metrics are basic; the speaker pulled history-table data into pandas for analysis [38:31, 48:41]. The GUI does not load a full 100,000-node list by default; use search and tree views [47:37].

**Use it:** for the platform: a post-render check of the first and last frames (black, NaN, wrong size) before marking a job done is a gap even mature farms leave to scripts.
