---
id: motion-korenman-responsive-rules-replace-multi-aspect-redesign
title: Rive-style responsive rules (percent of screen, flip when taller than wide) replace redoing an animation per aspect ratio
domain: motion
tags: [joey korenman, school of motion, rive, responsive design, aspect ratio, 16x9, 9x16, display ads, deep-read]
applies_to: Rive, After Effects
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=0Uxq1IEKpFE, src:yt-transcripts]
feeds: []
conflicts: none
---
The pain: animating at 16:9 and again at 9:16, or delivering about 15 display-ad sizes [27:40, 28:19].
UI tools (Webflow, Figma) already solved it with rules: this block takes 30% of the screen, that one 70%, flip the layout if the screen is taller than wide. After Effects only has clunky expressions for this; Rive has the rules built in and the same file plays correctly on any size [28:19-28:49].
Fits live events and conferences where the final screen size is unknown [28:49].

**Use it:** a design principle for multi-aspect broadcast deliverables: build layouts as rules (anchors, percentages) so aspect changes are rule changes, not rebuilds.
