---
id: comp-hugo-guerra-post-comp-grade-on-float-prerender
title: Render the heavy comp to 32-bit EXR and grade in a second, tiny comp that plays in real time with the client
domain: comp
tags: [hugo guerra, grading, prerender, exr, 32 bit float, make comp, nuke studio, real time review, deep-read]
applies_to: Nuke / Nuke Studio
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=FW942ZgK8Ic, src:yt-transcripts]
feeds: [comp, post-composite]
conflicts: none
---
A heavy final comp takes minutes to hours per frame, so it is nearly impossible to grade live [38:25-38:56]. Hugo's team renders the comp as float EXR (plus IDs and depth), then builds a second small comp over it from the timeline (the Make Comp function) with grade and colour nodes only; it often plays in real time [38:56-39:57].
Clients want fast feedback, not to watch the scanline [40:28]. If a big change is needed, go back, re-render that part, return to the 'post comp' (his joke name) [40:58]. He likens it to Flame pre-rendering sections [39:57].

**Use it:** C4D/AE: prerender to EXR 32-bit, then grade/finish in a light comp for client sessions.
