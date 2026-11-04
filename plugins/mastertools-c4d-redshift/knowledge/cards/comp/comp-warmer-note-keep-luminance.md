---
id: comp-warmer-note-keep-luminance
title: A 'make it warmer' note should not change brightness; use temperature, magenta, intensity and keep intensity at 1
domain: comp
tags: [tony lines, warmer, temperature, magenta, intensity, luminance, nuke color picker, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ZrOiwMSGmIw, src:yt-transcripts]
feeds: [comp, motion-critique]
conflicts: none
---
Dragging RGB multiply toward red dropped the viewer luminance from 0.149 to about 0.05, so the image got darker, not just warmer [32:10-32:41]. A supervisor asking for warmer wants the same image in a warmer tone [32:41].
Nuke's colour picker has a hidden TMI tab (temperature, magenta, intensity). Temperature runs warm to blue, magenta shifts green/magenta, intensity is the brightness [35:15-37:53]. Keep intensity at 1, or set it back to 1 after the colour move.
The Kelvin scale runs red/orange, then neutral white, then blue [29:02-30:36].

**Use it:** Judge a 'warmer' note done only if mean luminance stays within a small tolerance of the original.
