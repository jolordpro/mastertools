# Distribution & Signing

Volatility: MEDIUM (tooling breaks episodically). Stamp 2026-07-10.

## UXP plugins (.ccx)

- Package via UXP Developer Tool (or bolt-uxp's build) → `.ccx`; double-click installs through CC Desktop.
- Distribution channels: Adobe Marketplace/Exchange (review process), direct .ccx sharing (fine for internal tools), UPIA/CC Desktop for managed deploys.
- Marketplace review burden scales with permissions: `fullAccess`, `launchProcess`, `allowCodeGenerationFromStrings`, and hybrid addons all invite scrutiny — least-privilege manifests review faster and read safer.
- EU DSA note: Marketplace listings visible in the EU require publisher contact info in the profile (enforced since Feb 2025).

## UXP scripts (.psjs)

No packaging, no signing: a file. Run via double-click or File > Scripts. Internal distribution = your team's scripts library, wherever it is indexed.

## Hybrid addons — extra requirements (recap; details in hybrid-cpp-and-webview.md)

Sign + notarize the executables (real Apple Developer cert ≥1yr; Authenticode on Windows); admin credentials at install; ≤50 MB; all three architectures (Mac ARM / Mac Intel / Win Intel) mandatory for Marketplace.

## CEP panels (.zxp)

- Sign with **ZXPSignCmd 4.1.3+** (older builds segfault / fail timestamping):
```
ZXPSignCmd -selfsignedcert <country> <state> <org> "<common name>" <password> cert.p12        # dev cert
ZXPSignCmd -sign panelFolder panel.zxp cert.p12 <password> -tsa <timestamp-URL>  # ALWAYS -tsa
```
- **The `-tsa` timestamp is non-negotiable:** it extends signature validity past certificate expiry. Without it, the panel stops installing the day the cert expires, silently, in the field. TSA endpoints die periodically (GeoTrust/DigiCert SHA-1 sunsets) — if signing fails, try a current TSA URL before debugging anything else.
- Install paths: user (`~/Library/Application Support/Adobe/CEP/extensions` / `%APPDATA%\Adobe\CEP\extensions`), system (`/Library/Application Support/Adobe/CEP/extensions` / `C:\Program Files (x86)\Common Files\Adobe\CEP\extensions`), or ExManCmd/UPIA.
- **2024 UPIA symlink bug:** validly signed ZXPs installed via UPIA showed blank panels — workaround: install via host app as admin or ExManCmd; keep CC Desktop updated. (Verified — Adobe-CEP issues)
- Development bypass: **PlayerDebugMode = 1** (per CSXS version — `defaults write com.adobe.CSXS.12 PlayerDebugMode 1` / registry `HKCU\Software\Adobe\CSXS.12`) loads unsigned panels; also enables the `.debug` remote-debug ports. Never rely on it for distribution.

## Version pinning & compatibility

- UXP: manifest `host.minVersion` is the contract — set it to the lowest PS you actually test, not the lowest that parses. Feature-detect above the floor (`uxp.versions`, `uxp.host.version`).
- CEP: `<Host Version="[low,high]">` ranges; include PHXS and PHSP.
- LTS reality: managed machines may sit on PS 2025 LTS (26.x) while others run 27.x — test the floor, not just latest. Current values → `current-versions.md`.

## Internal distribution defaults

- .psjs/.jsx → the team's scripts library.
- Panels/plugins for a team → direct .ccx (UXP) with a one-line install note; skip Marketplace unless publishing publicly.
- Anything with a daemon or hybrid binary → document install steps in the team's SOPs; those don't fit in a .ccx and need their own installer story.
- Record new distributables wherever the team tracks its tools, so they're findable.
- A team overlay skill, when installed, sets the house rules here and wins over these defaults.
