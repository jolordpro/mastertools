---
id: broadcast-safe-areas-st2046
title: SMPTE ST 2046-1 safe areas: action safe 93%, title safe 90%; on 1920x1080 title safe is 1728x972 (margins 96 px sides, 54 px top and bottom)
domain: broadcast
tags: [safe area, title safe, action safe, st 2046-1, rp 218, 1080p]
applies_to: ST 2046-1
status: V2
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://pub.smpte.org/doc/st2046-1/, https://pub.smpte.org/pub/rp218/rp0218-2009.pdf, src:research-production-pipelines]
feeds: [safe-area overlay]
conflicts: none
---
Pixel figures are our arithmetic; action safe 93% is about 1786x1004. The older RP 218 90%/80% geometry is deprecated except for CEA-708 captions. EBU R 95 numbers were not retrieved.

**Use it:** overlay on every draft; check text and logos sit inside title safe.
