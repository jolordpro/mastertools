---
id: pipeline-sanity-check-and-breakdown-import-save-days-of-lost-work
title: Automated sanity checks and importing the production breakdown list into each shot keep a bad file from wasting days
domain: pipeline
tags: [sanity check, breakdown list, asset import, automation, exporter, pipeline tools, cube creative, deep-read]
applies_to: Blender 2.7x (2018)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=4R8PduY_vV4, src:yt-transcripts]
feeds: []
conflicts: none
---
Cube Creative's head of R&D [19:24-22:30]. Layer artists start from a scene already populated from the assistant production manager's breakdown list, so assets are imported automatically. They ported and strengthened a sanity check: when automated steps are chained, a small mistake found days or hours later breaks everything downstream, so the check tries to catch it early. Because Blender files are binary, they wrote data exporters and importers to hand data between tasks and to Substance and Nuke. They also wrote small tools for instancing particles on surfaces and painting density. Wish list: a software-agnostic asset manager and a smooth Blender-Substance bridge.

**Use it:** The platform's scene checks map directly onto this: run a sanity check at hand-off between tasks, and populate shots from the breakdown list.
