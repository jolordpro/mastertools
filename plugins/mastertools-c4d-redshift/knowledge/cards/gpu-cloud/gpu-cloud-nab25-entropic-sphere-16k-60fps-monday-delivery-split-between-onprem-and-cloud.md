---
id: gpu-cloud-nab25-entropic-sphere-16k-60fps-monday-delivery-split-between-onprem-and-cloud
title: Entropic delivered a 16K 60 fps Sphere piece by splitting Sunday-night client changes between its on-prem farm and a cloud farm
domain: gpu-cloud
tags: [entropic, nathan-robinson, andrew-sonagra, sphere, 16k, cloud-burst, deadline-cloud, gpu-cloud, deep-read]
applies_to: AWS Deadline Cloud
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=-Ks7SSgeHGg, src:yt-transcripts, https://www.youtube.com/watch?v=7DpHiT0CCSA]
feeds: [estimator]
conflicts: none
---
NAB 2025 panel. Entropic's Nathan Robinson: on a Sphere (Las Vegas) project at 16K, 60 frames per second (captions garbled around the format, "16k 902 piece"), client notes landed on Sunday night for a Monday delivery; the on-prem farm rendered one section while a cloud farm rendered another, and it shipped [03:16-03:47]. His summary rule: agility is the business, no renting another 300 nodes, you spin up 300 nodes without worrying about cooling or power [03:47-04:18]. Andrew Sonagra (also Entropic): on-prem farms mean fighting for priority between jobs and producers arguing over whose shots go first; in the cloud each job gets its own dedicated farm, so nobody steps on anyone [01:11-02:13]. Entropic is 27 years old [04:18]. The panel was moderated by an AWS Deadline Cloud product manager, so it is a customer story staged by the vendor.

**Use it:** when planning a rush, split the frame range between local nodes and a cloud farm rather than all-or-nothing, and give each rush job its own queue so priority fights do not delay it.
Transcript support: Cinesite (2020): the same hybrid pattern, with an escalation order and an 80-85% on-prem target. (https://www.youtube.com/watch?v=7DpHiT0CCSA [14:31-15:02])
