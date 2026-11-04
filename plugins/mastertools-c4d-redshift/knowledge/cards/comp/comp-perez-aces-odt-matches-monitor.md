---
id: comp-perez-aces-odt-matches-monitor
title: Pick the display transform to match the actual display (sRGB monitor, Rec.709 projector, Rec.2020 HDR) and know what your monitor really is
domain: comp
tags: [victor perez, foundry, fmx, aces, odt, monitor, display, deep-read]
applies_to: Nuke 13+
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Y2mcVM8c7cA, src:yt-transcripts]
feeds: [coach, shakedown]
conflicts: none
---
In the viewer choose the output transform for the screen you are on: sRGB for a normal computer monitor, Rec.709 for a projector or TV, Rec.2020 for HDR [36:02-37:04, 46:57].
His advice: know the colour space your monitor is set to. In his demo the laptop was sRGB and the projector Rec.709, and looking at one with the other's setting looks wrong [41:45-42:17].
Newer Nuke can give each monitor its own output, so each looks right [42:17].

**Use it:** Calibrate and tag the review monitor before judging colour; a wrong display transform is the first thing to rule out when a client says 'looks different'.
