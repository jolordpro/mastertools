---
id: motion-apple-spring-settling
title: A spring's perceptual duration is not its settling time, so do not wait on settling for UI changes
domain: motion
tags: [motion-tokens, product, jacob-apple-springs, springs, timing]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://developer.apple.com/videos/play/wwdc2023/10158/, https://www.youtube.com/watch?v=HaZ2jw9rx9M, src:yt-transcripts]
feeds: [studies/motion-leaders]
conflicts: none
---
Springs decay forever in theory; the settling duration (when motion is too small to see) varies with the other parameters. The duration parameter is a perceptual number chosen to stay stable. For follow-up UI changes, SwiftUI's completion handling keys off the perceptual duration.

**Use it:** Never chain UI work to a spring's end by hard-coded settling time.
