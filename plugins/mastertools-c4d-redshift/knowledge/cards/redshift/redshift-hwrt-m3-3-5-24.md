---
id: redshift-hwrt-m3-3-5-24
title: Hardware ray tracing on Apple M3 arrived in Redshift 3.5.24 (Feb 2024) for final GPU renders, not for RT
domain: redshift
tags: [hardware ray tracing, m3, apple silicon, metal, 3.5.24, history, redshift]
applies_to: Redshift 3.5.24+
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.cgchannel.com/2024/02/maxon-releases-redshift-3-5-24, src:research-agency-pipelines, https://www.youtube.com/watch?v=L4riSkE7FwA, src:yt-transcripts, https://www.youtube.com/watch?v=RpiCCLHjlWQ]
feeds: [mac preset design, PLAN 5b]
conflicts: none
---
CG Channel's 2024-02-22 report is the origin of M3-class hardware ray tracing in Redshift. It applied to final GPU rendering; the old RT mode was not covered. Newer Mac notes are in the ledger (section 9).
Merged from `gpu-cloud-m3-hardware-ray-tracing-redshift`: Metal is a listed Redshift processing option; M3-generation hardware RT arrived for final GPU render. Apple-specific notes for 2026/2027 were not found.

**Use it:** use as history only; current Mac behaviour comes from the ledger.
Transcript support: M3 has hardware RT; M1 and M2 do not (March 2024 stream). (https://www.youtube.com/watch?v=L4riSkE7FwA [42:13])
Transcript support: in mid 2022 (RS 3.5) the trainer on a Mac had no hardware RT option; the other trainer saves it in the default scene on his PC (https://www.youtube.com/watch?v=RpiCCLHjlWQ [2:08:28-2:10:02])
