---
id: comp-fmx-render-smoke-in-colour-regions-so-comp-can-tweak-each-light
title: "FMX 2014 TD student: render the rocket smoke lit in separate colours so compositing can retune each light afterwards"
domain: comp
tags: [fmx, comp, smoke, light-groups, houdini, student, manuel, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=8tW77BsgtPY, src:yt-transcripts]
feeds: [redshift, comp]
conflicts: none
---
For the spaceship launch the smoke emitter followed the ship and a downward force pushed it outward; to keep scale, the smoke had to read small [23:49-24:21]. Rendered in colour (a different colour per light area) so the compositor could tweak the three areas separately [24:21-24:57].
Same idea as light groups: bake light contribution into channels and balance in comp.

**Use it:** Volume shots: render per-light contributions (light groups or colour-coded lights) to relight in comp without re-simulating.
