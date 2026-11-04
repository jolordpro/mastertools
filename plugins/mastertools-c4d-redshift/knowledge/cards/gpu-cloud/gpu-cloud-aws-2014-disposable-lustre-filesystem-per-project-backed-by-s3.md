---
id: gpu-cloud-aws-2014-disposable-lustre-filesystem-per-project-backed-by-s3
title: AWS 2014 talk: keep everything in S3 and spin up a Lustre file system per project from one template, then delete it when the outputs are synced back
domain: gpu-cloud
tags: [aws, 2014, lustre, s3, cloudformation, disposable file system, render farm storage, usman shakil, gpu-cloud, deep-read]
applies_to: AWS EC2/S3/Lustre (2014); renderer Arnold, Maya 2015, Deadline
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=cm4sPe1nLjU, src:yt-transcripts]
feeds: [estimator, coach]
conflicts: none
---
AWS solutions architects (Usman Shakil and colleagues) at re:Invent 2014 built a pretend three-person VFX studio in the cloud. S3 holds textures, scripts, images and outputs [05:17-06:21]. For each project a CloudFormation template launches a Lustre file system that pre-fetches the folder tree from a named S3 bucket [08:27-09:30]. Storage nodes and metadata nodes can be added as the job grows, outputs sync back to S3, and the file system is deleted when the project ends [09:30-11:02].
The talk calls this a disposable file system: nothing precious lives on it, so there is nothing to keep paying for between jobs [10:00-11:02]. Archive the bucket to Glacier afterwards [10:00].
Caveat: 2014 services and names; the pattern is what transfers, not the products.

**Use it:** when advising on a cloud farm, ask where the source of truth lives and whether the working storage can be thrown away per job.
