---
id: broadcast-unreal-size-to-texture-adaptive-width
title: Size to Texture modifier keeps fixed height and changes width so wide and square logos both fit
domain: broadcast
tags: [unreal, logo, adaptive width, size to texture, team logos, deep-read]
applies_to: Unreal Engine 5.5-5.6 Motion Design
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=QWT8IAUfWSk, src:yt-transcripts]
feeds: []
conflicts: none
---
Speaker is David Grownick, Epic senior product specialist and ex Fox Sports real-time graphics, so vendor view. Logos vary in shape (a wide one vs a square one). With the modifier, geometry keeps a fixed height (512 in the demo) and adapts width, or the reverse; adaptive width is expected to be the 90 percent case [38:23-39:25]. The test swapped a square logo for a wide one of about 1260 px width and the layout held.

**Use it:** Specify logo plates as fixed height, variable width in team-based templates.
