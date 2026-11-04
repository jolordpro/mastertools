---
id: pipeline-home-two-pc-deadline-farm-checklist-same-paths-same-versions-test-the-cli-render-first
title: A two-PC home farm with Deadline and Nuke needs identical file paths, matching app versions and a command-line test render before Deadline is trusted
domain: pipeline
tags: [deadline, nuke, render node, mini farm, static ip, client certificate, lovevfx, deep-read]
applies_to: Deadline, Nuke, Windows
status: V
confidence: low
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=qhk0TYYV5ks, src:yt-transcripts, https://www.youtube.com/watch?v=QY5odtFbs5M, https://www.youtube.com/watch?v=CMVilcuF5dg]
feeds: [CHECKS, estimator]
conflicts: none
---
Lasse Vemmer (LoveVFX, Windows) built his farm because pre-comps took hours [0:44]. Checklist [1:47-8:29]: link the PCs by direct Ethernet with static IPs in the same range, shared drives with read and write for all users; map a network drive on the helper PC to the project and the Deadline repository; same Nuke and Deadline versions on both; a NukeX or Studio annual subscription includes two render node licenses [4:22]; Deadline is free via an AWS account (a trial account works) [4:22]; install the monitor and worker on both so either can be the node; the Deadline install needs a client certificate with a password, and both machines must point to the same repository, certificate file and password [4:53, 7:00]; script and asset paths must be identical on both PCs [5:24]; test a render node licence with a command-line Nuke render of a script before involving Deadline [6:26]; in Deadline's plugin configuration confirm the Nuke version matches (back up the config file before editing) [7:59]; install the Nuke submitter, then Submit Nuke to Deadline from the Write node [8:29]. He used a chatbot for steps and warns it was not always right [2:17]. Windows only.

**Use it:** A pre-flight list for the C4D farm: identical paths, matching versions, local CLI render passes, then submit.
Transcript support: Deadline Monitor Local Slave Controls and Stop Slave After Current Task Completion for machines that double as workstations. (https://www.youtube.com/watch?v=QY5odtFbs5M [01:05-05:13])
Transcript support: Every worker needs the repository at the same mapped path (Z:); mixed OS means UNC naming (https://www.youtube.com/watch?v=CMVilcuF5dg [09:59-10:31])
