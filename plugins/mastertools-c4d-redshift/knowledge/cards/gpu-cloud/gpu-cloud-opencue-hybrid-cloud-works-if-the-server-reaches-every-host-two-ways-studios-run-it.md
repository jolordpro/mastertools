---
id: gpu-cloud-opencue-hybrid-cloud-works-if-the-server-reaches-every-host-two-ways-studios-run-it
title: OpenCue (2020) supports on-prem plus cloud burst in one deployment as long as hosts can reach the server; studios either keep two deployments or one with instance groups per location
domain: gpu-cloud
tags: [opencue, hybrid, cloud-burst, brian-cipriano, deep-read]
applies_to: OpenCue 0.4.55, ASWF Open Source Day 2020
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=fnbRcTeKirw, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Brian Cipriano: nothing in OpenCue blocks one deployment spanning on-prem and cloud; licensing, file access and asset availability on the cloud nodes are on you [44:56-45:59].
Two patterns in use: separate cloud and on-prem deployments, where approved shows get resource limits to go to cloud; or one deployment with instance groups in different places [45:59-46:29].
A cloud-manager plugin for the GUI (GCP, Azure, AWS groups, from a Google Summer of Code student) was in progress, built so it would not interfere with existing cloud setups [04:10-04:40, 46:29-47:32].
The database can be moved to a managed cloud database if wanted [40:12-41:14].

**Use it:** for a small shop, start with one deployment and a single instance group of cloud nodes rather than two systems.
