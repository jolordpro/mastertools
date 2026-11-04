---
id: education-pattern-masks-and-undo-trail
title: Keep AI edits masked and non-destructive, and make each change one undoable step with a plain-words history line
domain: education
tags: [ux pattern, mask, undo, audit trail, cryptomatte, maxon mcp, firefly]
applies_to: 2026
status: V2
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://community.adobe.com/announcements-698/firefly-image-5-preview-in-photoshop-generative-fill-1554211, https://architosh.com/2026/10/whats-in-maxons-new-cinema-4d-mcp-server/, src:research-gaps-deep]
feeds: [undo log, mask check]
conflicts: none
---
Adobe advises limiting Firefly 5 effects with a layer mask; a July 2026 bug report said generation cut off at the selection edge. Maxon's MCP groups each AI batch into undo steps with a local audit log.

**Use it:** use Cryptomatte as the selection, always show the mask, and teach from the history list.
