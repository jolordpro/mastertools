---
id: comp-kramer-re-camera-a-locked-3d-track-by-parenting-a-second-camera-to-the-tracked-one
title: "Kramer's re-camera trick: duplicate the tracked camera, clear its keys, match FOV, parent the footage to the new camera and parent that camera to the tracked camera"
domain: comp
tags: [andrew kramer, 3d track, camera, parenting, after effects, re-camera, green screen, field of view, polish, andrew-kramer, deep-read]
applies_to: After Effects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=5KYo8zFy1Ew, src:yt-transcripts, src:polish-roster]
feeds: []
conflicts: none
---
Problem: footage keyed on green and solved with a 3D track is locked to the tracked camera, and you cannot change a bad camera move. Steps he shows [18:26-20:29]:
1. Duplicate the tracked camera; delete the keyframes on the copy and reset it, but give it the same field of view as the original [18:26].
2. Make the footage layer 3D; a 3D layer and default camera are synchronised, so parent the footage to the new camera [18:56-19:27].
3. Parent the new camera to the tracked camera so it follows the original move [19:57].
Now the new camera can be altered (zoom out, pan, change point of view), while the original motion stays in place [20:29-21:00]. It is just a matter of parenting the cameras in the right order [21:00]. He notes it is a thing you never get right the first try [18:26].

**Use it:** For a bad solved move, add a child camera and change the framing on top of the track instead of re-solving.
