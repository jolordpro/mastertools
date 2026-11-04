---
id: comp-nuke-grade-diffuse-by-depth-before-glossy
title: Darken a background with a depth mask on the diffuse stage, before the glossy pass is added, so reflections stay bright
domain: comp
tags: [alex, levelup plus vfx, nuke, depth pass, mask, reflections, background, focus, deep-read]
applies_to: Nuke
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=ETV1VTV0vNg, src:yt-transcripts]
feeds: [comp]
conflicts: none
---
Use depth shuffled to RGB and graded (black point near, white point far) as a mask; grade gain and gamma down on the background [15:34-16:38]. Lower gamma with lower gain = less contrast in that area.
Placing the same correction before the glossy pass keeps reflection brightness, whereas after the whole rebuild everything dims and reflections get dull; shiny metal then pops a bit more, so apply sparingly and recheck [17:09-18:40].
The background goes a bit muddy brown, which he accepted as more coherent [17:09]. Over-darkening lost the lights' direction, which fog later fixed [19:11].
He steers viewer attention by choice of which area to darken: bottom of frame in the dark version, top in the sunny version [05:38-06:10].

**Use it:** a standard way to push the subject forward without killing specular; ask which stage the darken sits in.
