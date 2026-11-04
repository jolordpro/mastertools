---
id: pipeline-deadline-scheduling-modes
title: Deadline Cloud has three scheduling modes: priority FIFO, priority balanced, and weighted balanced
domain: pipeline
tags: [deadline cloud, scheduling, priority, fairness, queue, aws]
applies_to: AWS Deadline Cloud (May 2026)
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=5qY4LFDbNnE, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
FIFO gives all workers to the top priority job first. Priority balanced spreads workers evenly over jobs at the top priority. Weighted balanced also uses error count, submission time and number of tasks [03:11-04:13].

**Use it:** the queue UI should explain which mode is active and its effect on wait.
