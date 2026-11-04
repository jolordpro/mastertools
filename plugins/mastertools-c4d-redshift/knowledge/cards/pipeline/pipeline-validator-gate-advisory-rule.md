---
id: pipeline-validator-gate-advisory-rule
title: A machine may block only on spec questions; look-match, quality and client questions stay advisory
domain: pipeline
tags: [validator, gate, advisory, tech check, creative review, supervisor, blocker]
applies_to: any
status: U
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [src:research-vfx-pipelines]
feeds: [validator engine design]
conflicts: none
---
Job posts and practice split it four ways: spec (levels, naming, passes, handles) is machine work; match to approved look and neighbours is CG supervision, measured by machine and ruled by a person; quality is the creative lead; satisfaction is producer and client. Proposal: three validator kinds, gate (blocks submit), advisory (ranked), optional (project switch), each with an optional click-to-fix. A model pass can never be a blocker.

**Use it:** only code checks against a written spec may stop a submit.
