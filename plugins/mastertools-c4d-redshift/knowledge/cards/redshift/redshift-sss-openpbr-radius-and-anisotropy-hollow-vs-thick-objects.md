---
id: redshift-sss-openpbr-radius-and-anisotropy-hollow-vs-thick-objects
title: Redshift OpenPBR SSS (Effectatron, June 2026): lower radius or anisotropy brings colour in; hollow models need both lowered
domain: redshift
tags: [redshift, sss, subsurface, openpbr, radius, anisotropy, hollow, product viz, effectatron, ledger-check, deep-read]
applies_to: Cinema 4D 2026 + Redshift OpenPBR (video June 2026)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=a9gxWJIFsc0, src:yt-transcripts]
feeds: [redshift, elevate]
conflicts: none
---
Derek Kirk, selling a material pack (read the claims as his). Subsurface colour and the radius-scale colour are the two colours; two numbers shape the result [04:43-06:48]. Radius: in his words, bigger radius lets light travel further before scattering, so more see-through and paler (10 reads as 10 cm); lowering it gives solid, bolder colour [05:14-06:48]. Anisotropy: near 0.9 brings in bolder colour with a wider edge; near 1 gives more see-through white edge lip even with the same radius [06:48-07:49]. A thick blob and a hollow saxophone look different with the same material; for hollow or thin objects lower both [09:55-10:57]. Lighting, especially backlight, matters [12:30]. Other levers: fuzz for softness, spec, IOR, roughness [08:51, 13:00].
Setup notes: use a denoiser, products modelled to real-world scale, UV'd objects work with the blended mapping, spherical mapping as fallback [00:32-01:34, 10:57].
Ledger-check: compare the anisotropy and radius meaning against the skill and `redshift-sss-radius-colour-and-scale`; his 'anisotropy balances colour vs white' is his explanation, not Maxon's doc.

**Use it:** coach: when SSS looks wrong on a thin or hollow model, suggest lowering radius then anisotropy before touching colour.
