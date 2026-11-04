---
id: motion-motionxp-fall-and-land-needs-accelerating-curve-plus-tiny-overshoot
title: A fall needs an accelerating curve and a landing keyframe 3 frames past the floor, and the value graph must not show a slowdown just before impact
domain: motion
tags: [motionxp, after effects, easing, gravity, fall, overshoot, value graph, graph editor, deep-read]
applies_to: After Effects
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=HpVtzOtaHlg, src:yt-transcripts]
feeds: [[motion-critique, coach]]
conflicts: none
---
MotionXP (tutorial channel, low). Timing is keyframe distance, spacing is the curve between them; changing easing alters spacing while timing stays [00:01-00:33]. Example: two position keys 10 frames apart, ease the first key so speed builds like gravity; add a third key about 3 frames after the landing and nudge it down slightly (overshoot), easy ease the last key, and the object gains weight [01:36-02:40]. Separate dimensions and use the value graph: a hump before the middle key means the object decelerates just before hitting, which gravity would not do, so break the handle with the convert vertex tool to remove it [02:40-03:41]. Use a lighter first handle so it already looks in motion off-screen [03:11].

**Use it:** Motion-critique check for drops and slams in sports graphics: look for a slow-down before contact and for a landing that stops dead with no settle.
