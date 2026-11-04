---
id: pipeline-usd-unreal-round-trip-gaps-in-5-3-and-blender-basic-export
title: Booth: Unreal 5.3 USD export did not fully round-trip back to Solaris; Blender's USD I/O was basic; MaterialX moves differently per app
domain: pipeline
tags: [paul booth, super motion collective, usd, solaris, houdini hive, unreal 5.3, blender, materialx, round trip, atlock, lighting plugin, deep-read]
applies_to: Unreal 5.3, Blender (2024)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=bwkCfp6G-F8, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Booth [24:43-25:52, 28:40-32:25]: lighting in Unreal with a plugin (named 'atlock' in captions), but re-saving a changed USD stage from 5.3 did not always match coming back; he said 5.4 reportedly fixed it and had not tested it. Blender has basic USD import/export (the Nvidia branch is better); artists there can export model and materials USD. MaterialX is visible in many apps but not all read it the same; Substance exports material USD well.

**Use it:** verify a round trip with a test asset before promising USD between C4D, Houdini and Unreal.
