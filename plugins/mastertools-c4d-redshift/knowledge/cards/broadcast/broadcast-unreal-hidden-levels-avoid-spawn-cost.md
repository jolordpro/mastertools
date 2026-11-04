---
id: broadcast-unreal-hidden-levels-avoid-spawn-cost
title: Keep every element preloaded in hidden levels and toggle visibility; spawning objects live can drop frames
domain: broadcast
tags: [unreal, levels, performance, spawning, frame drops, sequencer, deep-read]
applies_to: Unreal Engine 4.27 (concepts carry to UE5)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bcL001ZFHBQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Several levels are loaded but hidden for organisation and speed [06:48-07:35]. Spawning many new objects at once is expensive on the CPU and risks frame drops, so everything is stored in hidden levels and visibility is flipped during the show [07:35-08:07].
Lighting is split by use: one rig for centre-focused compositions, another for two-car match-ups, so ray-traced lighting is tuned once per layout [07:04]. A level-visibility track in Sequencer decides which level shows [09:10-09:41].

**Use it:** For live graphics, preload and toggle; never plan for objects to be created on air.
