---
id: pipeline-dailies-resolve-timeline-per-card-real-clip-names-and-burn-in-fields-for-vfx-and-sound
title: Resolve dailies recipe: one timeline per camera card, real clip names without the extension, and a burn-in carrying timecode, clip, card and project
domain: pipeline
tags: [dailies, resolve, burn-in, source timecode, clip name, card name, proxies, vfx editor, we are film, cameron gallagher, deep-read]
applies_to: DaVinci Resolve 18 (2023), RED R3D shoot
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-31
sources: [https://www.youtube.com/watch?v=rgZjL2e8yEg, src:yt-transcripts]
feeds: [CHECKS, coach]
conflicts: none
---
Cameron Gallagher (We Are Film) suggests dailies instead of ordinary proxies because a project full of originals bogs down, other teams on Avid cannot use Resolve proxies, and sound or VFX editors need the information [00:32-01:34].
Order: bins by shoot day then camera card; one timeline per card named after the card; project setting "use real names from source clip file name" so downstream apps see the name without .r3d [02:10-06:46]. Data burn-in: source timecode and frame number, source clip name, real name, a custom line with day and card, and a line with the production or "proxy" label; plain font, no background [10:03-14:31].
Reason: someone relinking in finishing, or finding a VFX plate, can trace the original at once [11:25-12:59].
Deliver as individual clips, ProRes 422 Proxy from Resolve, or DNxHD 1080p 36 8-bit for Avid after asking the editor; use 720p for very large projects; source name as file name; no audio unless synced [14:31-16:03].

**Use it:** turnover checklist: burn-in carries clip name, source timecode and card. See pipeline-dailies-deliverables-avid-proxy-and-pix-review-specs.
