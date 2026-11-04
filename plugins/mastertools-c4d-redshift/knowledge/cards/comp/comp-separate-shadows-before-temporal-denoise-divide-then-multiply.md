---
id: comp-separate-shadows-before-temporal-denoise-divide-then-multiply
title: To temporally denoise without shadow ghosting, render a second pass with shadow rays off, divide to isolate shadows, denoise, then multiply them back
domain: comp
tags: [shadow pass, temporal denoise, divide multiply, shadow ray visibility, shadow catcher, compositing, ghosting, deep-read]
applies_to: Blender Cycles (proof of concept)
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jyGQIKOPwGA, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Shadow Catcher could not do it, since it works on specific objects and he needed all shadows [07:45]. Proof of concept: duplicate scene with Shadow Ray Visibility disabled on every object (light changes slightly), divide the shadowed render by the unshadowed to isolate shadows, temporally denoise the base, then multiply the shadows back; thresholds no longer needed [07:45][08:19]. Cost: scene rendered twice, so not practical. Comparison at low samples: OptiX removed more temporal noise in one scene, the node version kept more detail in another; node approach is slower and fiddly but tweakable [08:50][09:23][09:55].

**Use it:** a pattern for light groups: denoise lighting separately from shadow or contact layers where time allows.
