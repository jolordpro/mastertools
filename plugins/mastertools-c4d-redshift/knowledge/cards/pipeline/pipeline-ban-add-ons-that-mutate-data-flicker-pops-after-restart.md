---
id: pipeline-ban-add-ons-that-mutate-data-flicker-pops-after-restart
title: DillonGoo banned add-ons that change data on the fly after a restart after a crash caused single-frame hair pops among 12,000 frames
domain: pipeline
tags: [cody winchester, dylan goo, dillongoo studios, blender conference 2024, add-on, flicker, hair pops, restart, render error, camera keys, deep-read]
applies_to: Blender
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aDsyNfISVLA, src:yt-transcripts]
feeds: [shakedown]
conflicts: none
---
Winchester [38:08-39:11]: one add-on deformed the character by camera angle with drivers; crashes made the render restart, and the first frame after restart had the wrong state, so the hair popped on about 20 frames out of 12,000, nearly impossible to find. They rebuilt the same effect with geometry nodes, which is fast and stable [25:00-26:02].
Rule: limit tools that change data dynamically; if you must, write your own so you can fix it. Hacky tools are fine when you own them [42:22].

**Use it:** scene check: flag render-time scripts and drivers that depend on state, and check frames after any farm restart.
