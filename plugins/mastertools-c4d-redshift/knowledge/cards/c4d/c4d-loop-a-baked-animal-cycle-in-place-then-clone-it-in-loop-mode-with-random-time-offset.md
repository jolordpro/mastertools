---
id: c4d-loop-a-baked-animal-cycle-in-place-then-clone-it-in-loop-mode-with-random-time-offset
title: Make a clone-ready flight loop: freeze the cycle near the world origin, bake to point-level animation, set the Cloner animation mode to Loop, add random time offset
domain: c4d
tags: [double motion design, bird, cycle, loop, bake, point level animation, cloner, random effector, time offset, formula effector, deep-read]
applies_to: Cinema 4D (version not stated; uploaded 2026-04)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=mq2eMicxJZ4, src:yt-transcripts]
feeds: []
conflicts: none
---
A bird animation from 3ds Max was re-keyed so it flies in place: position recorded, loop point found in the time curve and key tracks shown, last frame need not match the first exactly but should lead back to the start [00:00-01:06]. Keep the model near the world origin every frame, then bake to a point-level animation [01:06-01:36].
Only 5 baked frames existed, so the Cloner's default Play mode shows no motion later; set the animation mode to Loop [01:36-02:12].
Add a Random effector with random position, and enable time offset (7 frames total in his example) so clones desync [02:12-02:44]. A Formula effector adds a bobbing up and down so it is less dull [02:12-02:44]. A Time effector then moves them along X (rotation off) [02:44].
Transfers: the same recipe covers any short bake cycle (flags, crowds, bars) to fill a wall of clones cheaply.

**Use it:** build cycles in place near the origin, bake short, loop in the cloner, and desync with a few frames of random time offset.
