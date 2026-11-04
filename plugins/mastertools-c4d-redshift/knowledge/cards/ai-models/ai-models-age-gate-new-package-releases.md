---
id: ai-models-age-gate-new-package-releases
title: Delay pulling new package or model releases by 24 hours to a week, since compromised releases are usually pulled quickly
domain: ai-models
tags: [age gating, supply chain, packages, dependencies, malware, xz, update delay]
applies_to: any (2026 talk)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=xs5m-KEHqLk, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
[12:23] Many attacks need people to take the newest release; a delay of 24 hours or a week lets maintainers catch and remove it.
He cites open-source malware up 75% over the year (source not named) [10:20] and the XZ backdoor, found because logins ran half a second slower [10:51].

**Use it:** suggest age-gating updates for any ComfyUI or plugin set on render nodes.
