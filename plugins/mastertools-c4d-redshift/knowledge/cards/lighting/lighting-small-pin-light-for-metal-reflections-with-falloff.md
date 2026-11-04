---
id: lighting-small-pin-light-for-metal-reflections-with-falloff
title: Get shine on metal parts with a small, falloff-edged accent light kept dim, not a second big area light
domain: lighting
tags: [accent light, metal reflection, falloff, highlight, reflection only, deep-read]
applies_to: KeyShot
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=umnswWAS2vw, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
Metal parts looked dull, but a second area light would change the overall lighting; he instead added a pin (a point-like light with a set-highlight function), aimed the reflection where wanted, lowered the brightness since it lit the whole scene, and added edge falloff so reflections do not have sharp boundaries [05:48-06:52]. Result: slightly more general light, more sparkle on metal.

**Use it:** in C4D/Redshift use a small rect light with a gradient/falloff and light-linking to metal parts only (our inference; verify naming against the Redshift ledger).
