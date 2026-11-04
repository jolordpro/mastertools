---
id: ai-models-prism-comfyui-previews-the-lighting-of-a-new-shot-from-its-playblast-and-neighbour-shots
title: Prism + ComfyUI prototype: a farm job styles a layout playblast with lighting and materials from already lit shots, as a preview, not a render
domain: ai-models
tags: [ai-models, prism, comfyui, playblast, previs, lighting preview, deadline, deep-read]
applies_to: Prism execution graph with ComfyUI (2026 prototype)
status: V
confidence: medium
decay: fast
read: 2026-10-31
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=jfH7JpjDO_w, src:yt-transcripts]
feeds: []
conflicts: none
---
Richard (Prism). ComfyUI is treated like any DCC: a Prism menu, project browser, versioned saves, import of Maya playblast videos, EXR with colour conversion, even 3D assets (basic materials, unwrap, remesh), and a Prism export node to bring generations back [48:05-49:39]. The ComfyUI graph is triggered from the execution graph so inputs change and it re-runs [49:39-50:10]. Demo: when a playblast of a new layout/animation shot is made, Deadline runs a ComfyUI graph that takes a video plus reference images from lit shots and returns a clip carrying their lighting and materials in about a minute; "not perfect" but a good impression, swapped into the edit in RV for sequence feel [50:10-51:12]. In Q&A: consistency across long shots is not solved; the playblast carries camera, character and motion, and rendered passes can guide better [1:02:45-1:04:48].

**Use it:** Use AI as a look-development hint on playblasts only; final lighting remains rendered.
