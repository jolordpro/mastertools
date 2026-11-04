# 06 — CEP Extensions (the co-equal vehicle, from production)

> When Phase 0 (`00` §3) chooses CEP — the UI genuinely exceeds ScriptUI (rich/themed tables, charts, drag
> canvas, multi-view app, real network/auth, two-app communication) — this is the production playbook, distilled
> from shipping a commercial AE↔Illustrator CEP extension. CEP is **frozen, not dead** (CEP 12 is the last major
> version; security fixes, no EOL — verify status per the freshness protocol). The host layer is **still ES3**, so
> everything in `04` + `00` §4 applies to it. Scaffold with **Bolt-CEP** unless told otherwise; don't hand-roll
> the manifest/signing/HMR boilerplate.

---

## §1 — THE THREE LAYERS (and the bridge)

```
┌────────────────────────────────────────────────────────────┐
│ CLIENT  (index.html + index.js)   — CEF/Chromium, MODERN JS │  UI, polling, in-memory state
│   ↕ CSInterface.evalScript("hostFn(args)", cb)  → JSON str  │
│ HOST    (host/index.jsx)          — ExtendScript, STRICT ES3│  ALL app.project / DOM reads + writes
│   ↕ (optional, for two-app comms) JSON files on disk + poll │
│ BRIDGE  (no live socket)          — files in Folder.userData│  cross-app / cross-process messaging
└────────────────────────────────────────────────────────────┘
```

- **Client** = modern JS in Chromium. Renders the UI, polls state, calls the host *by name*; each call returns a
  **JSON string** the client `JSON.parse`s. Match the host theme via `CSInterface.getHostEnvironment()
  .appSkinInfo` — a CEP panel that ignores AE's theme looks bolted on.
- **Host** = ES3 only. The **only** layer that touches the DOM. All writes wrapped in a single
  `beginUndoGroup`/`endUndoGroup` closed in `finally`.
- **Bridge (two-app comms)** = **no live socket.** Use JSON files in `Folder.userData/<AppName>/`, written
  **temp-then-rename** (UTF-8), polled every ~1 s via `File.modified` (a cheap stamp). This is what lets two apps
  cooperate even when the other is closed.
- **State:** no browser `localStorage` (unsupported in this context). Persist in the host's settings API
  (`app.settings`); keep ephemeral UI state in client memory.

---

## §2 — THE TWO-ENGINE DISCIPLINE (the #1 way to break a host)

**Host = strict ES3** (assume NONE of: `let`/`const`/arrow/template-literals/destructuring, `Array.forEach/map/
filter/reduce`, `Object.keys`, native `JSON`; reserved words as object keys throw and `node --check` won't catch
it). Ship a **guarded JSON polyfill** at the top of every host file. **Client = modern JS** (Chromium — `const`/
arrow/Promise/`fetch` are fine). **Expressions are a third engine** (modern JS). Never apply ES3 rules to the
client/expressions, or modern syntax to the host. The phantom-polyfill trap (`00` §4) applies to the host →
ship guarded polyfills + run the cold-start test.

---

## §3 — THE hostFail INVARIANT (every entry point always returns JSON)

A bare `throw` in a host function makes CEP hand the client the literal string `"EvalScript error."`, which
`JSON.parse` chokes on → the client can only show a misleading "didn't respond." So **wrap every entry point:**

```javascript
function panelPeek(args) { try { return _panelPeek(args); } catch (e) { return hostFail("panelPeek", e); } }
function _panelPeek(args) { /* real logic */ }
function hostFail(where, e) {
    logLine("ERR " + where + ": " + e);                 // to the host's userData log file
    return JSON.stringify({ ok:false, _hostError:true, where:where, msg:String(e && e.message || e) });
}
```
A `null` parse on the client then means **only** a genuine no-response. **`node --check` does NOT catch a call
to an undefined function** (it's a runtime `ReferenceError` — the classic "every send throws because a helper was
never defined" bug). Run the **called-vs-defined audit** (`scripts/qc.sh`) on every host, and confirm every
`hostFn()` the client calls is defined in its host. **Keep the wrapper + the audit on every new entry point.**

---

## §4 — THE FILE BRIDGE PROTOCOL (for two-app or cross-process comms)

- **Atomic writes:** write to `path.tmp`, then rename to `path` (UTF-8). A torn read can never happen.
- **O(1) watcher:** each side polls only the *other* file's `File.modified` stamp (~1 s). **Never parse a large
  payload on every poll** — gate the parse on the cheap stamp and cache the result (a per-poll full parse of a
  big payload pins the host thread; this was a real, persistent-slowdown bug).
- **Round-trip confirmation:** stamp each send with a monotonic `tx`; the receiver echoes `tx` in a sidecar
  `*_ack.json` after it builds; the sender confirms only when `ack.tx` matches its own last send (no stale-ack
  false positives). The CEF client polls in its own process, so it reads progress/acks even while ExtendScript
  blocks the host's main thread.
- **First-poll baseline:** on first poll, treat any pre-existing file as already-seen (don't auto-act on state
  that predates the panel opening).

---

## §5 — THE CHROMIUM-CAPABILITY PRINCIPLE (check FIRST before calling a feature "impossible")

The client and host have **wildly different ceilings**, and it's easy to over-apply the host's limits:
- **Host = ES3 ExtendScript** — the only thing that can read/write the live Adobe DOM, but ancient and limited.
- **Client = full Chromium + Node.js** — `canvas`/WebGL, `fetch`, `MediaRecorder`/`captureStream`, WASM, bundled
  npm libs, Node `fs`/`child_process`. **Its ceiling is Chromium's, not ES3's.**

**The pattern:** when a feature seems blocked by ExtendScript, ask *can the CLIENT do it instead, fed by what the
host extracts?* — **host extracts/renders → client transforms with real horsepower → host builds back / client
writes a file.** Real examples: WebP export (ES3 can't encode it; the client transcodes the host's PNG via
`canvas.toBlob('image/webp')` + Node `fs`); WebM via `MediaRecorder` + `canvas.captureStream(0)` +
`track.requestFrame()` over host-rendered frames; raster→vector tracing; LLM/vision calls via `fetch`.

**The hard boundary (don't oversell):** the client touches the Adobe DOM **only** via `evalScript` into the ES3
host. So a generated script can do anything ExtendScript can — **but not more.** Things still genuinely blocked:
AE editable gradient shape fills aren't scriptable; "live" observation has no change-event API (stays
poll-based). Verify the specific limit against the changelog (a newer version may have lifted it).

---

## §6 — CEP UX (what differs from ScriptUI; learned the hard way)

Every canon principle (`01`) and UX mechanism (`03`) still applies — CEP gives you better tools to honor them.
Plus these CEP-specific lessons:

- **Prefer a top tab bar over per-density-tier `display:none`.** A drawer/popover in normal flow can inflate the
  panel's `scrollHeight` → a measure-and-step-down density system downgrades the tier → the very control you
  opened **vanishes**. (Real bug: "the info button does nothing"; "the gear simplifies the panel.")
- **Density tiering should be WIDTH-primary**, not height-measuring. Tier by `clientWidth` only (stable across
  reveals); let vertical overflow scroll (`body { overflow-y:auto }`). Opening a drawer never changes width → never
  re-tiers.
- **Never hide an interactive surface with a per-tier `display:none`.** A **sticky header** must never be hidden
  by any tier.
- **If you must use a popover, make it a `position:fixed` overlay** (`max-height:calc(100vh - Npx); overflow-y:auto;
  z-index`) so it can't inflate layout height.
- **Manifest resize gotcha:** a `<Geometry>` with `<Size>` + `<MinSize>` but **no `<MaxSize>`** locks the panel to
  its default size — always add a generous `<MaxSize>`.
- **House defaults (the user's):** inline errors (never a blocking host `alert()`); momentary success color that
  fades to calm; post-action round-trip confirmation; Enter = primary / Esc = close; compact, density-responsive;
  muted (not blue) links. Brand = **LORD (gold on warm ink)** via the `lord-brand` skill, with "match the host
  Adobe theme" as the neutral default.
- **Validation caveat:** debugger-driven checks (forcing `.hidden=false`, calling host fns) **cannot catch CSS/
  tier/visibility bugs.** Either a human clicks at the smallest realistic docked size, or drive the CEF debugger
  with `element.click()` + `getComputedStyle()`/`getBoundingClientRect()` reads while forcing each tier class.

---

## §7 — FEEDBACK & EXTERNAL LINKS (a real reliability trap)

- `CSInterface.openURLInDefaultBrowser(url)` accepts **http/https ONLY — `mailto:` and custom schemes are
  rejected**, and a plain `<a href="mailto:…">` is **unreliable in CEF**. A `mailto:` support link is a latent
  bug. Use an **https hosted form/board** instead; feature-detect both `window.cep.util.openURLInDefaultBrowser`
  and the `CSInterface` method, wrap in try/catch. To share an email, copy it to the clipboard rather than
  `mailto:`.
- **In-app feedback with no backend:** never embed a third-party widget/SDK (CSP breakage, offline, privacy).
  Open a **hosted form** (Tally / Featurebase / GitHub Discussions) in the default browser with version/app/OS
  **prefilled as query params** (consent-based; nothing sent until the user submits). Put the link in the About/
  settings area. Optionally a **one-time success nudge** after ~5 *confirmed* successful actions (count only real
  successes via the tx/ack signal, never errors/empties; persist a `prompted` flag; fire once, never nag).

---

## §8 — SIGNING, DISTRIBUTION & THE UPDATE LIFECYCLE

Sign with Adobe's **`ZXPSignCmd`** (from Adobe-CEP/CEP-Resources). A turnkey sign script should:
1. Create a **self-signed cert** (`.p12`) on first run — self-signed is correct and accepted for `.zxp` (no paid
   CA needed; `OS Trusted: false` from `-verify` is normal and accepted by installers).
2. Sign each bundle **with a timestamp** (`-tsa http://timestamp.digicert.com`). **This is the keystone — a
   timestamped signature stays installable even after the cert expires.**
3. Produce one `.zxp` per panel.

**Immutable forever — change these and you break the update chain:** the **certificate** (`.p12` + password) and
the **`ExtensionBundleId`**. Only the **version string** changes per release (manifest `ExtensionBundleVersion` +
`Extension Version`, host header, footer, About — grep to confirm none stale). Use **strict semver with NO
pre-release suffix** (a malformed version is silently rejected → the panel won't appear). Back up the `.p12` +
password off-machine — it's the only irreplaceable asset.

**Dev install (iteration):** drop the unsigned bundle into `~/Library/Application Support/Adobe/CEP/extensions/`,
enable `PlayerDebugMode` under the host **runtime's** CSXS key — **for AE 25/26 that's CSXS 11/12**, e.g.
`defaults write com.adobe.CSXS.12 PlayerDebugMode 1` (the runtime version, *not* the `RequiredRuntime` your
manifest declares — declare 9.0 + the node flags for the Apple-Silicon load fix, but debug under 11/12) — then
restart. A `.debug` file maps the panel to a localhost port for Chromium remote-debugging — **remove `.debug`
from the signed release.** **Distribution:** sign → install via the free ZXP/UXP Installer (drag the *unzipped*
`.zxp`) or the aescripts Manager.

**Install-hygiene trap (saves hours):** stale duplicate installs in the **user *and* `/Library`** CEP folders
masquerade as bugs ("feature broken" is often an old build loading). **Always confirm the *loaded* version via an
in-panel footer**, and check both folders for duplicates before installing a new one.

---

## §9 — MAINTAINABILITY ("where to edit" discipline)

- **One host file per panel — do NOT `#include`-split.** `#include` is only build-time concatenation; it **breaks
  the in-app debugger** and **hard-throws on a bad path**. Use clear section-banner comments instead.
- **Keep the host↔client contract in ONE canonical place** (a project `CLAUDE.md` "API contract" — every entry
  point's signature + return shape). The in-file host header *points to it*, doesn't duplicate it (duplicated
  lists drift). Change a signature on **both sides in the same edit**, then run the called-vs-defined check.
- **Client stays build-step-free** (no bundlers, ES modules, `localStorage`). **Share code across panels via a
  dual-export IIFE loaded with a `<script>` tag** (attaches `window.Foo`, loaded before `index.js`, aliased at
  the top of each IIFE) — never `#include`, never a bundler. Caveat: a `var` alias is **not** hoisted like a
  `function` decl, so the alias shim must sit **above** every reference (a referenced-before-assigned slip is a
  runtime `TypeError` that `node --check` won't catch — add a scan).
- **Hand-copied bundled modules are one forgotten `cp` from shipping mismatched panels** → make it a QC failure
  with a **drift-guard** (`cmp -s` each source against every bundled copy) + a `--sync` mode to re-copy.
- **Update protocol (every change, in order):** edit the **dev tree** → `bash qc.sh` (fix every failure) → bump
  the version everywhere (grep to confirm) → update the contract/changelog docs → re-cut the clean release copy
  (strip `.debug`/`.DS_Store`) → re-sign → re-install → **confirm the footer version** → the human runs the
  affected path in the real apps (the only DOM test).
- **Don't** modernize the manifest if an older CSXS version is a documented load-bearing fix (e.g., a CSXS-9.0 +
  CEF-flags combo chosen for an Apple-Silicon load issue); don't "tidy" a load-bearing divergence without
  re-reading why it exists.

---

## §10 — QC GATE (codified in `scripts/qc.sh`)

No DOM unit-test harness exists; "compiles + ES3-clean + math passes" is **necessary-but-not-sufficient** — the
human confirms real transfers in-app. The gate runs in sequence, exits non-zero on any failure:
host/client `node --check` · **ES3-purity grep** (`let/const/=>`, `forEach/map/filter/Object.keys` in hosts) ·
**called-vs-defined** (the `returnFile`-class ReferenceError) · **guarded-polyfill presence** · **undo-group
pairing** · HTML `<div>` balance + every `getElementById` resolves · manifest XML well-formed + version parity ·
optional pure-math self-test · **bundled-module drift-guard.** Plus by hand: the **cold-start test** + the
**adversarial fixtures** (`00` §6).

---

## §11 — CONTEXTUAL AWARENESS: other apps (shallow, clearly bounded)

CEP/ExtendScript is After Effects' home for the foreseeable future. For neighbours:
- **Illustrator** shares the **same CEP/ES3 model** — a CEP panel for AI is built the same way (different DOM:
  `app.activeDocument`, `pathItems`/`textFrames`, etc.). This is why an AE↔AI bridge fits one extension.
- **Photoshop / Premiere** are **UXP**, not CEP — a UXP port is a **rewrite, not a port** (new manifest, UXP
  Spectrum DOM client, async `batchPlay` host in modern ES6, `.ccx` packaging). **Native Apple-Silicon Photoshop
  can't run CEP at all** (Rosetta-only) — the AE/AI CEP trick doesn't carry over. Reusable across the boundary:
  the bridge protocol, JSON schema, geometry math, and most UX *thinking*; not reusable: the entire host.
- **CC Libraries** has no clean scripted "add to library" (the REST API is cloud/OAuth and closed to new
  third-party integrations; no reliable ExtendScript/CEP hook). Export **SVG/PNG** to a known folder instead.

Treat all of the above as *contextual* — verify the current state (UXP availability especially) per the freshness
protocol before relying on it.
