---
id: pipeline-usd-edits-as-nondestructive-overlay
title: Moving things in the Solaris viewport writes edit nodes with a bypass; the source USD file is untouched
domain: pipeline
tags: [usd, non-destructive, edit, bypass, layers, deep-read]
applies_to: Houdini Solaris
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hBYSHFRnFlo, src:yt-transcripts]
feeds: []
conflicts: none
---
Moving an xform-level light group transforms every light below it; toggling the edit node's bypass puts them back [42:01-42:33]. The edit is laid over the base file, so the original is not changed [42:33]. Transforms on meshes add an edit node holding each prim's changes; lights get a light-mixer node; cameras get a camera node that also holds focus distance [43:03-44:36].
Selection filters (prim type, kind, leaf vs xform level, visible-only) decide which level a move lands on [39:57-41:31]. Pick the leaf level for a single mesh, xform level for a whole group.

**Use it:** Describe USD edits as stacked overlays when coaching on versioned handoffs: bypass shows the base, no file is overwritten.
