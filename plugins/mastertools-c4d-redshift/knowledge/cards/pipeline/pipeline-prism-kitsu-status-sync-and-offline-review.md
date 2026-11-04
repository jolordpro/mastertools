---
id: pipeline-prism-kitsu-status-sync-and-offline-review
title: Task status, notes and review media sync between the DCC, Prism and Kitsu; dailies run in OpenRV with annotations pushed back
domain: pipeline
tags: [prism, kitsu, shotgrid, openrv, dailies, review, annotations, media playlist, deep-read]
applies_to: Prism 2 (private beta mid-2023), QuiltiX early dev
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=GE6Af6hjYfI, src:yt-transcripts]
feeds: []
conflicts: none
---
Prism's own project-management plugin only handles basic tasks, notes and version status; connecting Kitsu, ShotGrid or ftrack is much stronger [14:28-15:16]. Connect with a URL and user details and assets, shots, tasks, thumbnails, frame ranges and descriptions appear in the DCC; set a task to work-in-progress, save, then add a note and change status and the whole team sees it [15:47-16:50]. Publishing an image sequence auto-converts it to video for review; reviewers approve or retake [16:50-17:20].
Media playlists feed daily, client or department reviews; with the open-sourced OpenRV, annotations can be attached to a note and pushed straight to Kitsu [17:20-19:24].

**Use it:** Model a review loop that way: playlist, annotate on frame, note with attachment, status change, all written back to the tracker.
