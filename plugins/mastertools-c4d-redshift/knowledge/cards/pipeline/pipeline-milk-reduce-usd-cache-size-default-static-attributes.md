---
id: pipeline-milk-reduce-usd-cache-size-default-static-attributes
title: Long shots made USD caches too big; Milk set attributes that don't change per frame to defaults before caching
domain: pipeline
tags: [milk vfx, usd, cache size, configure sop, default values, time samples, deep-read]
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
Enrico (co-head of VFX, Milk VFX; surname not caught). Creature caches were fine on short frame ranges but on long scenes of Surviving Earth files grew too heavy to manage. Fix: a configure node before caching that sets attributes needing no per-frame evaluation to default, which sped up caching and cut size [24:19-24:50]. Departments get two exchangeable steps in their export template (a sanitize and an ingest) so a groom is split into beauty, proxy and guides [23:48].

**Use it:** Check for time-sampled attributes that never animate when a cache is unexpectedly large.
