---
id: motion-unreal-3d-text-fit-and-marquee-auto-tiling
title: Use the engine's 3D text actor for fitted text; marquee strips auto-tile from image size in the material
domain: motion
tags: [unreal, text, marquee, tiling, per-character animation, broadcast graphics, deep-read]
applies_to: Unreal Engine 4.27 (concepts carry to UE5)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bcL001ZFHBQ, src:yt-transcripts]
feeds: []
conflicts: none
---
The 3D Text actor (shown flat) offers outline, spacing, tracking and per-character animation, and can limit text size by character count and available space, which Sidhu calls one of broadcast graphics' most frustrating problems [13:02-13:55].
Scrolling marquees are just a panning texture prepared outside; since each strip differs in length, the material reads the texture resolution and calculates tiling itself, so no per-variant manual values [13:55-14:41].

**Use it:** Auto-fit text and length-independent scrolling strips are both worth building into any team-name template.
