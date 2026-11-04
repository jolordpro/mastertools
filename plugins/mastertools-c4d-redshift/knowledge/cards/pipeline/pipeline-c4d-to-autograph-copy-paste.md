---
id: pipeline-c4d-to-autograph-copy-paste
title: C4D to Autograph by copy and paste: match frame rate, scale objects with the scale parameters, and use a zero-opacity cube as a 3D mask
domain: pipeline
tags: [autograph, copy paste, cineware, 3d data, fps, primitives, 3d mask]
applies_to: Cinema 4D 2027.0 and Autograph 2027
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=FmaKhqSITFQ, src:yt-transcripts]
feeds: [comp-fix planner]
conflicts: none
---
Copy objects in C4D and paste in Autograph with the playhead at the start; the camera, light, text and primitives arrive as 3D layers [1:13:18-1:16:57]. Frame rates must match (30 in the demo) [1:14:51].
Scale cubes with the scale parameters, not the size field [1:15:21]. Put layers above the beauty layer so they show [1:17:30].
A cube set to opacity 0 still masks text, giving a free 3D matte for billboard replacement [1:19:07].

**Use it:** a comp route for sports stadium screens or billboard replacement without a re-render.
