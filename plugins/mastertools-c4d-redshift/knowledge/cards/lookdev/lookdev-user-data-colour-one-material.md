---
id: lookdev-user-data-colour-one-material
title: One Redshift material can carry many colours by reading the object display colour through a Color User Data node
domain: lookdev
tags: [color user data, display color, mograph color, material count, redshift]
applies_to: Cinema 4D 2025 + Redshift
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=wsF5c_UnE40, src:yt-transcripts, https://www.youtube.com/watch?v=MuVzbVhMUvI, https://www.youtube.com/watch?v=HlQhMbjrM6M, https://www.youtube.com/watch?v=_6toVWN7NMo]
feeds: [lookdev sheet, variant engine]
conflicts: none
---
Pipe a Color User Data node (MoGraph colour preset) into the colour input, then set each object display colour to Automatic and pick its colour [09:07-10:08]. Three statue parts shared one plastic material. He keeps roughly one plastic, one rough plastic, one metal and so on instead of 50 copies. Cloner clones need Render Instance mode for the colour to show [14:47].

**Use it:** Count materials in the scene card and suggest this when many near-identical materials differ only by colour.
Transcript support: Same one-shader idea using Geometry ID colour through ramp and Change Range (see new card). (https://www.youtube.com/watch?v=MuVzbVhMUvI [35:33-42:15])
Transcript support: Color User Data set to Redshift display colour drives one material per object (https://www.youtube.com/watch?v=HlQhMbjrM6M [05:16-05:59])
Transcript support: Adds the Geometry ID Color preset for clones, a Ramp with Step interpolation for flat colours, and knot width as colour share (https://www.youtube.com/watch?v=_6toVWN7NMo [32:54-35:28])
