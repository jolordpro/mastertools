---
id: gpu-cloud-spire-2022-resize-each-artists-vm-by-task-using-usage-logs
title: Spire Animation (2022): give each artist a cloud VM, change its GPU by task, and use usage logs to right-size it
domain: gpu-cloud
tags: [spire animation, rajesh sharma, coreweave, virtual workstation, a40, a4000, usage logs, right-sizing, onboarding, deep-read]
applies_to: Unreal Engine on CoreWeave virtual workstations, 2022
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=aJTLc7qQ1G0, src:yt-transcripts]
feeds: []
conflicts: none
---
Rajesh Sharma (VP engineering, Spire Animation Studios) and Jacob Feldman (CoreWeave) describe a studio founded in March 2020 with no on-prem hardware. A new artist's machine is provisioned automatically with the base image, DCCs, Python, USD and the studio's own tools, ready on day one [14:12, 20:58-21:30].
The spec is changed through the Kubernetes interface: an A40 for heavy ray-traced work, back to an A4000 for lighter tasks, or more RAM and a second GPU by restarting the VM [14:42, 17:17-18:19]. Sharma says the machine-usage logs are invaluable: an under-used machine is downgraded, one that keeps hitting limits gets more storage or a bigger spec [19:55]. Start from stopped to working takes under two minutes; works over weak café bandwidth, though the experience feels local on a fast link [20:27].

**Use it:** for a remote-workstation rental, plan to review usage monthly and switch GPU class per task rather than leaving the top card on all week.
