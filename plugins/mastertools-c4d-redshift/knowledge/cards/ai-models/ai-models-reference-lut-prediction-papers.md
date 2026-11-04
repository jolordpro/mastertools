---
id: ai-models-reference-lut-prediction-papers
title: Reference-to-grade models exist as papers only: SA-LUT predicts a 4D LUT from a style image (16 FPS claimed), AceTone a 3D LUT from a VLM
domain: ai-models
tags: [lut, color grade, reference image, sa-lut, acetone, canoncgt, style transfer]
applies_to: 2025-2026 papers
status: V2
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://newx.sg/paper/detail/88ece4c9-f823-11f0-b84c-00163e10baa7, https://arxiv.org/pdf/2604.00530v1, https://arxiv.org/html/2606.01638, src:research-gaps-deep]
feeds: [bet 1 light match]
conflicts: none
---
SA-LUT (Jun 2025) has code and the PST50 benchmark on GitHub. AceTone (2026) has a VLM predict tokens that decode to a 3D LUT from an image or text. CanonCGT (Jun 2026) uses two LUTs, one to normalise and one to apply the reference look (arXiv id mapping unverified). A 2026 video paper uses one LUT per video to avoid flicker.
No shipping product was found.

**Use it:** possible route for a match-this-grade step in comp; unproven.
