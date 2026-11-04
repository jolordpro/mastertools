---
id: comp-color-on-multiply-intensity-on-gain
title: Put colour on Multiply and intensity on Gain so a later 'half a stop down' note is one number
domain: comp
tags: [tony lines, grade node, multiply, gain, exposure, round trip, lighter, deep-read]
applies_to: Nuke Grade
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ZrOiwMSGmIw, src:yt-transcripts]
feeds: [comp, coach]
conflicts: none
---
Tony Lines' habit: never mix the two jobs in one set of sliders [38:23-41:34]. Color shift goes in Multiply, exposure change goes in Gain (say x4 for two stops). A later note such as 'half a stop down' then edits one clean number.
Lighting software exposes the same two controls per light, so the comp values can be handed to the lighter to re-render, and the result matches closer than a comp cheat [43:38-44:40].
Colour-blind compositors may prefer RGB, but should still watch the intensity value [42:05].

**Use it:** Comp handoff note format: per light group, 'colour = RGB multiply, exposure = +/-n stops'.
