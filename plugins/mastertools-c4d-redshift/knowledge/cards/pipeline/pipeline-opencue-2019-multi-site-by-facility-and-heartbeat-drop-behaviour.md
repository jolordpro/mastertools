---
id: pipeline-opencue-2019-multi-site-by-facility-and-heartbeat-drop-behaviour
title: OpenCue (2019): several Cuebots can serve separate facilities, a missed heartbeat drops a node from the pool in about a minute, and finished-job data moves to history tables
domain: pipeline
tags: [opencue, multi site, facility, heartbeat, history table, network partition, cuebot, siggraph 2019, deep-read]
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
Run more Cuebots and give each a facility; each facility operates independently, and the in-memory redesign must keep this [29:35-30:37]. Bandwidth awareness between sites is not in the scheduler [30:37]. Multiple masters share roles today because everything is database-based; the rewrite will likely have one scheduling node with others as backups [16:32-17:02]. If a node misses heartbeats the server flags it and removes it after about 30 seconds to a minute, and it is re-added when heartbeats resume; what a cut-off node does is uncertain, probably it finishes the current task and takes no more [53:27-54:32]. Finished jobs move to history tables so the primary tables stay small [31:09].

**Use it:** design notes for the platform's own worker pool: drop on missed heartbeat, re-add on return, requeue the frame.
