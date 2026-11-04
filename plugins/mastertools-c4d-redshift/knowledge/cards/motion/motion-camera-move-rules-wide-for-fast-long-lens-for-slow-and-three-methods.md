---
id: motion-camera-move-rules-wide-for-fast-long-lens-for-slow-and-three-methods
title: Keep a fast-moving camera wide and a close-up long lens slow, then build the move with keyframes, a path, or parenting, and add shake on top
domain: motion
tags: [camera animation, focal length, camera speed, bezier, follow path, parenting, camera shake, blender, deep-read]
applies_to: Blender (rules general)
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=pcBji0dSc8o, src:yt-transcripts]
feeds: [motion-critique, coach]
conflicts: none
---
Rule: keep the lens wide when the camera moves rapidly; use higher focal lengths for close-ups with slower movement, or the action is hard to follow [01:04]. Pick the move for the story: Dune's static camera feels grounded, superhero films use wild moves [00:33][01:04]. Methods: few keyframes with Bezier interpolation in the graph editor for smoothness [01:35][02:36]; a curve path with a follow-path constraint, keyframing offset, plus track-to for facing the subject [02:36][03:07]; parent to an object (keep transform) or a bone with a child-of constraint for POV [03:07][03:39]. Last step: add procedural shake on top of the finished move for handheld or vehicle realism [04:09].

**Use it:** quick critique rules for camera speed versus lens; shake is a final layer, not part of the animation.
