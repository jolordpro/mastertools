---
id: pipeline-milk-environment-library-copy-per-project-and-texture-res
title: Environment assets are composed from a library, made unique to the project, with texture resolution control, leaving the library untouched
domain: pipeline
tags: [milk vfx, environment, library, variants, texture resolution, copernicus, lockerbie, deep-read]
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
Enrico (co-head of VFX, Milk VFX; surname not caught). For Lockerbie (2025) they needed fast sourcing from a library [30:13-30:44]. A composer node controls composition arcs and variants, offers shader bundles and Copernicus-based texture edits, and sets texture resolution for fast previs or distant background [30:44-31:48]. When criteria are set the asset is imported as unique to the project, so the library is not changed [31:48-32:18]. A matching SOP-level copy lets artists edit and re-export to LOPs [32:18-32:50].

**Use it:** Copy-on-import protects the shared library; keep a low-res option for background dressing.
