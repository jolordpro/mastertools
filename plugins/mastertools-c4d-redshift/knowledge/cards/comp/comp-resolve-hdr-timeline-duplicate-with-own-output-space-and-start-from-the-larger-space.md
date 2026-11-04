---
id: comp-resolve-hdr-timeline-duplicate-with-own-output-space-and-start-from-the-larger-space
title: For SDR plus HDR deliverables, duplicate the timeline, uncheck inherit in timeline settings and set the Rec 2020 ST 2084 output; start from the larger space
domain: comp
tags: [team-2-films, davinci-resolve, hdr, sdr, rec2020, st2084, deliverables, deep-read]
applies_to: DaVinci Resolve
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=w0ubDSzEEYg, src:yt-transcripts]
feeds: [[post-composite]]
conflicts: none
---
Because grading is done in DaVinci Intermediate, one SDR grade can be a starting point for HDR: duplicate the timeline, in Timeline Settings > Color untick the project inheritance, and set output colour space to Rec 2020 ST 2084 [17:42][18:15]. Best practice from him: begin the grade in the larger space, because making an SDR grade from an HDR one is easier than the reverse [18:15]. A screen recording will not show HDR correctly [18:15]. A power grade saved from one camera's clip gave fairly consistent results on ARRI and RED clips because the grade lives in the scene-referred space [17:11][17:42].

**Use it:** delivery step for an SDR + HDR spot: one scene-referred grade, two timelines. See comp-volpatto-derive-hdr-and-theatrical-from-one-grade-and-review-both-daily.
