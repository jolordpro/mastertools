---
id: comp-aces-1-3-reference-gamut-compress-fixes-saturated-clipping
title: ACES 1.3 added Reference Gamut Compress: turn it on to stop tearing and clipping in saturated cyans, magentas and blues from wide-gamut cameras
domain: comp
tags: [aces 1.3, gamut compress, rgc, clipping, artifacts, vectorscope, resolve, arri, red, deep-read]
applies_to: DaVinci Resolve, ACES 1.3
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=drEi66Xj5Hg, src:yt-transcripts, https://www.youtube.com/watch?v=2WyZiIMFz-4, https://www.youtube.com/watch?v=f6-bPIWNdac, https://www.youtube.com/watch?v=FSzLwSTJjWo]
feeds: [CHECKS, shakedown]
conflicts: none
---
Cinema cameras (Arri, RED) capture a wider gamut than the ACES working space, so valid camera colours fall outside it and clip or tear, seen in bright saturated areas such as a light beam or cyan region [03:04][03:36]. Test: bypass colour management on the clip; if the artefact vanishes it is introduced by the pipeline [03:04]. Where it shows: the upper-right half of the vectorscope (magentas, blues, cyans) [07:47]. Fix: tick Apply ACES Reference Gamut Compress in Resolve's ACES project settings; detail and contour came back on all three test shots [08:49][09:20]. The risk of noticing it late, in a client room, made the presenter (Joey Daoust-style colourist; name not given) avoid ACES until 1.3 [09:51].

**Use it:** QC step: with ACES, scan the vectorscope's upper right and A/B with colour management bypassed; enable gamut compress.
