---
id: ai-models-mitsuba3-differentiable-rendering
title: Mitsuba 3 is a differentiable renderer for solving light colour and intensity by gradient descent; CPU works on Apple Silicon
domain: ai-models
tags: [mitsuba 3, differentiable rendering, inverse rendering, gradient descent, apple silicon, bsd]
applies_to: Mitsuba 3
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://github.com/mitsuba-renderer/mitsuba3, https://mitsuba.readthedocs.io/en/latest/src/inverse_rendering/gradient_based_opt.html, src:research-verticals]
feeds: [bet 1 light match]
conflicts: none
---
Backends are LLVM (CPU) and CUDA, no Metal named; macOS arm64 is tested. The scene must be rebuilt in Mitsuba, so for scenes with light groups plain least squares on the passes is simpler and exact.

**Use it:** use Mitsuba only for lights not yet in the scene.
