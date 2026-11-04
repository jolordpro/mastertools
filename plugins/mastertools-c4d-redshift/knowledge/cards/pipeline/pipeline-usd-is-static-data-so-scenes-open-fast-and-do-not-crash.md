---
id: pipeline-usd-is-static-data-so-scenes-open-fast-and-do-not-crash
title: Why studios want USD hand-offs: static data opens fast and cannot carry scripts or rig conflicts, unlike live Maya references that can take an hour to open
domain: pipeline
tags: [[usd, maya, performance, references, crash, cache], deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hNzbznG0ywU, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Presenter's claim: a heavy Maya reference scene can take up to an hour to open, and live files with scripts and rig operations conflict and crash [09:19-10:24]. USD holds data only, so neither happens; animation can come back as a USD cache with much smaller size and smoother playback, and nobody downstream needs the rig [07:12-07:45]. In Houdini, a Reduce node can build a proxy of a set for animation in Maya (he says animators rarely use Houdini APEX, and outsourced teams on it may cost more) [06:42-07:12]. Solaris can scatter grass and cull it by what the camera sees [07:45-08:18].
Single-speaker opinion, unmeasured.

**Use it:** Ask animation vendors for USD caches, not rigs, when only playback and render are needed.
