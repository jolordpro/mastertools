---
id: comp-yond-rebuild-style-frame-with-difference-check
title: Yond animator rebuilds the style frame in After Effects and checks it with a static copy in Difference mode: the frame should go black
domain: comp
tags: [yond, andrew marston, style frame, difference mode, after effects, illustrator, rebuild, glow, drop shadow, deep-read]
applies_to: After Effects, Illustrator
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=2ivlXc9yrWI, src:yt-transcripts]
feeds: [shakedown, CHECKS]
conflicts: none
---
On getting a style frame he goes through every element and plans how it reaches After Effects: send what he can, rebuild with native shapes and gradients, or import the Illustrator file; in a pinch export transparent PNGs at about 4x size [36:13-37:46].
He copies blend modes, opacity and effects (Gaussian blur and so on), then lays a static PNG of the style frame on top in Difference mode. If the rebuild is right the frame should be black; it will not match exactly once there is motion [37:46-38:17].
Illustrator glows and drop shadows do not convert one-to-one, so he recreates them in AE; if the result drifts, designer and animator talk about whether that glow must be exact [40:21-41:24].

**Use it:** this is a ready-made check for a hero frame against the approved style frame: difference blend, near-black means a faithful rebuild.
