---
id: redshift-render-view-not-final-for-scatter
title: Render view is not the final look for volumes, clouds, refraction or SSS, so test-render at low quality
domain: redshift
tags: [render view, preview, volumes, clouds, refraction, subsurface, test render, low quality]
applies_to: Redshift 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KoL7OAANlJ8, src:yt-transcripts, https://www.youtube.com/watch?v=74lleTzTfC4]
feeds: [redshift, coach, estimator]
conflicts: none
---
Anything involving light scattering (volumes, clouds, refraction, subsurface scattering) can change between the interactive render view and the final render [49:38-50:11].
Do a low-quality test render first: it only adds noise, and the look is represented the same way [50:11].

**Use it:** draft renders for scenes with those features use the real renderer at low quality, not the render view; the coach says so when a look is judged from the preview.
Transcript support: Second upload; same advice to test render at low quality. (https://www.youtube.com/watch?v=74lleTzTfC4 [49:51-50:56])
