---
id: redshift-release-2026-9
title: Redshift 2026.9 (16 Sep 2026) moved to OpenColorIO 2.5.2
domain: redshift
tags: [redshift 2026.9, ocio, opencolorio, version, release]
applies_to: Redshift 2026.9
status: V
confidence: medium
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://digitalproduction.com/2026/09/16/redshift-2026-9-tightens-the-bolts/, src:research-agency-pipelines, src:research-vfx-pipelines]
feeds: [version-match check]
conflicts: none
---
Redshift 2026.9 shipped 2026-09-16. It upgrades OpenColorIO to 2.5.2 and fixes a display-profile naming problem.
It also adds Houdini 22 and Solaris support, a USD 26.05 build and Hydra viewport hair controls (nothing C4D-specific).
Coverage advises testing any custom OCIO config before rolling it out. This sits after the ledger's version baseline (taken 2026-08-20), so it extends it rather than disagreeing.

**Use it:** version-match checks should know that 2026.9 carries OCIO 2.5.2 and re-test custom configs after the upgrade.
