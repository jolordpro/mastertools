# Model routing, local tools and safe compaction

Loaded at session start by {{plugin}}. Use the family aliases (`opus`, `sonnet`), never pinned model IDs. If the machine has `~/.claude/model-routing/PLAN.md`, it holds the data and decision rules behind this page.

## Main thread
- {{main_model}} Never switch the main thread's model: each model has its own cache, so a switch re-reads the whole conversation at full price. Effort changes keep the cache.
- {{effort_line}}
- Work in cycles: brainstorm → plan → challenger → approve → execute + gate check → repeat. The challenger pass also decides which chunks go to helpers.

## Helpers
Pick a helper by the kind of work. The {{plugin}} agents pin model and effort for you.

| Work | Helper |
|---|---|
| Visual, creative or judgment-heavy builds: UI, layout, images, motion, C4D / AE / Photoshop work, and code that needs design judgment | `{{plugin}}:opus-builder` (Opus, medium) |
| Research legwork (search, fetch, read, extract with sources) and lower-stakes bulk work (mechanical edits, renames, boilerplate, sweeps, data extraction, test scaffolding) | `{{plugin}}:sonnet-worker` (Sonnet, medium) |
| Gate checks on risky work: auth, security, data, money, migrations, architecture | `{{plugin}}:opus-reviewer` (Opus, high) |

- **Research rounds:** the Opus main thread writes the questions and the source bar, Sonnet workers gather (a URL for every claim), and Opus checks every claim that decides something before relying on it. Sonnet is weaker at factual recall, so an unsourced Sonnet finding doesn't count.
- **Planning, judging and synthesis stay in the main thread.**{{+plan_agent}}
- **Built-in helpers:** Explore runs on the main model (Opus). For big searches, use `sonnet-worker` instead. Any other helper without a {{plugin}} agent: pass `model` and `effort` on the call (Opus, medium unless it's clearly research or mechanical work).
- **Delegate only when it pays.** Helpers start cold and re-read everything. One small or tightly coupled step is cheaper in the main thread. Review a helper from its handoff: dig into "Unsure" and "Deviations" and re-run its claimed checks.
- **Parallel work:** run it in parallel when that speeds things up without lowering quality or overloading the machine or server.
- **Execution:** keep going until the approved steps are done. Don't end a turn on a progress report while plan steps remain, unless blocked or the decision is {{name's}}.

{{#mac}}
## Free local tools first
Prefer free tools on this machine when the quality gap is small. They cost nothing and keep bulky media out of the context window. Check a tool exists (`command -v <tool>`) and spot-check a sample before running a whole batch.

| Job | Local tool, and when to use Claude instead |
|---|---|
| Transcribe audio or video | `whisper-cli` (whisper.cpp) with a large-v3-turbo model (`mdfind -name ggml-large-v3-turbo.bin`), plus `ffmpeg` for the audio. Use Claude only to clean up or summarize the transcript |
| OCR printed text | Apple Vision (a short Swift script or the Shortcuts "Extract Text from Image" action), or `tesseract`. Use Claude's vision for handwriting, tables, dense layouts, or when the sample check fails |
| PDF and document text | `pdftotext`, `textutil`. Use Claude for scanned PDFs or when the layout matters |
| Images and video: resize, convert, metadata, frames, contact sheets, measuring | `sips`, `ffmpeg`, `ffprobe`, `exiftool` |
| Speech previews | `say` |

- If a needed tool is missing, install it and say so. Don't fall back to a paid path for bulk work without saying so.
- Don't use a local tool where the quality gap is real (judgment, writing, design, code review).

{{/mac}}
## Safe compaction
Compaction can happen at any turn boundary, so every point in the work has to be resumable.
- **Checkpoint:** keep a `## Now` section at the top of the project's `PROGRESS.md`. It holds the current step; which program, file, scene or comp is open and whether it's saved; the last step applied and how it was verified; the exact next action; anything that must not be redone; and a line `Safe to compact: yes` or `Safe to compact: no`.
- **Multi-step operations in a live program** (C4D, AE, Photoshop, long builds or test runs): before starting, write the checkpoint with `Safe to compact: no`. After each verified step, save the program's file and update the checkpoint. When the operation is finished and saved, set `Safe to compact: yes`.
- While it says `no`, {{plugin}} postpones automatic compaction (for up to 2 hours, and never past a hard size cap). Don't leave it at `no` once the step is done.
- **When a "compaction is close" notice appears:** finish the current atomic step, save, update the checkpoint and set it to `yes`. Don't start a new multi-step operation until compaction has run.
- **After compaction:** {{plugin}} puts the checkpoint back into context. Resume from its next action, and re-check the live state (read the scene, comp or file) before changing anything.
- **Between cycles:** once a gate check passes, update `PROGRESS.md` and suggest {{name}} run `/compact`. It's the cheapest point to summarize.
