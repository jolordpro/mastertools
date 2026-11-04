---
id: datasets-benchmarks
title: Datasets and benchmarks for composition, aesthetics, design and film
type: system
aliases: [datasets, benchmarks, CADB, KU-PCP, PICD, AVA, AADB, TAD66K, KonIQ, SPAQ, PARA, EVA, Crello, PubLayNet, Rico, WebUI, CGL, PKU-PosterLayout, ShotBench, ShotQA, VidComposition, AesEval-Bench, ArtiMuse-10K, MIT Tubingen saliency benchmark, Imp1k, UEyes, gold set, SRCC, PLCC]
tags: [systems, data, evaluation]
related: [tools-models, llm-critics, architecture, rubric]
evidence: dataset facts from source repos and papers; benchmark scores mostly from authors' own papers.
updated: 2026-10-20
---

# Datasets and benchmarks

## Quick answer
- Composition scores: CADB (9,497 photos, expert composition ratings). Composition types: PICD (24 categories), KU-PCP (9 classes).
- Design critique: AesEval-Bench. Cinematography: ShotBench. Video composition: VidComposition.
- Build a house gold set: about 100 of your own frames rated by you, ideally as A/B pairs. It is the most valuable dataset for your use.

## Composition
- **CADB** (BMVC 2021, SJTU BCMI): 9,497 photos from AADB; each rated 1 to 5 for composition by 5 fine-art-trained raters; composition attributes. SAMP-Net SRCC 0.6564 / LCC 0.6709.
- **KU-PCP**: 4,244 outdoor photos, 9 classes: rule of thirds, center, horizontal, symmetric, diagonal, curved, vertical, triangle, pattern.
- **PICD** (CVPR 2025 Highlight, BUPT): 36,857 images over 355 scenes in the paper; the repo lists 49,123 images (44,577 redistributable, 4,546 fetched from source). 24 categories. License CC BY-NC-SA 4.0 plus terms of use. Quality scores, negatives and text descriptions "coming soon" in the repo. Paper conclusion: current composition-embedding models and MLLMs show clear limits. (The "near chance" claim was not found in the sources checked.) Metric: CDA (composition discrimination accuracy).
- **APDDv2**: artwork aesthetic dataset. `[Unverified: not named in the KU Leuven abstract checked 2026-10-20; link to PICD work unconfirmed]`
- **Cropping sets**: GAICD, CPC, FCDB, FLMS, UGCrop5K.

## General aesthetics and quality
- **AVA** (DPChallenge votes), **AADB**, **TAD66K**, **EVA**, **PARA** (personalized), **FLICKR-AES**, **KonIQ-10k**, **SPAQ** (smartphone), **PCCD** (critiques). `[Unverified sizes]`
- **ArtiMuse-10K**: 10,000 images, 5 categories, 15 subcategories, with expert attribute text (partial release).

## Attention
- **MIT/Tübingen Saliency Benchmark**: standard for saliency models (AUC, sAUC, CC, NSS).
- **Imp1k**: graphic design importance (UMSI).
- **UEyes**: UI eye tracking; retraining UMSI on it raised AUC from 0.778 to 0.878.

## Graphic design and layout
- **Crello**: professional templates with layered JSON (boxes, fonts, colors).
- **PubLayNet** (documents), **Rico** and **WebUI** (apps, web), **CGL** and **PKU-PosterLayout** (posters over images), **SciPostLayout**.
- **AesEval-Bench** (ICLR 2026, arXiv 2603.01083, Microsoft Research Asia): 4 dimensions (layout, color, font, graphics), 12 indicators (balance, layering, whitespace, alignment, harmony, contrast, appeal, color psychology, legibility, hierarchy, graphic quality, relevance); Crello designs with injected flaws.

- **Venus / AesGuide** (CVPR 2026, arXiv 2602.23980): 10,748 photos with guidance annotations; evaluated models were over-positive.
- **RED-Aes** (Xiaomi, arXiv 2606.05778): edit-pair data with relative rankings; pair kept only if 3 judges agree.
- **Degradation pairs** (Sheng et al., AAAI 2020, arXiv 1911.11419): edits that degrade an image lower aesthetic scores; a template for synthetic test pairs.

## Cinematography and video
- **ShotBench** (NeurIPS 2025, arXiv 2506.21356; GPT-4o 59.3% average, ShotVL-3B 65.1%): 3.5k+ expert-annotated questions from 200+ Oscar-winning or nominated cinematography films; 8 dimensions: shot size, framing, camera angle, lens size, lighting type, lighting condition, composition, camera movement. **ShotQA**: about 70k QA pairs.
- **VidComposition**: 982 videos, 1,706 questions on edited-video composition.
- **MovieNet, CineScale**: film shot-type data. `[Unverified details]`

## Metrics glossary
- SRCC: rank correlation with human ratings. PLCC: linear correlation.
- IoU: overlap between predicted and true boxes.
- AUC, sAUC, CC, NSS: saliency agreement measures.
- CDA-1, CDA-2: composition classification accuracies used on PICD.

## House gold set recipe `[Infer]`
- 100 frames across your real work: lower thirds, full-screens, game frames, key art, social posts.
- Rate each with the `rubric`; for 50 pairs, pick A or B and write one reason.
- Use it to calibrate weights and compare tools before trusting them.
- Taste agreement varies by subject: high for faces and landscapes, low for artworks and architecture (Vessel et al. 2018, *Cognition* 179:121-131 `[E-mixed]`). Expect your own ratings to match a crowd more on portraits than on stylized frames.
- Add scripted degradations (competing highlight, flattened value, edge shift, tilt) as cheap test pairs; see `llm-critics` House measurements.
