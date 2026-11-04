---
id: c4d-keys-outside-timeline-are-deliberate
title: Keys recorded before frame 0 or after the last frame can be a deliberate pose backup, not stray data
domain: c4d
tags: [keyframes, out of range, timeline, pose backup, loop, scene check]
applies_to: Cinema 4D 2025
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=wsF5c_UnE40, src:yt-transcripts]
feeds: [shakedown]
conflicts: none
---
Newer C4D lets keys be recorded outside the timeline range. He keys the whole rig at frame -1 as a reset pose, then animates from 0; later model changes can return to it [34:59]. For loops he records one frame past the end [35:30].

**Use it:** A stray-key check should list out-of-range keys as info, not errors, because they do not render.
