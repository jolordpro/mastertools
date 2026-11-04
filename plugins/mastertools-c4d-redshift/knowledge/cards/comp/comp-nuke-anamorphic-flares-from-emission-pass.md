---
id: comp-nuke-anamorphic-flares-from-emission-pass
title: Make anamorphic flares by running Optical Glow on the emission pass with a threshold and a stretched aspect ratio
domain: comp
tags: [alex, levelup plus vfx, nuke, anamorphic flare, optical glow, emission pass, bloom, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ETV1VTV0vNg, src:yt-transcripts]
feeds: [comp, elevate]
conflicts: none
---
Feed the emission pass to Optical Glow, raise the threshold so only real lights flare, then raise aspect ratio to stretch horizontally; set effect-only and plus it over [40:06-41:09].
A roto/paint patch he had done on one frame must be set to all frames, or it leaves artifacts on the others [41:09].
Bloom: blur the image, plus it back at low strength (captioned only as '33', so the unit is unclear), then kill the highlights it makes too bright and drop saturation if needed [41:41-42:42]. Sharpen first and keep it modest (size about 2, amount about 0.5), before the defocus [42:42-43:12].

**Use it:** procedural flare route without a plugin; the emission/light-group AOV is the source.
