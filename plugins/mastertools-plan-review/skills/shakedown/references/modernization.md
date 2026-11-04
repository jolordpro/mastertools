# Shakedown — Modernization Reference

Moved word for word from SKILL.md §4 (2026-10-14). SKILL.md keeps a summary.

## Modernization research

Verify with real tools whether any part of the build is outdated or better
solved another way. Use search and fetch — do not vibe from memory; assume
training data is stale on anything fast-moving.

- Dependencies: check the **actual versions in the manifest/lockfile**
  against known advisories and end-of-life status. Not general impressions
  of the library — the pinned version.
- Patterns and approaches: has the technique been superseded? Is there now a
  purpose-built tool doing well what the build hand-rolls badly?
- Non-code: has the reference class moved since this was drafted? Are the
  benchmarks, examples, or standards cited still current?

**Churn guard.** A modernization suggestion makes the report only if it
clears one of three bars: (a) a security advisory or end-of-life on something
in use, (b) a *named* capability gain that matters to the milestone, or
(c) a maintenance cost being paid today that a swap demonstrably removes.
"Newer exists" is not a finding. Every claim of "the modern approach is X"
carries a source or it doesn't ship.
