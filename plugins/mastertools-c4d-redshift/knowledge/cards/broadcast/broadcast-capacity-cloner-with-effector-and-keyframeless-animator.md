---
id: broadcast-capacity-cloner-with-effector-and-keyframeless-animator
title: Cloner plus effector plus a keyframeless oscillate animator gives an endless background with no sequencer keys
domain: broadcast
tags: [cloner, effector, animator, oscillate, cycle duration, keyframeless, niagara, deep-read]
applies_to: Unreal Engine 5.6 motion design
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=YiMh6bEebIs, src:yt-transcripts, https://www.youtube.com/watch?v=Ty6etYkvaC8]
feeds: []
conflicts: none
---
A low-poly chevron mesh in a line cloner is made to move by an effector whose sphere pushes clones in offset or push modes [49:25-51:59]. The effector is moved by an animator (oscillate, bounce, curve, pulse) set to -300 to 300 on relative location with a cycle duration; one second looks too frantic, slow looks right [53:01-54:04]. This runs without keyframes. David called it very performant, giving most of Niagara's power with a simpler interface [52:30]. Avoid keyframing the clone count [50:27].

**Use it:** Same pattern as a MoGraph cloner with a falloff effector driven by a looped noise or time; choose long cycle times for backgrounds.
Transcript support: Chevron cloner moved by an effector oscillating in the operator stack animators, so it runs outside Sequencer. (https://www.youtube.com/watch?v=Ty6etYkvaC8 [08:24-10:00])
