---
id: pipeline-rebellion-usd-pref-attribute-keeps-comp-mask-stable
title: A rest-position (Pref) pass made in lighting before animation overlays gives comp a stable mask on moving characters
domain: pipeline
tags: [rebellion vfx, evil genius 2, houdini, solaris, usd, pref, reference position, comp, deep-read]
applies_to: Houdini 18, Solaris, USD
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NNUtKYRmcjY, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Marco (lead lighting TD, Rebellion VFX; surname captioned as Derna) wanted comp to have a reference-position pass that does not change as a character moves, to make masks. In USD layers, the animation layer overwrites point positions but passes other attributes through, so he created the rest position attribute right after importing the T-pose character and before the animation overlay [13:01-14:34].
Downstream the mesh is animated but still carries the T-pose positions. One node ends up holding all the scene data for any department to read [14:34].

**Use it:** a pass worth requesting for comp-heavy shots; in C4D/Redshift, the nearest idea is a rest-position or UV-based AOV.
