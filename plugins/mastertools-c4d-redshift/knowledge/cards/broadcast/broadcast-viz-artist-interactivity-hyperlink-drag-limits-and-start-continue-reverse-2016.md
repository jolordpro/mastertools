---
id: broadcast-viz-artist-interactivity-hyperlink-drag-limits-and-start-continue-reverse-2016
title: Viz Artist interactivity (2016): the Hyperlink plugin drags objects with limits, and start plus a duplicated button using continue reverse works around no boolean
domain: broadcast
tags: [viz artist, hyperlink, data pool, interactivity, touch screen, director, start, continue reverse, 2016, deep-read]
applies_to: Viz Artist 3.x, uploaded 2016-02-10
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=i8J26rvFgnc, src:yt-transcripts]
feeds: [broadcast templates]
conflicts: none
---
Presenter unnamed. Hyperlink plugin [00:07-04:52]: set it to drag-for-rotation, position or scale on the left pick button; limit axes (spin only on Y by zeroing X and Z), lower sensitivity (100 was twitchy, 20 felt like a drag), and for position limit to the screen (about -350 to 350 on X, -180 to 180 on up) [01:12-03:17].
Triggering animation from a button [03:48-08:09]: build a director (cube intro, a 2 second move); a button's hyperlink runs a command on press that tells the stage's director to start; button feedback is a separate scale director triggered by a second command.
Data pool has no boolean, so one click cannot toggle [08:09]. Workaround: duplicate the button, name the field out, and use continue reverse instead of start, then swap which one is visible with alpha [08:09-10:20].

**Use it:** For a touch-screen graphic, plan one trigger per direction and swap visible buttons instead of expecting a toggle.
