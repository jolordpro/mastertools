---
id: ai-models-mickmumpitz-vfx-inputs-mask-driving-video-refs-prompt
title: Local AI VFX needs four inputs (black-and-white mask, driving video, reference images, detailed prompt); the ControlNet you pick sets how much the model may change
domain: ai-models
tags: [mickmumpitz, comfyui, wan vace, controlnet, canny, depth, pose, mask, driving video, vfx, deep-read]
applies_to: ComfyUI, Wan-based VACE merge (2026)
status: V
confidence: low
decay: fast
read: 2026-10-30
recheck_by: 2027-01-30
sources: [https://www.youtube.com/watch?v=_n0ir5V5tX4, src:yt-transcripts]
feeds: [[coach]]
conflicts: none
---
Mickmumpitz (single creator, low). Inputs [03:39-04:09]: mask (white is the area the model may change), a driving video (plate combined with a ControlNet), 1-4 reference images (one image is treated as the start frame), and a prompt. ControlNet choice [02:06-03:08]: Canny keeps edges and detail exactly; depth (white near, black far, like a Z-depth or mist pass) gives the model more freedom to invent detail; pose carries human motion and a back-view reference keeps a creature consistent when it turns; camera-track points let the model recreate the camera move; leaving the replacement area blank turns it into a clean-plate or object-removal tool [03:08]. Mask choice matters: a cutout mask kept the subject but gave weak interaction at the feet; a full white mask gave much better integration (shadow, reflection, relit subject) but changed the subject's appearance, so exclude body and face from the mask and blur the feet edge [11:58-12:29, 14:33-15:05]. Prepare the plate in After Effects, Nuke or Fusion, or use his preprocess workflow, which outputs first frame, mask, depth, Canny, pose, track points and a keyed subject in one run [05:13-05:43].

**Use it:** Describes a controlled AI pass for background or FX replacement; relevant only as a look-test aid next to C4D renders, never a final.
