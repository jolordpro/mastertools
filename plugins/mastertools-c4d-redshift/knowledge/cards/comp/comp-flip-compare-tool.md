---
id: comp-flip-compare-tool
title: ꟻLIP (flip-evaluator 1.6/1.7) scores rendered images in LDR and HDR and installs with pip
domain: comp
tags: [comp, flip, error map, compare, look loss, evaluator, nvidia]
applies_to: flip-evaluator 1.6-1.7
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/NVlabs/flip, https://pypi.org/project/flip-evaluator/1.6.0.1/, src:research-verticals]
feeds: [PLAN Phase 0A ladder score]
conflicts: none
---
Built for rendered images; BSD-3 per mirrors, confirm on the official repo.
pyiqa is a different scorer and has no ꟻLIP, no Apple MPS support and a non-commercial licence.

**Use it:** use ꟻLIP to score comp fixes, denoise and upscale against a full render of the hero frame.
