---
id: pipeline-contact-sheet-output-for-multi-shot-consistency
title: Output a labelled contact sheet of all shots or all passes from the comp script to spot consistency issues that shot-by-shot review misses
domain: pipeline
tags: [contact sheet, consistency, multi-shot, passes, review, katana, nuke, foundry, deep-read]
applies_to: Katana 5 and Nuke (2022)
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=xCk4BO4WoTI, src:yt-transcripts]
feeds: []
conflicts: none
---
Foundry Learn [13:17-18:08]. A beauty-rebuild script had two outputs: the rebuilt beauty and a contact sheet of every shuffled pass (lights, depth, direct and indirect diffuse and specular, subsurface, transmission), to check each pass at once. A render-layer script gave a comped result plus a contact sheet of the layers. A shot script took each shot as an input and output a labelled contact sheet of the whole sequence, so lighting and material consistency across shots can be seen at once and issues spotted that shot-by-shot review misses. Multi-view compares the original render with the comped result.

**Use it:** Add a sequence contact sheet and a pass contact sheet to the review and delivery steps. Also checks colour space: the presenter noticed the project colour space was wrong while the sheet was open [15:26].
