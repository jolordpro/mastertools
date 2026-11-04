---
id: motion-unreal-text3d-per-letter-animation-controls
title: Unreal's Text 3D plus its character-transform component animates text per letter with one slider and no Blueprints
domain: motion
tags: [unreal, text 3d, kerning, per-letter animation, scale range, patrick-wongbo, deep-read]
applies_to: Unreal Engine 4.25
status: V
confidence: low
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=WLdmYnkFoK4, src:yt-transcripts]
feeds: [[]]
conflicts: none
---
Add the Text 3D actor, then add the character-transform component to get per-letter controls [1:33:31-1:39:10]. Scale begin and end are one progress slider that is keyframable in Sequencer. Scale range decides whether letters animate together or one after another. Kerning, line spacing, word spacing, pivot alignment (first line, top, centre, bottom) and max width/height squish are all exposed, and the front, bevel, back and extrude materials can be set per letter [1:39:41-1:40:43]. Changing values does not force a recompile. A transparent outline text only roughly works because the faces are single-sided [1:41:15].

**Use it:** Tell broadcast artists that title builds that took Blueprint work before 4.25 are now slider work.
