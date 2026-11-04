---
id: redshift-scalar-user-data-drives-metalness
title: Scalar User Data (for example MoGraph Weight) can drive metalness or roughness per clone without using the colour channel
domain: redshift
tags: [scalar user data, mograph weight, metalness, roughness, effector, redshift]
applies_to: Cinema 4D 2025 + Redshift
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=wsF5c_UnE40, src:yt-transcripts, https://www.youtube.com/watch?v=3Z6Td_LTpH0]
feeds: [lookdev sheet]
conflicts: none
---
Colour user data uses up the colour channel; scalar user data is a separate 0-100% value [15:20]. A plane effector with a weight transform and a field wrote weight; a Scalar User Data node set to MoGraph Weight into Metalness made only the weighted clones metallic [15:51]. Other scalar sources include object ID, index ratio, clone offset, fall-off weight and particle data [16:21]. After changing a variable, refresh the node.

**Use it:** Offer it when a variant needs per-clone material properties, and flag that it is not visible until the node is refreshed.
Transcript support: scalar user data named scale drives toon noise scale per object in one material. (https://www.youtube.com/watch?v=3Z6Td_LTpH0 [07:47-09:50])
