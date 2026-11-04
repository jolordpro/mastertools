---
id: broadcast-ebu-r103-levels
title: EBU R 103: flag out-of-range levels only when more than 1% of the picture is affected
domain: broadcast
tags: [broadcast, legal levels, gamut, qc, ebu, r103, clipping]
applies_to: EBU R 103 v3.0 (May 2020)
status: V
confidence: high
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://tech.ebu.ch/docs/r/r103.pdf]
feeds: [CHECKS 9, shakedown broadcast-legal]
conflicts: none
---
R 103 v3 gives preferred min/max code values for the active picture, measured after a filter. Call it out of gamut only when the error exceeds 1% of the image.

**Use it:** check 9 shows a map plus the percentage, and flags over 1%.
