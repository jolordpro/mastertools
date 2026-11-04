---
id: pipeline-vfx-tracker-shot-number-primary-key
title: Keep the VFX shot number as the primary key across plate sheet and tracker, with a link per turnover and status reset before redo
domain: pipeline
tags: [jack the avid assistant, vfx tracker, spreadsheet, shot number, turnover number, status, google sheets, vendor, deep-read]
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
Plate metadata is exported from the bin as a tab-delimited file and pasted into the tracker; a VFX shot number column is added and put first, because that, not the plate name, ties all the data together [56:23, 56:53].
The tracker's status moves to "turned over", names the vendor, and has a last column with a hyperlink to that turnover's plate sheet [1:01:42, 1:02:12].
Before redoing any turnover, set the shot back to "waiting turnover" so the vendor sees it live, then relink to the newer plate sheet [1:03:46].
Extra metadata (lens, camera, LUT, colour space) goes in via ALE if recorded [1:04:17].
He says it is less polished than ShotGrid or a code book but works in a pinch and was used on an action film [1:04:49].

**Use it:** In the estimator and shot sheet, key everything by shot ID and keep a visible status and a link to the current delivery.
