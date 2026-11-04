---
id: motion-apple-spring-duration-bounce
title: Apple's public spring controls (2023): duration and bounce, bounce from -1 to 1, default 0
domain: motion
tags: [motion-tokens, product, jacob-apple-springs, springs, tokens]
applies_to: any
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://developer.apple.com/videos/play/wwdc2023/10158/, https://www.youtube.com/watch?v=HaZ2jw9rx9M, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
'Jacob' (surname unconfirmed) says Apple adopted duration and bounce across its frameworks. 0 bounce is smooth, positive bounce overshoots, negative bounce is flatter. About 15% reads brisk, 30% clearly bouncy; he cautions against going above about 0.4 in UI. Pick pacing (duration) first, then character (bounce). Unsure? Use 0. SwiftUI presets such as snappy are tunable starting points. Apple supplies formulas to convert to mass, stiffness, damping.

**Use it:** Document springs as duration plus bounce; keep a conversion note for engineers.
