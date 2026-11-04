---
id: pipeline-deadline-submit-the-scene-and-use-job-not-hip
title: Submit the scene file to the repository and point assets with a project variable, not the scene's own folder
domain: pipeline
tags: [deadline, submit scene, $job, $hip, asset paths, houdini, tim van helsdingen, deep-read]
applies_to: Deadline, Houdini
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=v083eMXSwXw, src:yt-transcripts]
feeds: []
conflicts: none
---
If the scene is not submitted, the farm reads the live working file, so later edits change a running render [19:43-20:15]. If the scene is submitted, the farm opens a copy in the repository, so anything relative to the scene's folder ($HIP) breaks [20:15-20:46]. Use $JOB for caches and assets, and set it to the project location, as his folder structure does [20:46-21:18].

**Use it:** A pre-submit check: scene-relative paths break after submission; use project-rooted paths. Matches pipeline-pre-render-machine-checklist.
