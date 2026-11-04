---
id: motion-apple-gesture-rules
title: Gesture rules from Apple (2018): highlight on touch-down, confirm on lift, ~10 pt swipe threshold, 1:1 tracking, detect gestures in parallel
domain: motion
tags: [motion-tokens, product, marcos-alonso, gestures, specs]
applies_to: any
status: V
confidence: high
decay: slow
read: 2026-10-30
recheck_by: 2028-10-30
sources: [https://developer.apple.com/videos/play/wwdc2018/803/, https://www.youtube.com/watch?v=gttSJA-kDmQ, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Marcos Alonso: a button highlights at touch-down and confirms only on lift; add margin around the tap area; dragging out cancels, dragging back re-arms. A swipe begins after about 10 points of movement (hysteresis), then content and touch move 1:1 from the touch point, not the content center. Run all candidate gestures from the start and cancel losers once intent is clear. A double-tap listener adds about half a second to single taps.

**Use it:** List delay sources (double-tap, long press) in the handoff spec.
