---
id: comp-slap-comp-dof-and-per-light-relight-from-passes
title: A slap comp for lighting review: character over the back plate with two grade variants, a Z-defocus matched to the plate's focal plane, and per-light exposure
domain: comp
tags: [slap comp, z defocus, relight, light passes, exposure, grade variants, katana, nuke, deep-read]
applies_to: Nuke, Katana 5 (2022)
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=xCk4BO4WoTI, src:yt-transcripts, https://www.youtube.com/watch?v=jfH7JpjDO_w]
feeds: []
conflicts: none
---
Foundry Learn [18:39-24:29]. Lighting artists review a character on the real back plate with warm and cool grade outputs side by side, which shows lighting errors early. To integrate: ZDefocus with mask type depth, output 'focal plane setup', put the focal point on the character's face (it matched the plate's in-focus plane), then raise the depth of field and size sliders and compare to the plate. The foreground and background of the plate were slightly soft, so the CG armour on the far side was slightly defocused. Relight by shuffling each light AOV (window, environment, ceiling) and adjusting exposure per light before merging, like a beauty rebuild; the exposure values can be copied back into the lights or kept in comp. Here the ceiling light was lowered because the plate was darker to the right, and the window light raised.

**Use it:** The coach can use this as the per-light exposure route when a fix is cheaper in comp than in a re-render; the defocus step is a plate-match check.
