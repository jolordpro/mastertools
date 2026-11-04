---
id: gpu-cloud-opencue-pyoutline-builds-render-jobs-from-code-one-layer-per-houdini-node
title: OpenCue job files are XML/YAML but studios build jobs with pyoutline; at Imageworks each node in a Houdini graph becomes a layer and wires become dependencies
domain: gpu-cloud
tags: [opencue, pyoutline, houdini, dependencies, monitoring, grafana, ben-dynes, deep-read]
applies_to: OpenCue 0.4.55, ASWF Open Source Day 2020
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=fnbRcTeKirw, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Ben Dynes: outline files describe tasks, layers and dependencies, but nobody writes them by hand; pyoutline creates them in code, and custom UIs sit inside each DCC (Nuke, Houdini) [11:58-13:35].
In Houdini, each node of the graph is a separate layer and the flow between nodes is a layer dependency [13:35-14:07].
The Python API is light: thousands of jobs can be queried in seconds, so they run monitoring scripts, a web job viewer, and time-series reports in rrd and Grafana by show and department. These feed long-term farm-size forecasts [14:07-15:42].

**Use it:** a C4D/Redshift submit tool should map shot passes to layers with dependencies (render before comp) and log every job so capacity planning has data.
