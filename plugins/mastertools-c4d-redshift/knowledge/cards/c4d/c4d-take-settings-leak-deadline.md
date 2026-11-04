---
id: c4d-take-settings-leak-deadline
title: The Deadline C4D submitter pulled format, fps and frame range from the active take, mixing output in one job
domain: c4d
tags: [takes, deadline, farm, active take, output, submitter, c4d, output path, take token, overwrite]
applies_to: Deadline 10 C4D submitter
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://forums.thinkboxsoftware.com/t/deadline-c4d-uses-different-render-settings-for-a-take-on-every-other-task/27957, src:research-agency-pipelines, src:research-gaps-deep, https://irendering.net/cinema-4d-redshift-takes-render-farm/]
feeds: [take-aware preflight, CHECKS 4]
conflicts: none
---
A forum thread reports settings taken from the main or active take rather than the target take, with mixed output within one job. Workarounds: set the active take before submit, or split files per take. No confirmed fix.
Deadline Cloud's C4D docs do not mention Takes.
Merged from `pipeline-deadline-c4d-takes-leak`: A forum thread shows mixed output inside one job because some settings came from the main or active take. Workarounds: set the active take before submit, or split files per take; no confirmed fix. A vendor guide (unverified) says takes overwrite each other without a take token in output paths, and Redshift Direct AOV paths hard-coded to one folder collide too. Deadline Cloud's C4D docs do not mention Takes.

**Use it:** preflight resolves every take's resolution, fps, range, camera, output path and AOV path, and submits one take per job.
