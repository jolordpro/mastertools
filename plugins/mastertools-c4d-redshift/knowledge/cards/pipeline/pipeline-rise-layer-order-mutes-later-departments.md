---
id: pipeline-rise-layer-order-mutes-later-departments
title: Mute every layer later in the department order when you work on yours, so downstream edits cannot interfere
domain: pipeline
tags: [rise, usd, layer order, muting, shot template, layout, departments, shot info prim, deep-read]
applies_to: USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jpbMbafS9FY, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
Rise defines a department order for shot layers. Loading a shot to work on layout mutes all layers above that order (including an existing layout layer), keeping only the match-move camera and the project template layer [24:26-24:57]. The template gives every shot the same base hierarchy [24:57].
Each exported layer also gets a shot-info prim storing metadata and a relationship to every prim it modifies, so you can see which layer made which edit in a complex stage [27:33-28:04]. Intermediate pushes can go to the next department only, e.g. model changed before shading is updated, before the full push to the shot [1:03:52]. A reject option removes a pushed layer with a message [1:03:20].

**Use it:** Handoff checklist: order of departments, what gets muted, who may push to the shot.
