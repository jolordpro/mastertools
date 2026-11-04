---
id: redshift-openpbr-default
title: OpenPBR is the default for new Redshift materials in Cinema 4D since C4D 2026.2
domain: redshift
tags: [openpbr, materialx, material, default, c4d 2026.2, lookdev, redshift, standard]
applies_to: Cinema 4D 2026.2 and later (bundles Redshift 2026.5)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://help.maxon.net/c4d/en-us/Content/html/COM_REDSHIFT3D_REDSHIFT4C4D_NODES_CORE_OPENPBRMATERIAL.html, https://help.maxon.net/c4d/2027/en-us/Content/html/COM_REDSHIFT3D_REDSHIFT4C4D_NODES_CORE_OPENPBRMATERIAL.html.md, src:research-vfx-pipelines, https://arxiv.org/html/2512.23696v2, https://www.youtube.com/watch?v=dFYep-8B0aU, src:yt-transcripts, https://www.youtube.com/watch?v=ieWk4U63EBw]
feeds: [lookdev checks]
conflicts: none
---
OpenPBR is a MaterialX subproject at ASWF (spec v1.1.1, Apr 2026). Maxon's OpenPBR Material page says it is the default for new materials since C4D 2026.2. That is a Cinema 4D version, not Redshift 2026.2 (checked 2026-10-31; the Redshift ledger carries the same row).
C4D 2026.2 bundles Redshift 2026.5, which matches the Maxon stream below.
Merged from `lookdev-openpbr-default-material`: The Maxon help page confirms the OpenPBR material node; the 2026.2 default claim is from the research file's reading of it. Exports to USD still write Redshift materials as approximations, so a look can differ in other tools.

**Use it:** assume new 2026+ scenes start from OpenPBR, not Standard material, when reading a material graph.
Transcript support: Maxon stream for C4D 2026.2 + Redshift 2026.5 says double-click now defaults to OpenPBR, Auto follows the renderer, Preferences > Material allows Standard or Toon instead. Helps pin the release the ca (https://www.youtube.com/watch?v=dFYep-8B0aU [51:20])
Transcript support: Redshift 2025.4 era: OpenPBR is the new uber shader meant to eventually replace the Standard material; part of the ASWF OpenPBR / MaterialX effort (https://www.youtube.com/watch?v=ieWk4U63EBw [00:03-02:41])
