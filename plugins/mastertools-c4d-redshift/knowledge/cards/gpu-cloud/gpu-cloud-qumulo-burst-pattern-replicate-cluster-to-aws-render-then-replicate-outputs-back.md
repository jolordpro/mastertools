---
id: gpu-cloud-qumulo-burst-pattern-replicate-cluster-to-aws-render-then-replicate-outputs-back
title: Qumulo's burst recipe: start the same cluster in AWS in minutes, replicate the shots up, render, and replicate outputs back; host says burst always costs a premium
domain: gpu-cloud
tags: [storage, qumulo, aws, burst, replication, hybrid, sean-walbridge, deep-read]
applies_to: Qumulo, video uploaded 2022-07
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=XSqzTroN_ec, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Sean Walbridge (vendor): built-in replication lets an on-prem cluster copy to a cluster launched in AWS; 100 TB can be rendered on in the cloud, then the output replicates back [07:19-07:49]. He launched one live from a Terraform script in about the length of the chat [33:34-34:36]. The same replication engine can also move data to any S3-compatible bucket for archive and bring it back [31:32].
Host: studios usually stack options like a pyramid, general on-prem, rental machines, private cloud such as a leased room, and last public-cloud burst for a night or a week; burst is the costly tip and big sites keep data on-prem [08:20-09:21].
Sean: you cannot build on-prem for every peak [07:49].

