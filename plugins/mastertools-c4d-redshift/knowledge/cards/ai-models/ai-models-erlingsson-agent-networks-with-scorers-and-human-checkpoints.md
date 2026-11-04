---
id: ai-models-erlingsson-agent-networks-with-scorers-and-human-checkpoints
title: "Ingi Erlingsson's Systems studio builds agent pipelines with scoring checkers and set human check-in points, and avoids loops that take hours"
domain: ai-models
tags: [ingi-erlingsson, systems, agents, quality control, scoring, localization, nike, polish, deep-read]
applies_to: any
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=XnaT-aJQZM0, src:yt-transcripts, src:polish-roster]
feeds: [shakedown, coach]
conflicts: none
---
Each agent has a narrow job; configure them to remove ambiguity and add quality-control agents that score output (for example 25 of 50 sends it back) [1:34:38-1:36:11]. Place human decision points deliberately; a system where everyone checks everything can take 7 hours for an image [1:41:20-1:41:50]. Example: a footwear brand localising a campaign across markets needs predictable results: one checker compares the shoe to the 3D model or images, one checks type spelling, another scores against the original art out of 10 [1:40:17-1:42:21]. The system must be able to swap in the latest model [1:36:43].

**Use it:** A model for the platform's QC: narrow checkers with scores, a threshold that loops back, and a visible human gate.
