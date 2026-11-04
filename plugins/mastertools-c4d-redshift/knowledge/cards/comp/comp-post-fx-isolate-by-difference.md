---
id: comp-post-fx-isolate-by-difference
title: Redshift has no post-effects AOV; subtract the no-post Beauty from the with-post RGB to get the post effects
domain: comp
tags: [post effects, bloom, glow, beauty, difference, aov, comp]
applies_to: Redshift in C4D, After Effects
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, https://www.youtube.com/watch?v=7uY4-bPvRKs, src:yt-transcripts, https://www.youtube.com/watch?v=yl28HkA-qyo]
feeds: [comp-fix planner, CHECKS]
conflicts: none
---
The Beauty AOV is the render without post effects; the final image carries bloom, glow and streaks. Put Beauty over the final in Difference mode to see only the post look [30:47] [31:18].
Add that difference back over the rebuilt pass stack, with its own opacity or duplicates to dial it up or down. Zak shows the same method with Add on top [40:00-41:37].
Trainers say they want a real post-effects AOV; use Redshift post only as a preview and redo it in comp [31:18].

**Use it:** a comp-fix step that keeps both outputs (final and Beauty) so post effects can be dialled in comp without a re-render.
