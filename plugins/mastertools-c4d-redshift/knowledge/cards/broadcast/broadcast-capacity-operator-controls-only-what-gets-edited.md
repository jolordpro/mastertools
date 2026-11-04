---
id: broadcast-capacity-operator-controls-only-what-gets-edited
title: Expose only what the operator edits live: text, team code, and checkbox booleans for stat highlights
domain: broadcast
tags: [remote control, operator, visibility modifier, stat highlight, boolean controller, rundown, deep-read]
applies_to: Unreal Engine 5.6 motion design
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=YiMh6bEebIs, src:yt-transcripts]
feeds: []
conflicts: none
---
Anything the operator will edit live gets exposed in remote control [1:11:19]. Text fields are direct binds; if/else conditionals exist; team codes use path behaviors [1:11:51]. Highlighting a stat row uses a duplicated row with a yellow bar and inverted text, linked to the stat text so it is typed once [1:02:56]; a visibility modifier plus boolean checkboxes lets the operator choose which stats show (1st and 3rd, or 1st, 3rd and 5th) [1:04:30-1:05:32]. A mask sliding left or right is what actually moves the highlight [1:03:28]. Controller numbers stay fixed so a show is repeatable [1:23:11]. The rundown holds page templates dragged from levels; pages are previewed first, then taken to air through NDI, a capture card or a monitor output, and a keypad shortcut steps down the list [1:21:39-1:27:57].

**Use it:** Design the control surface as part of the graphic: one typed entry per fact, checkboxes for states, fixed IDs. Same thinking applies to the control panel of a MOGRT.
