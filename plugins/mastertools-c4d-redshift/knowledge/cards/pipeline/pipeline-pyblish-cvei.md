---
id: pipeline-pyblish-cvei
title: Pyblish defines the publish spine: Collect, Validate, Extract, Integrate; a failing validator stops extraction
domain: pipeline
tags: [pyblish, publish, validation, collector, validator, extractor, integrator, cvei]
applies_to: Pyblish
status: V
confidence: high
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://pyblish.gitbooks.io/developer-guide/content/workflow.html, src:research-vfx-pipelines]
feeds: [validator engine design]
conflicts: none
---
Order guideline: Collector 0, Validator 1, Extractor 2, Integrator 3. An instance is a slice of the scene that can become a file; plug-ins attach by family; shared data sits on a Context. Licence (LGPL) is from memory.

**Use it:** model the platform's checks as collect, validate, extract, integrate with stable families and ids.
