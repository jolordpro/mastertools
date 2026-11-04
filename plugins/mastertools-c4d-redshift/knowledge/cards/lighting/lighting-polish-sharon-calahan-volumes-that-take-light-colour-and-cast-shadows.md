---
id: lighting-polish-sharon-calahan-volumes-that-take-light-colour-and-cast-shadows
title: "Calahan on The Good Dinosaur: new volume rendering let clouds, steam and mist absorb light colour and cast shadows, so they are lit as part of the world"
domain: lighting
tags: [sharon calahan, the good dinosaur, volumetrics, clouds, mist, render cost, magnus wrenninge, deep-read, polish, sharon-calahan]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=hYCVLhycG2w, src:yt-transcripts, src:polish-roster]
feeds: [polish-coach]
conflicts: none
---
Calahan [03:22-04:54]: clouds, vapour and steam were always hard to light well, to make believable and to keep affordable, since they are render heavy. She worked closely with Magnus Wrenninge, the architect of Pixar's new volumetric technology.
What she needed: volumes that absorb the colour of the light and let light colour penetrate into them, and that cast shadows on the ground easily, so they become part of how the world is lit instead of a separate painted element added later [03:52-04:22].
She also wanted fine details such as a sun dog and a hint of rainbow in mist rising from hot pools [04:22-04:54], drawing on years of studying how natural light behaves.
Transfer: in Redshift volumes, check that haze takes the light colour and casts shadow, not just fog density.

**Use it:** The coach checks that atmospheric volumes pick up light colour and cast shadows before any post haze is added.
