---
id: comp-colorcorrect-node-is-destructive-use-last
title: The ColorCorrect node and gamma cannot be cleanly reversed; stay with multiply and exposure and use them last
domain: comp
tags: [tony lines, colorcorrect, gamma, destructive, non-destructive, luma key, nuke, notes, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=ZrOiwMSGmIw, src:yt-transcripts]
feeds: [shakedown, comp]
conflicts: none
---
Multiply reverses exactly and can be reordered freely. Gamma only reverses if the undo sits right after the original, and a swapped order gives a different image [49:18-50:51].
ColorCorrect applies luma-keyed shadow, mid and highlight ranges (smooth S-curves). After the first move the luma has changed, so a second node grabs different ranges and cannot undo it, even keyed from the original [51:53-54:57]. Changing anything upstream of it also changes its look, so you are node-locked [55:00-56:00]. Stacked ones are like paint with no undo: add more or start over [56:32-57:03].
His rule: do exposure and multiply first, ColorCorrect only at the very end, accepting that the lighter can never reproduce it [58:03-59:04].

**Use it:** Shakedown flag for comp scripts: many stacked ColorCorrect/gamma nodes mid-tree means notes will be hard to action.
