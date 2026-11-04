---
id: pipeline-rise-interactive-director-session-in-solaris
title: Rise ran director camera sessions in Solaris with Karma previews, backing up with three open instances
domain: pipeline
tags: [rise, director session, camera, solaris, karma, previs, stability, deep-read]
applies_to: Houdini Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jpbMbafS9FY, src:yt-transcripts]
feeds: [pipeline plan]
conflicts: none
---
The client asked for an interactive session with the director on full-CG shots. Switching between shots with camera and boat animation, plus fast Houdini GL to Karma toggles, gave previews better than a playblast, with correct light and shadow, which they said was crucial for judging layout [44:19-44:51].
Stability was the worry: the first session ran with three copies of the same Houdini file open. More than six sessions of one hour or more ran without a crash [44:51]. Cameras created were pushed to Maya for tweaks [45:21].

**Use it:** Live client sessions: prep a backup instance and a fast preview mode.
