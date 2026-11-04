---
id: c4d-python-aov-api
title: Python reads and writes Redshift AOVs through redshift.RSAOV, FindAddVideoPost, RendererSetAOVs and RendererGetAOVs
domain: c4d
tags: [python, aov, redshift, rsaov, videopost, render settings]
applies_to: C4D 2023-2025 threads
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://developers.maxon.net/forum/post/70800, https://developers.maxon.net/forum/post/70802, src:research-gaps-deep]
feeds: [PLAN 0.2]
conflicts: none
---
Get the Redshift video post with FindAddVideoPost(renderdata, redshift.VPrsrenderer), then set or read the AOV list. The forum threads are 2023-2025 on C4D 2025; a fully documented Redshift Python API was still awaited, so retest on 2027.

**Use it:** retest each call on the target C4D before depending on it.
