---
id: redshift-aov-direct-output-per-aov-settings
title: Let Redshift save the AOVs (Multi-Part EXR, Direct Output) to set bit depth and compression per AOV and shrink 4K files
domain: redshift
tags: [multi-part exr, direct output, dwaa, half float, aov file size, compression]
applies_to: Redshift 2024
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [delivery steps, estimator]
conflicts: none
---
Tick the Redshift AOV save option to bypass the C4D save, use half float with DWAA compression [09:42]. Multi-Part EXR with Direct Output gives each AOV its own data type, bits and compression [16:59]; at 4K some passes need not carry full bits [17:29]. A regular JPEG save can serve as a thumbnail for clients [18:32]. Cryptomatte always exports as a separate file [25:19]. Reported data-pass guidance elsewhere: half for data, full for lighting.

**Use it:** Estimate output size per AOV, and offer lighter settings for data passes.
