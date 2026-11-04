---
id: pipeline-qumulo-analytics-found-nine-terabytes-of-uncleaned-ifd-files-in-under-a-week
title: Sean Walbridge: storage analytics found nine terabytes of Houdini IFD files a missing cleanup job had left behind, and a directory quota stopped a runaway render
domain: pipeline
tags: [storage, qumulo, analytics, houdini, cleanup, failure-story, sean-walbridge, deep-read]
applies_to: Qumulo, video uploaded 2022-07
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=XSqzTroN_ec, src:yt-transcripts]
feeds: [shakedown]
conflicts: none
---
Sean Walbridge (Qumulo; earlier at Atomic Fiction, Montreal) tells two cases from his studio days [09:53-10:54].
A cleanup job that should have deleted Houdini IFD files after each render was not running; storage grew steadily for under a week until about 9 TB had piled up, and real-time directory analytics traced it [10:23-10:54].
On another day a render was filling disk fast; he put a quota on that directory, the render failed, and that told him which shot it was [09:53-10:23].
He also checks Monday mornings after a weekend of unexplained growth by clicking a capacity jump to see which directories grew [28:28-29:29].

**Use it:** the platform's disk check should compare scratch growth rate to expected, and every render job should have a delete-on-success step that is itself verified.
