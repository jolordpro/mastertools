---
id: gpu-cloud-home-farm-old-desktops-vs-mining-rig-vs-used-8-gpu-server
title: Building a home GPU farm: old desktops waste power, mining rigs starve on one PCIe lane, a used 8-GPU server is the better route (Blender view, 2024)
domain: gpu-cloud
tags: [home render farm, mining rig, pcie lanes, gpu server, supermicro, blender, power draw, used hardware, 2024, deep-read]
applies_to: Blender GPU rendering; consumer GPUs, Jan 2024
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=fdBdWJfwRVA, src:yt-transcripts]
feeds: []
conflicts: none
---
Contradiction Tech (channel owner, hobbyist). Old Dell workstations (T3600) cost a couple of hundred dollars but each has a ~300 W supply that fits only one or two GPUs, and every CPU and RAM stick burns power; he starts each render by remote-logging into every machine with a shared Blender file [01:04-02:37].
Mining rig: plenty of GPU slots but each is one PCIe lane, a weak old i3 to i7 CPU and 8 GB single-stick RAM; scene loading every frame makes it slow [03:41-05:48]. Suggestion: a refurbished dual-CPU GPU server (Supermicro example, just under $1,100 on eBay with no GPUs) with eight full x16 double-width slots; one motherboard to power; consumer GPUs are fine for Blender without data-centre licences; Linux server OS, so a learning curve [07:53-11:28].

**Use it:** a checklist for an in-house GPU box: lanes per card, PSU headroom, slot width, cooling; applies to Redshift too, but he only tested Blender.
