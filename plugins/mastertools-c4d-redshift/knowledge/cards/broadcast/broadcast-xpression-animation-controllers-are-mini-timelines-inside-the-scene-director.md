---
id: broadcast-xpression-animation-controllers-are-mini-timelines-inside-the-scene-director
title: XPression: an animation controller holds only keyframes; the scene director also holds audio, video and stagger clips
domain: broadcast
tags: [ross xpression, ross university, scene director, animation controller, key graph editor, keyframe, set key window, lower third in off, deep-read]
applies_to: Ross XPression (tutorial B108, uploaded 2026-01-27; feature added in 5.5 noted)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=71govSIChlQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Andrew Samson (Ross Video): every scene has a default scene director (ctrl-D) containing animation controllers, which can only hold keyframes, while the director can also hold stagger animations and audio or video clips [00:35-03:11]. Name controllers by task and let one controller key several objects, for example one for lower third in and one for lower third out [03:11-04:13]. A preference sets the default controller length (he uses 40 frames; fresh install is 200) [01:38].
Double-click a controller to make it active; the bottom timeline and the key graph editor show only that controller [04:44-05:44, 08:56]. Set keys with the set keyframe window (ctrl-K): green attributes are keyed, red are not [06:16-07:18]. Start frame 0, then go to the end frame, move or rotate the object, and set again [05:44-08:23]. Space plays the director [10:32].

**Use it:** Name controllers by action (in, out, loop) so a template's animation can be reused and triggered separately.
