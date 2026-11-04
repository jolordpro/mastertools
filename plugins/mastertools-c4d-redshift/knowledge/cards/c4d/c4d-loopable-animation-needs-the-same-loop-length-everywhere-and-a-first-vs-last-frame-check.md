---
id: c4d-loopable-animation-needs-the-same-loop-length-everywhere-and-a-first-vs-last-frame-check
title: Seamless loop in C4D - set one loop length (240 frames here), run noise on a null with that loop point, and compare frame 0 to the last frame
domain: c4d
tags: [loop, noise, camera-drift, null, signal, greyscalegorilla, cinema-4d-2023, deep-read]
applies_to: Cinema 4D 2023 with Greyscalegorilla Signal (a paid plugin)
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-31
sources: [https://www.youtube.com/watch?v=7-q1JKG8638, src:yt-transcripts]
feeds: [motion-critique, CHECKS]
conflicts: none
---
Greyscalegorilla, 2023 [12:37-19:47, 23:26].
- The field animation was 60 frames out and 60 back, so the loop is 120 or a multiple; he set the project to 240 frames and told every noise to loop at 240.
- Put the linear field in a null and rotate the null with loopable noise (variation up, speed down) so the sweep direction drifts but still loops [15:07-17:43].
- Do the same for the camera: parent it to a null and give that null loopable rotation noise at the same 240 loop, speed about 0.1, so reflections and lights move; bias/contrast makes it twitchier [18:14-19:47]. Speed changes never break the loop.
- Final check he insists on: go to frame 0, then the very last frame, and confirm they match, and check framing at the largest point [23:26].
- Signal's own tools (set linear 90 frames, sine in/out, ping-pong playback) are plugin-specific.

**Use it:** A loop QC gate: one loop length for all noise, and a first/last frame match before render.
