# Testing and driving the apps without developer mode

No UXP Developer Tool and no debugger, because developer mode needs admin. Prove things from outside the app.

## 1. Log + receipts (the template does this)
- Start-up line: `start: <APP> host=<uxp.host.name> <version> uxp=<uxp.versions.uxp>`. If it's missing after launch and
  opening the panel, the plugin didn't load (wrong host id, old version still installed, or the app wasn't restarted).
- Every status message is logged. Read with `tail /private/tmp/<plugin id>.log`.
- Features that do work write a **receipt** (timestamp + host + input) to `/private/tmp/...`. Delete it before the test,
  check after. A status line alone is not proof.
- Test the failure path too: a deliberately broken script/input must come back as a readable error in the panel, with no
  host modal. Use temporary files, then `trash` them.

## 2. Install → restart → open
```bash
python3 ~/.claude/skills/adobe-uxp/scripts/uxp_build.py <dir> --install     # bumps version, builds, UPIA installs
osascript -e 'tell application "Adobe Photoshop 2026" to quit'                # only if no unsaved user documents
open -a "Adobe Photoshop 2026"
```
Before quitting an app, check it has no user documents open (`count documents` for PS/ID via AppleScript). **Never
close something the user opened** (see feedback-never-close-unowned-project).
Open the panel through the menu with System Events (works even when the app isn't frontmost):
```bash
osascript -e 'tell application "System Events" to tell process "Adobe Photoshop 2026" to click menu item "My Panel" of menu 1 of menu item "My Panel" of menu "Plugins" of menu bar 1'
# InDesign: menu "Plug-Ins"   Premiere: menu item "UXP Plugins" of menu "Window"
```
Clicking the menu item of an already-open panel **closes** it. Check the log/window list first.

## 3. Seeing the panel
- Window list with ids and bounds:
  `nesnpy -c 'import Quartz; [print(w["kCGWindowNumber"], w["kCGWindowBounds"]) for w in Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, 0) if "Photoshop" in str(w.get("kCGWindowOwnerName"))]'`
- `screencapture -x -o -l <id> out.png` captures one window even behind the Claude window.
- A floating panel may restore **off-screen** (x beyond the display after a monitor change):
  `osascript -e 'tell application "System Events" to tell process "Adobe Photoshop 2026" to set position of window 1 to {1000, 200}'`
- Photoshop/InDesign **home screens cover docked panels**: with the app frontmost, `macctl key escape` dismisses it.

## 4. Clicking (real UI, real handlers)
- Locate with OCR: `macctl find "Panel Test"` prints click points in screen points. Don't compute coordinates by hand
  from a scaled screenshot; that's how a click landed in System Settings once.
- Click with `gclick "<App process name>" X Y`. It aborts unless that app is frontmost **at that instant**. The user works
  between steps and the Claude window comes forward often.
- The first click into a freshly restarted panel may only focus it. If nothing happened, click the row again.
- Never click in System Settings privacy panes, password prompts or IT Self Service.

## 5. Premiere specifics
- No AppleScript dictionary. Drive it through a CEP extension's debug port with the Chrome DevTools Protocol:
  `cdp-eval <port> 'new Promise(r=>__adobe_cep__.evalScript("app.version", r))'`.
- A CEP bundle can carry an invisible bridge extension that starts with Premiere, plus a panel on a local debug port.
  Useful ExtendScript: `app.newProject(path)`,
  `app.openDocument(path, true, true, true, true)`, `app.project.save()`, `app.projects.numProjects`, `app.quit()`,
  and `__adobe_cep__.requestOpenExtension("<ext id>", "")` / `closeExtension()` from the panel side.
- Launch with `open -a` (with `open -g` the bridge loaded then exited). Opening a `.prproj` with `open -a` also works.
- Use a scratch project in the session scratchpad for tests, never the user's.

## 6. After testing
Quit the apps you opened, bring Claude back (`osascript -e 'tell application id "com.anthropic.claudefordesktop" to activate'`),
remove temporary scripts, and remove probe plugins (`uxp_build.py --remove`). Leave the user's real plugins installed.
