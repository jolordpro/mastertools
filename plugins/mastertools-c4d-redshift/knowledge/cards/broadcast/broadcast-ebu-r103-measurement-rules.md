---
id: broadcast-ebu-r103-measurement-rules
title: R 103 measurement rules: ignore pixels outside the active picture, filter first (1/16 2/16 3/16 4/16 3/16 2/16 1/16 horizontal), and do not legalise before processing is done
domain: broadcast
tags: [ebu r103, measurement, filter, active picture, legaliser, full range]
applies_to: EBU R 103 v3.0
status: V
confidence: high
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://tech.ebu.ch/docs/r/r103.pdf, src:research-production-pipelines]
feeds: [CHECKS 9]
conflicts: none
---
Vertical filter is 1/4, 1/2, 1/4. The active picture is defined in EBU R 95. Legalisers can add artefacts worse than the error. Full-range files must be signalled in the container.

**Use it:** the check filters, counts area outside preferred range, flags over 1%, and ignores the blanking.
