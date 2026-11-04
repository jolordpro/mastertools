---
id: comp-cryptomatte-recolour-variants
title: Team-colour variants could be recoloured with Cryptomatte in comp instead of re-rendered, except where GI bounce must change
domain: comp
tags: [comp, cryptomatte, variants, recolour, team colours, takes, sports graphics]
applies_to: any
status: U
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [src:research-vfx-pipelines, src:research-gaps-deep, https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts]
feeds: [PLAN variant engine]
conflicts: none
---
Proposal: render once, vary in comp on ID-matted surfaces.
Also proposed: use Cryptomatte as the selection mask for masked AI edits, always showing the mask and testing its edges.

**Use it:** list per variant whether it needs a re-render or only a re-comp.
Transcript support: Cryptomatte matte plus hue/sat on the diffuse filter recolours one object; bounce limits large changes [1:19:01]. (https://www.youtube.com/watch?v=CXx75LxGxOw [1:16:26])
