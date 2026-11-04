---
id: lighting-led-volume-lens-focus-and-moire
title: Keep the volume out of focus to avoid moire, shoot tighter, and let the real lens do the depth of field
domain: lighting
tags: [10 dots, moire, virtual production, depth of field, camera lens, frustum, genlock, tracking, deep-read]
applies_to: LED volume, Unreal
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aKRcGoc_osQ, src:yt-transcripts]
feeds: [composition, elevate]
conflicts: none
---
Focusing on the screen pixels gives moire and shimmer, worse at strong angles; cameras with a strong optical low-pass filter help [20:40-21:11]. Better to keep real distance to the wall and let the lens blur it than to render depth of field in the engine, which fights the lens [21:42-22:18]. Tighter lenses lose the screen less than extreme wides, especially low angles [19:36-20:40].
Tracking sees 8 or more reflective stars on the ceiling; tracker view must stay clear; focal length does not matter, only position, so dolly zooms work [19:06-19:36].
The frustum is the camera-matched window of correct perspective, with overscan around it; multiple cameras need overlapping frustums flickering up to four images at 360 Hz [22:18-24:23]. A frustum can be set to green for keying while the wall still gives light [24:23].

**Use it:** Coach: in virtual or LED-wall plates, the camera focus plane should sit well in front of the wall.
