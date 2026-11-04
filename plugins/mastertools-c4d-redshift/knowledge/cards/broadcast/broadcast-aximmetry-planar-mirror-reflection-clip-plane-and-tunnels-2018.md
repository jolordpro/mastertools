---
id: broadcast-aximmetry-planar-mirror-reflection-clip-plane-and-tunnels-2018
title: Aximmetry 2018: real-time floor reflections come from a second render through a mirror camera, a clip plane and a tunnel to the shaders
domain: broadcast
tags: [aximmetry, planar reflection, mirror camera, clip plane, tunnel, transmit video, half resolution, virtual studio, 2018, deep-read]
applies_to: Aximmetry Studio/Broadcast tutorial, uploaded 2018-09-15 (Complete Studio Scene 06)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=leqVJhmy_zQ, src:yt-transcripts]
feeds: [lookdev]
conflicts: none
---
[00:02-05:13] The reflection is a duplicate render from a camera mirrored about a plane. The mirror camera is bound to the normal camera, with its mirror property on, and a Clip Plane module defines the plane (rotation is pointless for a floor).
To save GPU, override the mirror camera's output size to half the system frame size (divide module); fine only for faint or blurred reflections. A blur module softens it for rough surfaces.
To get the image to every shader without long wires, a Transmit Video module sends it into a named tunnel (mirror one); Transmitted Video modules anywhere in sub-compounds read it with a From Channel property.
Then change the object's shader (mirror folder, flat compal type), connect the image to its mirror pin, and slide the plane up with the arrow, holding Shift (or Shift+Ctrl) for fine moves, until objects meet their reflections [04:42-05:13]. Hide helper geometry in File > Properties first.

**Use it:** Real-time planar reflection is a second render: budget its resolution, and align the mirror plane to the real floor height.
