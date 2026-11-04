---
id: comp-passes-copy-matte-into-alpha-with-channel-choice
title: Pass files arrive without alpha: use a Copy node to put the matte into alpha, and pick red to alpha if the matte lives in RGB
domain: comp
tags: [alpha, matte pass, copy node, channel, nuke, aov, sarkamari, deep-read]
applies_to: Nuke 12.3
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=4A9kbUZpqIU, src:yt-transcripts]
feeds: []
conflicts: none
---
The read nodes for passes have no alpha channel [13:17]. Copy the matte pass in with a Copy node (K), channel set to alpha from rgba.red when the matte is a single-colour image; sometimes the default does not work [14:22-15:57]. The same trick and an RGB-to-red choice apply to Z depth, which must go into the depth channel for ZDefocus [25:37-26:41].

**Use it:** In pass-stack set-ups, the first step after building the beauty is to restore alpha and depth to proper channels.
