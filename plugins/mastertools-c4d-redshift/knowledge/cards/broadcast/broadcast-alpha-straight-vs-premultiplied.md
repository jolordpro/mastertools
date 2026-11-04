---
id: broadcast-alpha-straight-vs-premultiplied
title: Straight versus premultiplied alpha mismatch is the classic failure when overlays reach a post house
domain: broadcast
tags: [alpha, premultiplied, straight, prores 4444, export, premiere, resolve]
applies_to: practice
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://blog.frame.io/2024/09/25/insider-tips-export-with-alpha-davinci-resolve/, src:research-production-pipelines]
feeds: [delivery profile]
conflicts: none
---
Premiere cannot export premultiplied directly (export straight, convert in AE). Resolve exports alpha only with Export Alpha ticked and a straight or premultiplied choice. Sources are forum threads and a Frame.io guide.

**Use it:** the delivery check reads the real output file and names its alpha type.
