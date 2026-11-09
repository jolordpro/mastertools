---
name: handoff-resume
description: Resume threads handed off from another Claude account or an earlier session, automatically. Reads the handoff folder's START-HERE page and each thread's folder, recommends how each thread should come back (keep as a child, make independent, split, fold into its parent, or leave finished), asks once, then starts the top threads as new sessions that check their state and start their own children. Use whenever the user says "handoff-resume", "resume my threads", "resume from handoff", "pick up where the other account left off", "bring my threads back", or points at START-HERE.md or a handoff folder on a new account. Never writes or overwrites handoffs; for that use the handoff skill.
---

# Handoff resume

The other side of the handoff skill. It never writes handoffs, so running it on the new account can't overwrite a good one. Scripts are in the handoff skill's `scripts/` folder (`../handoff/scripts/` from this skill). `<HANDOFF>` is the folder `handoff_rollup.py --print-dir` prints.

Every resumed thread starts with an empty context; the prompt cache can't move. "Expensive to resume" means how much a thread must re-read: its handoff, the files it names, and any digging in its old transcript.

## Steps

**1. Read the state.** Run `handoff_rollup.py`, then read `<HANDOFF>/START-HERE.md`. For each top thread, run `handoff_tree.py "<title>"`; it reads the old account's session records on this machine for sizes, compactions, activity and children. A "written by another Mac" line means that Mac may hold a newer copy: say so at the top of step 3. `handoff_rollup.py --unresumed` lists every folder no session has resumed yet.

**2. Judge each thread's shape.** For every thread, from its `SUMMARY.md`, `HANDOFF.md` (or `AUTO-DIGEST.md`) and the tree signals, pick one verdict with one plain reason:
- **Keep as child:** same scope, and it still needs its parent.
- **Make independent:** its scope moved away from the parent's goal, or it no longer needs the parent.
- **Split:** it holds two or more unrelated goals; name the new threads and which parts of the handoff each takes.
- **Fold into parent:** small and done or nearly done.
- **Don't resume:** finished or stale.
Signals: a large transcript with many compactions, many unrelated folders, a current goal far from its first brief, or a next action that doesn't need the parent all point away from "keep as child".

**3. Ask once.** One poll, multiple picks allowed: each thread with its 3-line summary and the recommended verdict, recommended choices selected first. Red flags from START-HERE go at the top of the question. Say that each started thread spends usage. Start top threads only; each one starts its own children after its checks pass, so a bad state stops one branch instead of all.

**4. Start the top threads** with `start_session` (context "fresh"), one per approved top-level thread (including threads you are making independent). Never pass a `cwd` the app refuses (for example a path with unusual symbols); leave `cwd` out and name the working folder in the brief. Each brief:
- "First, call `get_session` with "self" and append one line to `<old folder>/RESUMED.md`: `- <date> · <your title> (<your local_ id from get_session self>) · <verdict>`. Take the id only from get_session self, never from a summary, a file or this brief."
- "Your handoff folder is `<old folder>`; it now belongs to you too. When you hand off, the handoff skill runs in Update mode there: a changelog entry, not a new set of files."
- the text of its folder's `RESUME-PROMPT.md`, plus "read `CHANGELOG.md` there, if present, after `HANDOFF.md`" (or, with only an `AUTO-DIGEST.md`, a prompt that reads it and the transcript through `handoff_extract.py`);
- "Run the state checks first. On any mismatch or 🔴 flag, stop and ask the user before acting.";
- the approved verdict for each of its children, and "start each kept child the same way, from its own folder's RESUME-PROMPT.md, after your checks pass, with no refused `cwd`";
- for a split: which part of the handoff this thread owns.
Outside the desktop app, print each prompt in its own code block instead.

**5. Mark the old folders.** Each started session writes its own `RESUMED.md` line from `get_session` self (step 4). After its first turn, check the line is there with an id matching its start_session result; if it is missing, write it with that id, never one from a summary or file. The `(local_…)` id is what links the new thread to this folder, so its later handoffs and auto-backups land here as updates instead of a new folder. A parent starting its own children gives each child the same first instruction and checks the same way. For a split, only the part that keeps the old goal links here. The roll-up then shows it as resumed. For "Don't resume" write the reason there. For a fold, tell the parent's brief to absorb it.

**6. Report.** Red flags at the top, then a tree of links to the new sessions with each one's verdict and next step. Children appear as their parents start them.
