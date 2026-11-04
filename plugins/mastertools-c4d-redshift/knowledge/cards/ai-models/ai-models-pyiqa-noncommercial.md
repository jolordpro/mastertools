---
id: ai-models-pyiqa-noncommercial
title: pyiqa is now PolyForm Noncommercial and has no Apple Silicon (MPS) support; use ꟻLIP for render scoring
domain: ai-models
tags: [pyiqa, flip, lpips, image quality, licence, scorer]
applies_to: pyiqa 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/chaofengc/IQA-PyTorch, https://github.com/NVlabs/flip]
feeds: [OPEN-STACK stage 4, ladder look-loss]
conflicts: none
---
pyiqa's page lists PolyForm Noncommercial and CUDA/CPU only. ꟻLIP (`pip install flip-evaluator`) is built for rendered images.

**Use it:** ꟻLIP scores every ladder rung; pyiqa only for research.
