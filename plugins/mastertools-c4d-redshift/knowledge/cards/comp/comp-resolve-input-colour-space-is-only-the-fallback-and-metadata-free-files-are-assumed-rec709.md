---
id: comp-resolve-input-colour-space-is-only-the-fallback-and-metadata-free-files-are-assumed-rec709
title: In Resolve colour management, "input color space" is just the default for clips without metadata, so ProRes files may be read as Rec 709 and look wrong
domain: comp
tags: [team-2-films, davinci-resolve, rcm, input color space, prores, metadata, red log, deep-read]
applies_to: DaVinci Resolve (colour managed)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=w0ubDSzEEYg, src:yt-transcripts]
feeds: [[shakedown, post-composite]]
conflicts: none
---
Setup he shows: colour science DaVinci YRGB Color Managed; timeline colour space DaVinci Intermediate; delivery Rec 709 gamma 2.4 [15:07][15:37][16:09]. Treat the project's input colour space as the default assumption used when Resolve cannot identify a clip; RED files with metadata were converted correctly, while ProRes files without metadata were assumed Rec 709 and displayed wrongly [15:37][16:09]. Fix: select the clips together, right-click, Input Color Space, choose the true space (his were LogC3) [16:39]. Individual clips can bypass colour management when troubleshooting [18:46]. For ACES, uncheck automatic colour management and set the processing mode to custom [15:07].

**Use it:** shakedown line for a client's rushes: check whether clips carry colour metadata, and fix input spaces by hand where they do not, before judging the grade.
