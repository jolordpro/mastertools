---
id: comp-octane-imager-exposure-highlight-compression-needs-srgb-and-bloom-is-a-flaw
title: Octane camera imager works after the render: highlight compression only shows if the colour space is sRGB, and bloom is a sensor defect to use sparingly
domain: comp
tags: [octane, new-plastic, camera imager, exposure, highlight compression, white point, bloom, glare, deep-read]
applies_to: Octane for Cinema 4D (2022 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=J5KwV7GfbEQ, src:yt-transcripts, https://www.youtube.com/watch?v=mNcq8GD1mfI]
feeds: [[redshift, shakedown]]
conflicts: none
---
Camera imager settings (exposure, gamma, highlight compression, white point, saturation, vignette, hot pixel remover) are applied after render, so changing them does not re-render; do them in post if you prefer [20:18][22:22]. Highlight compression recovers detail in bright areas when exposure is raised, but only if the render settings colour space is sRGB; in linear it will not show [20:48][21:20]. White point works like white balance: pick a white from the scene, and push its saturation to counter a colour cast, but too much overcompensates [21:20][21:51]. Bloom (post effects, with cutoff as the brightness threshold) and glare add glow; he says in real life bloom is a flaw and CG artists add such defects for realism, but "a little goes a long way" and an image that is good without it does not need it [22:54][23:25][23:56]. Hot pixel remover is for fireflies [21:51].

**Use it:** shakedown checks: confirm which colour space the highlight-compression test was made in, and treat bloom as a last 5% rather than a fix.
Transcript support: Highlight compression turned almost fully up in the camera imager to stop two white spots on the car; hot pixel removal on https://www.youtube.com/watch?v=8zCqKpeF5Uc [03:43-04:48] cleared fireflies on diamonds. (https://www.youtube.com/watch?v=mNcq8GD1mfI [04:15-04:47])
