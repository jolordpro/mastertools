---
id: gpu-cloud-deadline-cloud-2024-cost-guards-spot-max-workers-delete-unused
title: Deadline Cloud cost guards from beginner tutorials: spot, a low worker cap, budgets, and delete unused farms
domain: gpu-cloud
tags: [deadline cloud, cost control, spot, max workers, budget, bill shock, render licence, aws, 2024, deep-read]
applies_to: AWS Deadline Cloud, 2024
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=kyaphnaCDEU, https://www.youtube.com/watch?v=LZ-VaD5MZTk, src:yt-transcripts]
feeds: []
conflicts: none
---
Both presenters warn it gets expensive fast. Controls shown: choose spot (up to about 90% off, compute others are not using; on-demand when you need a GPU for the whole run) [06:21, D1; 06:50, D2]; set the fleet's auto-scaling maximum low (one presenter used 10, the other 1; it can reach thousands) [06:52, D1; 06:50, D2]; budgets exist and are set up after the wizard to avoid bill shock [01:36, D1]; delete the farm when unused [08:21, D2]. Billing note [08:25, D1]: you pay compute plus a renderer licence per use, not an editor licence, and no buckets of prepaid render time as in older Deadline. S3 rules can archive or double as a backup [05:16].

**Use it:** default recommendations in a cost checklist: spot first, cap max workers on the first run, add a budget before real jobs.
