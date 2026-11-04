---
name: photoshop-scripting
description: Engineering reference and decision system for programming, scripting, and extending Adobe Photoshop. Use this skill whenever the user wants to automate, script, or extend Photoshop — UXP plugins or .psjs scripts, batchPlay, executeAsModal, the Imaging API, Photoshop ExtendScript (.jsx), CEP panel maintenance or CEP-to-UXP migration, C++ hybrid addons, UXP manifest and permissions questions, plugin packaging/signing/distribution, driving Photoshop externally (COM, AppleScript, Remote Connections, MCP servers), server-side automation via the Firefly Services Photoshop API, or reading/writing PSD files with external libraries (ag-psd, psd-tools, @webtoon/psd). Also use when debugging Photoshop scripting errors (modal state, batchPlay descriptors, permission denials) or choosing between any of these approaches. NOT for After Effects, Premiere, or other Adobe-app scripting (Photoshop only), and not for general Photoshop usage or image-editing technique questions.
---

# Photoshop Scripting & Extensibility

Decision system and engineering reference for automating and extending Adobe Photoshop across every runtime: UXP (plugins, .psjs scripts, C++ hybrid), ExtendScript, CEP, external drivers, out-of-app PSD libraries, and the Firefly Services cloud API.

**Knowledge as of: 2026-07-10.** This stamp represents `references/current-versions.md` (the volatile-facts file). Stable-grammar content (batchPlay syntax, executeAsModal semantics, manifest schema) decays slowly; version facts decay in weeks. Each reference file carries its own volatility tag.

## Precedence rule

Photoshop's extensibility landscape shifted rapidly through 2024–2026. Where background knowledge conflicts with these reference files, **the files win** within their as-of window — in particular, do not default to ExtendScript-first instincts or pre-2024 CEP advice from training data. Where a file is stale (stamp older than the current date by >30 days on volatile facts), verify before relying on it.

## Step 1 — Triage the task, then run the right preflight tier

Classify the request before doing anything else:

**Tier A — Architecture, migration, version-dependent, or "what should we build" decisions.**
Examples: "build a plugin/panel," "port our CEP panel," "should we use the cloud API," "does PS 27 support X," anything touching minVersion, distribution, or generative features.
→ Run the **full freshness preflight**: read `references/current-versions.md`, and if its stamp is >30 days old OR the decision hinges on a fact tagged ⚠ verify-at-preflight, check the canonical sources listed in `references/ecosystem-watchlist.md` (release notes, UXP changelog, Firefly deprecation page, CEP releases) before proposing anything. Escalation rule: re-plan if (a) shipping PS version moved the UXP baseline for a manifest minVersion, (b) an EOL date passed or was reconciled, (c) an API the plan depends on changed in a changelog, (d) a signing/distribution tool had a breaking release, (e) CEP got a runtime bump. Otherwise note and proceed.

**Tier B — Tactical work inside a known architecture.**
Examples: "write a batchPlay call that does X," "fix this modal-scope error," "add a permission to this manifest."
→ Stamp check only: note the knowledge-as-of date; proceed unless the task touches a ⚠-flagged fact.

**Tier C — Concept explanation.**
Examples: "explain what executeAsModal does," "what's the difference between UXP and CEP."
→ No preflight. Answer from the reference files directly.

**If web access is unavailable:** state the knowledge stamp, flag that volatile facts were not re-verified, and proceed with that caveat — never silently pretend freshness, and never refuse solely for lack of a preflight.

## Step 2 — Runtime selection (for Tier A tasks)

Walk this tree top-down; first match wins. Full rationale, version constraints, and the capability matrix live in `references/runtime-decision-matrix.md`.

1. **Server-side / headless / high volume / no desktop app available?** → **Firefly Services Photoshop API v2.** Only sanctioned headless surface; only sanctioned path for bulk generative work. (v1 EOL 2026 — see hard boundaries.)
2. **Rich interactive panel UI inside Photoshop, new project?** → **UXP plugin** (Spectrum Web Components for native look).
3. **Pixel-heavy / native-library / tight-loop compute with a modern UI?** → **UXP hybrid** (UXP + C++ `.uxpaddon`). Accept signing, notarization, tri-architecture, admin-install costs.
4. **A filter or file format that must appear in Photoshop's menus?** → **C++ SDK plugin** (classic, not hybrid).
5. **Batch file processing or logic-driven automation, no UI?** → **UXP script (.psjs)** for new work. ExtendScript (.jsx) only to maintain legacy code or reach an API that exists nowhere else.
6. **Pure repetitive GUI sequence, no logic?** → **Action + Droplet.** Survives upgrades better than code; zero distribution burden.
7. **Cross-app pipeline, AI-agent control, or external orchestration?** → **External driver**: COM (Windows), AppleScript (macOS), Remote Connections socket, or MCP-server bridge. BridgeTalk only within legacy ExtendScript.

**Holding a CEP panel today?** → `references/cep-capabilities-and-migration.md` for the migration tree. Short version: CEP 12 is the last major version, frozen on Chromium 99 / Node 17.7.1, and runs Rosetta-only in Photoshop on Apple Silicon — plan the UXP rewrite; it is a reconstruction, not a port.

## Hard boundaries (rule + why)

- **Never script the in-app, credit-based generative features (Generative Fill/Expand, Harmonize) for volume work.** Adobe's generative-credits FAQ states guardrails exist "to help prevent misuse like automatic scripting," and tripping them can restrict the user's account. Route bulk generative work to Firefly Services. Community-reverse-engineered generative batchPlay descriptors are additionally undocumented and unstable across releases — never present them as stable API.
- **Firefly Photoshop API v1 dies in 2026 and Adobe publishes two conflicting dates** (July 31 on the overview/v2-GA pages; August 31 on the deprecation page, notice dated April 20, 2026). Plan to the conservative July 31 date. Never build new work on v1.
- **All state-modifying UXP operations run inside `await core.executeAsModal(...)`** (apiVersion 2). Anything else fails silently or throws modal-scope errors. Group user-facing edits with history suspension so one script = one undo step.
- **Scripted exports must explicitly convert and embed the color profile** (convert to sRGB for web delivery). The Export As pathway has a documented history of profile mishandling; untagged wide-gamut output renders desaturated downstream.
- **Always timestamp ZXP signatures** (ZXPSignCmd 4.1.3+, working `-tsa`). Without a timestamp, installs break silently when the signing cert expires.
- **Manifest permissions are least-privilege.** Start from `assets/manifest-v5.template.json` (minimal permissions, commented escalation notes); add permissions only when the task requires them, and say why in the manifest comment.

## Output policy

Confidence labels (Verified / Reported / Uncertain, with ⚠ flags) live in the reference layer and shape recommendations — they do not leak wholesale into user-facing output. Surface at most one consolidated caveat when an Uncertain fact materially affects the answer. Never embed uncertainty markers or hedging comments inside generated code. If a task depends on a ⚠-flagged fact that cannot be verified right now, say so once, plainly, and offer the runtime probe that would settle it (e.g., `require("uxp").versions.uxp`).

## Interplay with other skills

- **Timing:** if a timing or instrumentation skill is installed, shell-runnable automation follows it. In-app scripts (.psjs/.jsx) can't run shell blocks: they self-time with epoch timestamps and print the runtime.
- Durable team knowledge produced while using this skill (new SOPs, spec facts, script entries) routes to the team's own knowledge base (a team overlay skill says where), not into these reference files. These files hold only Photoshop-platform knowledge.

## Routing table — read the file that matches the task

| Read this | When the task involves |
|---|---|
| `references/current-versions.md` | Any version-dependent decision; every Tier A preflight. The only file that states current shipping/beta/UXP/CEP versions. |
| `references/runtime-decision-matrix.md` | Choosing between runtimes; capability comparisons; the full decision-tree rationale. |
| `references/uxp-batchplay-cookbook.md` | Writing UXP code: batchPlay grammar, executeAsModal, history, Imaging API, feature detection, .psjs specifics. |
| `references/extendscript-legacy.md` | Maintaining .jsx: ES3 constraints, Action Manager, ScriptingListener, VS Code debugging, BridgeTalk. |
| `references/cep-capabilities-and-migration.md` | CEP panel work: what Chromium 99/Node 17 grants and lacks, CEP-to-UXP migration strategy. |
| `references/hybrid-cpp-and-webview.md` | C++ .uxpaddon authoring; WebView (WebView2/WKWebView split); Spectrum Web Components. |
| `references/firefly-services-api.md` | Cloud automation: v2 endpoints, v1→v2 migration, auth, cloud-vs-local capability split. |
| `references/psd-tooling-and-external-control.md` | Out-of-app PSD read/write; COM/AppleScript/Remote Connections/MCP; color-managed export rules. |
| `references/pitfalls-registry.md` | Debugging: symptom → cause → fix lookup. Read this FIRST for any error report. |
| `references/distribution-and-signing.md` | Packaging (.ccx/.zxp), signing, notarization, Marketplace review, installers. |
| `references/ecosystem-watchlist.md` | Preflight URLs + triage rule; people/repos/forums to consult for anything these files don't answer. |

Load one reference file per task where possible; the routing above is designed so most tasks need exactly one.
