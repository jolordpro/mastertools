---
id: pipeline-katana-nuke-bridge-three-comp-modes
title: Nuke Bridge has three comp modes: preview (finished render, headless), live (streaming render, headless) and interactive (opens Nuke)
domain: pipeline
tags: [katana, nuke bridge, live comp, preview comp, interactive comp, lighting comp loop, foundry, deep-read]
applies_to: Katana 5, Nuke (2022)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=xCk4BO4WoTI, src:yt-transcripts]
feeds: []
conflicts: none
---
Foundry Learn [01:00-04:19, 08:27-12:39]. Katana Reader and Writer nodes stand in for Read and Write in a Nuke script; their names become the input points and outputs in the Katana tab. Preview comp: a completed render goes through headless Nuke and the result appears in Katana in seconds. Live comp: a live render streams through headless Nuke so lighting and material edits update the comp. Interactive comp: opens Nuke, and edits on either side show in both. Cancel the live comp but keep the live render to switch it into an interactive comp. Variations pile up in the catalog; graph state variables switch lighting or material setups so any number of looks can be viewed through the comp. The stated gain is no waiting for overnight renders and fewer artist hand-offs.

**Use it:** The idea for a render platform: show the comped result next to the render so lighting changes are judged through the comp, not the raw beauty.
