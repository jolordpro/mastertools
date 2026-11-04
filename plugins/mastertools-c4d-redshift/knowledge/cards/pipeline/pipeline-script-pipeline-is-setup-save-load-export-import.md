---
id: pipeline-script-pipeline-is-setup-save-load-export-import
title: A script pipeline mostly does three jobs: set up the software, save and load, export and import
domain: pipeline
tags: [pipeline, scripting, save load, publish, startup, automation, deep-read]
applies_to: any (film, animation, games pipelines)
status: V
confidence: medium
decay: slow
read: 2026-10-30
recheck_by: 2029-10-30
sources: [https://www.youtube.com/watch?v=MtFYQx3Jq5E, src:yt-transcripts]
feeds: []
conflicts: none
---
Speaker is the TD Academy host (surname garbled in captions). Setup: correct resolution, frame rate, plugins and paths when an app starts [24:04-24:34]. Save/load enforces file creation and naming; export/import controls what goes to the next department [25:06-25:38]. Anything else (an auto-rigger, say) is department tooling, not pipeline [25:38-26:09]. Typical GUIs: a launcher and a save dialog that enforces the naming so nobody types v1 vs v001 by hand [27:10-28:13]. The open-source example is Plex (GitHub) [22:30].

**Use it:** Use as the scope for any small tooling: setup, save, publish, import; keep the rest as separate tools.
