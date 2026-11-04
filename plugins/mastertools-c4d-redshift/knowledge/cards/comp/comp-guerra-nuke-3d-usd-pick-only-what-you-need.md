---
id: comp-guerra-nuke-3d-usd-pick-only-what-you-need
title: In Nuke's new USD 3D system, import the full scene but pick only the needed geometry; it gives true 3D motion blur, filtering and reflections
domain: comp
tags: [nuke 17, 3d system, usd, motion blur, reflections, filtering, hugo guerra, deep-read]
applies_to: Nuke 17
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=NaCJiquNnYY, src:yt-transcripts]
feeds: []
conflicts: none
---
Bringing the whole CG scene into Nuke is heavy, so he picked only the bridge and floor, then reduced further [09:27-10:31]. The new scanline renderer gives proper 3D motion blur (no vector-blur hack) and sampling, slower as sampling rises, plus working reflections [10:31-11:33]. He used a higher-res floor because the CG one relied on bump maps [12:37]. Positioning footage cards on real geometry made drop and rain placement accurate [14:41]. Limits he hit: ProRes must be converted to EXR sequences [14:09]; the particle system is not supported in the new 3D system [17:17]; it can also output AOV passes including UV [18:47].

**Use it:** Check Nuke 17 capabilities before asking for a CG re-render: a USD import with reflections may solve a puddle or floor request.
