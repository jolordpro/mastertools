---
id: broadcast-xpression-2018-auto-squeeze-and-separate-font-objects-for-headline-and-subline
title: XPression (2018): auto squeeze fits any name length inside a box; headline and subline need separate font objects or one edit changes both
domain: broadcast
tags: [ross xpression, auto squeeze, text, font object, lower third, long names, scene font, text overflow, deep-read]
applies_to: Ross XPression (2018)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=VZO7A0F7pZ0, src:yt-transcripts]
feeds: []
conflicts: none
---
Text runs off the lower third when a long name is typed. Enable auto squeeze on the text with its width set to the current box width, so letters are condensed to fit however many are typed [29:31-32:13]. Do it for headline and subline.
Gotcha: two text objects that use the same scene font change together. Make a new font object (for example a version 2) for a different headline and subline style [25:47-27:57].
Transfers: any template with typed names needs an overflow rule tested with the longest real name.

**Use it:** Test every name field with a very long string; set squeeze or clamp rules before handing a template over.
