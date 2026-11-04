---
id: lookdev-fmx-crystal-sss-with-animated-lights-failed-refraction-with-fog-layers-won
title: "FMX 2014 TD (Tim Wagner): an SSS crystal lit by animated lights inside was huge and uncontrollable; a refractive material with animated fog layers replaced it"
domain: lookdev
tags: [fmx, tim-wagner, lookdev, crystal, refraction, failure, student, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=8tW77BsgtPY, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
Goal: rich inner glow in the purple crystals and the FMX logo [42:05-42:37]. First setup: animated lights inside the geometry tracing through the SSS volume; end result was a horrible setup, large and uncontrollable [42:37].
Change: refractive material with animated layers of fog inside; it became the beauty with no comp on top, easier to control and to process later [42:37-43:08].

**Use it:** When a physically correct setup is slow or unreachable by artists, switch to a controllable fake and show it as the final beauty.
