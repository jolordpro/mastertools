# Shakedown — Code Reference

Layer-by-layer hunt checklists. Work the layers that exist in the build; skip
the ones that don't. Every item here is a question to answer against the
actual code, not a box to tick from memory. Locations or it didn't happen.

## Contents

1. Backend
2. Middleware / API layer
3. Frontend implementation
4. Seams — the vertical trace protocol
5. Workflows and pipelines
6. Dependencies
7. Security sub-pass
8. Tests and observability
9. Line-level pitfalls
10. What first passes miss (sweep list)

---

## 1. Backend

**Authorization, not just authentication.** The classic hole: login is
checked once, but individual endpoints don't verify the caller may act on
*this* resource. For every route that reads, mutates, or deletes: is there an
ownership/permission check on the resource itself? Pay special attention to
delete/update endpoints, ID-based lookups (can user A pass user B's ID?), and
admin routes.

**Input validation at the boundary.** Every external input — body, params,
query, headers, webhook payloads — validated for type, range, length, and
shape *before* use. Look for validation that exists on the frontend only.

**Injection.** Any query, command, or template built by string concatenation
from user input. Parameterized queries or a query builder throughout, or it's
a finding.

**Transactions and races.** Multi-step writes that must succeed or fail
together — are they in a transaction? Read-modify-write sequences on shared
state (counters, balances, inventory, seats) — what happens when two requests
interleave? Check-then-act patterns are race conditions until proven
otherwise.

**Idempotency.** Anything retriable (webhooks, payment confirms, job
processors, form resubmits): does a duplicate delivery create a duplicate
effect? Look for idempotency keys or natural-key upserts.

**Query patterns.** N+1s (a query inside a loop over query results).
Unbounded queries — every list endpoint needs pagination or a hard limit.
Missing indexes on columns used in hot WHERE/JOIN/ORDER BY (check the schema
against the queries).

**Error behavior.** Do error responses leak internals — stack traces, SQL,
file paths, dependency versions? Are errors swallowed silently (empty catch,
`.catch(() => {})`)? Does a failed downstream call return a coherent status
to the caller?

**Migrations and data safety.** Any destructive migration (drop, rename,
type change) — is there a rollback path? Is there a backup story before it
runs? Seed/fixture data that could ship to production?

**Configuration.** Secrets in the repo (see Security). Environment-specific
values hardcoded. Behavior that differs between dev and prod in ways the
build doesn't account for (TLS, proxies, case-sensitive filesystems).

## 2. Middleware / API layer

**Contract consistency.** For each endpoint the frontend consumes: does the
response actually match what the consumer expects — field names, casing,
nullability, types, date formats, enum values? This is checked for real in
the vertical trace (section 4); here, scan for the systemic version:
serializers that drift from the model, handwritten response shapes, `snake_
case` ↔ `camelCase` translation done inconsistently.

**Error shape consistency.** Do all endpoints return errors in one shape the
client can parse, or does each route improvise? A client that can't
distinguish 400-with-field-errors from 500-with-string is a client that shows
users nothing.

**Timeouts and retries.** Every outbound call to a third party: is there a
timeout? (No timeout = a hung dependency hangs the request, then the pool,
then the service.) Retries: bounded, with backoff, and only on idempotent
operations?

**Third-party failure modes.** For each external dependency (auth provider,
payment API, storage, email, webhook source): what does the build do when it
is down, slow, or returns garbage? "Crash" and "hang" are findings; "degrade
with a message" is the bar.

**Sessions and CORS.** Session/token expiry mid-flight — what does the user
experience? CORS configured deliberately (specific origins) or wildcarded?
Cookies: `HttpOnly`, `Secure`, `SameSite` set intentionally?

**Rate limiting.** On auth endpoints and anything expensive, at minimum.
Absence is a finding at Full tier for anything public-facing.

## 3. Frontend implementation

**The state matrix, per view.** Every data-driven view has at least six
states: loading, empty, populated, error, partial/degraded, and stale/
offline. Walk each significant view and check which states have actually been
built. Missing error states (fetch fails → silent blank screen) are the most
common seed of "it works on my machine, broke in the demo."

**Forms.** Validation on both sides (client for UX, server for truth).
Double-submit protection. What the user sees on server-side rejection — do
field errors map back to fields? Is entered data preserved on failure?

**Async correctness.** Race between navigations (response from screen A
arrives after user moved to screen B — is it discarded?). Unhandled promise
rejections. Optimistic updates: is there a rollback on failure, and does the
user learn the rollback happened?

**Browser reality.** Back button mid-flow. Deep link into a state that
assumes prior navigation. Hard refresh mid-wizard. Multiple tabs mutating the
same data. None of these are edge cases; all of them will happen in week one.

**State management.** Server state duplicated in local state that drifts.
Stale cache after mutations (is there invalidation?). Derived state computed
inconsistently in two places.

**Keys, memory, listeners.** List renders with unstable/index keys causing
state bleed. Event listeners and intervals without cleanup. Subscriptions
that outlive their component.

*(Experience-level frontend concerns — motion performance, accessibility,
perceived speed, first-run — live in `product.md`. Load both for anything
user-facing.)*

## 4. Seams — the vertical trace protocol

Per-layer checks catch per-layer bugs. Most production defects live between
layers. Run this on the 2–3 most critical journeys, demo path always
included:

1. **Pick the journey** and write its steps as the user experiences them.
2. **Walk the wire** for each step: interaction → event handler → request
   (method, path, payload) → middleware (auth, validation, transforms) →
   business logic → data layer → response → client state update → render.
3. **At every seam, check the contract:** field names and casing, types,
   nullability (does the client handle `null` where the server can produce
   it?), units (ms vs s, cents vs dollars), encodings, timezone handling,
   empty-vs-missing semantics (`[]` vs absent vs `null`).
4. **Trace the error path too.** Force (or trace) a failure at each layer
   and follow it forward: does it surface to the user as something
   actionable, or vanish into a console?
5. **Trace state assumptions.** Does step N read state that only some paths
   through step N−1 produce? Multi-step flows fail here.

Findings from the trace are usually High or Blocker — they sit on the paths
that matter most by definition.

## 5. Workflows and pipelines

Applies to automation chains, CI/CD, data pipelines, render pipelines,
content workflows, and multi-tool handoffs (including no-code/AI-agent
chains):

- **Partial failure.** The pipeline dies at step 3 of 6. What state is left
  behind? Can it resume, or does re-running duplicate steps 1–2's effects?
- **Handoff contracts.** Same seam discipline as section 4 — file formats,
  naming conventions, field expectations between tools.
- **Silent failure.** Who finds out when it breaks — a human via alert, or
  nobody until the output is missed? "Cron job that fails quietly" is a
  finding.
- **Ordering and concurrency.** Two runs overlap — do they collide? Is
  there a lock or a queue?
- **Poison inputs.** One malformed item — does it kill the whole batch or
  get quarantined and reported?

## 6. Dependencies

- Read the **actual manifest and lockfile** — audit pinned versions, not
  impressions of the library.
- Check pinned versions against known advisories (`npm audit` / `pip-audit`
  where executable; targeted web search on the exact version where not).
- Flag: end-of-life or unmaintained packages on critical paths, unpinned
  versions where builds must be reproducible, enormous dependencies pulled
  in for one function, licenses incompatible with the milestone (GPL in a
  proprietary client deliverable is a liability finding).
- The churn guard from SKILL.md governs recommendations: advisory, EOL, or
  named capability gain — otherwise silence.

## 7. Security sub-pass

Mandatory at Full tier. Beyond the items embedded above:

- **Secrets scan.** Keys, tokens, passwords, connection strings in the repo,
  in client-side code, in logs, in error output, in the git history if
  inspectable.
- **Authorization sweep.** Enumerate every route; mark each with its auth
  requirement; find the unmarked ones. (The single highest-yield security
  check in typical app code.)
- **Data handling.** What personal or client data is stored, where, for how
  long? Is anything sensitive logged? In transit encryption assumed or
  verified?
- **OWASP-class scan:** injection (checked above), broken access control
  (checked above), XSS (any user content rendered without
  escaping/sanitizing — check rich text and file names especially), SSRF
  (any server-side fetch of a user-supplied URL), insecure deserialization,
  file upload handling (type/size limits, storage outside webroot).
- **Client trust.** Anything security-relevant enforced only client-side
  (prices, roles, feature flags, validation) is a finding.

## 8. Tests and observability

- Does a test suite exist, does it run, does it pass — and what does it
  actually cover? A green suite covering 10% is coverage dishonesty in test
  form; say so.
- Are the risk concentrations (auth, money, mutation) tested at all?
- Can this build be debugged in production — logs with enough context,
  errors captured somewhere durable, health check endpoints? "It broke and
  we have no way to know why" is a Medium finding minimum at any milestone
  with real users.

## 9. Line-level pitfalls

The architecture checklists above miss bugs that live inside a single line.
Hunt these directly — in a delta audit, hunk by hunk; in a full audit, across
the risk concentrations. For every suspicious line ask: what input, state,
timing, or platform makes this line wrong?

**Universal:**

- Inverted or wrong conditions; off-by-one on boundaries the code doesn't
  exclude; wrong-variable copy-paste (two similar names, the wrong one used).
- Null/undefined dereference where nearby code shows the value can be
  absent; empty-vs-missing confusion (`[]` vs `null` vs absent key).
- Errors swallowed in a catch that should propagate; error paths that skip
  cleanup the happy path performs.
- Falsy-zero: `if (count)` treating a legitimate 0 (or empty string) as
  missing.
- Missing `await` / unawaited promise — the call succeeds, the result is a
  promise, the error vanishes.
- Unescaped regex metacharacters in patterns built from user input; regex or
  allowlist that lost its `^`/`$` anchor in an edit.
- Float equality; timezone/DST drift; unit mismatches (ms vs s, cents vs
  dollars) crossing a boundary.

**Language classics** (work the ones matching the stack):

- JS/TS: `==` coercion; closure-captured loop variables; `this` lost on
  method extraction; array `sort()` without a comparator on numbers.
- Python: mutable default arguments (evaluated once); late-binding closures
  in loops; bare `except:` swallowing `KeyboardInterrupt`.
- Go: nil-map writes; range-variable capture in goroutines; ignored `err`
  returns.
- SQL: injection via string building (see §1); `NULL` in `NOT IN` lists.

**Wrapper/proxy correctness.** Any type that wraps another (cache, proxy,
decorator, adapter): does every method route to the wrapped instance rather
than back through a registry/session/global (which re-enters the cache or
recurses)? Does the wrapper forward *all* the methods callers actually use,
or does a missed one silently bypass the wrapping behavior?

**Removed-behavior discipline** (delta audits and any recently refactored
zone): for every guard, check, or error path a change deleted or rewrote,
name the invariant it enforced and find where the new code re-establishes
it. Can't find it → candidate. Moved or extracted code drops guards more
often than new code forgets them.

## 10. What first passes miss (sweep list)

Steer the Sweep with these — the classic blind spots of a first pass that
worked the checklists honestly:

- **Moved/extracted code that dropped a guard or anchor** during a refactor
  — the diff looked like pure movement, the guard didn't survive the move.
- **Config defaults that differ between environments** — a flag flipped for
  dev convenience that ships flipped; behavior the build assumes is on.
- **Lock scope shrunk in an edit** — the critical section no longer covers
  the read-modify-write it was built for.
- **Second-tier footguns:** a default evaluated once and shared (Python
  dataclass/kwarg); ordering or `hash()` non-determinism leaking into
  output; predicate/getter methods with side effects.
- **Setup/teardown asymmetry in tests** — state one test leaks that makes a
  later test pass or fail for the wrong reason.
- **The second instance of a found bug** — every confirmed defect pattern
  gets one grep across the codebase; the same hands wrote the same bug
  twice.
- **Error paths added after the fact** that skip cleanup, logging, or state
  reset the happy path performs.
- **The unhappy half of new features** — the cancel, the retry, the
  mid-flow disconnect on the path everyone demoed forward-only.
