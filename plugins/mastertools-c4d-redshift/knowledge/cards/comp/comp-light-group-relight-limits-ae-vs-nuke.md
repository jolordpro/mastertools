---
id: comp-light-group-relight-limits-ae-vs-nuke
title: Light groups live only in the Diffuse Lighting AOV; relight intensities in comp, but stacks get huge and Nuke or Fusion are easier than After Effects
domain: comp
tags: [light groups, relight, diffuse lighting, nuke, fusion, after effects, file size]
applies_to: Redshift AOVs
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts, https://www.youtube.com/watch?v=ZrOiwMSGmIw, https://www.youtube.com/watch?v=HA6B5iYxwUI]
feeds: [light-group check]
conflicts: none
---
Filter has no light, so only diffuse lighting needs light groups [1:23:13-1:23:44]. Every light group multiplies the passes and the EXR size [1:24:15]. You can change intensities and turn lights off or on (night scene) but not move them [1:24:48]. After Effects is poor at 3D comp; the same workflow in Nuke or Fusion reads better as a node tree [1:31:35-1:32:39].

**Use it:** Warn about file size before suggesting many light groups, and suggest node-based comp for heavy rebuilds.
