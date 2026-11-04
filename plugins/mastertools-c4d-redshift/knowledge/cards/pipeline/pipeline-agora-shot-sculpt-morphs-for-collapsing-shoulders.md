---
id: pipeline-agora-shot-sculpt-morphs-for-collapsing-shoulders
title: Fix collapsing shoulders on raised arms with per-shot sculpted morph targets, named by shot and frame, driven by a one-control rig
domain: pipeline
tags: [morph target, sculpt, shoulder, corrective, control rig, naming, agora studio, deep-read]
applies_to: Unreal Engine 5.6
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hc6xf-3uDX8, src:yt-transcripts]
feeds: []
conflicts: none
---
Raised arms lose volume at the shoulder [37:14]. Set the preview controller to the running instance so the sequencer drives the pose in the sculpt viewport, then sculpt on the affected frames [37:44-38:47]. Name each morph by shot and frame (shot-sculpt, e.g. 'SS') so its use is clear [38:47]. A control rig with one root control and no joints carries float attributes that drive same-named curves; animators can then key them on and off [39:18-40:19]. Remy notes it could be automated.

**Use it:** Corrective sculpts should be tied to a shot and frame in the name; handle as a per-shot hand-off, not a global fix.
