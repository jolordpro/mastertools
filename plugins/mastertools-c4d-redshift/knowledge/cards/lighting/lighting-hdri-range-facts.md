---
id: lighting-hdri-range-facts
title: HDRI facts: use scene-linear 32-bit EXR with an unclipped sun; a sun-in-frame capture spans about 21-24 EV
domain: lighting
tags: [lighting, hdri, exr, dynamic range, sun, ev]
applies_to: any
status: V2
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.blendernation.com/2016/04/21/hdri-27-evs-dynamic-range/, src:research-production-pipelines]
feeds: [PLAN HDRI health check]
conflicts: none
---
No formal HDRI standard was found.
A forum rule says an HDRI below roughly 10,000:1 range gives ambient light only; one user's claim, weak.
The 21-24 EV figure comes from a well-known HDRI maker's post (search summary).

**Use it:** treat these as guidelines, not pass/fail limits.
