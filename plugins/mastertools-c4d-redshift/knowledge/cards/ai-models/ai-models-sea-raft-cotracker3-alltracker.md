---
id: ai-models-sea-raft-cotracker3-alltracker
title: Optical flow and tracking: SEA-RAFT (BSD-3, Spring EPE 3.69), CoTracker3 (mostly CC-BY-NC), AllTracker (16.5M params, ICCV 2025)
domain: ai-models
tags: [sea-raft, optical flow, cotracker3, alltracker, tracking, licence, spring benchmark, motion, cotracker]
applies_to: 2025
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://github.com/princeton-vl/SEA-RAFT, https://github.com/facebookresearch/co-tracker, https://arxiv.org/pdf/2506.07310, src:research-verticals]
feeds: [motion check, PLAN step 1.5]
conflicts: none
---
SEA-RAFT: 1px outlier 0.36 and 2.3x faster than prior methods (own claim). AllTracker beats CoTracker3 by 1.1 points on a 9-benchmark mean but its flow is less exact than SEA-RAFT. NVIDIA recommended; CPU slow; MPS not mentioned.
No open animation-curve quality tool was found.
Merged from `motion-sea-raft-flow`: SEA-RAFT: Spring benchmark EPE 3.69, 1px outlier 0.36, claimed 2.3x faster than earlier methods. AllTracker (ICCV 2025) tracks densely with 16.5M params but its flow is less exact than SEA-RAFT. GPU recommended; MPS not mentioned.

**Use it:** use SEA-RAFT for flow; Redshift motion vectors are better when passes exist.
