---
id: motion-unreal-animators-procedural-motion-no-code
title: Unreal animators add expression-like procedural motion to any property, with a low-frame-rate stop-motion option
domain: motion
tags: [unreal engine, animator, procedural animation, curve animator, stop motion, text animation, presets, deep-read]
applies_to: Unreal Engine 5.5
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=5P-sO_2aiwU, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Animators target any property without code, like expressions in After Effects: sine waves and curves give overshoot and looping spin [20:05]. A frame-rate setting samples the motion down to, for example, 8 fps for a stop-motion look [20:36].
Animators trigger and fade from Sequencer tracks [21:09]. A curve animator takes any curve asset for jiggle or bounce-in text, each property has a timing offset, and several animators can be stacked on position and scale; looks save as presets [21:42] [22:15] [22:48].
He wants to extend to sub-properties so a ripple can run through many children under a null [23:19].

**Use it:** Use as the Unreal analogue when asked how to do expression-driven text cascades without scripting. Good for end-tag style cascades.
