---
id: comp-add-camera-flaws-glow-lens-distortion-and-noise-so-cg-does-not-read-plastic
title: Add small camera flaws in comp (glow, mild lens distortion with dispersion, a little noise) so a clean CG render does not look plastic
domain: comp
tags: [comp, realism, glare, lens distortion, noise, agx, blender compositor, deep-read]
applies_to: Blender compositor (principle any)
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=jyAJKlZi4as, src:yt-transcripts]
feeds: []
conflicts: none
---
In his finishing pass in the render compositor: a fog glow with small size (0.2) and a mild haze, nearly invisible in the viewport but visible in render, kept from over-exposing; lens distortion with dispersion since real cameras are never perfect; and a bit more noise so it does not look polished and plastic [09:36-11:41]. He does saturation, exposure and view transform in the same render rather than in Photoshop, preferring AgX with lower gamma [11:41-12:12]. Final check: scuffs, cracks and dust visible, highlights not blown [12:12-12:43]. Numbers are approximate (auto captions).

**Use it:** Keep the effect so subtle it is hardly seen; one check frame with all three off vs on should prove it still reads real.
