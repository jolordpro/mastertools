---
id: pipeline-nvidia-usd-validator-rules
title: NVIDIA's open USD validator has 40 rules, including manifold, normals, zero-area faces, extents, units and up axis, missing references, normal-map colour space
domain: pipeline
tags: [usd validator, nvidia, geometry checks, normals, manifold, texture checker]
applies_to: usd-validation-nvidia
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://nvidia-omniverse.github.io/usd-validation-nvidia/validation/docs/rules.html, src:research-production-pipelines, https://www.youtube.com/watch?v=opfHGm0lWyM, src:yt-transcripts]
feeds: [CHECKS geometry hygiene]
conflicts: none
---
Named checkers: ManifoldChecker, NormalsExist/Valid/Windings, ZeroAreaFaceChecker, WeldChecker, UnusedMeshTopologyChecker, ExtentsChecker, StageMetadataChecker, MissingReferenceChecker, TextureChecker, NormalMapTextureChecker, MaterialUsdPreviewSurfaceChecker, UsdDanglingMaterialBinding. Apache-2.0.

**Use it:** name our geometry checks after these; a USD export lets the validator run for free.
Transcript support: BowerBot checks units, outside dependencies and structure on every asset package. (https://www.youtube.com/watch?v=opfHGm0lWyM [06:37])
