---
id: comp-spring-comp-fixes-cryptomatte-masks-and-subtle-lens-effects
title: Spring comp fixes: Cryptomatte masks lifted a black dog in a black forest, re-sim comped without a re-render, effects kept subtle
domain: comp
tags: [comp, cryptomatte, render fixes, fog breath, chromatic aberration, lens flare, plates, blender studio, deep-read]
applies_to: Blender compositor
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aR3yNNGK_sc, src:yt-transcripts]
feeds: [elevate, CHECKS]
conflicts: none
---
Compositing is shot-specific [34:48]. Cryptomatte plus custom animated masks brightened the black dog Autumn against a black forest, with small colour corrections only, since grading came last [35:23]. One shot got a new simulation after rendering, so the dog was comped in frame by frame with the new sim rather than re-rendering [35:55]. Floating-particle glitches were hidden with custom masks [35:55].
Fog breath was rendered as plates with smoke in the real-time renderer (EEVEE) because it did not need light interaction, stored in plates and added with colour correction and translation [36:29] [36:59]. Lens flares and very subtle chromatic aberration (an RGB offset) went on top [36:59].

**Use it:** Use for the comp-stage checklist: keep a path to fix by mask or plate before re-rendering. Elements with no light interaction can be rendered cheaply as separate plates.
