---
id: c4d-2024-rigid-body-emitter-stop-timer-after-emission-ends
title: With an emitter feeding rigid bodies, keyframe the sleep Timer to 0 only after the emitter stops, or fresh objects freeze in mid-air
domain: c4d
tags: [rigid body, emitter, timer, sleep, midair freeze, stop emission, particles, deep-read]
applies_to: Cinema 4D 2024 rigid body (School of Motion, EJ, Apr 2024)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=_6toVWN7NMo, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
EJ [21:45-24:28]. Put the Rigid Body tag on the Emitter, not on each brick under it. His 60-frame timer keyframe from the cloner scene froze emitted bricks in the air because emission continued; the fix is to move the keyframe past the emitter's stop-emission frame (150 in the demo) so the pile settles only when emission is done [22:50-23:57]. A few hidden stragglers keep moving under the pile and stay unseen.

**Use it:** When timing a settle keyframe, read it off the emitter's end frame, not the clip length.
