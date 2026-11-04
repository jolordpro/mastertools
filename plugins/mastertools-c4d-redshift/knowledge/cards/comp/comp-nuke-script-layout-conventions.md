---
id: comp-nuke-script-layout-conventions
title: Keep a comp tree readable: inputs top to bottom, elements from the left, mattes from the right, aligned nodes
domain: comp
tags: [courtney price, nuke, foundry, script layout, node graph, handoff, backdrop, deep-read]
applies_to: any
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=yl28HkA-qyo, src:yt-transcripts, https://www.youtube.com/watch?v=xwD_UPqbmCU]
feeds: [shakedown]
conflicts: none
---
Courtney Price [38:35-41:45]: reads at the top and writes at the bottom; elements come in from the left (like the A input of a merge) and mattes and key-mix masks enter from the right. Use backdrop nodes and right-angle elbows, and keep nodes snapped and spaced; a free Nukepedia aligner by Walter Gilsing helps. A spider-web script costs more time to debug.
Goal: anyone picking up the script can find and fix things without asking you.
She also warns against fast but unplanned work: speed is not efficiency; planning an approach costs a little early and saves time at the end [42:16].

**Use it:** Apply the same top-to-bottom, left-for-image, right-for-matte rule to After Effects precomp and layer order handoffs.
