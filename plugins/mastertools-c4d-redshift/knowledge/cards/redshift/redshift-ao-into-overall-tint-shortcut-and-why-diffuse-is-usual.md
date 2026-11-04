---
id: redshift-ao-into-overall-tint-shortcut-and-why-diffuse-is-usual
title: AO node into the material's Overall Tint darkens the whole material quickly, but diffuse is the usual place because it spares reflections
domain: redshift
tags: [ambient occlusion, overall tint, shortcut, material, lionel, maxon, deep-read]
applies_to: Redshift 3.x in C4D R26 (2022)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=TonSU8Ljm5c, src:yt-transcripts]
feeds: [lookdev, redshift]
conflicts: none
---
He plugged the AO node into the material's Overall Tint with lower intensity and a grey, which gave a much denser shadow [1:04:55-1:07:10]. Called almost dirty and a last-minute trick: the usual placement is the diffuse colour, because Overall Tint also dims reflections; here the dimming gave nicer shadows but was too strong [1:07:10-1:07:42].
Host Dustin said he had not used AO inside overall tint before.

**Use it:** coach: offer as a time-poor trick with the reflection-dimming warning.
