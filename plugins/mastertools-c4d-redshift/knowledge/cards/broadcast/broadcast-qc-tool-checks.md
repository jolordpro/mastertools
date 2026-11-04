---
id: broadcast-qc-tool-checks
title: Automated QC tools check loudness, RGB gamut, black and flash frames, freeze frames, luma/chroma limits; none checks against the approved look or the scene that made the frame
domain: broadcast
tags: [telestream vidchecker, qualify, interra baton, venera pulsar, colorfront, automated qc]
applies_to: 2025-2026
status: V2
confidence: medium
decay: medium
read: 2026-10-30
recheck_by: 2027-10-30
sources: [https://www.telestream.com/wp-content/uploads/2025/09/Telestream_Qualify-for-Vantage_Product_Sheet_Sept-2025.pdf, https://interrasystems.com/file-based-qc.php, https://colorfront.com/software/on-set-dailies, src:research-vfx-pipelines]
feeds: [delivery QC]
conflicts: none
---
Vidchecker/Qualify also check dead pixels, bars, containers, captions, duration and bitrate. BATON is AI/ML content-aware (HDR, blockiness, DPP, IMF). Colorfront dailies flag black borders, black and repeated frames, clipped highlights.

**Use it:** the platform's gap is look-aware, scene-aware and small-type checks.
