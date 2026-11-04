---
id: comp-composure-lit-plate-needs-unpremult-edge-extended-sequence
title: For a lit Composure plate, write the edge-extended unpremultiplied sequence; the premultiplied EXR is for the unlit material
domain: comp
tags: [[unreal, composure, edge-extend, premultiplied, exr, fusion, keying], deep-read]
applies_to: Unreal Engine 5.7, DaVinci Fusion
status: V
confidence: low
decay: medium
read: 2026-10-31
recheck_by: 2027-10-30
sources: [https://www.youtube.com/watch?v=zlZCKT-5pLU, src:yt-transcripts]
feeds: [coach, CHECKS]
conflicts: none
---
Premultiplied keys (over black) can be written as DWAA EXR sequences and used with Composure's unlit alpha material [10:54]. The lit mask material needs the unpremultiplied, edge-extended version instead, so dark fringe is replaced by plate colour at the edge [10:54-13:04].
Fusion recipe [07:54-10:51]: a second clean plate node fed through a blur and curves (boost alpha only) to grow the edge sampling, grow-edges to push colour out, a channel boolean laying that colour under the original alpha (output alpha = background alpha), mix back the strength to avoid a dark edge, and clip the matte high end if background bleeds. Then a Saver with a name ending in a period so the frame number follows; deactivate other savers before Render All [11:29-12:01].

**Use it:** When a keyed plate is placed in a 3D engine and relit, deliver edge-extended unpremult colour with a separate alpha, never premult over black.
