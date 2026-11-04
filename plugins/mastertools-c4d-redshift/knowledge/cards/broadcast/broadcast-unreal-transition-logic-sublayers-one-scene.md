---
id: broadcast-unreal-transition-logic-sublayers-one-scene
title: Unreal broadcast transition logic: each sublayer has an in and an out, so one scene manages the states of many on-air graphics
domain: broadcast
tags: [broadcast, unreal engine, transition logic, sublayers, ticker, lower third, live bug, state, deep-read]
applies_to: Unreal Engine 5.5
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=5P-sO_2aiwU, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
A broadcaster needs name plate, live bug and ticker on screen together; this is transition logic [23:50]. Epic's 5.4 version was complex, so 5.5 focused on ease of use [24:20].
Each sublayer (header, top line, footnote, ticker) gets an in and an out animated on the timeline; when any state changes, only the affected elements animate in or out, and graphics can shift, for example up when the ticker arrives [24:50]. Everything stays in one scene rather than split scenes, easier to test [25:22].
Also named: nDisplay clustering for big synchronised canvases and NDI support [30:31].

**Use it:** Design reference for a graphics package: define in/out per element and state-driven changes, in one scene. Pairs with broadcast-fox-transition-logic-wish.
