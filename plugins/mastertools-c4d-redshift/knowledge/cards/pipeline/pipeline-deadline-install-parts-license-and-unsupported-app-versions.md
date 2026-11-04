---
id: pipeline-deadline-install-parts-license-and-unsupported-app-versions
title: Deadline's parts: repository, MongoDB database, worker and monitor; free for two machines; a new app version can be added by editing plugin lines
domain: pipeline
tags: [deadline, repository, mongodb, worker, monitor, license, houdini 18, plugin config, tim van helsdingen, deep-read]
applies_to: Deadline 10 (2020 video)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=v083eMXSwXw, src:yt-transcripts, https://www.youtube.com/watch?v=CMVilcuF5dg]
feeds: []
conflicts: none
---
The repository holds config and submitted scene files; a MongoDB database stores settings; every render machine runs a worker; the monitor shows jobs [03:30-13:45]. Free licence covers two machines, then he believes around $48 per machine per year (2020, unverified) [02:47-03:20]. Certificates gave a permissions error and he reinstalled without one [09:11-11:25]. Super-user mode unlocks plugin configuration [13:45-14:16]. For a Houdini version not yet supported, add a line copying the previous version's executable entry in the plugin's param file, then fix the python path and environment file [28:34-32:32]. Dependencies chain a render after a sim [01:44].

**Use it:** Setup reference only; prices and versions will have changed. See pipeline-deadline-cloud-farm-queue-fleet-model for the modern route.
Transcript support: Second source: free for two slaves, $48 per year per slave (Clements, about 2019); repository drive must be the same path on every machine; plugin .pyp goes into C4D's plugins folder (https://www.youtube.com/watch?v=CMVilcuF5dg [06:54-11:05])
