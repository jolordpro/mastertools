---
id: pipeline-deadline-budget-limit-actions
title: Deadline Cloud budgets per queue can stop work automatically at a spending threshold
domain: pipeline
tags: [deadline cloud, budget, limit, usage explorer, cost, queue]
applies_to: AWS Deadline Cloud (May 2026)
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=5qY4LFDbNnE, src:yt-transcripts, https://www.youtube.com/watch?v=PjafAJ0-6SA]
feeds: [estimator, CHECKS]
conflicts: none
---
The usage explorer breaks spend down by queue, job and user in real time [02:06].
A queue budget can have automated actions that stop work when a threshold is reached [02:06].

**Use it:** the estimator can model a spend cap on the queue and show a stop threshold at submit.
Transcript support: adds the two action types in practice (soft stop after current jobs, hard stop now), the 10 and 1 percent habit, and that a required budget with a bad date range blocks the queue (https://www.youtube.com/watch?v=PjafAJ0-6SA [16:04])
