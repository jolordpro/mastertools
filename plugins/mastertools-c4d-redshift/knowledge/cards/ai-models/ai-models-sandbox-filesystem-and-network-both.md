---
id: ai-models-sandbox-filesystem-and-network-both
title: Run untrusted AI code in its own process with limits on both filesystem and network; one without the other leaks shots
domain: ai-models
tags: [sandbox, filesystem, network, process isolation, least privilege, supply chain, ai code]
applies_to: any (2026 talk)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=xs5m-KEHqLk, src:yt-transcripts]
feeds: [intake, coach]
conflicts: none
---
[11:21] Blocking the filesystem while leaving the network open lets untrusted code ship your shots out.
Sandbox runtimes named: Anthropic's sandbox runtime and Microsoft's Hyperlight micro-VM [11:53]. Scan dependencies including models and packages.

**Use it:** advise both limits when a user installs community nodes or plugins.
