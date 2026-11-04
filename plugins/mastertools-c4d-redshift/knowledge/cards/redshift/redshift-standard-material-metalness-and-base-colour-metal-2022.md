---
id: redshift-standard-material-metalness-and-base-colour-metal-2022
title: Redshift Standard material (2022): metalness 1 makes metal, base colour tints it, default roughness 0.2, iron near 0.4
domain: redshift
tags: [standard material, metalness, base color, roughness, thin film, pbr, ledger-check, lionel, maxon, deep-read]
applies_to: Redshift 3.x in C4D R26 (2022); newer builds default to OpenPBR
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=TonSU8Ljm5c, src:yt-transcripts]
feeds: [lookdev, redshift, coach]
conflicts: none
---
Lionel: the new Standard material follows the metalness workflow used by Arnold, Pixar and games. Metalness 0 is dielectric (plastic), 1 is metal [23:59-24:31]. Metal colour comes from base colour: light blue for bluish, very bright for chrome, dark grey for iron [24:31-25:34]. Default roughness 0.2; he used about 0.4 for iron [25:34].
Difference from the old RS Material: that one needs the Fresnel type changed to get metal; transmission, refraction and SSS behave as before; thin film is new, for soap or oil [38:36-40:13].
Sci-fi trick: build one good material then duplicate and change colour, roughness and texture scale (yellow, brown bronze) [1:01:23-1:04:24, host remark 1:03:52].

**Use it:** lookdev: current builds default to OpenPBR; check the Redshift ledger before quoting these values.
