---
id: pipeline-turnover-two-destinations-lab-and-vendor
title: A VFX turnover has two destinations: the pull package goes to the lab that makes plates, the references go straight to the vendor
domain: pipeline
tags: [jack the avid assistant, vfx turnover, pull package, lab, openexr plates, handles, edl, aaf, turnover folder, deep-read]
applies_to: Avid Media Composer (principles apply to any editor)
status: V
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=MoR7ncjN9Ds, src:yt-transcripts]
feeds: [CHECKS]
conflicts: none
---
Jack (The Avid Assistant, working VFX editor/assistant) defines a turnover as the plates, references, metadata and lens data a vendor needs [01:38].
Usually it goes first to the lab or post facility holding the camera backups; they cut the plates from source as OpenEXR sequences, exact shot length plus agreed handles [02:09].
Example: a 50-frame shot with 8-frame handles each side needs 66 frames [03:12].
The pull package for the lab: a QuickTime reference of the plates, an EDL with clip name and frame count only, and a linked-only AAF [39:11, 44:25]. The vendor gets the scene references and the spreadsheet [41:17, 45:27].
Keep each turnover in its own numbered, dated folder (plates, refs, working bins); a show has several, and a shot may be re-turned if the take changes or the shot grows past its handles [05:47].
His golden rule: write a checklist before starting a task [00:33].

**Use it:** A render-to-comp handoff should state what goes to the next person and what goes to the pipeline owner, and each handoff should live in a numbered, dated folder.
