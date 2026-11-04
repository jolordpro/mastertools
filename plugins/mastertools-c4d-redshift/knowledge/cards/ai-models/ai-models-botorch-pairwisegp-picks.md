---
id: ai-models-botorch-pairwisegp-picks
title: BoTorch PairwiseGP learns a hidden quality score from A-vs-B picks, and EUBO chooses the next pair to show
domain: ai-models
tags: [botorch, pairwise gp, preference learning, eubo, bayesian optimisation, taste model, ab picks]
applies_to: BoTorch / BoFire
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://experimental-design.github.io/bofire/docs/tutorials/advanced_examples/pairwise_gp.html, https://leojklarner.github.io/gauche/notebooks/preferential_bayesian_optimisation.html, src:research-verticals]
feeds: [PLAN 4.1, M4 Advisor]
conflicts: none
---
The default fit is an approximation and can be poor on skewed data; check with held-out picks. Licence MIT is unverified.

**Use it:** every option picked or turned down trains it, and it asks the most useful next question.
