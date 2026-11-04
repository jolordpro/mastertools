---
id: motion-ae-outsource-keyframes-one-slider
title: Drive many layers from one set of keyframes by tying each to a 0-100 slider with a linear expression
domain: motion
tags: [after effects, expressions, linear, slider, keyframes, leaderboard, live graphics]
applies_to: After Effects
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=M4FLVszXkbk, src:yt-transcripts]
feeds: [motion-critique, coach]
conflicts: none
---
BallerFX calls it "outsourcing keyframes" [F 16:35]. One slider goes 0 to 100; each layer's position uses linear(slider, 0, 100, start, end) so they all move by one number [20:54]. Keyframes sit once on a controller and every team layer points at that slider [16:35-17:36].
Result: updating a single value per team reorders the whole board; no per-layer keying.

**Use it:** template design advice for data-driven boards: one driver per item, keyframes in one place, tune timing once.
