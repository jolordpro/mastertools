---
id: ai-models-aesthetic-critique-datasets
title: Aesthetic critique data exists for photos (AesExpert 21,904 images, DPC-Captions 154K) but none for CG lighting
domain: ai-models
tags: [aesexpert, aesmmit, dpc-captions, artimuse, aeseval-bench, dataset, critique]
applies_to: 2024-2026
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://arxiv.org/abs/2404.09624, https://arxiv.org/abs/2206.08614, https://thunderbolt215.github.io/ArtiMuse-project, https://arxiv.org/pdf/2603.01083, src:research-verticals]
feeds: [taste critic]
conflicts: none
---
AesExpert/AesMMIT: 21,904 images, 88K human feedbacks, 409K instructions. Photo sets: AVA-Captions, DPC-Captions (154K images, 2.4M comments), RPCD (74K images), PCCD. ArtiMuse (ICLR/CVPR 2026) says model and dataset are "planned". AesEval-Bench (ICLR 2026): a fine-tuned 7B beat a 72B base on graphic design aesthetics.
No lighting-critique dataset for CG and no open preference pairs on renders were found.

