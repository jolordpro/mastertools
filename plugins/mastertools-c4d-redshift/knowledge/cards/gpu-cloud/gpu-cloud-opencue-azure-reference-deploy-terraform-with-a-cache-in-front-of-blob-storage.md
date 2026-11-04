---
id: gpu-cloud-opencue-azure-reference-deploy-terraform-with-a-cache-in-front-of-blob-storage
title: Microsoft's OpenCue-on-Azure sample (2020): Terraform builds a network, 16 x 64-core render nodes and a cache cluster in front of cheap blob storage
domain: gpu-cloud
tags: [opencue, azure, terraform, cache, blob, owen-bailey, deep-read]
applies_to: OpenCue on Azure, ASWF Open Source Day 2020
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=fnbRcTeKirw, src:yt-transcripts]
feeds: [pipeline]
conflicts: none
---
Owen Bailey (Microsoft): the deployment gives a virtual network with subnets, a server subnet open on only two ports (ssh and a VNC connection), the render nodes, and a caching cluster connected to blob storage [22:05-23:07].
Why cache: blob storage is cheap and durable but too slow to feed hundreds of nodes [23:07].
Demo size: 16 nodes of 64 cores, over 1,000 cores; Terraform apply takes roughly 20 minutes [26:24-27:42].
The server VM installs everything through cloud-init, with the database on the same VM (a known weakness he plans to split out); render nodes pull a setup script stored in the cache. Test scene was a pbrt render of the Moana island [28:46-30:50].

**Use it:** model for a small Redshift cloud: one control VM, N workers, a fast shared cache in front of cheap object storage; scripted setup so it can be torn down.
