---
id: agencies-man-vs-machine-polish-bake-time-remaps-into-the-keyframes-and-add-animated-displacement-detail
title: Polish rules from Man vs Machine: bake edit-level time remaps into the keyframes so the final is a pure render, and lay an animated depth/displacement texture over a simple sim to make it look more detailed
domain: agencies
tags: [tim-bolland, man-vs-machine, polish, time remap, displacement, final render, houdini, deep-read]
applies_to: Houdini, motion design
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=JCUks81cBtw, src:yt-transcripts]
feeds: [elevate, CHECKS]
conflicts: none
---
Polish means textures, lighting and sharper cameras on shots that may be locked weeks early or arrive last-minute [20:33]. They often time-remap in the edit, but for final renders carry the remap into the keyframes so the render is not retimed [21:06]. The sample shot: a simple viscous-lava sim from an earlier unused job, rendered with a capture camera to get a depth pass, then used as animated displacement over the glass-twist animation; because speed matches, it flows with it and the shot looks like a far more complicated sim [36:48-38:09]. The same shot carried the displacement animated down at the end, and parameters can be tweaked or time-remapped [38:09-38:41]. His tip: take a texture, especially an animated one, and put it on top for life.

**Use it:** Final-pass checklist items: no retimes on final renders; detail overlay on simple sims.
