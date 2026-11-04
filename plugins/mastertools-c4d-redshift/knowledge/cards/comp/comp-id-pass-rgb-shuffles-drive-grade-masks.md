---
id: comp-id-pass-rgb-shuffles-drive-grade-masks
title: Use an ID pass by shuffling red, green and blue into masks and grading only the matching part
domain: comp
tags: [sarkamari, reza, nuke, arnold, merged aov, id pass, object id, mask, grade, colour channels, deep-read]
applies_to: Nuke
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=xwD_UPqbmCU, src:yt-transcripts, https://www.youtube.com/watch?v=gSvBBw0k3PU]
feeds: [comp]
conflicts: none
---
Reza [20:35-23:17]: three Shuffle nodes, one per channel, each feeding a Grade's mask; green multiply 1.9 changed only the green-ID region. Then tint, lift, gain, gamma, or invert so the rest changes. Efficient and flexible.

**Use it:** use ID AOV (or Cryptomatte) for selective grades before reaching for roto.
