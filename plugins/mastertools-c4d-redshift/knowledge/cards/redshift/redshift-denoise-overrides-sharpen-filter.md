---
id: redshift-denoise-overrides-sharpen-filter
title: Denoise may silently fall back to a Gauss-style filter, losing a Lanczos sharpening look (single-source recollection)
domain: redshift
tags: [denoise, lanczos, filter, sharpness, bump]
applies_to: Redshift 2026
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=aheTC8N2xQg, src:yt-transcripts]
feeds: [coach, redshift]
conflicts: none
---
Chad says a Lanczos filter (size about 4) used to give a crunchy sharp look, but with denoise on Redshift quietly uses Gauss; he is not sure it is still true and asks for corrections [1:11:54-1:12:55]. To get the sharp look he turns denoise off and pays the render time.

**Use it:** coach: mention it as an unverified gotcha; verify on the target version before relying on it.
