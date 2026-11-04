---
id: gpu-cloud-aws-storage-choice-s3-is-about-ten-times-cheaper-than-efs-fsx-is-the-easy-hybrid
title: AWS render storage: S3 is about a tenth the cost of EFS (his guess: 50 dollars a month for 2 TB), FSx is the easy middle that mounts on the workstation
domain: gpu-cloud
tags: [aws, s3, efs, fsx, storage, cost, argo-casper, deep-read]
applies_to: AWS, webinar uploaded 2025-03
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=PjafAJ0-6SA, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Three options: managed file system (EFS), object storage (S3), and FSx in the middle [32:16-32:47].
FSx mounts as a folder on the local workstation but lives in AWS, so files are in both places and nothing needs transferring at render time [32:47-33:48].
Cost: 2 TB of assets is cheap in S3 (he says maybe 50 dollars a month, unsure) while EFS costs about ten times more; pay more for quick setup, less if you have the time and skill [34:18-35:24].
Storage is a large share of cloud cost for big data sets [35:24].

**Use it:** when comparing cloud storage for a project, quote price per TB-month and the setup effort side by side; do not copy his dollar figure without checking today's price.
