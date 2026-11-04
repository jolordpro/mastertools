---
id: llm-critics
title: How well AI models judge composition
type: system
aliases: [LLM critic, multimodal LLM, VLM, AI art critic, GPT composition, Claude composition, Gemini composition, AesEval results, ShotBench results, Venus AesGuide, flattery problem, AI design critique]
tags: [systems, llm, evaluation, benchmarks]
related: [protocol, architecture, datasets-benchmarks, tools-models, rubric, generation-loop]
evidence: benchmark results from authors' papers (2025-2026); Claude not evaluated in AesEval-Bench or ShotBench; house measurements are [Infer].
updated: 2026-10-20
---

# AI models as composition critics

## Quick answer
- General multimodal models describe composition well but diagnose and localize problems poorly, and they flatter. `[E-mixed]` (two 2026 author-run benchmarks, Claude not tested)
- Small models fine-tuned on region-grounded critiques can beat much larger general models on narrow tasks. `[E-strong]`
- Give the model measurements, layout metadata and a strict rubric; ask for problems first and A/B comparisons.

## Evidence
- **AesEval-Bench** (ICLR 2026, graphic design, arXiv 2603.01083)
  - Yes/no aesthetic judgment: GPT-5 0.7252 accuracy (best); Gemini-2.5-Pro 0.6368.
  - Reasoning models (o1, o3) gave no clear advantage.
  - Localizing the flaw with a box: GPT-5 below 0.20 IoU.
  - Photo-aesthetics models did worse on design: AesExpert 0.4056, UNIAA-LLaVA 0.29.
  - Fine-tuned Qwen-VL-7B with indicator-grounded reasoning: 0.6987 judgment, 0.2231 IoU (beat GPT-5 at localization).
  - Supplying layout metadata (boxes, fonts, colors as JSON) helped localization most.
- **Venus / AesGuide** (CVPR 2026, photography guidance, arXiv 2602.23980; 10,748 photos)
  - GPT-4o and aesthetic MLLMs mostly give overly positive feedback and miss issues (models over-positive).
  - Cropping (FLMS): GPT-4o 71.61% IoU vs about 85% for specialized croppers and 87.01% for fine-tuned Venus-Q. Code public.
- **ShotBench** (NeurIPS 2025, cinematography, arXiv 2506.21356)
  - GPT-4o averaged 59.3% across 8 dimensions; ShotVL-3B reached 65.1%.
  - ShotVL, trained on ShotQA, improved most on composition and camera movement.
- **VFLM, "Seeing is Improving"** (CVPR 2026, arXiv 2603.22187): render the layout, look, revise. Capped at 3 rounds; an OCR-based reward keeps text legible. Looking at the render each round improved layout results.
- **RED-Aes** (Xiaomi, arXiv 2606.05778): trains on edit pairs and ranks relatively (better/worse), not absolutely. A pair is kept only if 3 judges agree. Supports the pairwise-first rule in `protocol`.
- **Sheng et al.** (AAAI 2020, arXiv 1911.11419): degrading edits lower aesthetic scores in trained models. Backs the degradation test used in House measurements below.
- **PhotoEye / PhotoCritique** (Adobe, CVPR 2025): multi-view fusion for photo critique (several views of one photo fed together). Research-grade; not Claude-tested.
- **PICD** (CVPR 2025): the paper concludes current composition models and MLLMs have clear limits on composition embedding and understanding. See `datasets-benchmarks`. (The earlier note that specialized classifiers fall to near chance was not confirmed in the sources checked 2026-10-20.)

## House measurements `[Infer, n=24, one run, 2026-10-20]`
Blind A/B of 6 pro broadcast frames against scripted degradations. Two Claude judges, run in opposite left/right orders. 24 verdicts in total (6 frames x 4 degradations).
- Right in both orders: competing highlight 5/6, flattened value 5/6, edge shift 4/6, 2 degree tilt 2/6. Total 16/24.
- 7/24 verdicts flipped with order. Order bias is real, so every A/B runs in both orders.
- 0 of 14 high-confidence picks were wrong.
- Low-confidence picks came with invented reasons. Low confidence must trigger a measurement.
- Small tilt (2 degrees) is the weak spot: use the horizon measurement (Apple Vision, see `tools-models`), not the eye.
- One run, one model family, six frames. Treat as a starting calibration, not a result.

## Taste is partly shared `[E-mixed]`
- Vessel, Maurer, Denker & Starr (2018, *Cognition* 179:121-131): shared taste across people is high for faces and landscapes, low for artworks and architecture. A critic can be confident about portrait and landscape frames and should hedge on stylized work.

## Implications for prompting `[Infer]`
- Check every rubric criterion; report only problems with grid location, mechanism and a measurement or visible mark. "Nothing material to fix" is a valid verdict.
- Require each claim to cite a metric or region.
- Use pairwise comparisons for decisions, in both orders; only agreeing verdicts count.
- Provide layout JSON for designs and contact sheets for video.
- Ask the model to state uncertainty and what it cannot see.
- Keep the model on mechanisms, not rule names.

## Gaps
- Claude was not in the published benchmarks (the house run above is the only Claude data); test it on CADB, a PICD subset, ShotBench and your gold set before trusting it.
- Model versions change quickly; rerun benchmarks after upgrades.
