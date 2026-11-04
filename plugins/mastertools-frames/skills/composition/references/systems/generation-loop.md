---
id: generation-loop
title: Generating and improving compositions automatically
type: system
aliases: [composition generation, auto layout, layout generation, auto crop, ControlNet, layout to image, iterative refinement, propose render critique revise, LayoutGPT, LayoutPrompter, PosterLlama, AesthetiQ, VFLM, design agent]
tags: [systems, generation, layout, cropping]
related: [architecture, metric-recipes, tools-models, reframing, rubric, protocol, llm-critics]
evidence: research methods 2023-2026; render-and-iterate loops have the best support (VFLM, one paper [E-mixed]).
updated: 2026-10-20
---

# Generation loop

## Quick answer
- Loop: propose → render → measure → critique → revise. Looking at the rendered result each round improves layouts (VFLM, CVPR 2026). `[E-mixed]` (one paper; cap rounds at 3)
- For images: lock composition with conditioning (depth, edges, pose) and vary style. For crops: score candidate crops with the rubric metrics. `[Practice]`

## Methods
- **Layout generation with LLMs**: LayoutGPT, LayoutPrompter, PosterLlama, AesthetiQ (CVPR 2025, preference-aligned layouts on Crello and WebUI).
- **Visual feedback refinement**: VFLM, "Seeing is Improving" (CVPR 2026, arXiv 2603.22187): render, look, revise; capped at 3 rounds; OCR reward keeps text legible.
- **Relative ranking for edits**: RED-Aes (Xiaomi, arXiv 2606.05778) trains on edit pairs and ranks relatively. A pair is kept only if 3 judges agree. Use the same agree-or-drop rule for revise-loop pairs.
- **Degradation as test**: Sheng et al. (AAAI 2020, arXiv 1911.11419) show degrading edits lower aesthetic scores; scripted degradations make cheap test pairs.
- **Multi-view critique**: PhotoEye / PhotoCritique (Adobe, CVPR 2025) fuses several views of one photo.
- **Composition-locked image generation**: ControlNet-style conditioning on depth maps, edge maps, pose skeletons; layout-to-image models that place objects in given boxes.
- **Cropping and reframing**: composition-aware croppers (GAIC, CACNet, Venus); saliency-tracking reframers (AutoFlip, pyautoflip). See `reframing`.

## Practical loop for a Claude Code app `[Infer]`
1. Input: intent, format, required elements, brand rules.
2. Claude proposes 3 layout or crop candidates as structured JSON (boxes, sizes, colors).
3. Render each (HTML/SVG, After Effects template, or image crop).
4. Run `metric-recipes` on each render.
5. Claude critiques with `protocol` and ranks candidates pairwise.
6. Revise the winner; stop when scores plateau or after a fixed number of rounds.
7. Human picks; log the pick to calibrate the rubric.

## Guardrails `[Infer]`
- Hard gates first (safe areas, contrast, required elements) before aesthetic ranking.
- Keep human choice as the final step; log disagreements.
- Stop after 3 rounds (VFLM's cap), or sooner when two rounds change the measured metrics by less than a set margin.

## Failure modes
- Optimizing metrics that don't track quality (layout alignment scores alone).
- Generated images with composition drift from the conditioning.
- Endless loops polishing small differences.
