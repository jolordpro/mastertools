---
id: pipeline-vast-data-render-workload-is-90-percent-read-so-qlc-endurance-is-not-the-issue
title: VFX storage traffic is roughly 90% reads and 10% writes, and thousands of render hosts hit one updated asset at once; a vendor argues QLC flash copes with that
domain: pipeline
tags: [vast-data, howard-marks, read-write-ratio, qlc, endurance, render-farm, many-hosts-one-file, pipeline, deep-read]
applies_to: any
status: V
confidence: low
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=lCr3vIKUpwo, src:yt-transcripts]
feeds: [estimator]
conflicts: none
---
Host Joe states the rule of thumb of 10 to 1 read to write for VFX and animation ("a broad generalization but it holds up") [16:40]. Pattern: one artist updates a texture or look and thousands of hosts, dozens of artists, and thousands of frames then read that one file [17:11-17:41]. Marks's (vendor) explanation of why QLC flash survives: writes land in a high-endurance buffer, then go to QLC in 1 MB stripes with 1 GB erase blocks; small random writes cut QLC endurance to about one twentieth of large sequential writes [12:29-14:35]; data is grouped by expected life, with temp files in their own stripes so garbage collection moves less [15:05-15:36]. Reads do not wear flash noticeably [17:11]. Caution: the 90:10 split is the host's estimate for a studio, not a measurement.

**Use it:** size read throughput first for a render farm and treat writes (frame output, caches) as the smaller side; for sim caches the ratio can be different.
