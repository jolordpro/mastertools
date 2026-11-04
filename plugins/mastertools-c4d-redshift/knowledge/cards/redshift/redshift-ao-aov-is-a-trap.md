---
id: redshift-ao-aov-is-a-trap
title: The built-in Ambient Occlusion AOV is not the AO you want; use a Custom AOV with the AO Pass utility as the default material
domain: redshift
tags: [ambient occlusion, custom aov, ao pass, max distance, default material override]
applies_to: Redshift 2024-2025
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=CXx75LxGxOw, src:yt-transcripts, https://www.youtube.com/watch?v=xwD_UPqbmCU, https://www.youtube.com/watch?v=OMTPokoFp5E]
feeds: [AOV package]
conflicts: [redshift-ao-aov-built-in-from-c4d-2025-3-1-replaces-utility-material-route]  # Redshift with C4D 2025.3.1+ has a built-in AO AOV (U8); this card is the older route
---
The AO AOV only refers to the AO shader on materials, so almost nobody uses it [47:07]. Make a Custom AOV named AO, type Direct, with a default material of Utilities > AO Pass, which applies to every object [48:10]. It does not need bucket mode [49:17]. Set Max Distance in cm; left unset it renders very dark [49:48-51:55]. He tunes by eye.

**Use it:** The AOV package builder should create AO this way and the check should flag the stock AO AOV as the wrong one.
Transcript contradicts: From C4D 2025.3.1 there is a native AO AOV with the utility-material options built in, so the custom-AOV workaround may no longer be needed (older card is about earlier versions) (https://www.youtube.com/watch?v=OMTPokoFp5E [00:33-01:34])
