---
id: broadcast-capacity-unified-scene-rig-lighting-avoid-light-pop
title: A shared scene rig of lights across overlay levels avoids a light pop when one graphic transitions to another
domain: broadcast
tags: [scene rig, lighting, light pop, transition, unified camera, overlay graphics, deep-read]
applies_to: Unreal Engine 5.6 motion design
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=YiMh6bEebIs, src:yt-transcripts]
feeds: []
conflicts: none
---
Every overlay level carries the same scene rig: a unified lighting setup (the camera too in principle) so that levels swapped in and out do not pop [1:39:57-1:40:59]. A stray light causes aberrations on transition [1:40:27]. David said a graphic type needs one common scenario across all of its levels, and that they planned to look at it further.

**Use it:** If graphics from separate files will be cut together, light them all from one shared rig; check transition frames for lighting jumps.
