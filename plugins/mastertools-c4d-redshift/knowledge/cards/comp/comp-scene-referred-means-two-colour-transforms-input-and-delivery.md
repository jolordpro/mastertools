---
id: comp-scene-referred-means-two-colour-transforms-input-and-delivery
title: Scene-referred workflow converts footage once on the way in and once per delivery; everything between is only a viewer transform
domain: comp
tags: [color management, scene referred, display referred, input transform, view transform, archive, victor perez, foundry, whisper, deep-read]
applies_to: Nuke, any
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Hlj5ep-85ys, src:yt-transcripts]
feeds: [shakedown, redshift]
conflicts: none
---
Victor Perez (Foundry, Nuke) contrasts the two [1:03:57-1:12:18]. Display-referred: footage is changed to fit each screen, so many LUTs and a high risk of inconsistency, and old masters go obsolete. Scene-referred: pick one master space wide enough for every source and HDR-ready, apply an input transform to each source, render CG straight into that space if possible (no useless conversions) [1:04:31], work in 32-bit float, view through a display transform plus the shot's look in the viewer, then grade in DI and apply an output transform per destination. Store the masters in the scene space and keep grades as transforms, so future displays can be served [1:09:36]. A wide-gamut master does not improve an iPhone clip but does not lose it. After the grade, narrower destinations may need tweaks: Cars' Lightning McQueen red looked different cinema versus TV [1:08:58]. Whisper transcript.

**Use it:** The platform's colour check: confirm one input transform per source, EXR out of the render without extra conversion, and the viewer carrying display and look, never baked.
