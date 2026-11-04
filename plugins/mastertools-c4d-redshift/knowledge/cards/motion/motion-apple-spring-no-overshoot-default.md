---
id: motion-apple-spring-no-overshoot-default
title: Start springs at 100% damping; add overshoot only where the driving gesture carries momentum
domain: motion
tags: [motion-tokens, product, nathan-de-vries, springs, bounce]
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
Nathan de Vries' rule: tools should stay out of the way, so default to no overshoot. Example from the Music app: tapping the mini player uses 100% damping (no momentum in the tap); swiping to dismiss uses 80% for a little squish because the swipe has momentum. Bounce can also be a functional hint (the iPhone X flashlight button bounces to teach a firmer press).

**Use it:** Tie bounce to a stated cause in the spec: gesture momentum or a teaching hint.
