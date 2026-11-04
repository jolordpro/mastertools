---
id: lighting-maya-three-point-fill-at-half-key-quadratic-decay-and-gamma-off
title: Three-point recipe in Maya: key at 45 degrees, fill at half the key intensity, a low narrow rim behind; use quadratic decay and turn the preview gamma off
domain: lighting
tags: [maya, arnold, three point lighting, key light, fill light, rim light, decay, spotlight, what make art, deep-read]
applies_to: Maya 2020-21, Maya Hardware 2.0 and Arnold
status: V
confidence: low
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=1nYSVw6-GxA, src:yt-transcripts]
feeds: [elevate]
conflicts: none
---
What Make Art's block on a curved backdrop: key spotlight about 45 degrees to the subject, intensity 8,000, with soft penumbra, wide cone, ray-traced shadows with a light radius and about 20 shadow rays [03:54-06:13]. Fill is a duplicate at 4,000, half the key, at an angle to the key [06:43]. Rim is a third light brought low, level with the object, behind it, with a much narrower cone, to give reflected light that separates the object from the backdrop [07:18-08:23]. Default no-decay lights are unrealistic; quadratic decay needs far higher intensity (thousands) [04:30]. Turn off the sRGB gamma on the light to preview what the PNG will show [05:05]. Maya native lights keep intensity when scaled, Arnold lights change intensity when scaled [03:18]. Arnold needed roughly 14,000 key and 7,000 fill to match the hardware preview and gave much cleaner shadows [13:17]. Use a separate renderable camera so the preview view stays put while lights move [10:34].

**Use it:** The 2:1 key-to-fill starting point and "scale changes intensity" warning for area lights are handy defaults for the lighting coach.
