---
id: motion-salih-lottie-authoring-rules
title: Lottie authoring rules: shape layers, few keyframes, short layer names, test at 60 fps
domain: motion
tags: [motion-tokens, product, salih-abdul-karim, toolkit, spec]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=RAAVPSHik0k, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
From the 2017 School of Motion podcast: convert artwork to shape layers; know the supported list (strokes, gradients yes; some effects no); each keyframe adds file size so use few; keep layer names short; animate at 30 fps but preview at 60 because the app runs at 16 ms frames. Lottie rebuilds the Bezier timing curves instead of baking frames. Unsupported features were left out when approximating them risked breaking the animator's intent.

**Use it:** A toolkit spec should list what is supported, size costs and a test frame rate.
