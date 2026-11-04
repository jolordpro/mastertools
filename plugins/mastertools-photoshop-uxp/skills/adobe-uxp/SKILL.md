---
name: adobe-uxp
description: >-
  Building, packaging, installing and verifying Adobe UXP plugins (panels and commands) for Photoshop, InDesign and
  Premiere Pro, and checking whether After Effects or Illustrator accept them yet. Covers the no-admin install route
  (.ccx via Adobe's UPIA installer), the silent same-version update trap, running legacy .jsx ExtendScript from UXP,
  UXP's non-browser HTML/CSS quirks, and testing without developer mode. Use this skill whenever the work touches UXP
  in any form: a manifest.json with "manifestVersion", a .ccx file, a "Plugins" menu panel, batchPlay, executeAsModal,
  require("photoshop" | "indesign" | "premierepro" | "uxp"), .psjs or .idjs scripts, UXP Developer Tool,
  UnifiedPluginInstallerAgent, or moving a CEP/ExtendScript panel to UXP. Trigger it even when the user only says
  "Photoshop plugin", "make this work in Photoshop 2026", "Premiere panel", "Adobe is moving to UXP", or "the panel
  doesn't show up in Photoshop".
---

If `~/.claude/overlays/adobe-uxp/README.md` exists, read it first: the user's own picks, examples and paths. They win over this skill's defaults.

# Adobe UXP plugins

UXP is Adobe's replacement for CEP panels. Photoshop has already dropped CEP. The expensive failures here
are rarely bad JavaScript. A package doesn't update and nobody notices, or an app silently refuses the plugin. A
`<button>` renders three times too big, or an ExtendScript error pops a modal the panel never hears about. This
skill covers those failures, measured on a real Mac (Oct 2026). It hands the mechanical checks to scripts.

You already know modern JS and the shape of a UXP plugin. What follows is only the part that bites.

## Facts to start from (re-verify when versions move)

| App | `host.app` | Homemade plugins? | Opens from |
|---|---|---|---|
| Photoshop | `PS` | ✅ | Plugins ▸ *Plugin* ▸ *Panel* |
| InDesign | `ID` | ✅ | Plug-Ins ▸ *Plugin* ▸ *Panel* |
| Premiere Pro | `premierepro` | ✅ | Window ▸ UXP Plugins ▸ *Plugin* |
| After Effects | `aftereffects` | ❌ UPIA `status = -411` | — (use CEP / ScriptUI) |
| Illustrator | `AI` | ❌ UPIA `status = -411` | — (use CEP / ScriptUI) |

AE and Illustrator ship a UXP runtime but refuse outside plugins. Don't promise a UXP panel for them. Build it if
asked, keep it in `dist/`, and re-test with `uxp_build.py --install` after major updates. `references/host-matrix.md`
has the per-app detail, including what each host can and can't run (ExtendScript bridges).

## Workflow

1. **Scaffold**: `python3 scripts/uxp_new.py <project-dir> --name "My Panel" --id com.nesn.mypanel --apps PS,ID,PR`.
   It creates `uxp.config.json` plus `src/` (panel HTML/CSS/JS that already avoids the UI traps and logs to
   `/private/tmp/<id>.log`). One plugin id per app (`com.nesn.mypanel.ps`) so one app refusing can't block the others.
2. **Write the plugin** in `src/`. Read `references/runtime-gotchas.md` before touching files, ExtendScript or
   Photoshop modal state, and `references/ui-kit.md` before writing markup or CSS.
3. **Check**: `python3 scripts/uxp_check.py <project-dir>`. Static lint for UXP-hostile markup and CSS, permission/code
   mismatches (e.g. `AsyncFunction` without `allowCodeGenerationFromStrings`), `write("")` and manifest errors. Fix
   every ERROR.
4. **Build + install**: `python3 scripts/uxp_build.py <project-dir> --install`. It **bumps the patch version every
   build**, because UPIA reports "Installation Successful" for an unchanged version and keeps the old files. That's
   the trap this step exists to prevent. Writes `dist/<Name>-<APP>.ccx` and installs each through UPIA (per user,
   no admin). `--list` shows what's installed. `--remove` uninstalls by plugin **name**, so it removes every
   app's copy; give probe plugins their own name.
5. **Restart the app.** UXP plugins load at launch.
6. **Verify from outside the app** (`references/testing.md`): read the start-up line in the log, run the feature,
   and check a receipt file it wrote. Without developer mode there is no debugger, so the log *is* the debugger.

## The traps that cost the most time

- **Same version = no update.** Covered by the builder; never hand-zip and reinstall without bumping.
- **Developer mode needs admin** (`/Library/Application Support/Adobe/UXP/Developer/settings.json`), so UXP Developer
  Tool loading and debugging are out on managed Macs. Don't route around it through IT; use UPIA + logs.
- **Photoshop `.jsx` via batchPlay shows Photoshop's own error modal** even with `dialogOptions: "dontDisplay"`, and
  batchPlay only returns `-128`. Run a temp wrapper `.jsx` that `$.evalFile`s the target in try/catch and writes the
  result to a file you read back (code in `runtime-gotchas.md`).
- **Premiere/AE/AI UXP cannot run ExtendScript.** A UXP panel there runs UXP JS only. Keep the CEP panel for `.jsx`.
- **UXP is not a browser.** Native `<button>` ignores sizing, `<header>`/`<footer>` mis-lay out, `opacity` on divs
  doesn't render, `dblclick` is unreliable, window `focus` rarely fires, no sticky/grid/`::after`. Use the template.
- **`file.write("")` throws** `writeToFile: data cannot be null`.
- **Floating panels reopen where they last were**, which can be off-screen after a monitor change. System Events
  `set position of window 1 of process "<App>" to {x, y}` brings one back.

## Driving the apps for tests

Use whatever UI-driving helpers the machine has: an OCR click-point finder, a click helper that only clicks when the
target app is frontmost (the user may be working between steps, so never click without that check), `screencapture -l
<windowid>` for a window hidden behind others, and a Chrome DevTools Protocol eval helper for CEP panels.
Photoshop/InDesign home screens hide docked panels; Escape dismisses them. Never click in System Settings privacy
panes. Full procedure in `references/testing.md`.

## Delivery notes for the user

- Install per Mac user: `python3 scripts/uxp_build.py <dir> --install`, or double-click each `.ccx` (Creative Cloud
  asks "do you trust this?"). No admin.
- Tell them **what must travel to another Mac**: the project folder (or just `dist/*.ccx`) plus any data folders the
  plugin reads, and that each user runs the install once.
- Say plainly which apps took the plugin and which refused, and where the panel appears in each app's menus.
- Where an app still needs the CEP/ScriptUI version (AE, Illustrator, `.jsx` in Premiere), say so.
