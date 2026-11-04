---
id: c4d-script-log-records-commands-copy-them-into-script-manager-as-a-macro
title: Cinema 4D Script Log records your actions as Python lines; paste them into a new Script Manager script to make a one-click macro, but some commands do not record
domain: c4d
tags: [script log, script manager, python, macro, reset psr, center axis, brograph, deep-read]
applies_to: Cinema 4D (about R20-S24 era, Python scripting)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=jnpG4oNOkMI, src:yt-transcripts]
feeds: [c4d]
conflicts: none
---
Open Script, Script Log and Script Manager. Make a cube, make editable, edge mode and knife each appear as lines in the log [01:40-02:43]. Copy the lines into a new script, keep the same indentation, and run it [04:17-05:19].
Example: Camera plus Redshift camera tag in one run [03:14-05:19]. Save it into the preferences script folder and give it an icon [05:19].
Gap: commands run from the Shift+C commander (Center Axis) were noted but not parsed, so the speaker typed 0 in position, 0 in rotation and 1 in scale to make the log produce the reset-PSR lines and put the Center Axis line first [07:28-09:34]. Add the line that returns the active object so the script acts on the selection [10:04].
Then it appears in Customize Commands; middle-drag to the dock, bind a key or put it in the V popup menu [10:38, 16:05].

**Use it:** A free way to make repetitive setups (camera plus tag, zero-out) into buttons without learning the API.
