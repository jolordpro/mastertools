---
id: comp-blender-camera-track-pass-from-both-directions-then-delete-highest-error-tracks
title: Blender camera solve: detect features, track forward and backward from several frames, then clean tracks by reprojection error and re-solve; his solve error fell from about 30 to 3
domain: pipeline
tags: [max-novak, blender, motion tracking, solve error, clean tracks, reprojection, deep-read]
applies_to: Blender 3.x/4.x
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=QlbZDu2tZfE, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Detect Features with threshold and distance lowered until there are plenty of trackers; track forward from the start, detect again and track backward at the end, then do the same from the centre both ways [02:07-02:38]. Watch the solve error; Clean Tracks with the reprojection error raised, delete, and re-solve: 30 down to 3, and repeat if wanted [02:38-03:09]. Then Set as Background, set up tracking scene, set origin from a track point, and use three points for the floor [03:09]. Enable motion-tracking overlay to line objects up in 3D view.

**Use it:** Use as a reference for the solve-error target when a shot needs a tracked camera; his threshold of 3 is a beginner example, not a studio standard.
