---
id: pipeline-turnover-burn-in-reference-contents
title: Reference movies for a turnover burn in plate name, source camera file, source timecode and a per-shot VFX frame counter
domain: pipeline
tags: [jack the avid assistant, burn-in, reference quicktime, h264, scene reference, context, timecode, handles, deep-read]
applies_to: Avid Media Composer (principles apply to any editor)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=MoR7ncjN9Ds, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Pull-package reference: plate name top left, source camera file bottom left, source timecode, and a VFX frame counter bottom right that resets to 1001 on each shot [40:13, 42:52].
Reason: it gives the lab a frame-accurate picture of what to restore [43:23].
Separate vendor references are exported per scene, not just per plate, so the vendor sees the shot in context, any resize done in the offline, and timing and placement to match [45:27, 49:40].
Those references show plate name, a timecode and the frame counter only while a plate exists on the track; blank spots are cleaned up [52:15].
Updated references show how much handle has been eaten if the cut changed [53:49].
Save the burn-in presets in a shared effects bin [54:50].

**Use it:** Every review or handoff movie should burn in shot name, source file and a frame counter that matches the vendor's frame numbers.
