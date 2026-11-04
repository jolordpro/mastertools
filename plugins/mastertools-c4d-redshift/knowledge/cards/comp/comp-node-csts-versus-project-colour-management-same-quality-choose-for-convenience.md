---
id: comp-node-csts-versus-project-colour-management-same-quality-choose-for-convenience
title: Node-based CSTs and project-based colour management can deliver the same quality; choose project-level unless you need per-conversion tweaks
domain: comp
tags: [team-2-films, davinci-resolve, cst, project color management, workflow, deep-read]
applies_to: DaVinci Resolve
status: V
confidence: medium
decay: slow
read: 2026-10-31
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=w0ubDSzEEYg, src:yt-transcripts]
feeds: [[post-composite]]
conflicts: none
---
Team 2 Films: both can give the same high-quality image within reason; node-based gives extra settings on each conversion, but most jobs do not need that and it adds complication [14:04][14:36]. He combines them: project-level management for the bulk, and a pair of CSTs (camera to intermediate at the start, intermediate to delivery at the end) only when a clip needs tweaking; grades sit between them scene-referred [18:46][19:18]. Timeline-based grades can cause problems with the node setup [19:18]. Use project-based even when everything is Rec 709, for a scalable base when HDR or log arrives; color management is a technical process, not a creative choice [19:49][20:20][22:22]. "Time is money" is his reason to avoid extra complexity [22:22].

**Use it:** a default for the render/comp pipeline: one global colour setup, with per-clip overrides logged.
