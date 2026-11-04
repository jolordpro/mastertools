---
id: comp-composure-composite-mesh-vs-screen-space-texture
title: Composure plate mode: composite-mesh projection can show hard normal lines, screen-space texture gives best quality but is tied to the screen
domain: comp
tags: [[unreal, composure, screen-space, composite-mesh, normals], deep-read]
applies_to: Unreal Engine 5.7 Composure
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=zlZCKT-5pLU, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Composite mesh mode projects the plate from the camera onto geometry, so the card can be orbited around; hard lines tied to the geometry can appear in renders from odd normals [27:46-28:30]. Raising the mesh resolution helps a bit. Switching the plate layer mode from composite mesh to texture gives screen space: best fidelity, but it follows the screen when the camera moves away [28:30-29:02].
Setup order he uses [14:12-18:43]: enable plugin, place composite actor, assign camera, add a mesh to composite mesh content with the lit mask material, make an Image Media Source, a media player with media texture, and a Media Track in Sequencer at the same fps (24).

**Use it:** Choose the mode per shot: parallax needs the mesh, final polish uses screen space.
