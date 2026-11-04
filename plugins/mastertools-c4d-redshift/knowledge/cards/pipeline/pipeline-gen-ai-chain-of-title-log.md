---
id: pipeline-gen-ai-chain-of-title-log
title: Log every AI input (images, prompts, models, LoRAs, settings) per output as a chain-of-title CSV, and silo models per show
domain: pipeline
tags: [[chain-of-title, gen-ai, audit, lora, stellar-creative-lab, slingshot], deep-read]
applies_to: any
status: V
confidence: medium
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=bWvxBu_vVes, src:yt-transcripts]
feeds: [coach, CHECKS]
conflicts: none
---
Stellar's Slingshot app (Maya, Blender, Unreal plugins plus a web UI) exports each generation's inputs to CSV: input images and videos, prompts, models, LoRAs and dial settings [1:37:00][1:42:14]. Models and LoRAs allowed differ by show, so data and permissions are siloed [1:37:31].
Inputs, LoRAs, prompts and reference designs are called "the new assets". Not tracked: where an image was later used in comp; they match it by hand to ShotGrid-style tools [1:50:05]. Blockchain stamping was considered, not used.
Outputs are 80-90% and then retouched in Photoshop [1:54:50]. Inference runs on RTX 6000 machines in their own farm with cloud burst, so artist workstations are not the bottleneck [1:48:31].

**Use it:** A render-platform job sheet can carry the same fields for any AI-touched element.
