---
id: lookdev-fmx-frog-snail-sss-mask-the-belly-and-split-the-slime-reflection-pass
title: "FMX 2014 TD student: separate SSS controls by a mask for the belly, back-lights for subsurface, and a blurred-displacement reflection pass for the slime layer"
domain: lookdev
tags: [fmx, lookdev, subsurface-scattering, slime, student, manuel, deep-read]
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
Manuel (surname not caught; TD student, lighting/shading) on Rugby Bucks creatures frog and snail: needs photoreal, SSS, slimy look; the crystal had to glow through the frog's belly [15:01-16:05].
SSS was the hardest to tune; early blind test before the model existed; for the shot he added extra lights behind the snail to boost the subsurface on chosen parts [16:05-17:06].
A quick mask split SSS strength between belly and rest of the body [17:06-17:37].
Slime failure: the displacement map's distinct bumps gave a high-frequency reflection, so it did not read as a separate layer. Fix: blur the displacement used for that layer, render a separate reflection pass, and add it in comp [17:07-18:07].
The back of the snail shell was left untextured because it never shows in that shot, to save texture artist time [16:05].

**Use it:** Slimy skin: treat the wet layer as its own smoother reflection (blurred bump) and keep it as a separate pass for comp.
