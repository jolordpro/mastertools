---
id: pipeline-comfyui-desktop-auto-update-broke-workflow
title: ComfyUI Desktop auto-updated overnight and broke a style-transfer workflow; pin the version a job started on
domain: pipeline
tags: [comfyui, version pinning, auto update, ryan summers, lts, snapshot, deep-read]
applies_to: ComfyUI Desktop (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=dsYggO4lsSo, src:yt-transcripts, https://www.youtube.com/watch?v=ktSEt_8T9MA]
feeds: [pipeline, shakedown]
conflicts: none
---
Summers [22:19-24:55]: after a Friday-night run, his workflow was dead on Saturday morning. The desktop app had updated itself at about 3:30 am and a single mis-indented bracket in the update broke it; he fixed it line by line with strangers on Discord.
His rule: control it like a VFX pipeline, stay on the one version that works even if three new ones ship. A ComfyUI staffer said the git version does not auto-update and a snapshot feature to lock a workflow was planned or partly built [23:52-25:00].
Sarofsky wants a Blender-LTS style stable line so a six-month-later client change can reopen the same graph [24:23].

**Use it:** estimator and pipeline notes for AI shots: record tool version, turn off auto-update, keep the install that made the approved look.
