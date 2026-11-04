---
id: pipeline-opencue-windows-2020-cuebot-postgres-java-rqd-per-blade
title: OpenCue on Windows (2020): Cuebot needs Java and PostgreSQL, every blade runs RQD, GUI needs PySide 5.11.2
domain: pipeline
tags: [opencue, cuebot, rqd, postgresql, java, pyside, cuegui, cuesubmit, windows, render manager, deep-read]
applies_to: OpenCue (early 2020, Windows 10, Maya)
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-31
sources: [https://www.youtube.com/watch?v=AnVFAQv44Vs, src:yt-transcripts]
feeds: []
conflicts: none
---
VFX Pipeline channel, part 3 of a series. Parts: Cuebot server (a Java jar, run from a batch file with data source = PostgreSQL host, database user cuebot and password, and a log folder; Spring Boot start-up text means it is up) [02:09-05:19]; RQD, the daemon on every render machine [05:19-07:23]; GUI (CueCommander and Cuetopia) and CueSubmit, which need PySide 5.11.2 from an extra requirements file or they error [00:33-01:38, 05:51-07:23].
Submit fields: show, shot, facility (local or cloud), layer, job type, services, frame range, Maya scene path [08:25-10:34]. RQD starts and controls Maya batch processes; closing RQD kills them [12:41]. Add blades by running RQD on each with environment variables from a network location pointing at the database [15:18-15:49]. A frame-preview error was left unsolved [14:17].

**Use it:** a minimal checklist for a self-hosted OpenCue farm: database, Java, Cuebot, RQD per node, GUI deps, shared scene path.
