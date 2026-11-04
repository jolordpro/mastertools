---
id: ai-models-flip-evaluator-render-metric
title: ꟻLIP (`pip install flip-evaluator`, v1.6/1.7) gives LDR and HDR error maps built for rendered images
domain: ai-models
tags: [flip, flip-evaluator, nvlabs, error map, render metric, hdr, look loss]
applies_to: FLIP 1.6-1.7
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/NVlabs/flip, https://pypi.org/project/flip-evaluator/1.6.0.1/, src:research-verticals]
feeds: [ladder look-loss, OPEN-STACK stage 4]
conflicts: none
---
BSD-3 per mirrors; confirm on the official repo. It is not part of pyiqa. The pyiqa card covers why pyiqa is not used.

**Use it:** score every ladder rung and every comp-versus-render comparison with it.
