---
id: broadcast-xpression-2018-keyframes-scene-director-pause-cue-and-package-export
title: XPression (2018): animate on a keyframe timeline, hold with a pause event, and move work between machines with a package export
domain: broadcast
tags: [ross xpression, scene director, key graph editor, pause event, reverse, export package, incremental save, project file corruption, deep-read]
applies_to: Ross XPression (2018)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=VZO7A0F7pZ0, src:yt-transcripts]
feeds: []
conflicts: none
---
Animation lives on a scene timeline (100-frame window here). Keyframe position of a logo over 12 frames, then fade a box group between frames 12 and 25; use a spline instead of linear for a natural ramp [32:15-36:58]. Add a pause event in a scene director clip at frame 25 so a take stops there, and a second take plays the reverse [36:58-38:32].
Saving: use incremental saves (version 1, 2, 3) because XPression can occasionally corrupt a file [39:04]. Moving to another machine: export package, include font files, optional password, which relinks everything [39:04-39:34].

**Use it:** Adopt incremental saves and packaged export for any graphics system that holds a project file.
