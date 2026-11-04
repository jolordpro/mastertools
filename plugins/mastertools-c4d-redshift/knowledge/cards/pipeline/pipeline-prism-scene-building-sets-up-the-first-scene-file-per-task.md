---
id: pipeline-prism-scene-building-sets-up-the-first-scene-file-per-task
title: Prism scene building: one run applies frame range, imports environment, camera, character and animation caches, then a post script, per task
domain: pipeline
tags: [pipeline, prism, scene building, houdini, maya, nuke, blender, automation, deep-read]
applies_to: Prism 2 (FMX 2026 talk)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
Constantin (Prism team). The core scene building tool creates the first scene file automatically: it applies frame range and FPS, imports available products, and each step can be enabled by asset or shot and by department or task [12:07-12:38]. Available in Houdini, Maya, Nuke and Blender, with separate settings per DCC [12:07-12:38]. Demo, Maya lighting with Alembic: environment and camera from layout, character from surfacing, caches from animation, and a custom post script to turn on viewport textures [13:09-13:40]. USD demo: the animation scene loads the USD shot container, and Maya rigs convert to Maya data so animation starts at once [14:20]. In Nuke (version 16 and 17 graph-scope variables) the same tool builds a multi-shot comp with a shot switch at the top and per-shot overrides [46:34-47:35].

**Use it:** Script the empty-session start for each department so no artist sets frame range or imports by hand.
