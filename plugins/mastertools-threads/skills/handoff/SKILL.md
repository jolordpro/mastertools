---
name: handoff
description: Make Claude Code threads resumable from files alone, so the work can continue on another Claude account, in a fresh session, or after a long break. Writes one folder per thread (named by thread title, child threads nested inside their parent's folder) with a handoff, a short summary and a resume prompt; checks for live work the switch could lose (renders or servers started from a session, busy terminals, unsaved documents, uncommitted git work); asks once before waking child threads so they hand off too; and rolls everything up into one START-HERE page with red flags first. Use whenever the user says "handoff", "hand off", "/handoff", "I'm switching accounts", "moving to another Claude account", "back up my threads", "make this resumable", "write a pickup file", "roll up the handoffs", or asks how to carry context, compacted context or cached tokens to another account. To resume on the new account, use the handoff-resume skill instead. Not for summarizing a thread for a person to read, and not for moving a session to the cloud.
---

# Handoff

A new account can't see this conversation, its prompt cache, or anything the old account owns: artifacts, scheduled tasks, cloud routines, the desktop session list. On the same machine it can read every file on disk: each thread's raw transcript (`~/.claude/projects/<folder>/<transcript id>.jsonl`, compaction summaries included) and the desktop app's session records of every account. So a handoff is a folder of files that point into what's on disk.

The prompt cache cannot move. It lives on the provider's servers, belongs to one account and expires within an hour. Every resumed thread starts with an empty context; say so if asked.

Between handoffs, write decisions, plans, tests and reasoning into the repo or project docs as the work happens, so a new session or another AI can pick up from files alone.

## Pick the mode

| The user says | Mode |
|---|---|
| handoff, switching accounts, back up this thread | **Write**, or **Update** when the folder already holds a handoff (then cascades to child threads after asking) |
| switching back, done on this account, update the handoff | **Update** |
| handoff here only | **Write**, no cascade |
| a message from a parent thread asking for a handoff | **Write as a child** (see step 8) |
| roll up, refresh START-HERE, what's left across threads | **Roll-up** |
| merge duplicate folders | **Setup** (merge) |
| turn on auto-backup, fence a project, usage alert | **Setup** |
| resume, pick up, points at START-HERE or a handoff folder | use the **handoff-resume** skill |

Scripts live in this skill's `scripts/` folder. Run each with `python3 -I`. `<HANDOFF>` below means the folder printed by `handoff_rollup.py --print-dir` (`$HANDOFF_DIR`, else the path in `~/.config/handoff/dir`, else `~/.claude/handoffs`).

## What a thread's folder holds

`<HANDOFF>/<Thread title>/`, with a child's folder inside its parent's. A hidden `.thread-id` file holds the transcript id; scripts find folders by that id, so a renamed thread keeps its folder. A thread resumed on another account shares the old folder: its id is added on the next line of `.thread-id`, found through the `(local_…)` id that handoff-resume writes into the old folder's `RESUMED.md`. One project keeps one folder, whichever account works on it.

| File | Made by | What it is |
|---|---|---|
| `HANDOFF.md` | Write mode | The full handoff. Transfer check at the top |
| `SUMMARY.md` | Write mode | 5 lines: stopped, next, waiting on the user, red flags, folder. Parents read this, because only about 400 characters of a child's report reach them |
| `RESUME-PROMPT.md` | Write mode | Paste-ready prompt, for places without the handoff-resume skill |
| `CHANGELOG.md` | Update mode | One dated entry per later handoff, from either account: what changed since the last one. Newest at the bottom |
| `CHANGELOG-ARCHIVE.md` | Update mode | Entries already folded into `HANDOFF.md` |
| `AUTO-DIGEST.md` | auto-backup hook | Script-made backup after each turn (no model, no usage). In a shared folder, other sessions write `AUTO-DIGEST-<id>.md`, so accounts never overwrite each other |
| `POINTER.md` | fence | A regulated thread: nothing copied, only where its local transcript is |
| `files/` | Write mode | Copies of scratchpad files the next thread needs |

## Write mode

Don't start new work.

**0. Pause cleanly.** Finish or back out the current step so nothing is half-applied.

**1. Find yourself.** Your transcript id is the folder name in your scratchpad path. Run `handoff_tree.py <transcript id> --create`: it prints your title, parent, children (the whole subtree, with size, compactions and last activity) and creates your folder. Each thread line ends with `mode: WRITE` or `mode: UPDATE`. On UPDATE, switch to **Update mode** below now. If you were started outside the desktop app it finds no record: use `<HANDOFF>/<short title of your own>/` and write your transcript id into `.thread-id` there.

**2. Fence check.** If `handoff_tree.py` marks you FENCED, or your work is regulated (client, patient or other confidential records), write only `POINTER.md` (where your transcript is) and a `SUMMARY.md` with no content details. Copy nothing else. Report and stop.

**3. Live check.** Run `handoff_live.py --thread <transcript id> --paths <folders you worked in>`. In the desktop app also: `list_terminal_tabs` (a tab with `is_running_command: true` is a busy terminal in this session), your own background shells, scheduled tasks and artifacts you made. For each 🔴 that is yours: finish it, save it, or relaunch it detached (`nohup … &` or from the app) if it is safe and quick; otherwise record it. Never commit, push or close someone else's work to clear a flag; record it.

**4. Harvest.**
1. Your current context.
2. `handoff_extract.py <transcript id> --out <scratchpad>/digest.md` (never read a transcript whole). Only `[USER]` lines are the user's words; `FROM SESSION` and `BRIEF` lines came from other sessions. For older detail add `--summaries 4`. If `AUTO-DIGEST.md` exists in your folder, read its live check too.
3. Update state files you own (PROGRESS.md, COORDINATOR.md, notes) first. Files another thread owns: note what they miss.
4. Copy anything the next thread needs from a scratchpad or the app's support folder into `files/`. If it's gone, say where its content went.
5. Copy all scripts into the `<HANDOFF>` root, next to `INDEX.md` (never into a thread folder), if they're missing or older there.

**5. Write the files.** `HANDOFF.md` sections, in order:
1. **Transfer check.** 🔴 lines first: anything not transferred or off (live work from step 3, lost scratchpad files, unreachable children, missing paths). Then ⚪ expected items (prompt cache, artifacts to re-publish, scheduled tasks to re-create). Goal: no red.
2. Resume prompt (same text as `RESUME-PROMPT.md`).
3. Goal, mode (explore or ship), definition of done.
4. Where we stopped: the exact next action, the file or command it starts with, what done looks like. Then "Requests out" to other threads.
5. Decisions, dated, in three lists kept apart: what the user said (quoted), what sessions or Claude decided, proposals not ruled on.
6. Open decisions for the user, one line each.
7. Glossary of every label, id or shorthand a newcomer wouldn't know.
8. State on disk: files, repos, branches, uncommitted changes, backups, renders and builds with their output folders.
9. Account-bound items, each marked "works from any account" or "re-create on new account".
10. Gotchas and denials: what failed, what was ruled out, actions a permission check refused.
11. Verified vs. unverified.
12. Related threads with transcript ids and folders: parent, peers, children (each "pending" until it reports, or "covered by its auto-backup" if you won't wake it).
13. Sources: transcript path and id, number of compactions.

Rules: absolute paths everywhere, facts not narrative, under about 250 lines, no passwords, keys or tokens (say where they live), no client, patient or other regulated information (use placeholders like [CLIENT NAME]).

`SUMMARY.md`, exactly:
```
# <thread title>
Stopped: <one line>
Next: <one line>
Waiting on you: <one line, or none>
Red flags: <none, or each 🔴 on its own line>
Folder: <absolute path>
```
`RESUME-PROMPT.md`: resume <project> from handoff; read `<folder>/HANDOFF.md` first, then any `<folder>/CHANGELOG.md` entries after your own last one, then the 2 to 4 files it names; confirm the disk matches it (for growing files say "entry 147 or later", never an exact count) and report any mismatch; start at <next action>; effort <level>; if this thread has children, start each from its own folder's RESUME-PROMPT.md after these checks pass; old transcript at <path>, use the digest script on it, never read it whole.

**6. Index.** Append one line to `<HANDOFF>/INDEX.md` with a single `>>`: `- <date> | <project> | <title> | transcript <id> | <folder>/HANDOFF.md | parent: <title or none> | next: <one line>`.

**7. Check.** `ls` every path you named. Every term is plain or in the glossary. No secrets, no regulated information. Then run `handoff_rollup.py`.

**8. Cascade to child threads** (skip for "handoff here only", or when you have no children). Your own files are written first, so a cascade that stalls or runs out of usage loses nothing.
- Read each child's `SUMMARY.md` or `AUTO-DIGEST.md` if present. Recommend waking a child only if it has live work, a 🔴 flag, decisions in flight, or activity after the point your handoff captured its result. An idle child whose result is already in your handoff (section 12) doesn't need waking; its auto-backup covers it.
- Ask the user **once**, in a poll with the recommended option first: wake the recommended children (name them and why), wake all N, or none. Say that each woken thread spends usage.
- On a yes, message each chosen child (`send_message` to its session; `list_sessions {"linked": true}` gives ids). The message quotes the user's own words of approval, says "write your handoff into `<its folder>`", says the approval covers its own children, and asks it to end with `SUMMARY.md`. Never start a new session for a child; if `start_session` is ever needed, never pass a `cwd` the app refuses (for example a path with unusual symbols); give the path in the brief instead.
- **Write as a child:** when such a message arrives, do steps 0 to 9 into the folder it names. Cascade to your own children without asking again (quote the approval you received). Keep your final reply under 400 characters: your folder path and red-flag count.

**9. Report in chat.** Top: 🔴 red flags, or "🟢 Nothing left behind." Then a tree: your title with Stopped / Next / Waiting on you, and under it each child as a 3-line block (or "pending"). End with your folder path. Don't paste the resume prompt; it's in `RESUME-PROMPT.md`.

**10. When children report back** (the app wakes you after they finish): read each child's `SUMMARY.md`, fill in their folders in section 12, add their red flags to your transfer check, rerun the roll-up, and post the full tree again, red flags first. A child that never answered is a 🔴 flag: "covered only by its auto-backup".

## Update mode

The folder already holds a handoff, written by this thread or by a session on the other account. The other account has read it. Don't rewrite it; tell it what changed.

1. Do Write steps 0 to 3 as usual (pause, find yourself, fence, live check).
2. Harvest only what is new: `handoff_extract.py <transcript id> --since <value from the mode line> --out <scratchpad>/digest.md`. "whole transcript is new" means leave `--since` out. Read the folder's `SUMMARY.md` and the `CHANGELOG.md` entries after your last one, so you don't repeat what another session already logged.
3. Append one entry to `CHANGELOG.md` with a single `>>` (both accounts may write; never rewrite the file). The header is parsed by scripts, so keep it exact, in local time:
   ```
   ## 2026-10-28 21:14 · <account name> · <thread title> · transcript <first 8 characters of your id>
   - Changed: <what was built, decided, sent or ruled, with paths>
   - Decisions: <quoted user words kept apart from Claude's calls>
   - Now: <the exact next action and the file or command it starts with>
   - Waiting on the user: <one line, or none>
   - Red flags: <🔴 lines, or none>
   - Stale in HANDOFF.md: <sections you edited below, or none>
   ```
   `<account name>`: the name the tree line shows (set friendly names in `~/.config/handoff/accounts`).
4. Edit only the `HANDOFF.md` sections that are now wrong: usually 1 (transfer check), 4 (where we stopped), 6 (open decisions), 8 (state on disk). Leave the rest alone.
5. Rewrite `SUMMARY.md` (same 5 lines). `RESUME-PROMPT.md` changes only if the next action or effort changed; it already says to read `CHANGELOG.md` entries after the reader's last one.
6. **Fold** when `CHANGELOG.md` holds more than 5 entries: absorb the older ones into `HANDOFF.md`, move them to the end of `CHANGELOG-ARCHIVE.md`, keep the newest 2. A reader then faces at most a handful.
7. Then Write steps 6 to 10 (index line marked "update", check, cascade, report). A child woken by a cascade follows the same rule: Update when its folder has a handoff.

When the other account reopens a thread that shares this folder, the session-start hook tells it, in one line, that new entries are waiting and where to start reading. Nothing prints when nothing is new.

## Roll-up mode

`handoff_rollup.py` rewrites `<HANDOFF>/START-HERE.md`: red flags from every thread, then the thread tree (from the app's session records, else folder nesting) with each thread's status and next step, older single-file handoffs, and every open decision. Safe to rerun. `handoff_tree.py --active-days 7` lists every thread active this week, as trees.

## Setup mode

- **Auto-backup** (no usage cost): `mkdir -p ~/.config/handoff && touch ~/.config/handoff/auto`. The plugin's Stop hook then runs `handoff_auto.py` after each turn, at most every 30 minutes per thread, for desktop threads with transcripts over 150 KB. Remove the file to turn it off.
- **Fence:** one term per line in `~/.config/handoff/fence` (a project folder name, a client or program name). Threads whose title or folder contains a term get only `POINTER.md`; nothing from them is copied.
- **Folder:** write the handoff folder's path into `~/.config/handoff/dir`.
- **Usage alert:** in the desktop app, create a scheduled task every 6 hours whose prompt reads `get_usage`; when the weekly limit passes 85%, it sends one notification that week asking whether to back up the week's threads (`handoff_tree.py --active-days 7`). It never runs the backups itself, because each handoff spends usage. Check on its first run that the scheduled session can call `get_usage`.
- **Tidy:** `handoff_tree.py --tidy` moves child folders inside their parent's folder, judged by each folder's original thread only.
- **Account names:** lines like `1a2b3c4d = Personal` in `~/.config/handoff/accounts` (the id is the account folder under the app's `claude-code-sessions`). Changelog entries and tree lines then show the name.
- **Merge duplicates** (folders made before 1.4.1, when a resumed thread got its own folder): `handoff_merge.py` shows the plan and moves nothing. Show it to the user; lines marked GUESS need their call. `handoff_merge.py --apply [--skip "<folder name>"]` copies the whole handoff folder to a dated backup first, then merges. Files never overwrite; a clash gets the session id in its name.
