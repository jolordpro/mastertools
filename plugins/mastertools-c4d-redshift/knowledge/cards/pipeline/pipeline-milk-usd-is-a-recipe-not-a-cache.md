---
id: pipeline-milk-usd-is-a-recipe-not-a-cache
title: Milk treats USD as a recipe for assembling heavy caches, not as the place to store them
domain: pipeline
tags: [milk vfx, usd, alembic, recipe, non-destructive, composition, deep-read]
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
Enrico (co-head of VFX, Milk VFX; surname not caught). Alembic and FBX are efficient static snapshots that force stitching in a linear pipeline (2022-23 state) [05:38-06:42]. The move to USD was for parallel, non-destructive composition. His line: USD is built for dynamic composition, not for heavy caches; it stores instructions on how caches are built so the recipe can be altered at any pipeline step [07:13-08:15]. Alembic and FBX stay for legacy, rigging and animation needs [05:38].

**Use it:** Same logic suits a render platform: keep scene files light and point to caches.
