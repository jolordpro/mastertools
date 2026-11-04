---
id: lookdev-bepic-procedural-canyon-keep-curves-live-fix-cliffs-with-slope-masks
title: bEpic canyon environment: heightfield terrain driven by curves, cliffs made from steep-slope masks turned into displaced meshes, rocks placed big first
domain: lookdev
tags: [lookdev, bepic, houdini, heightfield, environment, rocks, procedural, deep-read]
applies_to: Houdini heightfield, Gaea with Labs tools
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=4D9GDZsCzy0, src:yt-transcripts]
feeds: []
conflicts: none
---
Goals: a Mars-like canyon that feels huge with a tiny rover, and fully procedural so changes stay cheap [06:48-07:49]. Terrain on Houdini heightfields, with Gaea passes for erosion and detail via Labs tools, and artist controls reusing curves with game-like handles [07:49-08:52]. Heightfields cannot hold overhangs, so cliffs are split off by a steep-slope mask and converted to displaced meshes, with final detail left to texturing and lighting [08:52-09:25]. Custom craters, sand banks in crevices and tall rocks (VDB displacement) form a small library [09:25-10:59]. Tiny rocks placed hierarchically: manual big boulders first, scatter around them, paint details, drop to settle them [10:59-12:00]. Late changes reused the first curves and a simple mesh as a deformer, fine for small changes only [12:00-12:31]. Rocks were published separately in USD for shot use [12:31-13:34].

**Use it:** For hero environments, keep the earliest curves live and split cliffs from terrain; reserve manual placement for the largest items.
