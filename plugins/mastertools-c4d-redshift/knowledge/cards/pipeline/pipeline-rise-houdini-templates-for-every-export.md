---
id: pipeline-rise-houdini-templates-for-every-export
title: Run every app's exports through a headless Houdini template so one set of nodes builds the final USD layers
domain: pipeline
tags: [rise, hython, maya export, usd, extract template, speedtree, publisher, flowpipe, deep-read]
applies_to: Houdini, Maya, USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jpbMbafS9FY, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Rise animation stays in Maya. The Maya publisher exports plain point-position and normal caches, then a background Houdini process builds the USD from a template hip using the same payload, variant and metadata nodes as native Houdini exports [28:34-29:36]. SpeedTree and crowd character exports use the same route [29:36-30:06].
Benefit: add a template instead of writing a plugin per app or waiting for missing plugin features [30:06].
Tools named: Publish-it style plugin publisher, flowpipe (Python flow graphs, used to send publishes to the farm) [51:05-52:08].

**Use it:** For C4D: export simple caches and let one shared tool do the packaging and metadata.
