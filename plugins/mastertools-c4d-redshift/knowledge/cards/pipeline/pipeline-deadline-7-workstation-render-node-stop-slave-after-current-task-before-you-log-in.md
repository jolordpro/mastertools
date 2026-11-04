---
id: pipeline-deadline-7-workstation-render-node-stop-slave-after-current-task-before-you-log-in
title: Deadline 7 on shared lab machines: use Local Slave Controls and Stop Slave After Current Task Completion, then log out of the render account, so no frame is cut in half
domain: pipeline
tags: [deadline, deadline monitor, workstation, stop slave, local slave controls, render account, lab, deep-read]
applies_to: Deadline 7 (university art lab, date not stated)
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=QY5odtFbs5M, src:yt-transcripts]
feeds: [pipeline, wrangler]
conflicts: none
---
UF Art + Technology lab walkthrough (channel Jack Stenner; "UF" is not expanded in the video) [00:03-05:18]. Machines are both render slaves and workstations, with a render account and a personal account. If the application icon (Maya) shows at the bottom, the render account is busy and cannot just be logged out, because a half-rendered frame would ruin someone's animation [00:34-01:05]. Steps: open Deadline Monitor, open Local Slave Controls (second button from the right at the top left), pick this machine in the list, right-click, Slave Commands, Stop Slave After Current Task Completion [01:05-02:39]. A window confirms the command. Wait up to one frame time (that job averaged about 7 minutes a frame, here 5 minutes in) until the Maya icon disappears and the slave shows offline with a shutting-down message [02:39-04:43]. Quit the monitor, log out, log into the personal account. If a workstation sits idle more than about 10 minutes it joins the farm again, and suspends the slave when the user comes back [04:43-05:13].

**Use it:** Add to wrangler notes and the home farm checklist: finish-then-stop, not kill. Newer Deadline versions and Cloud may name things differently.
