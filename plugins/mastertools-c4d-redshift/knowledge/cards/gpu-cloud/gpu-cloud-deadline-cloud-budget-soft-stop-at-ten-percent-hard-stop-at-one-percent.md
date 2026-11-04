---
id: gpu-cloud-deadline-cloud-budget-soft-stop-at-ten-percent-hard-stop-at-one-percent
title: Argo Casper's habit for Deadline Cloud budgets: soft stop at about 10 percent left, hard stop at about 1 percent
domain: gpu-cloud
tags: [aws, deadline-cloud, budget, stop-action, argo-casper, deep-read]
applies_to: AWS Deadline Cloud, webinar uploaded 2025-03
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PjafAJ0-6SA, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
He always sets both actions [16:35]. His usual thresholds are 10 percent and 1 percent of the budget remaining (he stumbled over the arithmetic aloud on a 333 dollar budget; the demo hard stop was under 30 dollars) [16:35-17:09].
Reason for the hard stop: one heavy render can blow through the remaining money before the next check [17:09].
Budgets can be edited later. A usage dashboard shows estimates and elapsed time; after a stable period he uses it to right-size the fleet [18:49].

**Use it:** suggest a two-step stop (finish-current-jobs, then kill) when the estimator or coach sets a cloud budget, and say the percentages are one person's habit.
