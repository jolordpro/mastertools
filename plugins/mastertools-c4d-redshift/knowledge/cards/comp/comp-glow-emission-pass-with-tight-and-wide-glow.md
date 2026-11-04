---
id: comp-glow-emission-pass-with-tight-and-wide-glow
title: Glow an emission pass with two glows, a tight one (size about 6) and a wide one (size about 29), and merge with Plus
domain: comp
tags: [glow, emission pass, nuke, bloom, light pass, sarkamari, deep-read, reza, arnold, merged aov, transmission, emission, grade, tight glow, wide glow]
applies_to: Nuke 12.3
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=4A9kbUZpqIU, src:yt-transcripts, https://www.youtube.com/watch?v=xwD_UPqbmCU]
feeds: [comp]
conflicts: none
---
For the emission pass he used two Glow nodes: tolerance 0, a slight orange tint, size 6, brightness reduced for the tight one; a copy at size 29 and brightness 1 for the wide halo [18:36-20:13]. They are combined and the light-pass group is merged into the primary passes with Plus [20:44-21:20]. A Grade can strengthen the subtle transmission pass [17:34-18:36].
Merged from `comp-transmission-and-emission-grade-then-two-glows`: Reza [13:46-17:27]: transmission is subtle: Grade multiply 3 and gain 2.5. Emission: two Glow nodes, one tight (size 6, orange tint, brightness 0.9), one wide (size 30, redder, brighter), merged with plus and then added to the main tree. The glow looks strong alone and calms after combining.

**Use it:** Starting recipe for a glowing-part look; tune size relative to the frame.
