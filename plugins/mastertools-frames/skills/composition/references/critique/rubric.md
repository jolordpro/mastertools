---
id: rubric
title: Composition scoring rubric with context weights
type: critique
aliases: [scoring rubric, grading rubric, composition score, crit rubric, evaluation criteria, weights, scorecard]
tags: [critique, scoring, machine-usable]
related: [protocol, formal-analysis, genre-checklists, metric-recipes, evidence-legend, architecture]
evidence: criteria chosen and weighted by evidence strength; weights are [Infer] starting points.
updated: 2026-10-20
---

# Rubric

## Quick answer
- The primary decision tool is pairwise comparison (A vs B, both left/right orders, only agreeing verdicts count). Use the criteria below as the checklist behind each comparison.
- The weighted 0 to 100 score is optional. Use it for app and JSON output only. It is never the headline of a critique.
- Ten criteria, each scored 0 to 3 when a score is wanted. Weights are starting points `[Infer]`, kept below.
- Never score grid compliance (thirds, phi) as such.
- Every criterion gets a check line: a located problem with evidence, or "clear".

## Pairwise comparison (primary)
- For each criterion, say which of A and B is better, or "no difference", with one evidence line.
- Run both orders. If the two runs disagree, the answer is "no reliable difference"; measure instead of arguing.
- Overall winner = the version that wins on the criteria with the highest context weight, with hard gates applied first.
- Low confidence means measure (see `protocol`). Do not invent a reason.

## Scale (all criteria)
- 0: fails; the problem dominates the image.
- 1: weak; noticeable problem that hurts the read.
- 2: solid; works, minor issues.
- 3: excellent; strong, deliberate, nothing to fix.

## Criteria
1. **Focal clarity and hierarchy** (`hierarchy-focal-point`, `attention-saliency`)
   - 3: one clear focal point wins on several channels; clear 2nd and 3rd levels.
   - 0: no focal point or split attention.
   - Metrics: saliency peak ratio, peak-subject overlap.
2. **Value structure** (`value-contrast`, `light`)
   - 3: reads in grayscale at thumbnail; 2 to 4 clear masses; max contrast at focus.
   - 0: mid-value soup or focal contrast elsewhere.
   - Metrics: posterized masses, subject ΔL*.
3. **Glanceability and clutter** (`clutter-peripheral`, `negative-space`)
   - 3: message survives one glance at 10% size.
   - 0: busy, nothing pops out.
   - Metrics: Feature Congestion, thumbnail saliency test.
4. **Placement and direction** (`spatial-composition`, `line-direction`)
   - 3: placement fits meaning; directional subjects face in with room; lines lead to focus.
   - 0: subject crowded against edge facing out, lines lead away.
   - Metrics: inward score, front-to-back space ratio, line convergence.
5. **Depth and space** (`depth-space`)
   - 3: space type intentional; cues consistent; subject on a clear plane.
   - 0: subject merges with background; contradictory cues.
6. **Grouping and figure-ground** (`gestalt`)
   - 3: intended groups obvious; strong figure-ground.
   - 0: accidental groupings, subject lost in ground.
7. **Balance** (`balance`)
   - 3: balanced, or imbalance clearly motivated.
   - 0: unmotivated lopsided weight.
   - Metrics: center-of-mass offset, APB.
8. **Color** (`color`)
   - 3: limited palette; accent on focus; color hierarchy agrees with value hierarchy.
   - 0: competing saturated hues; hue-only contrast.
9. **Framing and edges** (`framing-cropping`)
   - 3: clean edges, no tangents or bad amputations; works in delivery formats.
   - 0: tangents, cut joints, key content near edges or outside safe areas.
10. **Motion and editing attention** (video only; `motion-principles`, `continuity-attention`)
   - 3: only what must be read moves; eye trace across cuts; holds readable.
   - 0: competing motion, focus jumps at cuts, holds too short.

Flag-only (no score): image statistics (`image-statistics`), armature alignment (`geometry-proportion`).

## Context weights `[Infer]`
Format: criterion number → weight.

### Broadcast graphics and live frames
- 1 → 3 · 2 → 3 · 3 → 3 · 4 → 2 · 5 → 1 · 6 → 2 · 7 → 1 · 8 → 2 · 9 → 3 (safe areas) · 10 → 3
- Also apply hard gates: text inside graphics safe; contrast ratio threshold (see `accessibility-legibility`).

### Photography
- 1 → 3 · 2 → 3 · 3 → 2 · 4 → 2 · 5 → 2 · 6 → 2 · 7 → 1 · 8 → 2 · 9 → 2 · 10 → 0

### Graphic design and key art
- 1 → 3 · 2 → 2 · 3 → 3 · 4 → 1 · 5 → 1 · 6 → 3 · 7 → 2 · 8 → 2 · 9 → 2 · 10 → 0

### Cinematography (frames and sequences)
- 1 → 3 · 2 → 3 · 3 → 2 · 4 → 2 · 5 → 2 · 6 → 2 · 7 → 1 · 8 → 2 · 9 → 2 · 10 → 3

### Fine art
- 1 → 2 · 2 → 3 · 3 → 1 · 4 → 2 · 5 → 2 · 6 → 2 · 7 → 2 · 8 → 2 · 9 → 1 · 10 → 0

## Weighted score (optional, app/JSON only)
- Not the headline. A critique leads with the verdict, the single change that fixes most, and pairwise results.
- Score = Σ(score × weight) / Σ(3 × weight) × 100.
- If reported, put the number after the problems and checks; the number alone is not the critique.

## Hard gates (fail regardless of score)
- Broadcast: essential text outside 90% graphics safe; text contrast below threshold; graphic covering play-critical area.
- Any: misspelled or wrong information in text.

## Machine-readable output (suggested JSON shape)
```json
{
  "intent": "string",
  "context": "broadcast|photo|design|film|fine_art",
  "scores": [{"criterion": 1, "score": 2, "evidence": "peak ratio 1.3; second peak is the sponsor logo"}],
  "weighted_score": 74,
  "pairwise": [{"a": "v1", "b": "v2", "order_ab": "B", "order_ba": "B", "agreed": true, "winner": "v2"}],
  "hard_gate_failures": [],
  "top_problems": [{"rank": 1, "location": "upper right", "mechanism": "highlight competes with face", "fix": "darken window by about 1 stop"}],
  "strengths": ["string"],
  "meaning_fit": "string",
  "next_step": "string"
}
```

## Calibration `[Infer]`
- Grade 50 to 100 of your own examples by hand, ideally as A/B pairs.
- Compare model scores with yours; adjust weights where the model and you disagree consistently.
