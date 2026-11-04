---
id: broadcast-ebu-r103-code-values
title: EBU R 103 v3 code values: 8-bit nominal 16-235, preferred 5-246; 10-bit 64-940, preferred 20-984; 12-bit 256-3760, preferred 80-3936
domain: broadcast
tags: [ebu r103, code values, legal levels, 8-bit, 10-bit, 12-bit, preferred range]
applies_to: EBU R 103 v3.0 (May 2020)
status: V
confidence: high
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://tech.ebu.ch/docs/r/r103.pdf, src:research-production-pipelines]
feeds: [CHECKS 9]
conflicts: none
---
Total ranges: 1-254 (8-bit), 4-1019 (10-bit), 16-4079 (12-bit). RGB and luma should not normally leave preferred min/max. For graded or pre-produced work, follow nominal limits closely.

**Use it:** convert to the delivery range, then test against preferred min/max.
