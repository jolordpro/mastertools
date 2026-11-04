---
id: comp-post-dof-zdefocus
title: Post depth of field: anti-aliased depth breaks at edges; edge-extend the depth or render depth at double resolution
domain: comp
tags: [comp, depth of field, zdefocus, nuke, depth pass, edges, aa]
applies_to: Nuke ZDefocus
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://learn.foundry.com/nuke/content/reference_guide/filter_nodes/zdefocus.html, src:research-vfx-pipelines, https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts, https://www.youtube.com/watch?v=CXx75LxGxOw, https://www.youtube.com/watch?v=pKfKsUYpk4w, https://www.youtube.com/watch?v=4A9kbUZpqIU, https://www.youtube.com/watch?v=b0hbVd9aZkA, https://www.youtube.com/watch?v=fxfuhl8Q7ys]
feeds: []
conflicts: none
---
Anti-aliased depth gives wrong in-between depths at edges, so subjects get halos.
Fine hair is hard; glass, out-of-focus reflections and real bokeh shape should stay in the render.

**Use it:** move DoF to comp only for hard-edged opaque subjects with a clean depth pass.
Transcript support: near blurred object cannot be fixed in post; two renders; zone rendering hides fringes (https://www.youtube.com/watch?v=IcLiz8e8ffc [1:02:24])
Transcript support: Do post DoF last; extremely shallow DoF mixes blurry pixels, so render fg/bg elements separately [1:31:03]. (https://www.youtube.com/watch?v=CXx75LxGxOw [1:30:32])
