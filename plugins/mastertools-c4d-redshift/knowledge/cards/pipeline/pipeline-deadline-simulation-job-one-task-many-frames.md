---
id: pipeline-deadline-simulation-job-one-task-many-frames
title: Submit a simulation to Deadline as one task covering all frames; one frame per task restarts the sim every frame
domain: pipeline
tags: [deadline, simulation, frames per task, houdini, render manager, tim van helsdingen, deep-read]
applies_to: Deadline 10, Houdini 18
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=v083eMXSwXw, src:yt-transcripts]
feeds: []
conflicts: none
---
For sims, set frames per task very high (he used 120 for a 120 frame sim) so the whole sim is one task [21:18-22:23]. With 1 frame per task the sim starts over each frame [21:18]. For renders, use fewer frames per task, balancing start-up time against frame time [26:01-26:33].

**Use it:** A farm advisor should flag 'simulation job with frames-per-task of 1'.
