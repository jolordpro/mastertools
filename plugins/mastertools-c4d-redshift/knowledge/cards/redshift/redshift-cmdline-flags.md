---
id: redshift-cmdline-flags
title: redshiftCmdLine takes a scene file plus -oip, -opbp, -oro, -gpu, -cachepath, -texturecachebudget and -listdevices
domain: redshift
tags: [redshiftcmdline, command line, headless, farm, oip, gpu, rs file]
applies_to: Redshift 2025.2-2027
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://help.maxon.net/r3d/cinema/en-us/Content/html/The+redshiftCmdLine+tool.html, src:research-gaps-deep]
feeds: [PLAN 0A spike, Phase 2 farm]
conflicts: none
---
-oip overrides image and AOV paths; -opbp overrides the proxy base path; -oro reads a file of option overrides; -gpu picks devices; -listdevices lists them. Scene files are .rs files holding shaders, geometry, lights, camera, options and AOV setup.
The help pages mix 2.6 and 2025.2 text, so run the binary with no arguments for the real option list.

**Use it:** build farm wrappers from the binary's own output and keep the flag list version-stamped.
