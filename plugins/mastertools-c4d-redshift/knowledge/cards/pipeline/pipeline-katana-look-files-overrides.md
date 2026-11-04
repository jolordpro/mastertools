---
id: pipeline-katana-look-files-overrides
title: Katana look files bake materials and assignments per asset per pass, with overrides; lighting resolves the right look per pass
domain: pipeline
tags: [katana 9, look files, overrides, usd superlayer, layered templates]
applies_to: Katana 9 (Feb 2026)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://learn.foundry.com/katana/9.0/Content/ug/look_files/handing_off_looks.html, https://digitalproduction.com/2026/02/11/katana-9-deepens-usd-and-previews-hydra-2/, src:research-vfx-pipelines]
feeds: [layered templates]
conflicts: none
---
Katana 9 adds UsdSuperLayer and a UsdGaffer lighting node with light and shadow linking. The same layering shows in Gaffer Boxes and References and in USD composition: project, sequence, shot, variant, each changing only what differs, which makes diffs cheap.

**Use it:** save a look-dev sheet as a look record with variants.
