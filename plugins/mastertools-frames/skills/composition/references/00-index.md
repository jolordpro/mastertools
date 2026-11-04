---
id: index
title: Router and facet registry
type: reference
aliases: [router, table of contents, map, where to look]
tags: [meta, routing]
related: [readme, evidence-legend, glossary, rubric, protocol, sources]
evidence: n/a
updated: 2026-10-20
---

# 00 Index

## Quick answer
- Critiquing an image or frame: read `protocol`, then `rubric`, then the facet files the rubric flags.
- Checking whether a rule is real: read `myths-evidence`.
- Building software: read `architecture`, then `metric-recipes`, then `tools-models`.
- Job-type canon (what world-class looks like for one job): read the matching file in `canon/` (see File paths).
- Making a frame stronger by a specific move: read `push-moves`.
- Showing what a method or move looks like: `canon-images` lists 22 public-domain pictures (Dow plates, master paintings) and what each serves.

## Route by question
- "Why does this feel off?" → `protocol`, `rubric`
- "Where should the subject go?" → `spatial-composition`, `framing-cropping`
- "Is it balanced?" → `balance`
- "What will people look at first?" → `attention-saliency`, `hierarchy-focal-point`
- "It's too busy / can't read it at a glance" → `clutter-peripheral`, `negative-space`
- "Too simple or too complex?" → `fluency-complexity`, `image-statistics`, `unity-variety`
- "Is the rule of thirds / golden ratio real?" → `myths-evidence`, `geometry-proportion`
- Lighting, mood, key, contrast → `light`, `value-contrast`
- Palette, harmony, color grading → `color`
- Flat vs deep image → `depth-space`
- Leading lines, diagonals, tension, motion in frame → `line-direction`
- Shape psychology → `shape`
- Size relationships → `scale`
- Repetition, pattern → `rhythm-pattern`
- Surface, detail, sharpness → `texture-detail`
- Crop, aspect ratio, frame within frame → `framing-cropping`
- Grouping, figure-ground → `gestalt`
- Direction of reading, cultural differences → `culture-direction`
- How viewers experience art (form vs meaning) → `aesthetic-models`
- Lens, aperture, exposure, decisive moment → `photo-craft`
- Sports and action photos → `sports-action`
- Shot sizes, framing grammar → `shot-grammar`
- Camera angle, lens choice, camera moves → `camera-lens-movement`
- Story-driven visual structure (Block) → `visual-structure`
- Editing, cuts, gaze in film → `continuity-attention`
- How film style changed over time → `film-statistics`
- Safe areas, lower thirds, score bugs → `broadcast-standards`
- Easing, timing, staging graphics → `motion-principles`
- 16:9 to 9:16 cutdowns → `reframing`
- Grids, layout systems → `grids-layout`
- Type as composition → `typography`
- Contrast ratios, legibility rules → `accessibility-legibility`
- How masters did it → `painters`, `photographers`, `filmmakers`, `designers`
- Art-history analysis method → `formal-analysis`
- Checklist for a specific job (logo or mark, poster, lower third, thumbnail...) → `genre-checklists`
- When breaking a rule works → `rule-breaking`
- Which AI models can judge composition → `llm-critics`, `tools-models`
- Datasets to test against → `datasets-benchmarks`
- Auto-generate or auto-crop compositions → `generation-loop`
- Job-type canon (lower third, key art, thumbnail and similar) → `canon/` files, see File paths table
- Concrete moves that raise a frame a rung → `push-moves`

## Facet registry
Each line: id → evidence level · measurable by software.
- `light` → practice + strong physiology · partial
- `value-contrast` → strong · yes
- `color` → mixed · yes
- `depth-space` → strong (cues) · partial
- `balance` → mixed · yes
- `spatial-composition` → strong · yes
- `gestalt` → strong · partial
- `hierarchy-focal-point` → strong · yes
- `attention-saliency` → strong · yes
- `clutter-peripheral` → strong · yes
- `negative-space` → practice · yes
- `line-direction` → practice + partial evidence · yes
- `shape` → practice · partial
- `scale` → practice · yes
- `rhythm-pattern` → practice · partial
- `texture-detail` → practice · partial
- `framing-cropping` → mixed · yes
- `geometry-proportion` → mostly lore as quality law · yes (descriptive only)
- `unity-variety` → mixed · partial
- `image-statistics` → strong (descriptive) · yes
- `fluency-complexity` → strong / mixed · partial
- `culture-direction` → strong · partial

## File paths
Every file id and its path, relative to `references/`.

| id | path |
|---|---|
| `index` | 00-index.md |
| `evidence-legend` | 01-evidence-legend.md |
| `readme` | README.md |
| `broadcast-standards` | broadcast-motion/broadcast-standards.md |
| `motion-principles` | broadcast-motion/motion-principles.md |
| `reframing` | broadcast-motion/reframing.md |
| `camera-lens-movement` | cinematography/camera-lens-movement.md |
| `continuity-attention` | cinematography/continuity-attention.md |
| `film-statistics` | cinematography/film-statistics.md |
| `shot-grammar` | cinematography/shot-grammar.md |
| `visual-structure` | cinematography/visual-structure.md |
| `formal-analysis` | critique/formal-analysis.md |
| `genre-checklists` | critique/genre-checklists.md |
| `protocol` | critique/protocol.md |
| `rubric` | critique/rubric.md |
| `rule-breaking` | critique/rule-breaking.md |
| `accessibility-legibility` | design/accessibility-legibility.md |
| `grids-layout` | design/grids-layout.md |
| `typography` | design/typography.md |
| `color` | facets/color.md |
| `depth-space` | facets/depth-space.md |
| `framing-cropping` | facets/framing-cropping.md |
| `geometry-proportion` | facets/geometry-proportion.md |
| `hierarchy-focal-point` | facets/hierarchy-focal-point.md |
| `light` | facets/light.md |
| `line-direction` | facets/line-direction.md |
| `negative-space` | facets/negative-space.md |
| `rhythm-pattern` | facets/rhythm-pattern.md |
| `scale` | facets/scale.md |
| `shape` | facets/shape.md |
| `texture-detail` | facets/texture-detail.md |
| `unity-variety` | facets/unity-variety.md |
| `value-contrast` | facets/value-contrast.md |
| `glossary` | glossary.md |
| `designers` | masters/designers.md |
| `filmmakers` | masters/filmmakers.md |
| `painters` | masters/painters.md |
| `photographers` | masters/photographers.md |
| `photo-craft` | photography/photo-craft.md |
| `sports-action` | photography/sports-action.md |
| `aesthetic-models` | science/aesthetic-models.md |
| `attention-saliency` | science/attention-saliency.md |
| `balance` | science/balance.md |
| `clutter-peripheral` | science/clutter-peripheral.md |
| `culture-direction` | science/culture-direction.md |
| `fluency-complexity` | science/fluency-complexity.md |
| `gestalt` | science/gestalt.md |
| `image-statistics` | science/image-statistics.md |
| `myths-evidence` | science/myths-evidence.md |
| `spatial-composition` | science/spatial-composition.md |
| `sources` | sources.md |
| `architecture` | systems/architecture.md |
| `datasets-benchmarks` | systems/datasets-benchmarks.md |
| `generation-loop` | systems/generation-loop.md |
| `llm-critics` | systems/llm-critics.md |
| `metric-recipes` | systems/metric-recipes.md |
| `tools-models` | systems/tools-models.md |
| `canon-3d-brand-frame` | canon/3d-brand-frame.md |
| `canon-broadcast-graphics` | canon/broadcast-graphics.md |
| `canon-sports-photo-key-art` | canon/sports-photo-key-art.md |
| `canon-poster-social-vertical` | canon/poster-social-vertical.md |
| `canon-abstract-light-titles` | canon/abstract-light-titles.md |
| `textbook-methods` | canon/textbook-methods.md |
| `push-moves` | push-moves.md |
| `canon-images` | images/README.md |



## File list by folder
- root: `readme`, `index`, `evidence-legend`, `glossary`, `sources`
- science: `spatial-composition`, `balance`, `gestalt`, `fluency-complexity`, `image-statistics`, `attention-saliency`, `clutter-peripheral`, `aesthetic-models`, `culture-direction`, `myths-evidence`
- facets: `light`, `value-contrast`, `color`, `depth-space`, `geometry-proportion`, `line-direction`, `shape`, `hierarchy-focal-point`, `negative-space`, `scale`, `rhythm-pattern`, `texture-detail`, `framing-cropping`, `unity-variety`
- photography: `photo-craft`, `sports-action`
- cinematography: `shot-grammar`, `camera-lens-movement`, `visual-structure`, `continuity-attention`, `film-statistics`
- broadcast-motion: `broadcast-standards`, `motion-principles`, `reframing`
- canon: `canon-abstract-light-titles`, `canon-3d-brand-frame`, `canon-broadcast-graphics`, `canon-sports-photo-key-art`, `canon-poster-social-vertical`, `textbook-methods`
- playbook: `push-moves`
- images: `canon-images` (22 public-domain pictures)
- design: `grids-layout`, `typography`, `accessibility-legibility`
- masters: `painters`, `photographers`, `filmmakers`, `designers`
- critique: `protocol`, `rubric`, `formal-analysis`, `genre-checklists`, `rule-breaking`
- systems: `architecture`, `tools-models`, `datasets-benchmarks`, `metric-recipes`, `llm-critics`, `generation-loop`
