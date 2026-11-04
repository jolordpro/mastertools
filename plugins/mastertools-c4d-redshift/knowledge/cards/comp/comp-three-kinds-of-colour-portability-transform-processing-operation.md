---
id: comp-three-kinds-of-colour-portability-transform-processing-operation
title: Moving a colour transform does not guarantee the same processing or the same operations: separate input meaning, processing representation and approved appearance
domain: comp
tags: [[colour management, ocio, aces, portability, handoff, operation semantics, imagica, tomohiro hasegawa, approved appearance], deep-read]
applies_to: any OCIO or ACES pipeline
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=-g6JTD8cge4, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Tomohiro Hasegawa (colour imaging engineer, Imagica): "transform portability does not automatically guarantee processing portability or operation portability" [01:32]. His working principle is to keep three things separate: what the input means, the representation used for processing, and the appearance that was approved; one colour-space label cannot describe all three [02:39-03:10].
Practical consequence from the first production: when an operation could not be made portable between apps (screen above 1.0), the team put the approved appearance first and moved the hand-off boundary later, baking the part into a render element, so the question became how much of the approved look is already fixed in the image [08:56-09:29].
Assumptions should not stay implicit even for basics [01:32].

**Use it:** a hand-off check can ask three questions per element: what do values mean, what working domain, what look was approved.
