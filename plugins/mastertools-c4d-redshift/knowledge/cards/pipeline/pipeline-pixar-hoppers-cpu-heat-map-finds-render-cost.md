---
id: pipeline-pixar-hoppers-cpu-heat-map-finds-render-cost
title: Pixar's Lightspeed team uses a CPU heat map to find what makes a shot slow, then has departments simplify it with no visible change
domain: pipeline
tags: [pixar, hoppers, lightspeed, render time, heat map, diagnostic render, leaves, deep-read]
applies_to: any (Pixar RenderMan pipeline)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=Vj2OAptTQD4, src:yt-transcripts]
feeds: [[estimator, redshift, shakedown]]
conflicts: none
---
Ann Fu (Pixar Lightspeed, Hoppers) [24:09-25:44]: shots are rendered many times during development, so cost compounds. A diagnostic render shows a CPU heat map where brighter pixels mean more time spent. A tree in one shot rendered much slower than similar shots; the heat map pointed at the leaves; departments supplied a version with the leaves simplified; the heat map got much dimmer and the image showed little or no difference. Why it happens: artists work rough to fine and leave geometry that does not reach the final image, and it steals resources from what matters. Goal stated: faster and more efficient while keeping the artistic intent.

**Use it:** Same move for a heavy Redshift frame: find the hot region (time or sample heat view if available), simplify only there, A/B against the full version at the same crop.
