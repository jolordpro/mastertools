---
id: pipeline-usd-automated-publish-check-before-human-review
title: Let a plain-Python USD script check that every referenced texture and shader exists before a person reviews the publish
domain: pipeline
tags: [[usd, validation, publish, review, python, automation, textures], deep-read]
applies_to: any
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=hNzbznG0ywU, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
The presenter (channel 辛浩然, manual English subtitles) adds a machine review step ahead of the human one: use USD's Python module to confirm every texture referenced by a USD file can be found on the server, and that a submitted folder holds all its files; if most shaders are missing, never send it to a person [10:24-11:30]. It runs on vanilla Python without opening Maya or Houdini, so it is fast [11:30]. He ties it to a written spec document that the stage checks are validating against [10:24].

**Use it:** A cheap gate for the platform's scene check: resolve all asset paths from the file itself before any artist time.
