---
id: pipeline-mig-dual-use-gpu-nodes
title: NVIDIA MIG lets one workstation card be split for artist, render or AI use
domain: pipeline
tags: [mig, vgpu, vdi, rtx 6000 blackwell, proxmox, hp anyware]
applies_to: SIGGRAPH 2026 recap
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=F97verNmkmU, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
MIG splits an RTX 6000 Blackwell or RTX 4500 server card into isolated slices [11:25].
Idea: workstation by day, render or AI node at night. Nearly everyone in the room was hit by HP Anyware end of life; Proxmox is the main replacement [10:55-11:56].

**Use it:** an on-site capacity model may count nights as render hours.
