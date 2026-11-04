---
id: pipeline-hofmann-check-server-space-before-overnight-batch
title: "Hofmann's failure story: an overnight render batch filled the server and killed every other project's renders; check free space first"
domain: pipeline
tags: [polish, deep-read, falk hofmann, rise fx, render, disk space, failure, oblivion]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://benmcewan-website.pages.dev/blog/interview-falk-hofmann-compositing-supervisor, src:polish-roster]
feeds: [polish-coach]
conflicts: none
---
On Oblivion pre-production he had set up many dependencies to render about 13 HD tiles per scenery overnight, with proof QuickTimes due by morning. He never checked space left, filled the whole server to the last kilobyte and every other running render failed; it happened a second time [§3-§4]. He now checks free space repeatedly and is very careful with the main server [§4].

**Use it:** Before queuing a big overnight batch, estimate output size against free space on the target volume.
