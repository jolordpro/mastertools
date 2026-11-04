---
id: comp-aov-add-vs-multiply
title: Light-adding AOVs combine with Add in any order; light-removing ones (shadow, AO) use Multiply and sit on top
domain: comp
tags: [aov, add, multiply, comp, shadow, ambient occlusion, blend mode]
applies_to: Redshift AOVs in After Effects, any compositor
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts, https://www.youtube.com/watch?v=4A9kbUZpqIU, https://www.youtube.com/watch?v=b0hbVd9aZkA, https://www.youtube.com/watch?v=mchPC1LeMAE]
feeds: [comp-fix planner, coach]
conflicts: none
---
Diffuse, GI, emission, reflection, specular, refraction and SSS each contribute light, so they stack with Add. Order does not change the result, like adding numbers [27:36] [1:34:39].
Passes that take light away (shadows, ambient occlusion) use Multiply instead. Once Add and Multiply are mixed, order matters, so the Multiply layers go on top.
The trainer says Add and Multiply are the only modes needed; Subtract is only the inverse of Add [29:11].

**Use it:** the comp-fix planner builds the stack as Add for light passes and Multiply for shadow and AO last, and the coach explains why a wrong mode brightens or darkens the frame.
