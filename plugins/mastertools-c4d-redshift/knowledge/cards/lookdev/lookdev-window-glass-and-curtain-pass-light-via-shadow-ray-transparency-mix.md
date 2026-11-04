---
id: lookdev-window-glass-and-curtain-pass-light-via-shadow-ray-transparency-mix
title: For interiors, make window glass and thin curtains transparent to shadow rays so light enters the room
domain: lookdev
tags: [interior, window glass, shadow ray, light path, mix shader, curtain, noise, cycles, deep-read]
applies_to: Blender Cycles 3.x (principle transfers)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dLZEmfqob7k, src:yt-transcripts, https://help.maxon.net/r3d/cinema/en-us/Content/html/Standard_Material.html]
feeds: [redshift, coach]
conflicts: none
---
rileyb3d: interior noise means too few samples or too little light; piling up lights makes the scene flat and low contrast, when the real light should come from the window [00:43, 01:37]. Fix 1: a rectangular area light fitted to the opening, set as a portal, focuses samples through the window [02:16]. Fix 2: glass normally blocks light with a shadow; mix the glass shader with a transparent shader and drive the factor from the Light Path 'is shadow ray' output, so camera and reflections see glass but shadows see nothing [03:18]. Same for the curtain (diffuse plus translucency), then darken its colour so it is not radioactive [04:38]. Goal: every render stopped under one minute on one RTX 2080; he rarely lets interiors run over 5 minutes [10:31].

**Use it:** the same idea is the Redshift 'cast shadows off' or thin-glass trick on window panes; check the equivalent flag before adding lights.
Maxon check (2026-10-31): Maxon docs (Redshift Standard Material): use Thin Walled for window glass. Shadow control is Fresnel Affects Shadow (default On, no internal reflection) plus Shadow Opacity; Fresnel Affects Shadow matters only with Thin Walled off. (https://help.maxon.net/r3d/cinema/en-us/Content/html/Standard_Material.html)
