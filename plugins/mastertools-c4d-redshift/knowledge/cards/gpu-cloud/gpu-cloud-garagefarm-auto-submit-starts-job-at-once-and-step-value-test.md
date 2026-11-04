---
id: gpu-cloud-garagefarm-auto-submit-starts-job-at-once-and-step-value-test
title: GarageFarm's Auto Submit option starts a job the moment it uploads; test cost by rendering every Nth frame with the step value
domain: gpu-cloud
tags: [garagefarm, auto submit, step value, test render, render beamer, estimate, deep-read]
applies_to: GarageFarm Render Beamer, Blender plugin (2021)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=6y4PSQOsJck, src:yt-transcripts]
feeds: [estimator, CHECKS]
conflicts: none
---
Gotcha: with Render Beamer's Auto Submit ticked, the project starts rendering as soon as the upload finishes at default medium priority, so you cannot test first or pick priority [05:15-05:46]. Untick it and use the web manager to set priority [07:19]. The plugin warned to run a test render but offered no button for it [04:14]; the farm's operations director later explained the answer [08:19-08:50]: set the step value so only every Nth frame renders (for example every 20th), read the average cost per frame, and multiply by the frame count. Upload took almost 20 min with unneeded large files in the project [04:45-05:15].

**Use it:** Matches the estimator idea: price a sample of frames on the farm, then scale. Remove unneeded assets before upload.
