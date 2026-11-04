---
id: pipeline-opencue-2019-gaps-no-licence-scheduling-no-user-system-linux-only
title: OpenCue roadmap at SIGGRAPH 2019: Linux-only, no licence-aware scheduling, no user management and no REST API yet; Windows support was a month or two away
domain: pipeline
tags: [opencue, roadmap, windows, licence limits, user management, rest api, in memory scheduler, siggraph 2019, deep-read]
applies_to: OpenCue 2019 (state as of Aug 2019)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=0gXT3sntiFg, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Roadmap items said aloud: Windows support (blocked mainly by Python 3 conversion, estimated one to two months, [11:30-12:01]); general resource limits including software licences, which the scheduler could not yet count, near release [07:33, 17:39]; built-in users with LDAP or Active Directory and finer permissions (nothing then, so jobs ran with open access [07:33-08:04]); more host-app plugins (Blender first, Houdini next [09:07]); a scheduler rewrite from database queries to in-memory [09:39]; no REST API, only gRPC with published proto files [51:21]; an event API for job-done notifications in development [48:09]. Licensing per user cannot be handled per job: all jobs run as one generic user or each as its own user [40:37-41:08].

**Use it:** before choosing OpenCue or similar for a C4D+Redshift farm, check these gaps today (Windows, licence limits); this list is from 2019 and likely out of date.
