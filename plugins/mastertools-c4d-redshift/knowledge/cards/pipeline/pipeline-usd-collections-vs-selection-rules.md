---
id: pipeline-usd-collections-vs-selection-rules
title: USD collections are saved in the file; Solaris selection rules live only in the Houdini project
domain: pipeline
tags: [usd, collections, selection rules, handoff, solaris, deep-read]
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
Both save a group of prims by path pattern (for example toy-circle slash star) [46:42-49:21]. The difference: selection rules are Houdini-only and are stored in the project file; collections are written into the USD file on disk [50:24-50:54].
Rule given: if the grouping has to travel to someone else through a file, make a collection; if it is only for your own working, a selection rule is fine.
A collection is then recalled in later nodes with a percent sign plus its name, for example moving only the "random toys" group [54:03-54:33].

**Use it:** When setting up a handoff, store named groups (hero assets, bg props) as collections so the next department sees them.
