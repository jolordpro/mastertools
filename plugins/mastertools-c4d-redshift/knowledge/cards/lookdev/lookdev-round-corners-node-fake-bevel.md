---
id: lookdev-round-corners-node-fake-bevel
title: The Round Corners node plugged straight into the bump input fakes a bevel highlight without changing geometry
domain: lookdev
tags: [round corners, bevel, bump, shader, rim light, highlight, radius, redshift, bump blender, edge highlight, material, deep-read]
applies_to: Redshift 2026
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=kN00Z7UsW5U, src:yt-transcripts, https://www.youtube.com/watch?v=UjThhVMuV18, https://www.youtube.com/watch?v=TonSU8Ljm5c]
feeds: [elevate, shakedown, redshift]
conflicts: none
---
Effectatron [18:17-19:49]: add Round Corners, preview through colour, samples 12, radius about 0.05 (cm), then connect it to the material's bump input directly, not through a bump node. Keep it tiny; large radii look wrong. A real 0.02 fillet on a cube already adds believable edge light [17:45].
Merged from `lookdev-rs-round-corners-into-bump-blender-parametric-bevel`: Harsh 90 degree edges look computery [13:29]. Instead of a geometry bevel he adds a Round Corners node, then a Bump Blender whose first input is the existing bump and second is Round Corners; blend weight starts at nothing and must be raised [14:00]. Default radius is too soft, bring it down; he ends around 0.25 (spoken, units not stated) [14:32]. Copy the same two nodes to the veneer material [15:03]. Benefit: no modelling, stays parametric. Keep the bevel subtle.

**Use it:** supports the existing bevel card; offer the shader bevel when geometry cannot be beveled.
Transcript support: Used instead of bevel on bad topology; plugs straight into bump. (https://www.youtube.com/watch?v=TonSU8Ljm5c [54:53-56:31])
