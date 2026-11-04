---
id: redshift-openpbr-convert-tool-anisotropy-caveat
title: Material Tools can convert Redshift Standard materials to OpenPBR; anisotropy rotation needs a manual surface tangent step
domain: redshift
tags: [openpbr, convert, standard material, anisotropy, surface tangent, material tools, redshift 2026.5]
applies_to: C4D 2026.2 / Redshift 2026.5
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=dFYep-8B0aU, src:yt-transcripts, https://www.youtube.com/watch?v=ieWk4U63EBw]
feeds: [redshift, shakedown]
conflicts: none
---
[53:00] Material tools > convert and replace RS standard materials to OpenPBR. Wiring is kept; four test materials (substance, fabric, plastic, wood) looked identical.
[55:36] Exception: OpenPBR has no anisotropy rotation input. Connect a Surface Tangent (user tangent) node to rotate the reflection stretch, e.g. brushed metal.
[51:20] Preferences > Material has a Default Material setting: Auto gives OpenPBR for Redshift; Standard or Toon can be chosen.

**Use it:** after a bulk conversion, flag anisotropic materials for a check.
Transcript support: No anisotropy rotation in OpenPBR; connect a Surface Tangent node to the anisotropy tangent input (specular and coat), then rotation works (https://www.youtube.com/watch?v=ieWk4U63EBw [04:46-05:55])
