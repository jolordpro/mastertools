---
id: comp-nuke-grade-only-the-reflections-subtract-grade-add-with-a-cryptomatte-mask
title: To regrade one material's reflections or colour separately: Shuffle out the glossy pass, Merge 'from' it, Grade with a Cryptomatte mask, then Merge 'plus' it back
domain: comp
tags: [alfie-vaughan, nuke, cryptomatte, glossy direct, shuffle, merge from, merge plus, mask, deep-read]
applies_to: Nuke, Blender Cycles passes
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=fxfuhl8Q7ys, src:yt-transcripts]
feeds: [composition]
conflicts: none
---
Cryptomat node: pick Crypto Material, Ctrl-click or drag to add areas (car paint), Ctrl to remove, alpha view shows the matte [08:50-09:53]. Shuffle Glossy Direct, Merge with operation 'from' under the Unpremult to take reflections out, a second Merge 'plus' to put them back; with nothing between them the result is unchanged [10:24-11:26]. Put a Grade between the two with the Cryptomat as its mask to raise reflections on the paint only [11:26]. Put a ColorCorrect there instead to make the paint redder under untouched reflections [11:56-12:27]. He judged by eye over the footage: the reflections looked muted next to the real world.

**Use it:** Use as the pattern for 'make the car paint redder without touching highlights' notes; needs Cryptomatte and a separate glossy pass in the render.
