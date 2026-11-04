---
id: pipeline-lab-render-farm-project-on-shared-storage-relative-paths-frame-list-and-logged-in-workers
title: Shared-farm submission checks (Maya + V-Ray + Deadline lab): project and assets on the shared drive with relative paths, frame list and project path correct in the submit box, workers must be logged into the render account
domain: pipeline
tags: [jack-stenner, deadline, maya, v-ray, shared storage, render farm, submit, deep-read]
applies_to: Maya, V-Ray, Thinkbox Deadline (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=rwipw4o4gMQ, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Twelve lab machines; every file must sit on the shared storage because other machines cannot read a local drive, desktop or USB [00:04-01:36]. Set the Maya project on the shared drive and keep everything relative [00:35]. Example wireframe: 240 frames at 1080p, 4 min 24 s per frame, so use the farm, not a local batch [02:07-03:40]. Submit: leave defaults, check frame list 1-240 and project path (wrong path means the project was not set) [05:23]. Machines in use or not logged in to the render account do not contribute [06:27-06:57]. Deadline Monitor shows errors, job reports (missing files) and lets you view output frames [07:42-09:17]. He renders PNG for the demo, EXR normally [03:40].

**Use it:** Pre-submit checklist items for any farm: shared paths, frame range, project path, worker availability.
