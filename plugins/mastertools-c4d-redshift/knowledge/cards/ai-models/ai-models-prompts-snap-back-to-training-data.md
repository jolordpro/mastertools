---
id: ai-models-prompts-snap-back-to-training-data
title: Gen-AI models always answer and drift back to what they were trained on, so prompts only work inside the model's data
domain: ai-models
tags: [[prompting, hallucination, training-data, bias, basse], deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bWvxBu_vVes, src:yt-transcripts]
feeds: [coach]
conflicts: none
---
Hanno Basse's working model: a network always outputs something, so a missing concept (an unknown term, a 360 camera orbit never in training data) gets a plausible guess instead of "I don't know" [30:07][37:22]. The 360 orbit usually just spins the subject [37:54].
Training data has peaks and gaps; a prompt inside a peak (or between two peaks, like pajamas on a dog) works, one on a slope is unpredictable, so a prompt that "works" for one person fails for the next [58:07][59:38].
Example: changing a late-30s woman's outfit to a nurse's uniform gave a younger, shinier-haired woman, because curated social photos dominate the data [1:00:09]. An "Italian plumber" can return Mario [1:04:18].
His image: models act like cats, not dogs; you follow where they go [1:05:51]. Fixes are added training data: LoRA or fine-tuning [1:06:22].
Caveat: a high-level talk by a CTO, not measured.

**Use it:** When a director asks AI for a specific camera move or a named look, assume it falls outside the data and plan a conditioned or 3D-driven route instead of more prompt words.
