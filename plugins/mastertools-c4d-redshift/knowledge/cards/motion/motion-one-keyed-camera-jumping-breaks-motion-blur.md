---
id: motion-one-keyed-camera-jumping-breaks-motion-blur
title: Do not cut between angles by teleporting one keyed camera: it breaks motion blur on render
domain: motion
tags: [camera cuts, motion blur, camera sequencer, teleport, shot list, deep-read]
applies_to: Maya camera sequencer; check C4D equivalent
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=43ID41Jrhjs, src:yt-transcripts]
feeds: [c4d, shakedown]
conflicts: none
---
Sir Wade says a single camera keyed to jump around the scene is fine for a viewport playblast but breaks when rendered with motion blur; the proper way is separate cameras switched by a sequencer, with each shot given a name, a camera, a frame range, and optionally a storyboard image overlay [19:09-21:16]. Shots can also overlap in time, the sequencer rewinding on the next camera.
Less is more with cuts: in CG there is no need to hide anything, so keep the camera mostly still and show the action [21:47].

**Use it:** flag a render that has a camera with teleport keys while motion blur is on; in C4D use separate cameras with a Stage object (our inference).
