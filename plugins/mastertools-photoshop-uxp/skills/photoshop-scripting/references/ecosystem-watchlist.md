# Ecosystem Watchlist & Preflight Sources

Volatility: LOW (the sources themselves are stable; what they report is not). Stamp 2026-07-10.

## Tier A preflight — canonical URLs and what to extract

| # | Source | Extract |
|---|---|---|
| 1 | helpx.adobe.com/photoshop/desktop/whats-new/photoshop-on-desktop-release-notes.html | Current shipping + LTS versions; scripting-relevant fixed/known issues |
| 2 | Photoshop Beta release notes (helpx, beta page) | Current beta build string; incoming UXP APIs/flags |
| 3 | developer.adobe.com/photoshop/uxp/ps_reference/changelog/ | New/changed/deprecated DOM, imaging, action APIs |
| 4 | AdobeDocs UXP versions table (uxp-api/versions3P) | Whether the UXP↔PS mapping finally extends past 8.1/26.1 |
| 5 | developer.adobe.com/firefly-services/docs/photoshop/ + .../getting-started/deprecation-announcement/ | v1 EOL date reconciliation (July 31 vs Aug 31, 2026); new v2 endpoints; beta→GA moves |
| 6 | github.com/Adobe-CEP/CEP-Resources (releases) | Any CEP point release; runtime bumps; ZXPSignCmd updates; removal-date news |
| 7 | forums.creativeclouddeveloper.com + community.adobe.com announcements | Beta build strings; regressions; deprecation signals |
| 8 | Release feeds: hyperbrew/bolt-uxp · jardicc/alchemist · @types/photoshop · Agamnentzar/ag-psd · psd-tools/psd-tools | Tooling drift that changes recommendations |

**Triage rule (escalate = re-plan; otherwise note and proceed).** Escalate when: (a) shipping PS moved the UXP baseline behind a manifest minVersion in play; (b) an EOL date passed or the v1 conflict was reconciled; (c) an API the current plan depends on was added/removed/deprecated; (d) ZXPSignCmd/UPIA/CC Desktop had a breaking release; (e) CEP got a runtime bump or a removal date. After any preflight that changes facts: update `current-versions.md`, bump its stamp and the SKILL.md stamp, repackage, reinstall (maintenance SOP lives in the repo README).

## Runtime probes (in-app, seconds each)

```js
require("uxp").versions.uxp      // exact UXP build — the authoritative mapping
require("photoshop").app.version // PS version
require("photoshop").core        // .isModal, .mainThreadTimeOutCount, .v8HeapSize
```

## People & venues (verified active as of 2026-07)

- **Davide Barranca** — davidebarranca.com; books/courses on PS panels & UXP ("Adobe UXP: Things you need to know" series). The deepest independent instructional source.
- **Jaroslav Bereza (jardicc)** — Alchemist (batchPlay inspector), vscode-uxp-validator, UXP debugger tooling.
- **Greg Benz** — gregbenzphotography.com; Lumenzia; the definitive CEP→UXP migration postmortems.
- **rendertom** — Clean SL (ScriptingListener log cleaner).
- **Hyper Brew** — bolt-uxp / bolt-cep boilerplates; active Discord.
- **bubblydoo/uxp-toolkit** — typesafe batchPlay (Zod), UTLayer fast tree parsing, UXP testing; their README doubles as a candid state-of-UXP field report.
- **Mike Chambers** — adb-mcp (agent control experiments).
- **Forums:** forums.creativeclouddeveloper.com (primary official UXP venue), ps-scripts.com (ExtendScript deep lore), Stack Overflow tags photoshop-script / extendscript / uxp.

## Key repos (starting nodes)

Adobe: AdobeDocs/uxp-photoshop (+ plugin-samples, issue tracker doubles as bug intel), Adobe-CEP/CEP-Resources, adobe-photoshop/generator-core, adobe-uxp/ps-es-to-uxp.
Community: hyperbrew/bolt-uxp, jardicc/alchemist, Agamnentzar/ag-psd, webtoon/psd, psd-tools/psd-tools, loonghao/photoshop-python-api, kyamagu/photoshop-connection.

## Skill self-maintenance pointers

- Anthropic skill format/rules: github.com/anthropics/skills + the platform skill-authoring best-practices doc — recheck when repackaging.
- This skill's source of truth is this plugin's source repo; an installed copy is a snapshot. Sync or reinstall as one step; tag releases.
