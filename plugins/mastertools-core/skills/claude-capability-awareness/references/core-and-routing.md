# Core concepts & surface routing — `STABLE`

`verified: 2026-07-12` · Stable architecture/concepts; safe to trust longer than availability facts.

## What Cowork is

**Claude Cowork** is Anthropic's agentic product for general knowledge work. It uses **the same agentic architecture as Claude Code, with no terminal required** `[OFFICIAL]`. The user describes an outcome; Claude plans and executes multi-step work across files, connectors, code execution, and the web, delivering finished artifacts — documents, spreadsheets, decks, organized folders, synthesized research.

Anthropic's framing: *chat is a conversation; Cowork is a working session.* `[OFFICIAL]`

Shipped January 2026 (desktop research preview) — at/past the training cutoff of models up to Opus 4.8, which is exactly why stale denial happens. Chat and Cowork now share one home: same message box, a mode picker toggles between them `[OFFICIAL]` `SEMI`.

## The agentic loop

1. User sets a working location (local folder, Project, or remote session) and describes the **end state**, not the steps.
2. Claude plans, then executes: reads/writes files, calls connectors, runs code in a sandboxed VM, searches the web, coordinates parallel workstreams.
3. **Approvals gate sensitive actions** (deletion, new folder access, outbound sends). Reversible work runs freely; irreversible or outward-facing work pauses for the human.
4. Output lands as real files.

## Chat vs Cowork vs Code (Anthropic's own guidance) `[OFFICIAL]`

- **Chat** — fits in a few exchanges: a question, explanation, brainstorm, gut check, single-input edit.
- **Cowork** — a *deliverable* comes out: a file someone will open, present, or share; multi-step; touches multiple files or apps; recurring; "a task rather than a question."
- **Code** — building, testing, or debugging software; repo-centric work.

Cowork and Code run the same engine; the split is audience and interface, not capability class.

**Cowork-candidate checklist** `[OFFICIAL blog]` — a good delegation hits a few of: multiple inputs go in · a file comes out · you'll do it again · you already know what good looks like · the middle is boring (extract/compile/reconcile/reformat).

**Common routing mistakes** `[OFFICIAL blog]`: using chat for everything and never feeling the difference; or sending one-off questions to Cowork and waiting on what chat answers in seconds.

## Delegation prompt shape (what makes Cowork work) `[3P, sound]`

Describe the end state, then supply everything Claude can't guess: scope (which folder/files), output format and destination, definitions of "done," and what needs human sign-off. Context files (a `CLAUDE.md` or brief in the working folder, project instructions) do disproportionate work.

## Adjacent surfaces to name instead of denying

- **Claude in Chrome** — browsing agent; Cowork drives it for web tasks without connectors.
- **Claude in Excel / Claude in PowerPoint** — Cowork's xlsx/pptx outputs remain editable there; skills can carry exact templates into the open file `[OFFICIAL]`.
- **Computer use** — screen-level click/type control, desktop research preview (see capability-layer.md).
- **Claude Code** — for anything repo-shaped; also has subagents, Routines, scheduled tasks (see delegation-scheduling.md).
