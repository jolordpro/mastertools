---
id: pipeline-usd-prefilter-by-schema-kind-and-custom-kinds
title: Pre-filter USD traversal on cheap metadata (schema type, kind, specifier) before checking attributes; define own kinds in JSON
domain: pipeline
tags: [usd, traversal, kind, schema, metadata, filter, plugin json, luca scheller, deep-read]
applies_to: OpenUSD
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=VSE7ayrRStg, src:yt-transcripts]
feeds: []
conflicts: none
---
Pipeline work is mostly traversing the hierarchy and getting or setting attributes [17:25]. Core metadata is fast to look up, so filter by type schema, specifier, activation and kind first [23:38-24:08]. Stage traversal uses an iterator; layer traversal runs a function over every path, including attributes and variants, and sees the whole layer [24:40, 58:48]. The base kinds are only a start, so make your own with a JSON file; custom metadata fields and fallback properties are also just JSON [25:13-26:16]. Only the asset resolver needs compiled code [26:16].

**Use it:** A scene-check scripted on USD should start with schema/kind filters.
