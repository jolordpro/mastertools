---
id: pipeline-solo-one-button-scene-builder-and-render-budget
title: A one-button scene builder (cameras, shadow floor, sky, sun, soft backlight, speed settings) and a render budget of seconds per frame
domain: pipeline
tags: [sacha, omens studios, blender conference, scene builder, eevee, render time, backlight, hair, deep-read]
applies_to: Blender Eevee
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=W01lQrcCz9s, src:yt-transcripts]
feeds: []
conflicts: none
---
Render rule: he will not accept more than about 10 seconds per frame including hair, on a modest laptop, which is why he uses Eevee [10:47].
His scene builder adds cameras, replaces the default cube with a shadow-only floor, switches the view to rendered, adds a sky, a sun with small fixes, and a very subtle backlight (works well on hair), and optimises the viewport and render settings; all steps are chained on one button kept in quick favourites [22:12-23:21].
Sky nodes are created by script and controlled through custom properties in a panel [23:21-23:52].

**Use it:** a template for a C4D/Redshift starter script and a per-frame budget stated up front.
