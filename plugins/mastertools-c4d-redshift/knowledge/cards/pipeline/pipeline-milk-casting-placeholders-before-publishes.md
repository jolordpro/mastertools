---
id: pipeline-milk-casting-placeholders-before-publishes
title: Milk 'casts' a shot as placeholders from the pipeline-step hierarchy; published layers fill the slots later
domain: pipeline
tags: [milk vfx, casting, shotgrid, json, pipeline step, placeholder, scale, deep-read]
applies_to: Houdini Solaris, ShotGrid (Milk VFX, FMX HIVE 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=XfMp13jOSxE, src:yt-transcripts]
feeds: []
conflicts: none
---
Enrico (co-head of VFX, Milk VFX; surname not caught). The old system failed on an eight-episode series with 70-plus creature assets and variants [13:58-14:30]. Block one (CG supervision): ShotGrid is the database; anything published as USD can be cast against the default pipeline-step hierarchy, each publication tied to a task. Casting makes a template of what must go in, not any version; it is a JSON description stored as a ShotGrid attribute through their MBrew API [14:30-16:33]. Block two runs in Houdini, with the same idea for other DCCs [16:33-17:03].

**Use it:** Plan big jobs by listing the slots first (shot, assets, cameras) and let versions fill them.
