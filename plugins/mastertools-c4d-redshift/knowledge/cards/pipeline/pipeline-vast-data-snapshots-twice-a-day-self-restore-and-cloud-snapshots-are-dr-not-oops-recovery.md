---
id: pipeline-vast-data-snapshots-twice-a-day-self-restore-and-cloud-snapshots-are-dr-not-oops-recovery
title: Studios typically take a couple of snapshots a day plus a nightly one for oops recovery; snapshots to cloud or tape are a disaster-recovery tier, not a fast undo
domain: pipeline
tags: [vast-data, snapshots, restore, tape, disaster-recovery, s3, howard-marks, pipeline, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=lCr3vIKUpwo, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Host Joe: the usual studio pattern is a couple of snapshots a day plus a bigger nightly round, used mainly to roll back that day's mistakes quickly [34:46-35:49]. Marks: users can restore their own files from a .snapshot folder at each mount point; snapshot to S3 is more of a backup or DR path and the system is both file and object (write via NFS, read via S3) [34:14-35:49]. Joe's point: finding a mistake three weeks later means pulling from tape, which ties up drives and can take days, not minutes [35:49-36:50]. This supports the existing storage-restore card.

**Use it:** a pipeline needs both layers: frequent local snapshots for artist undo, and a slower off-site copy for disaster recovery; do not count the second as the first.
