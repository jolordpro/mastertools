---
id: pipeline-farm-same-app-version-on-all-nodes
title: Run the same render-app version on every node; mixed versions made the farm hang on a version check
domain: pipeline
tags: [kent trammell, cg cookie, render farm, version mismatch, blender, nodes, deep-read]
applies_to: Blender 2.6x
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=FNhUnPWzVaw, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
His nodes ran Blender 2.67, 2.68 and 2.66; the first test rendered fine, but a later job kept hanging on a version check until he installed the same release (2.68a) on all machines [54:08-54:40].

**Use it:** pre-flight check for any farm or cloud job: same C4D build, same Redshift build and same plugin versions across machines, before queueing a sequence.
