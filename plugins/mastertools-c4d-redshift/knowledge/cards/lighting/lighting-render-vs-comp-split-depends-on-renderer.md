---
id: lighting-render-vs-comp-split-depends-on-renderer
title: Do lighting work in render when the renderer lets you shape light; push to comp only when the engine cannot
domain: lighting
tags: [francesco giroldini, dreamworks, render vs comp, aov per light, gradients, nuke, moonray, deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=GcPlNw9kFVk, src:yt-transcripts]
feeds: []
conflicts: none
---
Francesco Giroldini (lead lighting/comp artist at DreamWorks, ex-Pixar and Blue Sky; Academy of Animated Art interview): if you can control light shaping or darken areas in render, do it there because it pays off for the whole sequence; big gradients in comp give artifacts when information is thin [28:30-30:07].
At DreamWorks the renderer outputs an AOV per light, so a gradient is easier in Nuke; some engines cannot do that so you must plan [30:39-31:41].
Trade-off: 3D depth of field simplifies comp scripts but gives different artifacts than putting everything in one layer [31:41-32:29].
He says the studio renderer MoonRay is very fast but gives fewer controls than the prior complex engine [09:32-10:46]. Some looks need heavy comp: nuke scripts like miniature cities [30:07-30:39].

**Use it:** Render-vs-comp advice by engine: with light-group AOVs, put gradients in comp; otherwise in render.
