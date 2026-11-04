---
id: metric-recipes
title: Metric recipes for each facet
type: system
aliases: [metrics, formulas, how to compute, measurement recipes, computational composition, balance formula, contrast ratio formula, saliency peak ratio, inward score, alignment metric, overlap metric, occlusion, notan posterization, Fourier slope, clutter metric]
tags: [systems, metrics, formulas, build-spec]
related: [architecture, tools-models, rubric, balance, value-contrast, spatial-composition, hierarchy-focal-point, clutter-peripheral, image-statistics, grids-layout, accessibility-legibility, broadcast-standards]
evidence: formulas from cited research where noted; thresholds are [Infer] starting points to calibrate.
updated: 2026-10-20
---

# Metric recipes

## Quick answer
- Each recipe: inputs → steps → output → starting threshold. Thresholds marked `[Infer]` must be calibrated on your own graded examples.
- Report every metric in the JSON for Claude; let Claude weigh them with the rubric.

## Shared inputs
- `img`: RGB image, sRGB.
- `L`: CIELAB L* channel (0 to 100).
- `mask`: subject mask from segmentation (SAM 2), plus face and text boxes.
- `sal`: saliency map normalized to sum 1.
- `depth`: relative depth map.

## Value and contrast (`value-contrast`)
- Histogram of L; spread = 5th to 95th percentile range.
- RMS contrast = standard deviation of L / 100.
- Notan: k-means on L with k = 3 and k = 4 → area share and centroid of each cluster.
- Subject ΔL* = |mean L in mask − mean L in a ring around mask (e.g. 10% dilation)|. `[Infer]` Flag below 20.
- Equiluminance flag: at mask boundary, hue difference large (ΔE high) while ΔL* < about 5. `[Infer]`

## Hierarchy and saliency (`hierarchy-focal-point`, `attention-saliency`)
- Find local maxima of `sal` after smoothing; peak strengths p1 ≥ p2.
- Peak ratio = p1 / p2. `[Infer]` Target > 1.5.
- Subject capture = share of `sal` mass inside `mask`. `[Infer]` Target > 0.4 for single-subject images.
- Channel audit: for subject vs strongest non-subject region, compare ΔL*, chroma, area, sharpness, isolation distance; count wins.

## Placement and direction (`spatial-composition`)
- Centroid (cx, cy) of mask, normalized 0 to 1.
- Facing vector f from face yaw, pose or optical flow.
- Inward score = sign(f · (center − centroid)). +1 inward, −1 outward.
- Space ratio = free distance ahead along f / free distance behind.
- `[Infer]` Flag outward-facing subject within 0.15 of an edge.

## Balance (`balance`)
- Weight map W = normalized local contrast × (sal + small epsilon); add boosts for faces and text.
- Center of mass: (Σ x·W / ΣW, Σ y·W / ΣW). DCM = distance from (0.5, 0.5).
- Report horizontal and vertical offsets separately.
- APB-style: for each axis (vertical, horizontal, two diagonals; Wilson & Chatterjee use eight), weight difference between the two halves divided by total. Lower = more balanced. `[Unverified exact APB construction]`

## Depth (`depth-space`)
- Histogram of depth inside the frame; count peaks = planes.
- Subject plane separation = |median depth in mask − median depth of background|.
- Aerial perspective check: correlation of depth with contrast and saturation (expect negative).

## Lines (`line-direction`)
- Line segment detection (LSD or Hough) → lengths and angles.
- Orientation shares: horizontal (±10°), vertical (±10°), diagonal (rest).
- Horizon tilt: angle of the longest near-horizontal line or depth/sky boundary. `[Infer]` Flag 0.5° to 3° as accidental.
- Convergence: extend long lines; densest intersection region; distance to subject centroid.

## Clutter (`clutter-peripheral`)
- Feature Congestion and Subband Entropy (Rosenholtz code).
- Edge density = edge pixels / total.
- Thumbnail test: resize to 10%, blur slightly, recompute saliency; check subject still holds p1.

## Color (`color`)
- Convert to Lab; k-means palette (k = 5 to 8) with area shares.
- Subject chroma vs background chroma; subject ΔE vs ring.
- Count of high-chroma clusters. `[Infer]` More than 2 large high-chroma clusters, review.

## Framing (`framing-cropping`)
- Minimum distance from mask to each edge (% of dimension).
- Tangent flag: mask contour within 1% of an edge without crossing.
- Joint-crop flag: pose keypoints (wrist, elbow, knee, ankle) within 2% of an edge.
- Multi-format survival: share of mask and text boxes inside each target crop (16:9, 1:1, 4:5, 9:16).

## Layout (`grids-layout`)
- Alignment: for each element, minimum distance between its left/center/right (and top/middle/bottom) and those of any other element; average. Lower is better.
- Overlap: mean pairwise IoU of element boxes.
- Occlusion: share of `sal` mass under text or graphic boxes.
- Spacing consistency: variance of gaps within groups vs between groups.
- Caveat: these do not reliably predict perceived quality; use as linting.

## Legibility (`accessibility-legibility`)
- Linearize sRGB channel c (0 to 1): c ≤ 0.04045 → c / 12.92; else ((c + 0.055) / 1.055)^2.4.
- Relative luminance = 0.2126 R + 0.7152 G + 0.0722 B.
- Contrast ratio = (L_light + 0.05) / (L_dark + 0.05). Use the worst-case background pixel region behind text.
- Targets `[Standard]`: 4.5:1 normal text, 3:1 large text.

## Broadcast (`broadcast-standards`)
- Graphics safe rectangle = inner 90% (5% margin each side); action safe = inner 93% (3.5% margin).
- Flag any text box outside graphics safe.
- Simultaneous graphics count; motion magnitude inside graphic regions during holds.

## Image statistics (`image-statistics`)
- Fourier slope: grayscale → FFT → radial average of power → linear fit in log-log over mid frequencies.
- Edge-orientation entropy: orientation histogram of gradient edges → Shannon entropy.
- Fractal dimension: box counting on edge map.

## Video (`continuity-attention`, `motion-principles`)
- Shot boundaries (histogram or learned detector) → shot length list.
- Optical flow magnitude per region per frame.
- Saliency peak distance across each cut (last frame A vs first frame B).

## Value plan for abstract and title frames (`scripts/value_plan.py`, DRAFT 2026-10-23)
- Dark share = share of pixels with L* < 8. Bright share = share with L* > 50.
- Light event = bright share >= 0.3% `[Infer]`. Not a percentile: a single thin streak is a real event but never reaches L* p95.
- Title zone = largest all-calm rectangle on a 16x9 grid (cell mean L* < 6, edge density < 0.2%), as a share of the frame.
- Legibility of type meant to be subtle: the count of `text` boxes look.py's reader finds (Between Words: 9 lines in a top-down ring
  of words, 0 in the grazing frames). More boxes = more readable; set the target from the brief ("about 1 word in 5").

## Sanity checks for every metric
- Run on a known positive and a known negative before trusting it.
- An empty or zero result is a finding about the method until proven otherwise.
