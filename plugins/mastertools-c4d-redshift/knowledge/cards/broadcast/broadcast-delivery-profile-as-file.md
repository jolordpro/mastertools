---
id: broadcast-delivery-profile-as-file
title: QC tools ship a profile per destination (DPP, Netflix, broadcaster); the platform's delivery check should be a profile file per client, not code
domain: broadcast
tags: [delivery profile, qc profile, dpp, netflix, codec, range, alpha, frame rate, safe margins]
applies_to: any
status: U
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [src:research-production-pipelines, src:research-vfx-pipelines]
feeds: [delivery check]
conflicts: none
---
Fields: codec, bit depth, range, alpha type, fill and key or embedded, frame rate, safe margins, colour tags, container signalling. The check runs on the real output file. US sports usually run 59.94p or 29.97 (our assumption; confirm with the broadcaster).

**Use it:** one profile per client, edited by the user.
