---
id: pipeline-vfx-frame-count-starts-at-1001
title: VFX plates count from frame 1001, so 8-frame handles put the working shot at 1009
domain: pipeline
tags: [jack the avid assistant, 1001, frame count, handles, working range, duration formula, vfx, deep-read]
applies_to: Avid Media Composer (principles apply to any editor)
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=MoR7ncjN9Ds, src:yt-transcripts, https://www.youtube.com/watch?v=aR3yNNGK_sc]
feeds: []
conflicts: none
---
Vendors commonly start plate frame counts at 1001, which gives headroom to add frames before the start [34:28].
With 8-frame handles the working range starts at 1009 [35:00].
Add a working start (1001 plus handle), working end (frame count end minus handle) and working duration (duration minus both handles) to the plate sheet; working duration should equal the shot's length in the cut and be checked against the tracker [58:28, 59:31].
Avid quirk: a start-frame counter does not reset to 1001 per clip, so a custom VFX counter column was used for burn-ins [41:49].

**Use it:** Standardise a frame offset (1001) and a handle value in the shot sheet and compute working start, end and duration automatically.
