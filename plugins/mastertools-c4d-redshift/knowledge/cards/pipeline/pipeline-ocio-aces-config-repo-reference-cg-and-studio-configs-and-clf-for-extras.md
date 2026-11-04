---
id: pipeline-ocio-aces-config-repo-reference-cg-and-studio-configs-and-clf-for-extras
title: OCIO's ACES config repo: a reference config (one-to-one with ACES), a minimal CG config for rendering and textures, a studio config later
domain: pipeline
tags: [ocio, aces, config, reference config, cg config, studio config, clf, yaml, built-in transforms, deep-read]
applies_to: OpenColorIO 2.x, 2021 status (planned items may have shipped)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=FSzLwSTJjWo, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Michael Dolan (Epic, OCIO TSC chair) [13:44]. Goals: new BSD-3 code, generated from the ACES dev transform IDs, built on OCIO v2 built-in transforms (algorithms, not LUTs) so the config is self-contained [14:47]. Reference config: one-to-one with ACES dev transforms, a single YAML with no external files, meant to track accuracy and as a base, not a studio config [17:26]. CG config (by Thomas Mansencal of Weta): minimal, only the texture, rendering and display spaces a CG pipeline needs, no camera spaces [19:41]. Studio config: the planned replacement for the v1 ACES config; extra spaces are added through CLF files, and camera IDTs should come from the vendors as CLF [23:13]. Shot-based looks were left out for lack of consensus [24:13]. Also: OCIO 2.1 adds the ACES 1.3 gamut compression, OpenFX plugins, pip-installable Python bindings, and preliminary OSL support (no LUT colour spaces) [06:55, 09:01].

**Use it:** background for choosing the CG config as the platform default; check the repo for what has since shipped.
