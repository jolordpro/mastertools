---
id: architecture
title: Evaluator app architecture (measure, critique, cite)
type: system
aliases: [system design, app architecture, build plan, composition grader, evaluator pipeline, Claude Code app spec, how to build]
tags: [systems, architecture, claude-code, build-spec]
related: [tools-models, metric-recipes, llm-critics, rubric, protocol, datasets-benchmarks, generation-loop]
evidence: architecture built on 2025-2026 benchmark findings [E-mixed]; the claim that no open model grades composition reliably is [Infer].
updated: 2026-10-20
---

# Architecture

## Quick answer
- No downloadable model grades composition like a senior art director. `[Infer]`
- Build three layers: measure (local tools) → critique (Claude with rubric) → cite (this library).
- Start with layer 3 plus Claude (no install), then add measurement tools one at a time.

## Layer 1: Measure (runs on a Mac)
Output: one JSON report plus overlay images per image or frame.
1. Apple Vision (v1 stack, free OS API, macOS 15+, fine for work use): attention and objectness saliency heatmaps, horizon angle, foreground instance mask, faces + landmarks, body pose, text recognition, and the aesthetics score (`overallScore` −1 to 1, `isUtility`). Tested 2026-10-20 on a synthetic frame `[Infer, n=1]`: horizon 1.0 deg read vs 0.9 drawn; attention peak (0.72, 0.35) vs subject (0.75, 0.37); Apple's salient-object box too broad (66% of width), so use heatmap peaks, not boxes; objectness found nothing on that frame.
2. Subject mask (SAM 2) → centroid, area %, negative space %, distance to edges, front-to-back space.
3. Saliency or importance map → first look, competing peaks, peak-subject match. Prototype only unless licensed (DeepGaze, UMSI).
4. Depth map (Depth Anything V2 Small) → plane count, separation.
5. Lines (OpenCV) → horizon tilt, orientation histogram, convergence.
6. Value structure → histogram, 3 and 4 value posterization, subject ΔL*.
7. Color → Lab palette, chroma contrast subject vs ground.
8. Balance → center of mass and APB on luminance and saliency.
9. Clutter → Feature Congestion, Subband Entropy.
10. Graphics with layer data → alignment, overlap, occlusion, safe-area compliance.
11. Video → shot boundaries, optical flow, saliency at cuts.
Recipes in `metric-recipes`. Tools and licenses in `tools-models`.

## Layer 2: Critique (Claude)
- Inputs: image, overlays, JSON metrics, intent, context.
- Instructions: `protocol` plus `rubric`.
- Rules that counter known model weaknesses (see `llm-critics`)
  - Check every rubric criterion; report only problems with location, mechanism and a measurement or visible mark. "Nothing material to fix" is valid.
  - Pairwise A/B comparisons over absolute scores, in both left/right orders; only agreeing verdicts count. Low confidence triggers a measurement.
  - Infer intent from the frame and state the assumption; ask only if the answer would flip the verdict.
  - Video: analyze a frame sequence or contact sheet, not one still.

## Layer 3: Knowledge (this library)
- Facet files tagged by evidence.
- House rules file (add later): brand guide, safe areas, legibility minimums, package conventions.

## Build order (ranked)
1. Claude Project or skill with this library and the rubric. No install.
2. Apple Vision CLI (Swift, small): saliency, horizon, mask, faces, text, aesthetics.
3. Permissive measurement tools: SAM 2, Depth Anything V2 Small, OpenCV, clutter port, balance, palette, notan.
4. LAION Aesthetic v2 as a cheap general gauge, calibrated on your own graded frames.
5. Prototype-only comparisons: pyiqa models, DeepGaze IIE, UMSI, Depth Pro.
6. Benchmark on CADB, a PICD subset, ShotBench and a 100-frame house gold set (A/B pairs).
7. Later: fine-tune a small open VLM on your own region-grounded critiques.

## Production licensing rule
- Internal company use counts as commercial use under non-commercial licenses. Use Apache/MIT components in production; get legal sign-off. See `tools-models`.

## Generation loop (later)
- Propose → render → measure → critique → revise. See `generation-loop`.

## Data flow (plain words)
- Image in → measurement scripts write `report.json` and overlays → Claude reads image + report + rubric + relevant facet files → returns critique JSON (shape in `rubric`) → optional revise loop.

## Failure modes to design against
- Trusting raw aesthetic scores across content types.
- A detector's silence treated as proof (test each detector on a known positive first).
- Rubric scores without evidence lines.
