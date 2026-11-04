---
id: ai-models-nuke-copycat-train-on-pairs
title: Nuke's CopyCat trains a network on a few before/after frame pairs and runs it with Inference; BigCat is a larger model for NukeX
domain: ai-models
tags: [nuke, copycat, bigcat, machine learning, deblur, upscale, training pairs]
applies_to: Nuke 13 onward, Nuke 17
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.foundry.com/insights/machine-learning/copy-cat-guide, src:research-vfx-pipelines, https://www.youtube.com/watch?v=NaCJiquNnYY]
feeds: [per-project model idea]
conflicts: none
---
Used for deblur, upscale and beauty fixes. Nuke 17 (26 Feb 2026) added BigCat; that detail is from a search summary.

**Use it:** a per-project model trained on a project's own frame pairs is an established pattern.
