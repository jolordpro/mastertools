---
id: image-statistics
title: Statistical image properties, scale invariance and fractals
type: science
aliases: [natural image statistics, SIPs, statistical image properties, 1/f, Fourier slope, scale invariance, fractal dimension, edge orientation entropy, PHOG, self-similarity]
tags: [redies, taylor, spehar, computational, evidence-strong-descriptive]
related: [fluency-complexity, texture-detail, clutter-peripheral, metric-recipes, tools-models]
evidence: strong as description of art and nature; mixed as a cause of beauty.
updated: 2026-10-20
---

# Image statistics

## Quick answer
- Artworks across cultures share statistics with natural scenes: Fourier power slope near −2 and high edge-orientation entropy. `[E-strong]`
- People on average prefer fractal patterns with dimension D around 1.3 to 1.5. `[E-strong on average]`
- Use these as naturalness and texture diagnostics. Do not use them as quality scores.

## Definition
- **Fourier slope**: how image energy falls from coarse to fine detail. Natural scenes ≈ −2 for power (−1 for amplitude).
- **Edge-orientation entropy (EOE)**: first-order = how evenly edge directions are spread; second-order = how independent orientations are across positions.
- **Fractal dimension D**: from 1 (smooth line) to 2 (fills the plane).
- **PHOG self-similarity**: how alike the gradient patterns are across image regions and scales.

## Mechanism
- `[E-mixed]` The visual system is tuned to natural-scene statistics; images matching them may be processed efficiently (links to fluency).
- `[Infer]` Artists may converge on these statistics by matching what looks "right," not by intent.

## Evidence
- Graham & Field 2007; Redies et al. 2007: monochrome art and natural scenes share a power slope near −2. `[E-strong]`
- Redies, Brachmann & Wagemans 2017: high first- and second-order EOE in artworks from diverse cultures, independent of content. `[E-strong]`
- Spehar, Clifford, Newell & Taylor 2003 (n = 220): D 1.1 to 1.2 low preference; 1.3 to 1.5 high; 1.6 to 1.9 low. Density-matched random dots showed no preference. `[E-strong on average]`
- Street et al. 2016: individual differences shape fractal preference. `[E-mixed]`
- Taylor et al. 2011: Pollock's D rose from about 1.1 to 1.3 (1945) to about 1.7 to 1.9 (1950). Mid-range D linked to lower physiological stress. `[E-mixed]`
- Geller et al. 2022: statistical image properties predicted ratings of style-transferred abstract images. `[E-mixed]`
- Tool: Redies-lab Aesthetics Toolbox (2025, *Behavior Research Methods*; arXiv 2408.10616). Computes color and lightness stats, three Fourier-slope variants, fractality, PHOG self-similarity, symmetry, EOE, CNN feature variances.

## Techniques
- `[Practice]` Natural textures (foliage, water, clouds, crowds) bring scale-rich detail that tends to read as pleasant.
- `[Infer]` Flat vector graphics will score "unnatural" on these metrics. That is fine for design.

## By medium
- Photography and painting: most useful here.
- Design and typography: type has legitimately lower EOE and different spectra. Do not penalize.
- Film: Cutting et al. 2018 found shot durations, scene durations, motion and sound became more fractal-like over film history; luminance, clutter and shot scale did not. `[E-mixed]`

## How to measure
- Grayscale → 2D FFT → radially averaged power → log-log fit slope.
- Edge detection → orientation histogram → Shannon entropy (first order); pairwise orientation correlation across distance (second order).
- Box-counting fractal dimension on edge map.
- Easiest route: run the Redies toolbox (check its license before production).

## Failure modes
- Treating "closer to −2" as "better."
- Comparing statistics across different content types (portraits vs posters).

## Critique questions
- Is the texture richness natural and scale-varied, or uniform and mechanical?
- Does a flat design intend to look graphic, so these stats don't apply?

## Terms
- 1/f, scale invariance, Fourier power spectrum, spectral slope, edge orientation entropy, fractal dimension, box counting, PHOG, self-similarity

## Sources
- Graham & Field 2007; Redies et al. 2007, 2017; Spehar et al. 2003; Street et al. 2016; Taylor et al. 2011; Geller et al. 2022; Redies toolbox 2025.
