---
id: c4d-2024-rigid-body-jitter-fix-thresholds-sleep-timer-and-keyframing-it-to-zero
title: Kill rigid body jitter by letting objects go to sleep: raise velocity thresholds, shorten the new Timer, add damping, and keyframe the Timer from 5 to 0 once the pile has settled
domain: c4d
tags: [rigid body, jitter, deactivation, sleep, timer, damping, smoothing iterations, linear velocity threshold, sleep strength, deep-read]
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
EJ [10:22-21:15]. A black wireframe means the object is deactivated (asleep) and no longer simulated until hit; getting every object to sleep is the jitter cure [10:22].
Steps in his order: friction up on cloner and collider; Dynamics tab thresholds linear and angular velocity raised from their low defaults to about 40/40 [11:24]; the Timer (new) is the number of frames an object must stay under the thresholds before sleeping, default 60 (2 s), so set 5 [12:26]; Project simulation settings smoothing iterations up (works for cloth and soft too, as all are unified) [12:57]; damping about 10% and extra iterations 1 [13:28-13:58]; tag-level Damping override (15%) and angular damping [14:30].
Timer at 0 kills jitter but objects freeze in mid-air. Balance: keyframe the Timer from 5 to 0 around frame 60 when the pile has settled; also keyframe thresholds higher [17:08-18:40]. Fewer stacked layers jitter less. Break up the grid: random effector on rotation, Push Apart with more iterations, a sphere-shaped cloner and random small and big clones [15:01-16:04].
Sleep Strength is the percent of the threshold needed to wake a sleeper; at 200% a collider must move faster than twice the threshold [19:11-21:15].

**Use it:** Settle a cached pile for a title or logo build-up without wobble: thresholds up, timer down, then keyframe the timer to 0.
