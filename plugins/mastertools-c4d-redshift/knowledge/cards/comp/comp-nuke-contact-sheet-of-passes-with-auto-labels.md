---
id: comp-nuke-contact-sheet-of-passes-with-auto-labels
title: Make a review contact sheet of every pass: split layers, auto text label from the layer name, contact sheet, reformat
domain: comp
tags: [nuke, contact sheet, aovs, review, layer name, tcl, reformat, deep-read]
applies_to: Nuke, Redshift/Arnold/Octane passes
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=UCUXhXKDnWQ, src:yt-transcripts]
feeds: []
conflicts: none
---
Tony Lyons (CompositingMentor). Steps [19:25-29:52]: (1) split channels into one shuffle per layer (a script exists for this); (2) add one Text node whose message is the TCL expression that reads the input node's 'in' knob, so it prints the layer name; (3) copy that text node and paste-to-selected onto all shuffles; (4) use a ContactSheetAuto node, select it first and then the texts left to right, press Y to connect inputs in selection order; (5) reformat to about HD to send to a supervisor. Note: a plain layer contact sheet is a UI view and does not render, which is why this is built from real nodes [19:25-19:57]. Channel clean-up for the demo used a remove-many-channels tool.

**Use it:** The equivalent for AE: an automated pass-label sheet is a standard deliverable for supervisors.
