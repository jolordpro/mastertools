---
id: ai-models-erlingsson-hud-nodes-label-small-objects-with-boxes-from-a-vision-model
title: "Erlingsson's HUD nodes ask a vision model (Moondream) to find named things per frame and draw boxes, markers, labels or connectors on them"
domain: ai-models
tags: [ingi erlingsson, comfyui, hud, moondream, bounding boxes, overlay, florence, sam 3, licence, polish, ingi-erlingsson, deep-read]
applies_to: ComfyUI
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=4xS4LOn3CTE, src:yt-transcripts, src:polish-roster]
feeds: []
conflicts: none
---
The nodes use Moondream (earlier Florence) to find prompted items, for example window, wood, graffiti, rock, in every frame and produce bounding boxes; SAM 3 can do the same [54:38-56:42]. Overlays: boxes with custom colours per word, X markers, cursors or any image, text labels at the box corner, connector lines between boxes (a mesh look); masks and a MIDI-like timing node are planned for revealing items over time [58:15-59:47].
Tip: ask for smaller objects. Tagging something present everywhere (like 'building') blocks out the whole frame, and he leans on the model getting it wrong occasionally for flicker [55:40-56:42].
They are RAM-hungry and slow on clips of 300+ frames, so unreleased [54:38, 1:00:18]. He avoided an NVIDIA model whose terms were non-commercial; Moondream is open [57:15-58:15].

**Use it:** Before building on a model, check its licence for commercial use. Use detection boxes as a source of tracked graphics layers in a motion piece.
