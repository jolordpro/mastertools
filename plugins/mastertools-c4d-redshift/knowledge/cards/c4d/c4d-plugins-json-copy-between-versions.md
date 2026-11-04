---
id: c4d-plugins-json-copy-between-versions
title: Plugins survive a C4D version or machine change if plugins.json is copied from the old preferences folder to the new one
domain: c4d
tags: [plugins, plugins.json, preferences folder, upgrade, new machine, cinema 4d 2027]
applies_to: C4D 2027.0
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=PCtsdWnYhx8, src:yt-transcripts]
feeds: []
conflicts: none
---
Rocket Lasso [00:36]: 2027 did not break plugins, but moving versions or machines drops the plugin links and the Plugins preference page is empty.
Method [01:06]: in the old version open Edit > Preferences > Plugins > Open Preferences Folder, copy plugins.json, open the new version's preferences folder, paste, reopen preferences. All plugins then load and show in Extensions.

**Use it:** put 'copy plugins.json' in the upgrade and new-render-node checklist instead of re-adding plugins by hand.
