---
id: ai-models-hpsv3-pickscore-preference-recipe
title: HPSv3 and PickScore show the recipe: pairwise picks into a reward head on a frozen VLM
domain: ai-models
tags: [hpsv3, pickscore, pick-a-pic, reward model, preference, bradley-terry]
applies_to: 2025
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://arxiv.org/html/2508.03789v1, https://github.com/ModelTC/HPSv3, https://arxiv.org/pdf/2305.01569, src:research-verticals]
feeds: [taste critic M4]
conflicts: none
---
HPSv3 (ICCV 2025) is Qwen2-VL based, trained on HPDv3 (1.08M text-image pairs, 1.17M pairwise comparisons), `pip install hpsv3`. PickScore/Pick-a-Pic is CLIP-H tuned on open user picks. Licence shown as Apache on the HF card with a conflicting mirror.

**Use it:** use as a second opinion and as the template for a taste reward head.
