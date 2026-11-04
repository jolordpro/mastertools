# Host matrix

Measured 2026-10-08 on macOS 26 (Darwin 25.4), Creative Cloud UPIA 8.5.0.13, UXP 9.3.0 in PS/ID/PR.
App versions: Photoshop 27.9.0, InDesign 21.4.1, Premiere Pro 26.5.0, After Effects 26.5.0, Illustrator 30.8.1.
Confidence: **measured** = installed and ran on this Mac; **observed** = seen in app bundles/logs; **docs** = Adobe docs.

## Per app

### Photoshop: `host.app: "PS"`, minVersion used `24.0.0` (manifest v5 needs 23+)
- Third-party install via UPIA: **measured** ✅. `uxp.host.name` = `Photoshop`.
- Menu: Plugins ▸ *Plugin name* ▸ *Panel label*. Also Plugins ▸ Plugins Panel / Manage Plugins.
- Runs UXP JS (`require("photoshop")`). DOM edits must be inside `core.executeAsModal`.
- Runs legacy ExtendScript `.jsx` via batchPlay `AdobeScriptAutomation Scripts` (**measured**; needs the error wrapper).
- `.psjs` files are Photoshop's own UXP script format (File ▸ Scripts ▸ Browse also runs them; **docs**).
- Photoshop 2026 and Beta load **no CEP** at all (no CSXS log, no Extensions menu) (**measured**).
- Photoshop Beta is a separate product (`PHSPBETA` storage folder); UPIA `--list` did not list it separately (observed).

### InDesign: `host.app: "ID"` (Adobe's own manifests also use `"indesign"`), minVersion used `18.5.0`
- Third-party install via UPIA: **measured** ✅. `uxp.host.name` = `InDesign`.
- Menu: Plug-Ins ▸ *Plugin name* ▸ *Panel label*.
- Runs ExtendScript from UXP: `app.doScript(code, ScriptLanguage.JAVASCRIPT)` returns the script's value (**measured**).
  `ScriptLanguage.UXPSCRIPT` exists for UXP code. `.idjs` = InDesign UXP script files.
- CEP still works too (classic panels load under Window ▸ Extensions).

### Premiere Pro: `host.app: "premierepro"`, minVersion used `25.6.0`
- Third-party install via UPIA: **measured** ✅. `uxp.host.name` = `premierepro`.
- Menu: Window ▸ UXP Plugins ▸ *Plugin name*.
- **No ExtendScript bridge from UXP** (no batchPlay, no doScript). UXP JS only: `require("premierepro")`.
- CEP still works; CEP panels are greyed in Window ▸ Extensions until a project is open.
- Premiere has **no AppleScript dictionary** (`sdef` is empty). External control = CEP debug port (see testing.md).

### After Effects: `aftereffects` ❌
- UPIA `--install` → `Failed to install, status = -411!` for host ids `aftereffects`, `AEFT`, `AE`, minVersions 20–26.
- The app bundle has `Contents/UXP/plugins` (Adobe's own: Frame.io, Stock, creative-copilot with `"app": "aftereffects"`)
  and `dvauxphost.framework`, so the runtime exists; outside plugins are blocked (observed).
- Use ScriptUI panels / CEP for AE.

### Illustrator: `AI` ❌
- UPIA → `status = -411` for `AI` (min 26/30) and `ILST`.
- Bundle has `Required/UXP`, `AIUXPExtensionHostAPI.framework`; Adobe's own UXP plugins target `"AI"` (observed).
- Use CEP / ExtendScript for Illustrator.

## Re-probing a host (when a new version ships)
Build a throwaway package with the host id and a probe plugin id, try UPIA, then remove it:
```bash
UPIA="/Library/Application Support/Adobe/Adobe Desktop Common/RemoteComponents/UPI/UnifiedPluginInstallerAgent/UnifiedPluginInstallerAgent.app/Contents/MacOS/UnifiedPluginInstallerAgent"
"$UPIA" --install probe.ccx      # "Installation Successful" = open; "status = -411" = still closed
"$UPIA" --list all               # products UPIA knows + installed plugins
```
`uxp_build.py --install` reports this per app in plain words.

Where Adobe's own plugins declare hosts (useful for the current host ids):
`/Applications/<App>/<App>.app/Contents/UXP/plugins/*/manifest.json` (AE, PR),
`.../Contents/Required/UXP/*/manifest.json` (PS, AI), `.../Contents/Resources/UXP/` (ID).

## Install locations (per user)
- Installed plugins: `~/Library/Application Support/Adobe/UXP/Plugins/External/<id>_<version>/`
- Plugin storage: `~/Library/Application Support/Adobe/UXP/PluginsStorage/<PHSP|ILST|...>/<major>/`
- UPIA itself: `/Library/Application Support/Adobe/Adobe Desktop Common/RemoteComponents/UPI/UnifiedPluginInstallerAgent/`
