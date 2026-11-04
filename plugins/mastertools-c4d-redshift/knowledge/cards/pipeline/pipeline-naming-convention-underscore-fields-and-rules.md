---
id: pipeline-naming-convention-underscore-fields-and-rules
title: Name files as underscore-separated fields (name, task, version, comment) and define every rule once
domain: pipeline
tags: [pipeline, naming convention, underscore, version v001, abbreviations, scripts, deep-read]
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
Speaker is the TD Academy host (surname garbled in captions). Why: consistency lets later scripts parse names; split on underscore to get name, task, version, comment, extension [13:37-14:39]. Define version format once (v1, v01 and v001 all appear in the wild) [14:39-15:10]. Rules he lists: English only, no spaces, underscores, versions as v plus three digits, artists as initials, defined abbreviations (for example geo, scan) [16:43-17:49]. Inside software, suffix group names (_grp) so scripts can find them [17:49-18:21]. Artist name and comment can go in a tracker rather than the filename [18:21-18:54].

**Use it:** Adopt as the render-file naming standard; document abbreviations in the same note.
