---
id: pipeline-polish-cave-failed-checks-stay-in-pipe-but-never-go-to-client
title: "CAVE: an element that fails tech checks or a client round can keep feeding the pipeline, but only a tech-checked version goes to the client"
domain: pipeline
tags: [cave academy, production statuses, tech check, published, client review, element in pipe, polish, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://caveacademy.com/wiki/production/production-statuses/, src:polish-roster]
feeds: [pipeline]
conflicts: none
---
Published-Element-In-Pipe means internally approved but failed tech checks: use it downstream, but do not send it to the client [§5]. Published-Element-Approved passes the tech checks and may go to the client [§6]. Published-Proposed-Final marks it on its way to the client, and the team prefers it to be an approved element rather than an in-pipe one [§6]. After a client decline the element stays in the pipeline as in-pipe while the requested tweaks go back to WIP [§5].

**Use it:** Tell users to keep downstream work moving with a flagged in-pipe version while fixes happen, and never pass that version to the client.
