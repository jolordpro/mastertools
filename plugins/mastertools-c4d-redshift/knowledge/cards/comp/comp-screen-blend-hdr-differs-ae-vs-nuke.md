---
id: comp-screen-blend-hdr-differs-ae-vs-nuke
title: Screen blends only match between After Effects and Nuke while values stay in 0-1; above 1 they diverge and hues can shift
domain: comp
tags: [screen, blend mode, hdr, after effects, nuke, handoff, scene linear, hue shift]
applies_to: After Effects, Nuke (Aug 2026 talk)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-g6JTD8cge4, src:yt-transcripts]
feeds: [comp planner, shakedown]
conflicts: none
---
Imagica [07:46]: AE uses A + B - A*B always. Nuke uses that between 0 and 1 and the maximum of A and B outside. A=5, B=0.9 gives 5 in Nuke and 1.4 in AE.
The effect differs per RGB channel, so hue changes: bright blues drifted toward green. It was operation semantics, not the OCIO transform [08:23].
Fix [09:29]: bake the non-portable operation in Nuke and pass it to AE as a render element, moving the hand-off later.

**Use it:** flag screen/add layers above 1.0 when a comp changes app; ask for a baked element.
