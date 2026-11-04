---
id: motion-vlms-weak-at-speed
title: Video models judge speed badly (best 14.3% on MotionBlind), so measure motion with flow and keyframes and let the model write the words
domain: motion
tags: [motion, critique, vlm, speed, motionblind, optical flow, keyframes]
applies_to: Q3 2026 models
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.alphaxiv.org/abs/2609.09528, src:research-frontier-ai]
feeds: [PLAN Phase 1 motion critique]
conflicts: none
---
MotionBlind pairs clips that differ only in motion: Gemini 3.1 Pro scored 60% overall but 14.3% on speed; open models sat near chance.
Safe design: feed the model measured numbers plus a contact sheet, ask for timestamped notes, drop notes that disagree with the curves.

**Use it:** build motion critique on measured curves first; use the model only for wording.
