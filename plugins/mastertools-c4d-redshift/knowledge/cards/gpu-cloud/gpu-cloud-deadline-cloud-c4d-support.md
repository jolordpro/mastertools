---
id: gpu-cloud-deadline-cloud-c4d-support
title: AWS Deadline Cloud lists C4D 2024-2026 only, latest 2026.1 with Redshift 2026.2.0 (Dec 2025)
domain: gpu-cloud
tags: [deadline cloud, aws, cinema 4d, redshift, version, c4d 2027, submitter, c4d, version support]
applies_to: docs read 2026-10-30
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://docs.aws.amazon.com/deadline-cloud/latest/userguide/release-notes.html, https://docs.aws.amazon.com/deadline-cloud/latest/userguide/maxon-cinema-4d.html, https://github.com/aws-deadline/deadline-cloud-for-cinema-4d, src:research-agency-pipelines, src:research-gaps-deep, src:research-render-farms, https://www.youtube.com/watch?v=Sz-Bmxj4POU, src:yt-transcripts]
feeds: [PLAN 5b, version match, version-match check]
conflicts: none
---
No C4D 2027 entry in the docs read. Submit from Windows or macOS, render on Windows or Linux. GPU workers need system RAM at twice VRAM or may be unstable. Task chunking added Feb 2026; Assistant for failed jobs Apr 2026.
Nested Redshift proxies are not detected (documented limit), and a GitHub issue reports an out-of-memory Redshift job marked SUCCEEDED (unverified detail).
Merged from `pipeline-deadline-cloud-c4d-support`: Submit from Windows or macOS, render on Windows or Linux. Docs list C4D 2024, 2025, 2026 and Redshift natively. The 10 Dec 2025 note added C4D 2026.1 with Redshift 2026.2.0. No C4D 2027 entry was seen on 30 Oct 2026. GPU workers want system RAM of about 2x their VRAM or rendering may be unstable.

**Use it:** do not plan on Deadline Cloud for C4D 2027 until the docs list it.
Transcript support: AWS lists Cinema 4D and Redshift among conda-package apps. (https://www.youtube.com/watch?v=Sz-Bmxj4POU [19:50])
