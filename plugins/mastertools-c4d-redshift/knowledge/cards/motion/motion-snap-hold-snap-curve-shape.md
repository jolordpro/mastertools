---
id: motion-snap-hold-snap-curve-shape
title: Broadcast camera moves share one curve: sharp bezier handles at both ends, a flatter but not flat middle, over about 45 frames
domain: motion
tags: [easing, f-curve, snap hold snap, camera move, broadcast, bezier]
applies_to: Cinema 4D
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=LhnHh94lvLo, src:yt-transcripts]
feeds: [motion curve metrics, motion-critique]
conflicts: none
---
C4D keys default to a soft ease that reads slow [03:08]. Select both keys, pull handles so ends are steep and the middle is flat [03:40-04:11]; do not make the middle fully flat, or the move stops [08:17]. All four moves use 45 frames [03:08].

**Use it:** Curve metric target: steep entry and exit, low slope mid-move, no dead stop.
