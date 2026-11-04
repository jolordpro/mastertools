---
id: redshift-toon-tone-map-pattern-halftone-and-smooth-airbrush-ramp-grain
title: Redshift Toon: smooth ramp steps give an airbrush edge, noise through a bump map grains the shade edge, and Tone Map Pattern gives halftone dots
domain: redshift
tags: [redshift toon, halftone, tone map pattern, bump, grain, anime, c4d, school-of-motion, deep-read]
applies_to: Cinema 4D + first Redshift Toon release (video April 2024)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=i3YczHKxtbo, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
Three shading tricks from EJ [27:00-33:16]. (1) Set the tone-map ramp's interpolation from step to smooth for one chip pair: a sharp edge fading into a soft one, the airbrushed anime look [27:00-28:03]. (2) For grainy gradients, plug a Maxon Noise into the Toon material's bump input and raise its contrast; for a larger organic break-up, route noise through a bump-map node and use the low clip, with bump strength to soften it (he notes this behaves oddly and had to be reset) [28:03-30:41]. (3) Tone Map Pattern node into the base tone map gives halftone; it had only three presets then (dots, sine waves, grid, no hatching) and takes a ramp in its intensity override; the ramp's darkness sets dot size, and it uses value not colour [31:13-33:16].
Transfers to broadcast style frames: grain and halftone are comp-friendly looks that render fast because the toon system is cheap [01:01-01:33].

**Use it:** offer these three as separate, stackable look options when asked for a print or comic finish; test at draft size first.
