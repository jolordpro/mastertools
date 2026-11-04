---
id: pipeline-reprise-rlm-v15-install-non-admin-user-own-folder
title: Reprise License Manager v15 install (Windows): non-admin user, own folder outside Program Files, service run as that user
domain: pipeline
tags: [rlm, reprise license manager, floating license, analytica, windows service, lumina, license server, v15, deep-read]
applies_to: RLM 15, Windows 11, Dec 2022
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=KUkjI7xprPM, src:yt-transcripts]
feeds: []
conflicts: none
---
IT-side job; not needed for single-user licences [00:04]. Steps and the reason for each (video follows Analytica's wiki) [01:07-08:26]: create a non-admin user (v15 will not run as a service account). Make a folder on C: (not Program Files or ProgramData), full control for all users, with a licenses subfolder. Download the Windows 64-bit installer (unsigned, click through warnings) and install there. Put the ISV's .set file in the folder. In an admin command line: write an admin password entry file, then install the service with log, licence directory and no-password flag. Then set the service's logon account to the new user and start it. Check the admin panel shows activate and diagnostics and that the working directory is not System32. Without -z, change the admin password at once.

**Use it:** for a studio licence server, record these three traps: wrong account type, wrong install location, working directory.
