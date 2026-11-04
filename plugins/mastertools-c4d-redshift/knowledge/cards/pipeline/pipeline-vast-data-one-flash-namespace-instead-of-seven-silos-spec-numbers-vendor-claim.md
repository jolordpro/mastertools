---
id: pipeline-vast-data-one-flash-namespace-instead-of-seven-silos-spec-numbers-vendor-claim
title: Vast Data pitch, one all-flash namespace replaces separate edit, color and transcode silos; spec numbers 40 GB/s read and 5 GB/s write per enclosure, 600 TB usable block
domain: pipeline
tags: [vast-data, howard-marks, all-flash, qlc, nas, single-namespace, nfs, smb, vendor-claim, pipeline, deep-read]
applies_to: any (2022 hardware)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=lCr3vIKUpwo, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Howard Marks (technologist at Vast, so a sales view; talk from August 2022). Design: compute servers (C nodes) run the storage logic; enclosures hold cheap QLC flash plus Optane-class write buffers; all connect over NVMe fabric, and compute and capacity scale independently [04:14-06:48]. Claims: one pool replaces about seven stage-specific systems (edit, colour, transcode) and avoids data moving between them [09:56-10:27]; 200 TB to 50 PB is one namespace, shared over NFS and SMB with quotas, no client agents [10:27-11:28]. One enclosure delivers 40 GB/s read and 5 GB/s write [18:12-18:42]; a building block is 600 TB usable, licensed from 100 or 200 TB [26:58-28:01]; a minimal system is 1 or 2 enclosures, a pair of 100 GbE switches and a 4-server 2U compute appliance [28:01]. Data protection tolerates up to 4 SSD failures at about 3% overhead against the usual 20-30% [08:21]; VFX assets like Houdini data reduce 2:1 to 3:1 [09:24]. Rolling upgrades are claimed to be invisible even for SMB sessions [23:53]. Roadmap said: a 1U 338 TB enclosure and SMB multichannel [33:42-34:14]. Marks says Vast does not sell hardware; the customer buys at cost and pays a capacity-based subscription, rate locked up to 10 years [16:07-16:40].

**Use it:** use as a spec sheet for what a modern all-flash NAS claims; verify any number against Vast's current docs before quoting it.
