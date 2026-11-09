# 11 — Speed triage (a slow project, not a slow script)

> For "AE is slow", "the preview won't play in real time", "this render takes forever". A slow *script* is
> `04-extendscript-rigor.md` (threading, DOM-read cost). Order matters: **measure, find the one bottleneck, fix
> it, measure again.** Most speed advice online predates Multi-Frame Rendering; the profiler outranks any list.
> **Last verified: October 2026** (feature versions from Adobe's help and release coverage; re-verify per
> `00-platform-facts.md` §0 before quoting a version).

---

## §1 — MEASURE FIRST

- **Composition Profiler (AE 22.0+, Oct 2021).** Click the snail icon at the bottom left of the Timeline, or
  right-click the column headings ▸ Render Time. It shows how long each layer, mask, layer style, expression and
  effect took for the **current frame**. Adobe's help says leaving the column on does not slow AE.
- Read 3-4 frames (a busy one, a quiet one, a transition), not one. A precomp layer's time includes everything
  inside it: open the precomp to see which part.
- Write the number down. Every fix below is judged against it; a fix that does not move it is reverted.

## §2 — USE THE MACHINE YOU HAVE

- **Multi-Frame Rendering (AE 22.0+).** Settings ▸ Memory & Performance ▸ Enable Multi-Frame Rendering: check it
  is on. Effects without MFR support show a **yellow warning icon** in Effect Controls; frames that use them gain
  little. Replace those effects or pre-render the layers that carry them (§5).
- **Speculative Preview (AE 22.0+).** AE caches frames while idle (default after 8 s). Settings ▸ Previews ▸
  Cache Frames When Idle.
- **Storage.** AE is only as fast as its slowest part. Media and disk cache on a fast local SSD is the best single
  upgrade; in studios, network storage often limits more than the CPU (Zwar, Part 4).

## §3 — PROCESS FEWER PIXELS

- **Preview resolution matched to zoom.** At 50% zoom, Half resolution renders a quarter of the pixels and looks
  the same. Auto does this for you.
- **Region of Interest** while working on one area.
- **Pre-render what never changes** (a finished background, a heavy subtree) and swap the plate in (§5).

## §4 — DO FEWER CALCULATIONS

- **Bit depth.** Work at 8 or 16 bpc unless the final needs 32 bpc (float); 32 bpc costs memory and time in every
  effect.
- **Display colour management off while animating** (View ▸ Use Display Color Management); back on for colour
  decisions.
- **One adjustment layer** instead of the same effect repeated on many layers.
- **Expressions** show their own time in the profiler. Bake the costly ones once the rig is final (`08-expressions.md`
  §4 has the cost model and the baking route).
- **Heavy camera footage** (log, RAW, long-GOP) decodes slowly: transcode or pre-render it to an intermediate.

## §5 — PRE-RENDER FORMATS (measured; read before choosing)

These are this skill's own test results. Cite them as tested findings ("in testing on AE 26.5"), never as
something you measured in this conversation.

- **Not ProRes for plates you re-import into AE.** Measured on AE 26.5 (Sep 2026): a ProRes 4444 / 422 HQ render of
  a dark patch (mean level about 8.8) came back at about 3.5 when re-imported into AE, shadows crushed, brights
  unchanged. macOS decoders read the same file correctly, so it is AE's ProRes *import*, not the encode. ProRes
  deliverables are fine. Footage colour interpretation is not exposed to scripting, so a script cannot correct it.
  One machine, one AE version: when a plate matters, re-import a short test and compare shadow levels before
  committing a whole render.
- **An 8-bit PNG sequence round-tripped bit-exact** in the same test. Zwar (2020) prefers TIFF to PNG sequences
  because PNG is slow to write; EXR for 32 bpc. Pick by need: PNG or TIFF for 8/16-bit plates, EXR for float.
  Size check: uncompressed 16-bit RGB at 3840x2160 is about 50 MB a frame, about 1.2 GB/s at 24 fps. Make sure the
  drive can play that back, or use 8-bit when the plate does not need more.
- **Re-rendering a plate to the same path** keeps AE's cached metadata (an old frame count, for one). Remove the
  footage item first, or render to a new file name.

## §6 — OPTIONAL: A READ-ONLY SPEED AUDIT

A script can flag the usual suspects across a project without opening every comp: comps at 32 bpc, PNG-sequence
footage, expression counts per comp, the same effect stacked on many layers of one comp, footage much larger than
the comp it sits in. Build it to `04-extendscript-rigor.md` (progress, structured result object, no mutation).
It reports **suspects with counts**; the profiler confirms which ones cost time.

---

**Sources:** Adobe help, "Preview and render with Multi-Frame Rendering" and "Composition Profiler"; CG Channel,
"Adobe ships After Effects 22.0" (Oct 27, 2021); Chris Zwar, "After Effects & Performance" Parts 4 (2019) and
14 (2020), ProVideo Coalition. §5 results are this skill's own measurements.
