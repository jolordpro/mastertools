---
id: pipeline-ocio-v2-speed-and-robustness-numbers
title: OCIO v2: CPU conversion up to 20x faster, integer buffers supported, over 1,000 tests; v2 final planned for end of 2020
domain: pipeline
tags: [ocio, performance, sse, unit tests, vfx reference platform, timeline, deep-read]
applies_to: OpenColorIO v2 (2020 preview, feature complete Aug 2020)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=7e0SSka8Ar8, src:yt-transcripts]
feeds: []
conflicts: none
---
CPU pixel conversion up to 20x faster through SSE on all ops (auto-disabled if the CPU lacks SSE); integer pixel buffers accepted so apps need not pre-convert to float [22:25-23:28]. Unit tests grew over 10-fold to more than 1,000, with GPU tests against CPU and a Python test framework; CI covers 10 Linux, 5 Mac, 5 Windows configs [27:09-28:45]. Feature-complete Aug 2020, four months of stabilisation, stable release end of 2020, part of VFX Reference Platform 2021 [29:24-30:59]. A processor cache keyed so unrelated context variables don't invalidate it [24:04].

**Use it:** Date-stamp as a 2020 plan; check which OCIO version a DCC ships before relying on v2 features.
