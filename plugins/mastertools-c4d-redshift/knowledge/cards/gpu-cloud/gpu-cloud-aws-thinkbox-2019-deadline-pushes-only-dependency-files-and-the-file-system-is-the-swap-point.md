---
id: gpu-cloud-aws-thinkbox-2019-deadline-pushes-only-dependency-files-and-the-file-system-is-the-swap-point
title: AWS Thinkbox 2019: Deadline walks the scene's dependencies and syncs only what it needs through S3 and EBS; Weka, Qumulo or FSx replace EBS for thousands of parallel workers
domain: gpu-cloud
tags: [deadline, s3, ebs, weka, qumulo, fsx for lustre, fsx for windows, asset sync, siggraph 2019, deep-read]
applies_to: AWS Deadline 10 hybrid storage, 2019
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=Fl_FdVgp2E0, src:yt-transcripts]
feeds: [CHECKS, estimator]
conflicts: none
---
Out of the box Deadline syncs between on-prem and S3, then hydrates EBS volumes that feed the render nodes [16:18-17:09]. It reads the dependency tree and pushes only what the job needs, not terabytes of the whole file set [17:09-17:40]. When 300-400 parallel instances grow to 3,000-4,000, people swap the EBS tier for Weka (elastically scaling HPC file system) or Qumulo (hybrid with on-prem sync) [17:40-19:46]. AWS's own managed options are FSx for Lustre (compute-heavy Linux) and FSx for Windows [19:46-20:48]. Forecasting render demand is hard, so being able to expand the file system at once matters [18:43].

**Use it:** a scene check should resolve every dependency before upload; unresolved paths are what break cloud renders. The pattern 'storage tier scales with node count' is the cost step to model.
