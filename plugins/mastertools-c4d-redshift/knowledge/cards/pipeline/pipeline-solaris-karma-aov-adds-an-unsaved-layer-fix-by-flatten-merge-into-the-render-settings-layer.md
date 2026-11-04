---
id: pipeline-solaris-karma-aov-adds-an-unsaved-layer-fix-by-flatten-merge-into-the-render-settings-layer
title: Solaris: Karma render settings with an AOV create an extra layer with no save path; flatten-merge them into the settings layer to clear the warning
domain: pipeline
tags: [houdini, solaris, karma, aov, render settings layer, merge style, flatten layers, usd warning, deep-read]
applies_to: Houdini Solaris with Karma (Sept 2026 video)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=XUsleR7wJhk, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Adding a beauty AOV after the Karma render settings node makes a second layer with no save path; the USD ROP warns and puts it in an auto location, which still works [09:30-10:31].
Fix [10:31-12:02]: merge the settings and the AOV with the merge node's style set to flatten layers, set the render-settings layer's save path on that, then use another merge in separate-layers mode. The AOV's properties then live inside the render-settings USD, with the output path, and no stray folder appears.
Take care: this is one presenter's walkthrough, with translated captions.

**Use it:** a USD handoff check can flag any layer without a save path before it ships.
