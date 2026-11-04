---
id: broadcast-add-new-team-enum-datatable-steps
title: Adding a team to a data-driven package: enum row, data table row, duplicated material, car blueprint
domain: broadcast
tags: [unreal, new team, enum, data table, tricode, workflow, deep-read]
applies_to: Unreal Engine 4.27 (concepts carry to UE5)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bcL001ZFHBQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Order [17:35-20:13]: (1) add a row to the team enum by tricode (full name optional for hover); (2) add a data-table row whose first column matches the tricode; (3) duplicate an existing team's material and swap in the textures; (4) link textures and choose the colour set in the row; (5) for a custom car, duplicate the existing car blueprint so it shares the same child class (sponsors change often) and point the row at it; (6) switch to the team in the controller and play the sequence to confirm.
They use blueprints not raw meshes so lights and options can be added to each variant [19:40].

**Use it:** This is the template for 'onboard a new team in under an hour'; reuse the order when speccing a client package.
