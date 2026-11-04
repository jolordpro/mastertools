---
id: tools-models
title: Tools and models with licenses and Mac fit
type: system
aliases: [models, libraries, open source tools, aesthetic models, IQA, IAA, saliency models, segmentation, depth estimation, licenses, pyiqa, NIMA, MUSIQ, TOPIQ, CLIP-IQA, Q-Align, LAION aesthetic predictor, ArtiMuse, Apple Vision aesthetics, DeepGaze, UMSI, SAM 2, Depth Anything, Depth Pro, OpenCV, clutter code]
tags: [systems, tools, licenses, mac]
related: [architecture, metric-recipes, datasets-benchmarks, llm-critics, generation-loop, reframing]
evidence: license statuses and paper facts re-checked live 2026-10-20 (see docs/CHANGELOG-library.md); several licenses are internally inconsistent. Verify before production.
updated: 2026-10-20
---

# Tools and models

## Quick answer
- Production-safe core (permissive licenses): SAM 2, Depth Anything V2 Small, OpenCV, LAION Aesthetic v2, MIT clutter port, Aesthetics Toolbox (MIT), Apple Vision (OS API).
- Prototype only (non-commercial or no license): pyiqa toolbox, DeepGaze IIE, UMSI, Apple Depth Pro, Q-Align code.
- Aesthetic scores measure "how good," not "why." Composition diagnosis comes from combining primitives plus Claude.

## Format
Each entry: what it does · license · Mac fit · use.

## Aesthetic and quality scorers
- **Apple Vision `CalculateImageAestheticsScoresRequest`** · `overallScore` −1 to 1 and `isUtility`; considers blur, exposure and more · free OS API (iOS 18 / macOS 15); symbol confirmed to compile on macOS 26.6 (2026-10-20); not in Simulator · first scorer to add. The rest of the Vision stack is below.
- **LAION Aesthetic Predictor** · v1 linear head on CLIP (MIT); v2 CLIP + MLP (Apache-2.0), trained on SAC, logos, AVA · permissive · easy on Mac · cheap general gauge; calibrate on your frames.
- **pyiqa / IQA-PyTorch** (Chaofeng Chen, NTU) · one-line access to NIMA, MUSIQ, TOPIQ, CLIP-IQA, Q-Align, Q-ReAlign (Qwen3.5-VL backbone, `qrealign-mini` 0.8B / `-lite` 4B / `-pro` 9B, changelog June 2026, needs transformers>=5.0) · README states PolyForm Noncommercial 1.0.0 (and cites NTU S-Lab for some components; repo shows an unexplained MIT label, so read LICENSE before use) · small models fine on CPU/MPS · prototyping and benchmarking only.
- **Q-Align / OneAlign** (ICML 2024) · LMM scored with words, unified quality/aesthetic/video; AVA SRCC 0.822 / PLCC 0.817 (per a comparison table) · HF weights labeled MIT, GitHub code non-commercial S-Lab · 7B class, better on GPU · research.
- **ArtiMuse** (CVPR 2026, accepted 2026-02-21) · built on InternVL-3 (the "8B" size was not confirmed); score plus 8-attribute analysis; ArtiMuse-10K dataset · repo states no code or checkpoint license (an "Apache-2.0" claim could not be confirmed; read the HF model cards); ArtiMuse-10K is academic, non-commercial, no redistribution; test set public, full set by request form; ArtiMuse-R1 and the online demo not downloadable · high-RAM Mac possible · interesting for text critiques; treat as research-only.
- **AesExpert, UNIAA, PhotoEye, CALM** · aesthetic MLLMs · research · underperform frontier models on design and guidance (2026 benchmarks).

## Composition-specific
- **SAMP-Net** (CADB, BMVC 2021) · composition score with saliency and pattern pooling; SRCC 0.6564 · GitHub code and data · research.
- **VFCNet** (TU Wien Computer Vision Lab + UAS St. Pölten; accepted ICPR 2026; arXiv 2604.16500) · DeepGaze IIE saliency + gradient-vector flow of edges (dual stream, attention fusion) + DINOv3 backbone · PICD re-evaluation subset: CDA-1 0.683, CDA-2 0.629 vs CACNet 0.513 / 0.462 (+33.1% / +36.1%). Under the original PICD evaluation CACNet scored 0.419 / 0.405, so "previous best" depends on the protocol · code at github.com/ADadras/VFCNet · insight: composition reads from saliency plus edge flow. Inherits DeepGaze IIE's unclear license.
- **KU Leuven composition embeddings** (Behrad, Tuytelaars, Wagemans; arXiv 2608.06142, Aug 2026; ECCV 2026 workshops) · compares a perceptual-grouping method (object-centric regions + graph attention) with fine-tuned foundation models on composition score/category, retrieval and saliency; frozen encoders: grouping method competitive and more interpretable; fine-tuned large models win with enough data but generalize less. Code and weights said to be on GitHub. The abstract does not list affiliation or datasets (KU Leuven is from the authors' known home; PICD/APDDv2 use unconfirmed).
- **COMEX** (arXiv 2608.07570, Aug 2026; Rui Yang, Wei Zhou et al.) · composition-grounded benchmark and learning framework for explainable cropping (crop → composition category → explanation); 33,161 quadruples; SFT + GRPO; 15 VLMs benchmarked · authors' own claims only.
- **Cropping models**: CACNet, GAIC (GAICD), CPC, FCDB, FLMS, UGCrop5K · mixed research code · auto-crop baselines.

## Apple Vision measurement stack (v1)
Free OS API (Vision framework, macOS 15+), fine for work use. Called from Swift (`scripts/vision.swift`).
- Attention-based and objectness-based saliency heatmaps.
- Horizon detection (angle).
- Foreground instance mask.
- Faces with landmarks; body pose.
- Text recognition (OCR).
- Aesthetics score (`overallScore`, `isUtility`).
Tested 2026-10-20 on one synthetic frame `[Infer, n=1]`:
- Horizon: read 1.0 degrees vs 0.9 drawn.
- Attention heatmap peak at (0.72, 0.35) vs subject at (0.75, 0.37).
- Apple's own salient-object bounding box was too broad (66% of frame width). Use heatmap peaks, not boxes.
- Objectness saliency found nothing on that frame. A detector's silence is not proof; test on a known positive.

## Attention and saliency
- **DeepGaze IIE** (Tübingen, ICCV 2021) · top on MIT/Tübingen benchmark · github.com/matthias-k/DeepGaze has no LICENSE file (raw LICENSE returns 404, checked 2026-10-20); the "request unanswered since 2023" detail was not verified · runs on Mac · prototype only.
- **UMSI** (MIT + Adobe, UIST 2020) · importance for graphic designs and saliency for photos; Imp1k dataset · repo LICENSE: copyrighted by the authors, MIT and Adobe, non-commercial research use only; contact Adobe for commercial licensing (corrected: not "no license stated") · weights downloadable (Keras .h5) · prototype only.
- **Rosenholtz clutter** (Feature Congestion, Subband Entropy) · MIT-licensed Python port github.com/kargaranamir/visual-clutter (copyright line names Aalto University's User Interfaces group; original is MATLAB). `visual-attention-audit` (github.com/AlexeyGOblov/visual-attention-audit) exists: MIT, packaged as a Claude Code skill, Feature Congestion + Subband Entropy on numpy/scipy/Pillow, optional MSI-Net attention map; its README says absolute values are unverified against the reference, so use for comparing frames only. Needs scipy, which the house python3 lacks · permissive · easy.

## Geometry, depth, segmentation
- **SAM 2 / 2.1** (Meta) · segmentation masks for images and video · code and checkpoints Apache-2.0 (some files BSD-3-Clause; one third-party piece has its own license) (confirmed 2026-10-20) · Mac OK.
- **Depth Anything V2 Small** · monocular depth · Small is Apache-2.0; Base/Large are CC-BY-NC-4.0, Giant "coming soon" (confirmed on the official repo 2026-10-20) · Apple Core ML version, about 50 MB F16.
- **Apple Depth Pro** · sharp metric depth · ambiguous: GitHub Apple Sample Code License originally; HF now "apple-amlr" research-only · prototype only.
- **OpenCV** · lines (Hough, LSD), color conversion, histograms, optical flow · Apache-2.0.

## Video
- **Google AutoFlip** (MediaPipe, 2020) · saliency-aware reframing · unmaintained · **pyautoflip** maintained Python re-implementation (check license).

## Measurement toolboxes
- **Aesthetics Toolbox** (Redies, Bartho et al., *Behavior Research Methods* 2025, doi 10.3758/s13428-025-02632-3; arXiv 2408.10616) · github.com/RBartho/Aesthetics-Toolbox · MIT (LICENSE file); Streamlit app plus `QIP_machine_script.py` for batch runs; Fourier slopes, fractality, PHOG, symmetry, EOE, CNN variances · use for `image-statistics`.

## Notes
- Aesthetic datasets encode crowd taste (photo-contest voters, web users), not broadcast taste.
- Test every detector on a known positive before trusting a null result.
