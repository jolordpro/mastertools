---
id: lookdev-glass-gradient-emission-backdrop-renders-faster
title: A gradient emission backdrop lights glass faster than a lit gradient ground, since light no longer bounces off the ground first
domain: lookdev
tags: [glass, gradient backdrop, emission, render time, map range, smoother step, polyfjord, deep-read]
applies_to: Blender 3.3 Cycles
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Jwl48psPrxU, src:yt-transcripts, https://www.youtube.com/watch?v=WreZ_VKDn4M]
feeds: []
conflicts: none
---
A lit gradient ground makes light bounce from the lamp to the ground and into the glass, which is slow [09:55]. Instead, an emission gradient plane only emits into the glass, speeding up the render significantly [10:19]. Make a smooth gradient with a gradient texture (quadratic) in object coordinates through a Map Range set to smoother step [10:49-11:51]. Scaling the gradient reshapes the glass look entirely [21:10]. An area light on the z-axis adds interesting highlights [11:51].

**Use it:** For glass hero shots in C4D+Redshift, a gradient emissive backdrop is a cheap way to get controlled refractions.
