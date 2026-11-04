---
id: comp-post-dof-zone-render-fringe-fix
title: Fast Bokeh Pro's zone control blurs near, focus and far separately to cut fringing from post depth of field
domain: comp
tags: [depth of field, fast bokeh, post dof, fringe, zones, z depth]
applies_to: After Effects plug-in Fast Bokeh Pro (about $50 in 2024)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=IcLiz8e8ffc, src:yt-transcripts, https://www.youtube.com/watch?v=pKfKsUYpk4w]
feeds: [comp-fix planner, coach]
conflicts: none
---
Post DoF fails when a near object is strongly blurred: the pass cannot know what is behind it, like shooting through a fence. The fix is two renders, about double the time [1:02:24-1:03:26].
Render each zone (near, focus, far) separately then re-composite to hide fringes; the focus plane and blur radius stay editable without a re-render [1:15:06-1:18:24].
Every post DoF pixel is technically wrong; low values hide it. Turn off the camera DoF in Redshift or it is applied twice [1:36:36].

**Use it:** advise post DoF only when the scene has no near strongly-blurred foreground, and offer the zone approach otherwise.
