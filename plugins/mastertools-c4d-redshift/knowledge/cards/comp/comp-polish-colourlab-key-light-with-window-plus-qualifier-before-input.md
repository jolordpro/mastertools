---
id: comp-polish-colourlab-key-light-with-window-plus-qualifier-before-input
title: To match a reference's lighting, add a soft key on the face with a window plus qualifier combined in one node, ignoring the bright background
domain: comp
tags: [colourlab-ai, relighting, window, qualifier, grading, deep-read, polish]
applies_to: DaVinci Resolve
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=KE085zdpi_I, src:yt-transcripts, src:polish-roster]
feeds: [elevate]
conflicts: none
---
He placed a node before the input transform (against his own usual rule, as a temporary look-matching exception) to add key light to the face only; a window combined with a qualifier on the same node gives separation without AI isolation, so the window highlight behind does not lift [13:44-15:17]. He labels nodes (IDT, AI, look designer) and sets output blanking to legal range so reference and result compare in the same format [03:17-06:55]. Reference stills must be tagged with their true source space or the match is wrong [09:33-10:38].
**Use it:** Relight faces with window + qualifier; compare reference and result in one colour/range format; label which node is a temporary exception.
