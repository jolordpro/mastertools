---
id: lighting-big-lights-portals-and-importance-sampling-cut-speckle
title: Small lights speckle because rays miss them: use larger lights, portals for window world light, and keep light sampling on
domain: lighting
tags: [spencer magnusson, blender, cycles, noise, portal, multiple importance sampling, small lights, speckle, window, deep-read]
applies_to: Blender Cycles 5.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=0amlKMClE4s, src:yt-transcripts, https://www.youtube.com/watch?v=dLZEmfqob7k]
feeds: [redshift, advisor]
conflicts: none
---
Magnusson [12:14-15:20, 19:36-20:09]: interior with a window looked splotchy because rays could not decide if they saw the world outside. A window portal tells the renderer to sample the world there, which cleaned it. Very small lights also leave dark spots as surfaces miss them; making lights physically bigger (lights are normalised, so they dim) makes sampling reliable but changes the look.
Switching importance sampling back on for lamps that had it off removed speckle right away. Per-light bounce limits exist, global ones in render settings.

**Use it:** the advisor's first noise check on interiors: window portals present, tiny emitters, light sampling enabled.
