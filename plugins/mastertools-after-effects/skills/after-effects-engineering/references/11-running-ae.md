# Running scripts in After Effects

`scripts/aerun.py` is the one default way to run any `.jsx` in AE, from any project. Call it from this skill's
`scripts/` folder. Never copy it into a project: a copy drifts from the frozen one and stops getting fixes. Its header
names the source sha (a29cd534), the QC freeze (FREEZE_render v2 b941ea8aa0c04258) and the only changes made for the skill.

```
python3 -I <skill>/scripts/aerun.py --app 2026|beta <tool.jsx> [KEY=VALUE ...] [--lane A] [--timeout SEC]
python3 -I <skill>/scripts/aerun.py --app 2026|beta --running        exit 0 runs, 5 not running (sends nothing)
python3 -I <skill>/scripts/aerun.py --app 2026|beta --dialogs launch  G3 scan only: 0 clean, 6 a dialog
python3 -I <skill>/scripts/aerun.py --gateinfo                        the qc_gate.py it will use, with its sha
```

Exit codes: 0 done, 1 script error / lint or gate refusal / no END line / osascript failed, 2 usage, 3 lock wait
ran out, 4 slot held by another lane, 5 AE not running, 6 a dialog (or breadcrumbs unreadable).

Settings, all optional except the ES3 lint:
- `AE_ES3LINT`: path to an `es3lint.sh` (else the one shipped next to aerun.py in this skill). It needs `node` on PATH (a launchd or cron PATH may lack it). Missing: every call is refused.
- `AE_QC_GATE`: used only when the skill's own `scripts/qc_gate.py` is missing.
- `AERUN_KITS="name=/abs/tools/dir;name2=/abs/dir2"` and `AERUN_KIT=name`: look a bare tool name up in a kit folder.
- `AE_LANE` (or `--lane`): the lane that owns the AE 2026 slot (`--slot take|free|show`).
- `AERUN_TEST=<dir>`: stubs only. Moves every file into `<dir>` and takes `pgrep`, `ps`, `osascript` from `<dir>/bin`.
  Tests: `tests/test_aerun.py` in this plugin's source repo.

## Hard rules (QC dialog-proofing ruling, Nov 1)

1. **Never launch AE from a script call.** aerun checks the exact app binary with `pgrep` first and asks "is running"
   inside the AppleScript. AE not running: exit 5, nothing sent. The user starts AE.
2. **Open projects in the background:** `open -g -a "<full app path>" file.aep`, never `open -a` alone.
3. **Never make an `.aep` read-only** (no `chmod 444`, no locked flag). AE answers a locked file with a modal
   ("File is locked") that swallows the next call. Guard every save in ES3:
   `if (dst.exists && dst.readonly) throw new Error("locked " + dst.fsName);`
4. **Scan for dialogs after every call.** aerun reads AE's Sentry breadcrumbs (the newest `SentryIO-db/*.run`,
   `__sentry-breadcrumb1` and `2`) for `Up_DlgShow` / `AEErrorDialog` entries, before the send and after it. A hit
   prints `DIALOG`, writes the stop flag and exits 6; every later call to that AE exits 6 until AE is relaunched.
   Stop on a hit: send nothing more, and tell the user what the dialog said. Unreadable breadcrumbs count as a hit.
5. **Exit 0 needs two things:** osascript's own rc 0, and a log whose last line starts `END`, written by `H.run`'s
   `finally`. Any `ERR ` line, a missing END or a missing log is exit 1, even when other lines are there.
- Re-pin `SENTRY` in aerun.py when AE or the Beta changes major version: a pinned folder for an old version stays readable, so the scan would report clean and miss real dialogs.
6. **Lint before send:** `scripts/ae_dialog_lint.py` on every `.jsx`, `.sh` and `.py` the job uses (alert/confirm/
   prompt, entry code outside `H.run`, `endSuppressDialogs` outside `finally`, `app.quit`, unguarded `.save(`,
   `open -a` without `-g`, `tell application` with no "is running" check, `chmod` read-only on an `.aep`). aerun then
   runs es3lint and `qc_gate.py` on the filled script itself. Never pass `--nogate`.
   ae_dialog_lint.py is a tool, not a job input: run on itself it flags rule S1 on its own message text. Leave it out of self-checks.
7. **Pick AE by its full app path, never the bundle id.** AE 2026 and 2025 share `com.adobe.AfterEffects.application`,
   so an id can reach the wrong AE. aerun targets `/Applications/Adobe After Effects 2026/...` and the Beta by path.
8. **No call within 10 s of AE's launch** (aerun waits out the rest).

## Parallel work

- **Scripted builds: one slot per AE app.** AE 2026 and AE Beta can each run one scripted build at a time (one lock
  per app). Two jobs on one AE wait on the lock; they do not run side by side.
- **Renders scale with `aerender` processes**, not with script calls. Book them through whatever
  owns render slots on your machines.
- AE has no headless script runner like `c4dpy`: every script call goes to a running AE with its UI up.
- A socket listener inside AE (a startup script that takes jobs over a port) is unproven here. Not recommended.
