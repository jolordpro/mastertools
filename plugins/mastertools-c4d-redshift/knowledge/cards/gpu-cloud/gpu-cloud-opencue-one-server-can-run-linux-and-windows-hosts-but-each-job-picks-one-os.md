---
id: gpu-cloud-opencue-one-server-can-run-linux-and-windows-hosts-but-each-job-picks-one-os
title: OpenCue (2020): one Linux server can drive Windows and Linux render hosts, but with no drive mapping a job must target a single OS because paths are sent as written
domain: gpu-cloud
tags: [opencue, windows, linux, paths, mixed-farm, deep-read]
applies_to: OpenCue 0.4.55 (Windows in beta), ASWF Open Source Day 2020
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=fnbRcTeKirw, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Windows support moved from alpha to beta during the year; Imageworks already ran Windows hosts in production, e.g. Unreal on Windows and another tool on Linux for the same show, with jobs tagged by OS [02:07, 19:25-19:56].
Caveat from Brian Cipriano: no drive-mapping concept, so submission paths go to the host as Windows or Linux strings and a job has to pick one platform; fixing it was a roadmap item [38:38-40:12].
The host agent (rqd) just has to reach the server, wherever it runs [39:09].

**Use it:** on a mixed Mac/Windows/Linux farm, expect to maintain separate path styles per job type or add a path-translation step.
