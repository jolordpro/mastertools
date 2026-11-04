---
id: pipeline-deadline-redshift-standalone-rs-export-then-submit-as-a-redshift-job
title: Deadline with Redshift: export the frame range as Redshift Proxy/standalone .rs files, then submit them as a Redshift job so the farm needs no Cinema 4D
domain: pipeline
tags: [deadline, redshift standalone, rs files, proxy export, render management, glass hand, deep-read]
applies_to: Deadline 10 era, Redshift in C4D (video undated, about 2019)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=CMVilcuF5dg, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Two routes: submit the C4D scene normally from the Deadline menu, or use Export, Redshift Proxy with a frame range, creating one .rs file per frame (0 to 268 in the demo) [03:34-05:19].
In Deadline Monitor choose Submit, Redshift; point at the sequence and it counts the files itself; add comments (he notes resolution), department, priority and an output directory [05:19-06:22]. Right-click a job for 'notify me when complete', job reports, history and output [06:22].
Speaker (Brandon Clements, Glass Hand) says the standalone route is the one that works with the AWS portal and any DCC with the Redshift plugin [04:16-05:19]. The Cinema 4D submitter is a .pyp in the plugins folder; Monitor lets you requeue one task or all tasks from a machine [13:09-14:45].

**Use it:** Pipeline option: bake frames to .rs when the farm has no C4D licence or version to match.
