---
id: comp-nuke-grain-fades-in-highlights
title: Mask grain down in the brightest areas, because real grain decreases as highlights approach clipping
domain: comp
tags: [alex, levelup plus vfx, nuke, grain, luma grain, highlights, mask, realism, deep-read]
applies_to: Nuke, Luma Pictures grain gizmo
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ETV1VTV0vNg, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
A luma-driven grain gizmo lets a mask input weaken grain; he keys luma, inverts it so very hot areas are selected, and feeds that as the mask [48:26-49:20].
Reason given: grain going all the way up into the highlights is unrealistic [48:26]. Also uses a soften node on CG, which differs from defocus [47:55].

**Use it:** extra rule for the existing grain match cards: reduce grain in the top of the range.
