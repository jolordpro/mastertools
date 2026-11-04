---
id: pipeline-deadline-priority-concurrent-tasks-and-frames-per-task
title: Deadline lets a higher-priority job take the farm; tune concurrent tasks and frames per task to the machine
domain: pipeline
tags: [deadline, priority, concurrent tasks, frames per task, job pause, tim van helsdingen, deep-read]
applies_to: Deadline 10
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=v083eMXSwXw, src:yt-transcripts]
feeds: []
conflicts: none
---
Higher priority jumps ahead (a 60 beat a 50 once the running tasks finished) [25:27-27:36]. Concurrent tasks run several tasks at once on one machine, useful when cores or RAM sit idle: he used 3 for a Redshift scene [24:57-26:01]. Frames per task: more per task for fast frames, because each task has start-up overhead [26:01]. GPU affinity and machine lists are also available [28:07]. In his demo the lower-priority job finished its running tasks, then the higher one took over [26:33-27:36].

**Use it:** Use priority only for real emergencies; match concurrent tasks to idle resources.
