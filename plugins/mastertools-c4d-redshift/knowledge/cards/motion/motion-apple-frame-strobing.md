---
id: motion-apple-frame-strobing
title: Smoothness depends on change between adjacent frames, not frame rate alone
domain: motion
tags: [motion-tokens, product, chan-karunamuni, frame-rate, motion-blur]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2028-10-30
sources: [https://developer.apple.com/videos/play/wwdc2018/803/, https://www.youtube.com/watch?v=gttSJA-kDmQ, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Chan Karunamuni: a fast object at 30 fps strobes; at 60 fps the same look tolerates faster movement. Motion blur and motion stretching add information per frame (the iPhone X app-launch icon stretches as it opens and closes). Speed limits follow from frame rate, so check peak speed, not just fps.

**Use it:** When setting a max travel speed token, test it at the lowest target frame rate.
