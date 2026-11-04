---
id: redshift-gpu-licence-per-node
title: Maxon: Redshift GPU rendering on network nodes needs one licence per node; the workstation subscription covers only that machine
domain: redshift
tags: [licence, license, render farm, node, team render, commandline, gpu, redshift licence, per node, farm licensing, maxon, redshift, farm]
applies_to: Redshift 2026
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://support.maxon.net/hc/en-us/articles/23810398005404-Understanding-how-Redshift-GPU-CPU-licenses-work-with-your-personal-workstation-and-render-farm-nodes, src:research-render-farms, src:research-gaps-deep, https://support.maxon.net/hc/en-us/articles/23810398005404, src:research-agency-pipelines, https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts, https://www.youtube.com/watch?v=1Gtp3BjlTjY]
feeds: [Phase 2 licensing, PLAN licensing; email Maxon first, PLAN 5b, licensing gate]
conflicts: none
---
Team Render Client does not bring a Redshift GPU licence. Redshift CPU through Team Render Client or Commandline needs no extra licence. The Maxon page returned 403 to the fetcher, so this comes from a search excerpt: re-read it by hand before relying on it.
Other farm facts (usage-based licensing, Conductor, Deadline Cloud) are left to the pipeline and gpu-cloud domains.
Merged from `pipeline-redshift-gpu-licence-per-node`: Read only through a search excerpt (the page returned 403). Team Render Client brings no Redshift GPU licence. Redshift CPU via Team Render Client or Commandline needs no extra licence. Team Render licences cannot drive Deadline, Qube or Royal Render; those need a Commandline licence (search snippet only).
Merged from `gpu-cloud-redshift-gpu-licence-per-node`: Redshift GPU on network nodes needs one licence per node. Team Render Client does not bring a Redshift GPU licence. Redshift CPU through Team Render Client or Commandline needs no extra licence. The Maxon page returned 403 to the researcher; this comes from a search excerpt of it.

**Use it:** treat per-node licensing as the gate in any farm or BYOL design until Maxon confirms otherwise in writing.
Transcript support: Greyscalegorilla: a Redshift licence is needed on every rendering machine. (https://www.youtube.com/watch?v=aheTC8N2xQg [34:37])
Transcript support: speaker says a second GPU node needs its own Redshift licence, about $40 a month by his figure; guesses CPU-only and Arm need none (unverified) (https://www.youtube.com/watch?v=1Gtp3BjlTjY [01:34-03:38])
