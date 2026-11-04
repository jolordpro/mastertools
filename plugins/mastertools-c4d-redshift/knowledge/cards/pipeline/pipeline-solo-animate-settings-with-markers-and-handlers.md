---
id: pipeline-solo-animate-settings-with-markers-and-handlers
title: Animate world settings and motion blur per shot using custom properties and markers, with a frame-change handler
domain: pipeline
tags: [sacha, omens studios, blender conference, markers, handlers, camera binding, motion blur, render time, deep-read]
applies_to: Blender
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=W01lQrcCz9s, src:yt-transcripts]
feeds: []
conflicts: none
---
Custom properties on a panel can be keyframed (constant interpolation) to switch sky or lighting between shots, but they do not drive the node setup by themselves; a frame-change handler reads them and applies them [23:52-25:27].
He binds the camera to markers for shot cuts and uses markers to switch motion blur off in shots that do not need it, saving around 2 s per frame in his estimate [25:27-27:07].
He renders one view layer per frame with a tool that cycles layers automatically [28:41-29:14].

**Use it:** one scene file, many shots: per-shot render settings keyed to markers keeps cost down.
