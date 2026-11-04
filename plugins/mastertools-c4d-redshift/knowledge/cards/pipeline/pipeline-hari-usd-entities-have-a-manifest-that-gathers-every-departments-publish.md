---
id: pipeline-hari-usd-entities-have-a-manifest-that-gathers-every-departments-publish
title: Hari's USD entities (asset, asset instance, shot group, shot) each have a manifest USD that collects every department's publish; an asset instance starts from the asset's manifest and adds shot layers
domain: pipeline
tags: [flavien-rojon, hari, usd, manifest, asset instance, shot group, set dress, fx loop, deep-read]
applies_to: USD, Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=Dd1eYWpgpkw, src:yt-transcripts]
feeds: []
conflicts: none
---
Four entities: assets (characters, props, sets), asset instances (an asset prepared for use in a shot), shot groups (multi-shot lighting and layout over a sequence), shots [03:37-05:44, 08:19-09:21]. Each has a master USD called the manifest that gathers the department publishes: modelling geometry, groom, lookdev shaders and assignments, render settings, rig controls, animation cycles [04:09-05:44]. A prop (a lamp) can carry an FX cache of insects looping around the bulbs and light-link data [06:15]. A set holds a set-dress layer, an FX river cache of 500 frames looping over 10,000 frames inside USD, lookdev overrides, instanced trees, and light rigs for day and night [06:45-07:49]. An asset instance manifest always starts from the asset and adds animation, groom and automatic eye-light layers [07:49-08:50]. Python API exposes the production data [04:09]. Aim: one structure for series and features [09:21].

**Use it:** Reference layout when designing publish/assemble steps. Related: pipeline-union-manifest-per-shot-versioned-usd.
