---
id: pipeline-blender-studio-edit-to-tracker-frame-range-sync-and-contact-sheet
title: Keep shot frame ranges synced from the edit to the tracker by tool, validate on file open, and review a whole sequence as a contact sheet for consistency
domain: pipeline
tags: [blender studio, kitsu, frame range, editorial, contact sheet, shot tracker, validation, deep-read]
applies_to: Blender Studio pipeline (2022)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IBTEBhAouKc, src:yt-transcripts]
feeds: [[shakedown, CHECKS]]
conflicts: none
---
Paul [02:40-05:48]: the edit is the source of truth and the shot tracker (Kitsu) must mirror it, or mismatching data causes errors further down. A add-on links each edit clip to a tracker shot and updates frame range, thumbnail and name for every selected shot in one click. Frame ranges are the number to get right: animating less than needed or more than needed is waste or a hole, and hand copying numbers swaps digits easily. Artists' shot files validate their frame range against the tracker on open and warn with an option to update. A contact-sheet tool lays all shots of a sequence on screen so lighting and comp can check the look is consistent [05:18]. A bare-bones media viewer built as an application template was also shown (arrow-key browsing of video, image sequences, multi-layer EXR with annotation).

**Use it:** Turnover check: shot length in the layout/animation file equals the edit's range; add a sequence contact sheet to every lighting and comp review.
