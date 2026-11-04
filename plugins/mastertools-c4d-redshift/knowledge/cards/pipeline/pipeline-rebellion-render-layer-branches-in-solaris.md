---
id: pipeline-rebellion-render-layer-branches-in-solaris
title: Split a USD scene into parallel branches per comp layer, each with its own visibility and matte settings
domain: pipeline
tags: [rebellion vfx, evil genius 2, solaris, render layers, takes, matte, holdout, deep-read]
applies_to: Houdini Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NNUtKYRmcjY, src:yt-transcripts]
feeds: [comp, CHECKS]
conflicts: none
---
The opening island shot needed many comp and matte-painting layers: objects hidden from camera but still casting shadows, matted, or hidden entirely. In Solaris he splits the stream and edits each branch separately, so the top of all branches is identical and each branch's settings are visible as nodes [17:41-18:44].
He prefers this to Houdini takes, which get hard to track across versions or when also used for lighting and rendering [17:10].
Benefit: if a frame is wrong, follow the node chain upstream to see where it changes [18:44].

**Use it:** model for a render-layer plan - one visible chain per layer, not hidden overrides.
