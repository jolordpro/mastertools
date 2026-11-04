---
id: pipeline-prism-unreal-two-project-folders-exchange
title: Prism links a versioned Unreal project folder to the Prism project and exchanges USD, cameras and renders between them
domain: pipeline
tags: [prism, unreal, perforce, usd, sequencer, shots, deadline, epic mega grant, deep-read]
applies_to: Prism 2 (private beta mid-2023), QuiltiX early dev
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=GE6Af6hjYfI, src:yt-transcripts]
feeds: []
conflicts: none
---
Unreal keeps its own project folder under version control (for example Perforce); Prism keeps its folder. The plugin moves data both ways: export USD, Alembic, FBX or OBJ into Unreal; export a layout camera back for animators; render from Sequencer into the Prism structure so Nuke or Resolve load it with the normal naming [10:29-12:05]. Three shots from Houdini came into one Sequencer with matching frame ranges, camera, lights and materials, and could be rendered locally or sent to Deadline [12:35-14:13]. A camera tweak made in Unreal was exported as USD and layered on top of the shot in Houdini [13:39-14:13]. Funded by an Epic MegaGrant [10:29].

**Use it:** Pattern for C4D-to-engine work: keep two roots, move only published versions, and bring camera changes back as files.
