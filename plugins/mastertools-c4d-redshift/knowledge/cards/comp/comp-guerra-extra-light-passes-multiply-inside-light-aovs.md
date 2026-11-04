---
id: comp-guerra-extra-light-passes-multiply-inside-light-aovs
title: Make extra light passes from normals and position, but multiply them inside the diffuse of the matching light AOV, and reduce the sun there
domain: comp
tags: [relight, normals pass, position pass, light passes, point lights, aov, hugo guerra, deep-read]
applies_to: Nuke relight, USD 3D
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=NaCJiquNnYY, src:yt-transcripts]
feeds: []
conflicts: none
---
Using Foundry's relighting template with normals and position passes, he positioned lights and rendered raw light passes [21:29-22:23]. Do not put them over the top or just multiply: apply them in the diffuse section of the light AOVs. This shot had dome, sun and GI; he cut the sun and added the new lights there [22:23-22:55]. Point lights snapped to USD tower positions made rudimentary light passes, which were then filtered [22:55-23:27].

**Use it:** When adding practical lights in comp, treat them as part of the light-AOV stack, not a top layer. Pairs with comp-relight-normals-detail.
