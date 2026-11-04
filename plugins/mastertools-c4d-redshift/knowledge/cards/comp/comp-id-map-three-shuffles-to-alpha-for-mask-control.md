---
id: comp-id-map-three-shuffles-to-alpha-for-mask-control
title: Split an ID map into red, green and blue with three Shuffle nodes (each to alpha) so one Grade can be masked per ID
domain: comp
tags: [id map, shuffle, mask, grade, nuke, aov, sarkamari, deep-read]
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
Instead of feeding the ID pass to a Grade mask and switching the mask channel, set up three Shuffles: red to alpha, green to alpha, blue to alpha [27:46-29:26]. Connect the one you want to the mask input and change that grade without touching its mask-channel setting [29:58-30:30]. His demo raised the green ID's multiply to 1.9.

**Use it:** Cleaner ID mask setup for QC passes: label each shuffle by what the colour means.
