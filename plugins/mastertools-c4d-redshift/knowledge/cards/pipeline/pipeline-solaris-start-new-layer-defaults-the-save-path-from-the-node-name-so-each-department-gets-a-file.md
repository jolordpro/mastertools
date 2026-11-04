---
id: pipeline-solaris-start-new-layer-defaults-the-save-path-from-the-node-name-so-each-department-gets-a-file
title: Solaris: set a node default so every new Start New Layer fills its save path from the node name, giving geo, lights, camera, material and render-settings files
domain: pipeline
tags: [houdini, solaris, usd, start new layer, configure layer, save path, node default, hip, department layers, deep-read]
applies_to: Houdini Solaris (video title says USD 4.2, Sept 2026)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=XUsleR7wJhk, src:yt-transcripts]
feeds: [CHECKS, coach]
conflicts: none
---
The presenter (captions are machine-translated, so details are approximate) shows that Solaris splits layers by built-in rules, and the USD ROP's default save style, flatten implied layers, merges them into one file [00:33-03:42]. Switching to separate layers writes one file per layer [03:42-04:48].
To control it, drop a Start New Layer (same node as Configure Layer) per department, tick start new layer, and set the save path to a $HIP-based expression using the node name, e.g. under a geo/stage folder; rename the node to geo layer, light layer, camera layer, material, render settings [04:48-08:29]. Right-click the path and "make current value default" for both the checkbox and the path so each new node arrives filled in [07:26-07:58].
Save the hip file first, as the path depends on it [02:38-03:10]. Benefit: the light layer can be reused in other shots without one big file [08:29-09:30]. Choose "flatten all layers" only when you want a single file [12:32].

**Use it:** pairs with pipeline-nineb-usd-layers-explicit-save-paths-per-department; this is the node-default shortcut.
