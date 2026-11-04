---
id: pipeline-output-tokens-project-camera
title: Name outputs from tokens, such as a project-name folder and a project_camera file name, so nothing is named by hand
domain: pipeline
tags: [tokens, output path, naming, $prj, $camera, exr, 8-bit png]
applies_to: Cinema 4D tokens (2023)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=le17-h6tUD0, src:yt-transcripts, https://www.youtube.com/watch?v=Mw5hb-hVEh0]
feeds: [CHECKS, delivery step]
conflicts: none
---
Output path pattern: initials folder, a project-name folder from $prj, then file name made of $prj and $camera [42:04-43:07].
Tokens also read computer name, frame, pass, date and time; Cineversity adds more [40:31-42:04]. For comping render half-float EXR; ACES is baked in an 8-bit PNG [41:01].

**Use it:** a pre-flight check should confirm output uses tokens for project, camera and take.
Transcript support: Another C4D user types renders/ then project-name token, project-name file with the camera token; the folders are created on first render and an incremented project file gives test0001 style names (https://www.youtube.com/watch?v=Mw5hb-hVEh0 [05:15-07:52])
