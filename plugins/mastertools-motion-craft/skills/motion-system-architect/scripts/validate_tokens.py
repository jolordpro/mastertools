#!/usr/bin/env python3
"""validate_tokens.py - validate a DTCG-style motion token file (stdlib only).

Usage:
    python3 validate_tokens.py tokens.json [--strict] [--json] [--ns NAMESPACE]

Exit codes: 0 = no errors, 1 = errors found (or warnings under --strict),
            2 = file could not be read / parsed.

Conventions this validator assumes (see references/token-architecture.md):
  * Four tiers as top-level groups: primitive / semantic / component / choreography
    (an optional single wrapper group such as "motion" is tolerated).
  * DTCG 2025.10 value shapes: duration {"value": n, "unit": "ms"|"s"},
    cubicBezier [x1, y1, x2, y2], transition {duration, delay, timingFunction}.
    Legacy duration strings like "200ms" are accepted with a warning.
  * Aliases are "{group.token}" strings.
  * Motion semantics DTCG cannot express live in $extensions[NAMESPACE]:
    semanticRole, contexts, reducedMotion, modes, status, version, provenance,
    platformMappings, replacedBy, spring, stagger, sequence, pairsWith.
  * Duration and easing are coupled. Pairs bundled in a transition token, or
    declared with pairsWith (an alias or list of aliases on either token), get an
    exact snap check. Undeclared semantic durations and easings get a snap-risk
    sweep, because the validator cannot see which ones code combines.
"""
import argparse
import json
import re
import sys

DEFAULT_NS = "dev.motion-system"
TIERS = ("primitive", "semantic", "component", "choreography")
STATUSES = ("proposed", "experimental", "active", "preferred", "deprecated", "retired")
REDUCED_STRATEGIES = (
    "instant", "fade", "reduce-amplitude", "reduce-depth", "reduce-parallax",
    "tighten-spring", "remove-repetition", "state-only", "static",
)
STAGGER_ORDERS = ("forward", "reverse", "center-out", "edges-in")
MODE_TYPES = ("duration", "transition")  # types that must carry reduced + instant modes
ALIAS_RE = re.compile(r"^\{([^{}]+)\}$")
LEGACY_DURATION_RE = re.compile(r"^\s*(\d+(?:\.\d+)?)\s*(ms|s)\s*$")
DWELL_RE = re.compile(r"dwell|hold|read|timeout|linger|autodismiss|auto-dismiss")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


class Report:
    def __init__(self):
        self.items = []  # (level, path, message)

    def add(self, level, path, msg):
        item = (level, path, msg)
        if item not in self.items:  # one finding per distinct problem
            self.items.append(item)

    def error(self, path, msg):
        self.add("ERROR", path, msg)

    def warn(self, path, msg):
        self.add("WARN", path, msg)

    def house(self, path, msg):
        """House convention (this skill's discipline), not a DTCG spec error."""
        self.add("HOUSE", path, msg)

    def info(self, path, msg):
        self.add("INFO", path, msg)

    def count(self, level):
        return sum(1 for i in self.items if i[0] == level)


def is_alias(v):
    return isinstance(v, str) and ALIAS_RE.match(v.strip()) is not None


def alias_target(v):
    return ALIAS_RE.match(v.strip()).group(1).strip()


def is_num(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


class Tokens:
    """Flattens a DTCG tree into {dotted.path: token-dict}, inheriting group $type."""

    def __init__(self, data):
        self.tokens = {}
        self.groups = set()
        self.types = {}
        self._walk(data, [], None)

    def _walk(self, node, path, inherited_type):
        if not isinstance(node, dict):
            return
        gtype = node.get("$type", inherited_type)
        for key, child in node.items():
            if key.startswith("$"):
                continue
            if not isinstance(child, dict):
                continue
            cpath = path + [key]
            dotted = ".".join(cpath)
            if "$value" in child:
                self.tokens[dotted] = child
                self.types[dotted] = child.get("$type", gtype)
            else:
                self.groups.add(dotted)
                self._walk(child, cpath, gtype)


def tier_of(path):
    parts = path.split(".")
    if parts[0] in TIERS:
        return parts[0]
    if len(parts) > 1 and parts[1] in TIERS:
        return parts[1]
    return None


def ext_of(token, ns):
    ext = token.get("$extensions", {})
    return ext.get(ns, {}) if isinstance(ext, dict) else {}


class Validator:
    def __init__(self, data, ns):
        self.ns = ns
        self.t = Tokens(data)
        self.r = Report()
        self._resolved = {}

    # ---- alias resolution -------------------------------------------------
    def resolve_type(self, path, seen=None):
        """Return the effective $type of a token, following whole-token aliases."""
        seen = seen or []
        if path in seen:
            return None
        tok = self.t.tokens.get(path)
        if tok is None:
            return None
        declared = self.t.types.get(path)
        if declared:
            return declared
        v = tok.get("$value")
        if is_alias(v):
            return self.resolve_type(alias_target(v), seen + [path])
        return None

    def check_alias(self, owner, alias, expect_type=None, label="alias"):
        """Verify alias resolves, is acyclic and (optionally) has the expected type."""
        target = alias_target(alias)
        chain = [owner]
        cur = target
        while True:
            if cur in self.t.groups:
                self.r.error(owner, "%s %s points at a group, not a token" % (label, alias))
                return None
            if cur not in self.t.tokens:
                if cur == target:
                    self.r.error(owner, "%s %s does not resolve to any token" % (label, alias))
                else:
                    self.r.error(owner, "%s %s: chain broken, {%s} does not exist" % (label, alias, cur))
                return None
            if cur in chain:
                self.r.error(owner, "alias cycle: %s" % " -> ".join(chain + [cur]))
                return None
            chain.append(cur)
            v = self.t.tokens[cur].get("$value")
            if is_alias(v):
                cur = alias_target(v)
                continue
            break
        final = chain[-1]
        if expect_type:
            actual = self.resolve_type(final)
            if actual and actual != expect_type:
                self.r.error(owner, "%s %s resolves to $type %s, expected %s" % (label, alias, actual, expect_type))
        return final

    # ---- value shape checks ----------------------------------------------
    def duration_ms(self, owner, v, label="duration"):
        """Validate a duration value (inline or alias); return milliseconds or None."""
        if is_alias(v):
            final = self.check_alias(owner, v, "duration", label)
            if final:
                return self.duration_ms(final, self.t.tokens[final].get("$value"), label)
            return None
        if isinstance(v, dict):
            val, unit = v.get("value"), v.get("unit")
            if not is_num(val) or val < 0:
                self.r.error(owner, "%s: value must be a non-negative number, got %r" % (label, val))
                return None
            if unit not in ("ms", "s"):
                self.r.error(owner, "%s: unit must be 'ms' or 's', got %r" % (label, unit))
                return None
            return val * (1000.0 if unit == "s" else 1.0)
        if isinstance(v, str):
            m = LEGACY_DURATION_RE.match(v)
            if m:
                self.r.warn(owner, "%s: legacy string %r; DTCG 2025.10 uses {\"value\":n,\"unit\":\"ms\"}" % (label, v))
                n = float(m.group(1))
                return n * (1000.0 if m.group(2) == "s" else 1.0)
        self.r.error(owner, "%s: not a valid duration value: %r" % (label, v))
        return None

    def check_bezier(self, owner, v, label="cubicBezier"):
        if is_alias(v):
            final = self.check_alias(owner, v, "cubicBezier", label)
            if final:
                self.check_bezier(final, self.t.tokens[final].get("$value"), label)
            return
        if not (isinstance(v, list) and len(v) == 4 and all(is_num(x) for x in v)):
            self.r.error(owner, "%s: must be an array of 4 numbers, got %r" % (label, v))
            return
        if not (0 <= v[0] <= 1 and 0 <= v[2] <= 1):
            self.r.error(owner, "%s: x1 and x2 must be within [0,1], got x1=%s x2=%s" % (label, v[0], v[2]))

    def check_transition(self, owner, v, snap=True):
        """Return (duration_ms, raw_members) where raw_members counts inline literals."""
        raw = 0
        if is_alias(v):
            final = self.check_alias(owner, v, "transition", "transition")
            if final:
                return self.check_transition(final, self.t.tokens[final].get("$value"), snap)[0], 0
            return None, 0
        if not isinstance(v, dict):
            self.r.error(owner, "transition: $value must be an object {duration, delay, timingFunction}")
            return None, 0
        for req in ("duration", "timingFunction"):
            if req not in v:
                self.r.error(owner, "transition: missing '%s'" % req)
        if "delay" not in v:
            self.r.warn(owner, "transition: 'delay' absent (DTCG 2025.10 lists duration, delay, timingFunction)")
        dur = None
        if "duration" in v:
            dur = self.duration_ms(owner, v["duration"], "transition.duration")
            raw += 0 if is_alias(v["duration"]) else 1
        if "delay" in v:
            self.duration_ms(owner, v["delay"], "transition.delay")
            raw += 0 if is_alias(v["delay"]) else 1
        if "timingFunction" in v:
            self.check_bezier(owner, v["timingFunction"], "transition.timingFunction")
            raw += 0 if is_alias(v["timingFunction"]) else 1
            if snap:  # reduced/instant modes are deliberately minimal; judge the full mode only
                self.check_snap(owner, dur, v["timingFunction"])
        return dur, raw

    def follow(self, v, depth=0):
        """Resolve a whole-token alias chain to its literal $value (None if broken)."""
        while is_alias(v) and depth < 32:
            tok = self.t.tokens.get(alias_target(v))
            if tok is None:
                return None
            v, depth = tok.get("$value"), depth + 1
        return None if is_alias(v) else v

    def check_snap(self, owner, dur_ms, curve, fps=60.0, limit=0.4):
        """Perceptual check: a strong ease-out on a short duration lands most of its
        travel in the first frame and reads as a cut. Warn when frame 1 (at 60fps)
        already covers more than 40% of travel. Duration and curve are not independent."""
        c = self.follow(curve)
        if not dur_ms or dur_ms <= 0 or not (isinstance(c, list) and len(c) == 4 and all(is_num(x) for x in c)):
            return
        x1, y1, x2, y2 = c
        bz = lambda a, b, t: 3 * (1 - t) ** 2 * t * a + 3 * (1 - t) * t * t * b + t ** 3
        target = min(1.0, (1000.0 / fps) / dur_ms)
        lo, hi = 0.0, 1.0
        for _ in range(50):
            m = (lo + hi) / 2
            lo, hi = (m, hi) if bz(x1, x2, m) < target else (lo, m)
        p = bz(y1, y2, lo)
        if p > limit:
            self.r.warn(owner, "snap: %.0fms on cubic-bezier%s covers %.0f%% of travel in frame 1 at %dfps (reads as a cut). "
                        "Lengthen the duration or use a gentler curve for this tier." % (dur_ms, tuple(c), p * 100, fps))

    @staticmethod
    def frame1(c, dur_ms, fps=60.0):
        """Fraction of travel a cubic-bezier covers in the first frame."""
        x1, y1, x2, y2 = c
        bz = lambda a, b, t: 3 * (1 - t) ** 2 * t * a + 3 * (1 - t) * t * t * b + t ** 3
        target = min(1.0, (1000.0 / fps) / dur_ms)
        lo, hi = 0.0, 1.0
        for _ in range(50):
            m = (lo + hi) / 2
            lo, hi = (m, hi) if bz(x1, x2, m) < target else (lo, m)
        return bz(y1, y2, lo)

    def snap_floor(self, c, fps=60.0, limit=0.4):
        """Shortest duration (ms) at which the curve stays at or under the frame-1 limit."""
        lo, hi = 1000.0 / fps, 5000.0
        if self.frame1(c, hi, fps) > limit:
            return hi
        for _ in range(40):
            m = (lo + hi) / 2
            lo, hi = (lo, m) if self.frame1(c, m, fps) <= limit else (m, hi)
        return hi

    def check_pairs(self):
        """Snap checks outside transition tokens: declared pairs exactly, the rest as a risk sweep."""
        typ = lambda p: self.resolve_type(p)
        durs, eases, declared = {}, {}, set()
        for path, tok in self.t.tokens.items():
            if tier_of(path) not in ("semantic", "component"):
                continue
            t = typ(path)
            role = str(ext_of(tok, self.ns).get("semanticRole", "")) + " " + path.split(".")[-1]
            if t == "duration" and re.search(r"stagger|delay|interval|offset", role, re.I):
                continue  # gaps between items, not motion durations
            if t == "duration":
                ms = self.duration_ms(path, tok.get("$value"))
                if ms:
                    durs[path] = ms
            elif t == "cubicBezier":
                c = self.follow(tok.get("$value"))
                if isinstance(c, list) and len(c) == 4 and all(is_num(x) for x in c):
                    eases[path] = c
        for path, tok in self.t.tokens.items():
            pw = ext_of(tok, self.ns).get("pairsWith")
            if pw is None:
                continue
            items = pw if isinstance(pw, list) else [pw]
            if not all(is_alias(i) for i in items):
                self.r.error(path, "pairsWith must be an alias or a list of aliases")
                continue
            for i in items:
                other = alias_target(i)
                if other not in self.t.tokens:
                    self.r.error(path, "pairsWith %s does not resolve to any token" % i)
                    continue
                d, e = (path, other) if path in durs else (other, path)
                declared.update((path, other))
                if d in durs and e in eases:
                    self.check_snap("%s + %s" % (d, e), durs[d], eases[e])
        for e, c in sorted(eases.items()):
            if e in declared:
                continue
            floor = self.snap_floor(c)
            short = sorted((ms, d) for d, ms in durs.items() if d not in declared and ms < floor)
            if short:
                self.r.warn(e, "snap-risk: cubic-bezier%s reads as a cut below %.0fms (over 40%% of travel in frame 1 at 60fps). "
                            "Shorter durations in this file: %s. If code combines them, lengthen or use a gentler curve; "
                            "declare intended pairs with pairsWith to get an exact check." %
                            (tuple(c), floor, ", ".join("%s (%.0fms)" % (d, ms) for ms, d in short)))

    def check_value(self, path, ttype, value):
        """Dispatch by type; returns (duration_ms or None, raw_literal_count)."""
        if ttype == "duration":
            ms = self.duration_ms(path, value)
            return ms, (0 if is_alias(value) else 1)
        if ttype == "cubicBezier":
            self.check_bezier(path, value)
            return None, (0 if is_alias(value) else 1)
        if ttype == "transition":
            return self.check_transition(path, value)
        if is_alias(value):
            self.check_alias(path, value)
            return None, 0
        self.r.info(path, "$type %r is not validated by this script" % ttype)
        return None, 1

    # ---- extensions --------------------------------------------------------
    def check_spring(self, path, spring):
        if not isinstance(spring, dict):
            self.r.error(path, "spring extension must be an object")
            return
        has_phys = "stiffness" in spring and "damping" in spring
        has_perc = "duration" in spring and "bounce" in spring
        if not (has_phys or has_perc):
            self.r.error(path, "spring needs {stiffness, damping[, mass]} or {duration, bounce}")
            return
        if has_phys:
            for k in ("stiffness", "damping", "mass"):
                if k in spring and (not is_num(spring[k]) or spring[k] <= 0):
                    self.r.error(path, "spring.%s must be a positive number" % k)
        if has_perc:
            if not is_num(spring["duration"]) or spring["duration"] <= 0:
                self.r.error(path, "spring.duration must be a positive number (seconds)")
            if not is_num(spring["bounce"]) or not -1 < spring["bounce"] < 1:
                self.r.error(path, "spring.bounce must be a number in (-1, 1)")
        if "bounce" in spring and is_num(spring["bounce"]) and spring["bounce"] > 0.4:
            self.r.warn(path, "spring.bounce > 0.4 is playful; confirm the brand's anti-rules allow overshoot")

    def check_stagger(self, path, st):
        if not isinstance(st, dict):
            self.r.error(path, "stagger extension must be an object")
            return
        if "interval" not in st:
            self.r.error(path, "stagger needs 'interval' (duration value or alias)")
        else:
            self.duration_ms(path, st["interval"], "stagger.interval")
        if st.get("order", "forward") not in STAGGER_ORDERS:
            self.r.error(path, "stagger.order must be one of %s" % (STAGGER_ORDERS,))
        mi = st.get("maxItems")
        if mi is not None and not (isinstance(mi, int) and not isinstance(mi, bool) and mi > 0):
            self.r.error(path, "stagger.maxItems must be a positive integer")
        if "maxItems" not in st:
            self.r.warn(path, "stagger has no maxItems cap; long lists make total time unbounded")

    def check_sequence(self, path, seq):
        if not (isinstance(seq, list) and seq):
            self.r.error(path, "sequence must be a non-empty array of steps")
            return
        leads = 0
        for i, step in enumerate(seq):
            sp = "%s.sequence[%d]" % (path, i)
            if not isinstance(step, dict) or not is_alias(step.get("token", None)):
                self.r.error(sp, "each step needs a 'token' alias")
                continue
            self.check_alias(path, step["token"], None, "sequence step")
            if "offset" in step:
                self.duration_ms(path, step["offset"], "sequence.offset")
            if step.get("role") == "lead":
                leads += 1
        if leads != 1:
            self.r.warn(path, "sequence should have exactly one step with role 'lead' (found %d)" % leads)

    # ---- per-token ---------------------------------------------------------
    def check_token(self, path, tok):
        r = self.r
        tier = tier_of(path)
        ttype = self.resolve_type(path)
        ext = ext_of(tok, self.ns)
        value = tok.get("$value")

        if ttype is None:
            r.error(path, "no $type on token or enclosing group, and none inherited via alias")
        if isinstance(value, dict) and "$ref" in value:
            r.error(path, "'$ref' is not a DTCG alias; use \"{group.token}\" strings")

        full_ms, raw = (None, 0)
        if ttype is not None:
            full_ms, raw = self.check_value(path, ttype, value)

        if tier is None:
            r.warn(path, "token is outside the primitive/semantic/component/choreography tiers")

        # tier discipline
        whole_alias = is_alias(value)
        if tier == "primitive" and whole_alias:
            r.warn(path, "primitive tokens should hold literal values, not aliases")
        if tier == "semantic" and raw:
            r.warn(path, "semantic token contains %d raw literal(s); alias primitives so one scale change propagates" % raw)
        if tier == "component":
            if raw:
                r.error(path, "raw primitive value at component tier (%d literal(s)); alias a semantic token instead" % raw)
            elif whole_alias:
                tgt = alias_target(value)
                if tier_of(tgt) == "primitive":
                    r.warn(path, "component token aliases a primitive directly (%s); route through a semantic token" % tgt)
            else:
                members = value.values() if isinstance(value, dict) else []
                for m in members:
                    if is_alias(m) and tier_of(alias_target(m)) == "primitive":
                        r.warn(path, "component token aliases primitive %s directly; route through a semantic token" % alias_target(m))
        if tier == "choreography" and raw:
            r.warn(path, "choreography token contains raw literals; compose semantic/component tokens instead")

        # semantic metadata
        if tier == "semantic":
            if not ext.get("semanticRole"):
                r.house(path, "semantic token missing $extensions.%s.semanticRole" % self.ns)
            if not tok.get("$description"):
                r.warn(path, "semantic token has no $description (intent in one sentence)")
            if ttype in MODE_TYPES:
                self.check_modes(path, ttype, ext, full_ms)
                rm = ext.get("reducedMotion")
                if not isinstance(rm, dict) or rm.get("strategy") not in REDUCED_STRATEGIES:
                    r.house(path, "semantic %s token needs reducedMotion.strategy in %s" % (ttype, REDUCED_STRATEGIES))
            if not ext.get("contexts"):
                r.info(path, "semantic token lists no contexts (where it may be used)")
            if not ext.get("version"):
                r.info(path, "semantic token has no version")
            if not ext.get("provenance"):
                r.info(path, "semantic token has no provenance (owner / origin)")

        if "version" in ext and not (isinstance(ext["version"], str) and SEMVER_RE.match(ext["version"])):
            r.error(path, "version %r is not semver (MAJOR.MINOR.PATCH)" % (ext["version"],))

        # lifecycle
        status = ext.get("status")
        if tier in ("semantic", "component", "choreography") and status is None:
            r.info(path, "no status (one of %s)" % (STATUSES,))
        if status is not None and status not in STATUSES:
            r.error(path, "status %r not in %s" % (status, STATUSES))
        if status in ("deprecated", "retired"):
            if not tok.get("$deprecated"):
                r.error(path, "status is %s but DTCG $deprecated is not set" % status)
            rb = ext.get("replacedBy")
            if not rb:
                r.error(path, "%s token needs replacedBy (alias to successor) for migration" % status)
            elif not is_alias(rb):
                r.error(path, "replacedBy must be an alias string like \"{semantic.x}\"")
            else:
                self.check_alias(path, rb, None, "replacedBy")
        if tok.get("$deprecated") and status not in ("deprecated", "retired"):
            r.warn(path, "$deprecated set but status is %r" % (status,))

        # extensions
        if "spring" in ext:
            self.check_spring(path, ext["spring"])
        if "stagger" in ext:
            self.check_stagger(path, ext["stagger"])
        if "sequence" in ext:
            self.check_sequence(path, ext["sequence"])
        if "platformMappings" in ext and not isinstance(ext["platformMappings"], dict):
            r.error(path, "platformMappings must be an object keyed by platform")

        # active things must not depend on deprecated/retired ones
        if status in (None, "active", "preferred", "experimental", "proposed"):
            for target in self.referenced(value):
                tt = self.t.tokens.get(target)
                if tt is None:
                    continue
                ts = ext_of(tt, self.ns).get("status")
                if ts == "retired":
                    r.error(path, "references retired token %s" % target)
                elif ts == "deprecated":
                    r.warn(path, "references deprecated token %s; migrate" % target)

    def referenced(self, value):
        out = []
        if is_alias(value):
            out.append(alias_target(value))
        elif isinstance(value, dict):
            for v in value.values():
                if is_alias(v):
                    out.append(alias_target(v))
        return out

    def check_modes(self, path, ttype, ext, full_ms):
        modes = ext.get("modes")
        if not isinstance(modes, dict):
            self.r.house(path, "semantic %s token missing modes {reduced, instant}" % ttype)
            return
        mode_ms = {}
        for mode in ("reduced", "instant"):
            if mode not in modes:
                self.r.house(path, "modes.%s missing (every semantic %s token needs full/reduced/instant)" % (mode, ttype))
                continue
            mv = modes[mode]
            if ttype == "duration":
                mode_ms[mode] = self.duration_ms(path, mv, "modes.%s" % mode)
            else:
                mode_ms[mode], _ = self.check_transition(path, mv, snap=False)
        role = (str(ext.get("semanticRole", "")) + " " + path.split(".")[-1]).lower()
        if DWELL_RE.search(role):
            # Dwell is reading or decision time, not motion: reduced/instant must not shorten it.
            for mode in ("reduced", "instant"):
                if full_ms is not None and mode_ms.get(mode) is not None and mode_ms[mode] < full_ms:
                    self.r.warn(path, "modes.%s (%sms) shortens a dwell/reading time (%sms); reduced motion removes travel, not time to read or act" % (mode, mode_ms[mode], full_ms))
            return
        if mode_ms.get("instant") not in (None, 0):
            self.r.warn(path, "modes.instant duration is %sms; instant should be 0" % mode_ms["instant"])
        if full_ms is not None and mode_ms.get("reduced") is not None and mode_ms["reduced"] > full_ms:
            self.r.warn(path, "modes.reduced (%sms) is slower than full (%sms)" % (mode_ms["reduced"], full_ms))

    # ---- run ---------------------------------------------------------------
    def run(self):
        if not self.t.tokens:
            self.r.error("<file>", "no tokens found (a token is an object with $value)")
        for path in sorted(self.t.tokens):
            self.check_token(path, self.t.tokens[path])
        self.check_orphans()
        self.check_pairs()
        return self.r

    def check_orphans(self):
        """Primitives that nothing references are a token-cemetery signal."""
        used = set()
        for path, tok in self.t.tokens.items():
            ext = ext_of(tok, self.ns)
            for t in self.referenced(tok.get("$value")):
                used.add(t)
            for mv in (ext.get("modes") or {}).values():
                for t in self.referenced(mv):
                    used.add(t)
            if isinstance(ext.get("stagger"), dict) and is_alias(ext["stagger"].get("interval")):
                used.add(alias_target(ext["stagger"]["interval"]))
            for step in ext.get("sequence", []) if isinstance(ext.get("sequence"), list) else []:
                if isinstance(step, dict) and is_alias(step.get("token")):
                    used.add(alias_target(step["token"]))
            if is_alias(ext.get("replacedBy")):
                used.add(alias_target(ext["replacedBy"]))
        for path, tok in self.t.tokens.items():
            if tier_of(path) == "primitive" and path not in used:
                self.r.warn(path, "primitive is never referenced (token cemetery candidate)")


def render(report, path):
    lines = ["Motion token validation: %s" % path, ""]
    order = {"ERROR": 0, "HOUSE": 1, "WARN": 2, "INFO": 3}
    for level, p, msg in sorted(report.items, key=lambda i: (order[i[0]], i[1])):
        lines.append("  %-6s %s: %s" % (level, p, msg))
    lines.append("")
    lines.append("Summary: %d error(s) (DTCG/structure), %d house-convention gap(s), %d warning(s), %d note(s)" %
                 (report.count("ERROR"), report.count("HOUSE"), report.count("WARN"), report.count("INFO")))
    if report.count("HOUSE"):
        lines.append("House gaps are this skill's discipline (roles, modes, reduced-motion strategy), not spec violations; "
                     "the file can be valid DTCG with them. They fail this run because this skill's own deliverables must meet them; "
                     "when auditing someone else's file, report them separately from spec errors.")
    return "\n".join(lines)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Validate a DTCG motion token JSON file.")
    ap.add_argument("file")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    ap.add_argument("--ns", default=DEFAULT_NS, help="$extensions namespace (default %s)" % DEFAULT_NS)
    args = ap.parse_args(argv)
    try:
        with open(args.file, "r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError) as exc:
        sys.stderr.write("Cannot read %s: %s\n" % (args.file, exc))
        return 2
    if not isinstance(data, dict):
        sys.stderr.write("Top-level JSON value must be an object\n")
        return 2
    report = Validator(data, args.ns).run()
    if args.json:
        print(json.dumps({
            "file": args.file,
            "errors": report.count("ERROR"),
            "house": report.count("HOUSE"),
            "warnings": report.count("WARN"),
            "items": [{"level": l, "path": p, "message": m} for l, p, m in report.items],
        }, indent=2))
    else:
        print(render(report, args.file))
    failed = report.count("ERROR") + report.count("HOUSE") > 0 or (args.strict and report.count("WARN") > 0)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
