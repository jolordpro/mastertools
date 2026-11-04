---
id: pipeline-dailies-matte-the-delivery-aspect-with-output-blanking-and-do-not-reframe-or-grade-unless-asked
title: Resolve dailies: add the delivery aspect as a black matte with Output Blanking, leave framing alone, and add a look only if the project calls for it
domain: pipeline
tags: [dailies, output blanking, 2.39, framing, lut, colour, editor, we are film, resolve, deep-read]
applies_to: DaVinci Resolve 18 (2023)
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=rgZjL2e8yEg, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
For a film finishing at 2.39:1, Timeline > Output Blanking adds the bars so director and editor see proper framing in the dailies [06:52-07:47].
Do not reposition clips at first. The editor can ask for a shot to be moved, as an Avid team did after hard-matting a series [08:18].
He applied a project LUT and changed RAW settings only because it was his own film; a real colourist would normally own the look, so most workflows would not do this [08:50-10:22].
Downside: if the edit later punches in or does a digital zoom on these clips, finishing needs the originals back, via XML or reference media [16:34-17:38]. Reason for the whole recipe: separate editing from finishing, since different companies often do each [16:03-16:34].

**Use it:** state the delivery frame in the dailies, keep reframing and grade decisions for the department that owns them.
