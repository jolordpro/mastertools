---
id: comp-nuke-cg-blacks-are-crunchier-so-a-black-point-grade-ends-the-chain
title: CG renders almost always have darker blacks than camera footage, so end the CG chain with a labelled black-point Grade and raise it until the blacks match the plate
domain: comp
tags: [alfie-vaughan, nuke, black point, grade, matching, cg comp, deep-read]
applies_to: Nuke
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=fxfuhl8Q7ys, src:yt-transcripts]
feeds: [composition, motion-critique]
conflicts: none
---
He raises the viewer gamma to see the shadows and the car's blacks are much darker than the footage's [07:17-07:48]. Fix: a Grade labelled black point, raising the black point a little until CG blacks match live action [08:18]. It must be the last node before the Copy so everything upstream ends with the black set correctly [07:48]. Press D on the node to compare before and after; Ctrl-click the viewer gamma slider to reset. He also graded the plate down a little first because it was blown out but not clipped [01:04].

**Use it:** Add black-point match as the first QC question on any CG over a plate. Extends comp-three-grade-nodes-match-black-white-gamma with the placement rule.
