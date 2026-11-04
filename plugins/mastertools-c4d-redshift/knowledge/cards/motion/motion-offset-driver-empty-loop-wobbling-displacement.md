---
id: motion-offset-driver-empty-loop-wobbling-displacement
title: A looping liquid wobble: move the displacement's coordinate object with the same keyframes as the mesh, offset by four frames
domain: motion
tags: [displacement, empty controller, offset animation, loop, wobble, voronoi, polyfjord, deep-read]
applies_to: Blender 3.3
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=Jwl48psPrxU, src:yt-transcripts]
feeds: []
conflicts: none
---
Set the displacement texture coordinates to an empty object (the displacement controller) [12:22-12:52]. Record a motion of the mesh with auto-key, smooth keys twice, then copy the same keys to the empty so the effect cancels, then slide the empty's keys by four frames to get the wobble [13:23-14:58]. Extend the end frame by those 4 frames, e.g. 194, to loop perfectly [15:28].

**Use it:** The 'same motion, small time offset' trick works for any driver; in C4D use a delay on a driver object.
