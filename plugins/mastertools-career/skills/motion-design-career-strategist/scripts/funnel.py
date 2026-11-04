#!/usr/bin/env python3
"""funnel.py - find where your job-application funnel leaks.

Usage:
    python3 funnel.py tracker.csv [--format markdown|json] [--today YYYY-MM-DD]
        [--stale-days 14] [--no-response-days 30] [--min-n 5]
        [--predictions predictions.json] [--expected rates.json]

Input is a CSV only (export spreadsheets to CSV first). Required columns:
company, role, channel, stage, status. Optional: level_target, posted_date,
applied_date, last_update, notes. Column names are case-insensitive.
Every report opens with a data check: rows skipped, labels interpreted, unreadable dates.
Active rows quiet for over --no-response-days count as "no response" at their stage (0 turns this off).
Python 3.8+, standard library only, no network.
"""
import argparse
import csv
import json
import math
import re
import sys
from datetime import date, datetime
from statistics import median

# Heuristic thresholds. All are rules of thumb, NOT measured benchmarks.
HEURISTICS = {
    "min_n": 5,             # heuristic: fewer resolved rows than this is too noisy to diagnose
    "stale_days": 14,       # heuristic: two weeks without news is the usual follow-up point
    "fast_apply_days": 3,   # heuristic: "applied early" means within 3 days of posting
    "min_bucket": 5,        # heuristic: need 5+ rows per speed bucket to compare them
    "channel_ratio": 2.0,   # heuristic: a 2x gap between channels is worth acting on
    "interval_z": 1.645,    # z for a two-sided 90% interval (math, not a benchmark)
    "low_n": 10,            # heuristic: below this, a leak call is labeled low-confidence
    "no_response_days": 30, # heuristic: an active row quiet this long is treated as no response (0 = off)
    "max_skipped_share": 0.10,  # heuristic: skip more than this share of rows and the diagnosis is withheld
    "clear_leak_ratio": 0.8,    # heuristic: within 20% of its reference, a stage is noise unless the interval excludes it
}

# Reference conversion per stage, so a stage is judged against what it normally converts: a low
# applied->screen rate (normal for cold applying) must not hide a weak hiring_manager->panel rate.
# Directional, tech-skewed vendor data (see references/search-operations.md §4), NOT benchmarks for
# any one employer. Override with --expected FILE.
EXPECTED_APPLIED_BY_CHANNEL = {
    "cold": 0.05,                # Ashby Q1 2026: 3.6-4.7% of applications reach interview; Gem 2024: 6% inbound to first screen
    "referral": 0.40,            # Ashby 2025: 40% of referred candidates reach interview
    "recruiter_inbound": 0.44,   # Gem 2025: 44% of sourced candidates reach first screen
    "recruiter_outreach": 0.20,  # heuristic: candidate-initiated recruiter contact, no published rate
    "hm_outreach": 0.20,         # heuristic: no published rate
    "other": 0.05,               # heuristic: treated like cold
}
EXPECTED = {
    "applied->recruiter_screen": None,         # computed from the channel mix (above)
    "recruiter_screen->hiring_manager": 0.55,  # heuristic split of Gem 2024: ~20% of inbound first screens reach onsite
    "hiring_manager->panel": 0.45,             # heuristic split (0.55 x 0.45 ~ 0.25 screen->panel)
    "panel->offer": 0.35,                      # Gem 2024: 35% of inbound onsites get offers
}

STAGES = ["applied", "recruiter_screen", "hiring_manager", "panel", "offer"]
CHANNELS = ["cold", "referral", "recruiter_inbound", "recruiter_outreach", "hm_outreach", "other"]
STATUSES = ["active", "rejected", "withdrawn", "ghosted", "accepted", "declined"]
REQUIRED = ["company", "role", "channel", "stage", "status"]

SYNONYMS = {
    "channel": {
        "cold": "cold", "applied": "cold", "website": "cold", "site": "cold", "job_board": "cold",
        "referral": "referral", "referred": "referral", "ref": "referral",
        "recruiter_inbound": "recruiter_inbound", "inbound": "recruiter_inbound",
        "recruiter_outreach": "recruiter_outreach", "recruiter_outbound": "recruiter_outreach",
        "hm_outreach": "hm_outreach", "hiring_manager_outreach": "hm_outreach",
        "other": "other",
    },
    "stage": {
        "applied": "applied", "application": "applied", "submitted": "applied", "sent": "applied",
        "applied_online": "applied",
        "screen": "recruiter_screen", "recruiter": "recruiter_screen", "recruiter_screen": "recruiter_screen",
        "phone_screen": "recruiter_screen", "phone": "recruiter_screen", "phone_interview": "recruiter_screen",
        "recruiter_call": "recruiter_screen", "recruiter_interview": "recruiter_screen",
        "intro_call": "recruiter_screen", "screening": "recruiter_screen", "hr_screen": "recruiter_screen",
        "initial_interview": "recruiter_screen", "first_interview": "recruiter_screen",
        "1st_interview": "recruiter_screen", "first_round": "recruiter_screen", "1st_round": "recruiter_screen",
        # A bare "interview" is read as the earliest interview stage; the data check asks to relabel if later.
        "interview": "recruiter_screen", "interviewing": "recruiter_screen",
        "hm": "hiring_manager", "hiring_manager": "hiring_manager", "hm_screen": "hiring_manager",
        "hm_interview": "hiring_manager", "hiring_manager_interview": "hiring_manager",
        "hiring_manager_screen": "hiring_manager", "manager_interview": "hiring_manager",
        "second_interview": "hiring_manager", "2nd_interview": "hiring_manager",
        "second_round": "hiring_manager", "2nd_round": "hiring_manager",
        "take_home": "hiring_manager", "design_exercise": "hiring_manager", "design_challenge": "hiring_manager",
        "panel": "panel", "onsite": "panel", "on_site": "panel", "loop": "panel", "final": "panel",
        "final_round": "panel", "final_interview": "panel", "finals": "panel", "virtual_onsite": "panel",
        "onsite_interview": "panel", "panel_interview": "panel",
        "portfolio_review": "panel", "portfolio_presentation": "panel",
        "offer": "offer", "offered": "offer", "offer_received": "offer", "offer_extended": "offer",
    },
    "status": {
        "active": "active", "open": "active", "in_progress": "active", "pending": "active",
        "waiting": "active", "submitted": "active", "applied": "active", "scheduled": "active",
        "under_review": "active", "in_review": "active", "reviewing": "active", "interviewing": "active",
        "in_process": "active",
        "rejected": "rejected", "closed": "rejected", "rejection": "rejected", "not_selected": "rejected",
        "not_moving_forward": "rejected", "position_filled": "rejected", "role_filled": "rejected",
        "withdrawn": "withdrawn", "withdrew": "withdrawn", "pulled_out": "withdrawn",
        "ghosted": "ghosted", "no_response": "ghosted", "no_reply": "ghosted", "no_answer": "ghosted",
        "accepted": "accepted", "hired": "accepted", "accepted_offer": "accepted",
        "declined": "declined", "declined_offer": "declined",
    },
}

# Channel words for labels that aren't an exact synonym ("Friend referral", "LinkedIn Easy Apply"); see norm_channel.
RECRUITER_ROOTS = ("recruit", "headhunter", "staffing", "talent")  # talent agencies act as recruiters in motion
HM_WORDS = ("hiring_manager", "design_manager", "head_of")
HM_TOKENS = {"hm", "director"}  # in motion, a creative or art director is usually the hiring manager
INBOUND_WORDS = ("to_me", "contacted_me", "messaged_me", "emailed_me", "found_me", "inbound")
FIRST_PERSON_OUTREACH = ("i_reached", "i_contacted", "i_messaged", "i_emailed", "i_dm", "i_wrote", "i_pinged")
OUTREACH_TOKENS = {"i", "messaged", "emailed", "dm", "dmed", "cold", "contacted", "wrote", "pinged", "outreach",
                   "outbound", "reached", "to"}  # checked only before the recruiter word
COLD_WORDS = ("cold", "appli", "apply", "linkedin", "indeed", "career", "company_site", "website",
              "job_board", "jobboard", "online", "glassdoor", "wellfound", "portal", "posting", "site", "agency")
COLD_TOKENS = {"direct", "directly"}
NEGATIONS = {"no", "not", "non", "didn", "didnt", "without"}

# Plain-words usual causes by leaking transition. Heuristics, not data.
LEAK_CAUSES = {
    "applied->recruiter_screen": "targeting, or materials at a glance (resume / LinkedIn / reel first seconds), or no warm path",
    "recruiter_screen->hiring_manager": "level or comp mismatch, or your story at recruiter level",
    "hiring_manager->panel": "scope or portfolio depth for the level",
    "panel->offer": "interview performance, or level calibration",
}


def key(text):
    return re.sub(r"[^a-z0-9]+", "_", (text or "").strip().lower()).strip("_")


SLASH_DATE = re.compile(r"^(\d{1,2})[/-](\d{1,2})[/-](\d{2}|\d{4})$")


DATE_FIELDS = ("posted_date", "applied_date", "last_update")


def date_order(raw_rows, day_first=False):
    """One slash-date order for the whole file: "day" when a first number over 12 proves it (or --day-first),
    "month" otherwise (US default), "mixed" when the file has proof of both.
    Returns (order, proven, the first day-first value that proves it)."""
    day = month = None
    for line_no, row in raw_rows:
        for f in DATE_FIELDS:
            text = (row.get(f) or "").strip()
            m = SLASH_DATE.match(text)
            if m:
                if day is None and int(m.group(1)) > 12:
                    day = {"line": line_no, "field": f, "raw": text}
                if month is None and int(m.group(2)) > 12:
                    month = {"line": line_no, "field": f, "raw": text}
    if day and month:
        return "mixed", True, day
    if day_first:
        return "day", True, None
    return ("day", True, day) if day else ("month", bool(month), None)


def parse_date(text, day_first=False):
    text = (text or "").strip()
    if re.match(r"^\d{4}-\d{2}-\d{2}[T ]", text):
        text = text[:10]  # ISO datetime: keep the date
    slash = ("%d/%m/%Y", "%d/%m/%y", "%d-%m-%Y") if day_first else ("%m/%d/%Y", "%m/%d/%y", "%m-%d-%Y")
    for fmt in ("%Y-%m-%d",) + slash + ("%Y/%m/%d", "%d %b %Y", "%d %B %Y",
                                        "%b %d, %Y", "%B %d, %Y", "%b %d %Y", "%B %d %Y"):
        try:
            return datetime.strptime(text, fmt).date()
        except ValueError:
            pass
    return None


def norm_channel(text):
    """Exact synonym first, then word hints in a fixed order. A negated channel ("No referral") isn't guessed;
    a negated status note inside the label ("Referral - no response") is ignored."""
    k = key(text)
    if k in SYNONYMS["channel"]:
        return SYNONYMS["channel"][k]
    tokens = k.split("_")
    for i, t in enumerate(tokens):
        nxt = tokens[i + 1:i + 4]  # "Not a referral", "Didn't use referral"
        if t in NEGATIONS and any("referr" in n or "recruit" in n or n in ("hm", "hiring", "cold") for n in nxt):
            return None
    if "referr" in k:
        return "cold" if "self" in tokens else "referral"
    rec = [i for i, t in enumerate(tokens) if any(t.startswith(w) for w in RECRUITER_ROOTS)]
    if rec:
        # Direction comes from word order: "Messaged recruiter" is outreach, "Recruiter messaged" is inbound.
        r = rec[0]
        before = tokens[:r]
        lead = [t for t in before if t not in ("a", "an", "the")][-1:]  # "by a recruiter" -> ["by"]
        if any(w in k for w in FIRST_PERSON_OUTREACH):
            return "recruiter_outreach"
        if any(w in k for w in INBOUND_WORDS) or lead in (["by"], ["from"]) or "me" in tokens[r + 1:]:
            return "recruiter_inbound"
        return "recruiter_outreach" if OUTREACH_TOKENS & set(before) else "recruiter_inbound"
    if HM_TOKENS & set(tokens) or any(w in k for w in HM_WORDS):
        return "hm_outreach"
    if any(w in k for w in COLD_WORDS) or COLD_TOKENS & set(tokens):
        return "cold"
    return None


def read_csv(path, encoding):
    """Return (fieldnames, [(line_no, row)]) with normalized column names and stripped values."""
    with open(path, newline="", encoding=encoding) as fh:
        reader = csv.DictReader(fh)
        fieldnames = [key(h) for h in (reader.fieldnames or [])]
        reader.fieldnames = fieldnames
        return fieldnames, [(line_no, {k: (v or "").strip() for k, v in raw.items() if k})
                            for line_no, raw in enumerate(reader, start=2)]


def load_rows(path, check=None, day_first=False):
    """Return (rows, warnings). Each row has normalized channel/stage/status and si (stage index).
    Rows keep their raw labels (raw_channel, raw_stage, raw_status), bad_dates and unsure_dates
    for the data check. Pass a dict as check to receive rows_read, the skipped rows and the date order."""
    if path.lower().endswith((".xlsx", ".xls")):
        raise SystemExit("error: this script reads CSV only. Export the sheet as CSV and try again.")
    try:
        fieldnames, raw_rows = read_csv(path, "utf-8-sig")
    except UnicodeDecodeError:
        fieldnames, raw_rows = read_csv(path, "cp1252")  # Excel on Windows saves CSV this way
    missing = [c for c in REQUIRED if c not in fieldnames]
    if missing:
        raise SystemExit("error: missing required column(s): " + ", ".join(missing))
    order, proven, day_proof = date_order(raw_rows, day_first)
    slash = sum(bool(SLASH_DATE.match(row.get(f) or "")) for _, row in raw_rows for f in DATE_FIELDS)
    rows, warnings, skipped, read = [], [], [], 0
    for line_no, row in raw_rows:
        if not any(row.values()):
            continue  # blank line
        read += 1
        norm = {"channel": norm_channel(row["channel"]),
                "stage": SYNONYMS["stage"].get(key(row["stage"])),
                "status": SYNONYMS["status"].get(key(row["status"]))}
        if norm["stage"] is None or norm["status"] is None:
            warnings.append("line %d skipped: unrecognized stage or status (%r, %r)"
                            % (line_no, row["stage"], row["status"]))
            skipped.append({"line": line_no, "company": row["company"], "stage": row["stage"],
                            "status": row["status"]})
            continue
        row.update(raw_channel=row["channel"], raw_stage=row["stage"], raw_status=row["status"])
        row.update(norm)
        if row["channel"] is None:
            row["channel"] = "other"
        row["si"] = STAGES.index(row["stage"])
        row["bad_dates"], row["unsure_dates"] = [], []
        for f in DATE_FIELDS:
            text = row.get(f, "")
            m = SLASH_DATE.match(text)
            value_day_first = order == "day"
            if m and order == "mixed":
                # Mixed file: a number over 12 settles each value; one that could be either is unsure.
                value_day_first = int(m.group(1)) > 12
                if int(m.group(1)) <= 12 and int(m.group(2)) <= 12 and m.group(1) != m.group(2):
                    row["unsure_dates"].append({"line": line_no, "field": f, "raw": text})
            row[f] = parse_date(text, value_day_first)
            if text and row[f] is None:
                row["bad_dates"].append({"line": line_no, "field": f, "raw": text})
        rows.append(row)
    if check is not None:
        check.update(rows_read=read, skipped=skipped, date_order=order if slash else None,
                     date_order_proven=proven, day_first_flag=bool(day_first), day_proof=day_proof)
    return rows, warnings


def last_activity(r):
    """last_update, else None. last_update wins even when older than applied_date: it records the last news.
    applied_date stands in only at the applied stage: a row that advanced had news after applying."""
    if r.get("last_update"):
        return r["last_update"]
    return r.get("applied_date") if r["si"] == 0 else None


def is_open(r):
    """Still waiting at its stage: active and not presumed no-response."""
    return r["status"] == "active" and not r.get("no_response")


def data_check(rows, check, no_response_days):
    """What the script read, skipped and interpreted, so a reader can trust (or fix) the numbers."""
    check = dict(check or {})
    skipped = check.get("skipped", [])
    read = check.get("rows_read", len(rows) + len(skipped))
    interpreted, defaulted = {}, {}
    for r in rows:
        for field in ("stage", "status", "channel"):
            raw = r.get("raw_" + field, r[field])
            if field == "channel" and norm_channel(raw) is None:
                defaulted[raw or "(blank)"] = defaulted.get(raw or "(blank)", 0) + 1
            elif key(raw) != r[field]:
                tag = (field, raw, r[field])
                interpreted[tag] = interpreted.get(tag, 0) + 1
    return {
        "rows_read": read, "rows_used": len(rows), "skipped": skipped,
        "skipped_share": (len(skipped) / read) if read else 0.0,
        "interpreted": [{"field": f, "raw": raw, "read_as": to, "count": n}
                        for (f, raw, to), n in sorted(interpreted.items())],
        "channel_defaulted_to_other": [{"raw": raw, "count": n} for raw, n in sorted(defaulted.items())],
        "unreadable_dates": [d for r in rows for d in r.get("bad_dates", [])],
        "date_order": check.get("date_order"), "date_order_proven": check.get("date_order_proven", True),
        "day_first_flag": check.get("day_first_flag", False), "day_proof": check.get("day_proof"),
        "unsure_dates": [d for r in rows for d in r.get("unsure_dates", [])],
        "active_without_dates": sum(r["status"] == "active" and last_activity(r) is None for r in rows),
        "presumed_no_response": sum(bool(r.get("no_response")) for r in rows),
        "no_response_days": no_response_days,
    }


def wilson(k, n, z):
    """Wilson score interval for k successes in n trials."""
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    return (max(0.0, centre - half), min(1.0, centre + half))


def group_stats(rows):
    """Per-stage counts. Conversion S->S+1 uses RESOLVED rows only: rows that reached S and
    either went further or are no longer open at S (open rows haven't had a chance yet; active rows
    quiet past no_response_days count as resolved, not advanced)."""
    stages = []
    for i, name in enumerate(STAGES):
        entry = {"stage": name, "reached": sum(r["si"] >= i for r in rows)}
        if i < len(STAGES) - 1:
            resolved = [r for r in rows if r["si"] > i or (r["si"] == i and not is_open(r))]
            k = sum(r["si"] > i for r in resolved)
            entry.update(n=len(resolved), k=k, rate=(k / len(resolved) if resolved else None))
        stages.append(entry)
    offers = [r for r in rows if r["si"] == len(STAGES) - 1]
    return {
        "rows": len(rows),
        "stages": stages,
        "offers": {"total": len(offers),
                   "accepted": sum(r["status"] == "accepted" for r in offers),
                   "declined": sum(r["status"] == "declined" for r in offers)},
    }


def trans_name(i):
    return "%s->%s" % (STAGES[i], STAGES[i + 1])


def speed(rows, hv):
    # Rows whose posted or applied date could be read either way stay out: a wrong guess inverts the buckets.
    rows = [r for r in rows if not {d["field"] for d in r.get("unsure_dates", [])} & {"posted_date", "applied_date"}]
    gaps = [(r["applied_date"] - r["posted_date"]).days for r in rows
            if r["posted_date"] and r["applied_date"] and r["applied_date"] >= r["posted_date"]]
    out = {"n_with_dates": len(gaps), "median_days": median(gaps) if gaps else None, "buckets": None}
    fast, slow = [], []
    for r in rows:
        if r["posted_date"] and r["applied_date"] and r["applied_date"] >= r["posted_date"]:
            if r["si"] > 0 or not is_open(r):  # resolved at applied
                bucket = fast if (r["applied_date"] - r["posted_date"]).days <= hv["fast_apply_days"] else slow
                bucket.append(r["si"] >= 1)
    if len(fast) >= hv["min_bucket"] and len(slow) >= hv["min_bucket"]:
        out["buckets"] = {"fast": {"k": sum(fast), "n": len(fast)}, "slow": {"k": sum(slow), "n": len(slow)}}
    return out


def diagnose(overall, groups, min_n, hv, dcheck=None):
    lines = {"min_n": min_n}
    cands = [(s["rate"], i, s) for i, s in enumerate(overall["stages"][:-1]) if s["n"] >= max(min_n, 1)]
    if dcheck and dcheck["skipped_share"] > hv["max_skipped_share"]:
        lines.update(status="data_problem", leak=None, message=(
            "Diagnosis withheld: %d of %d rows (%.0f%%) were skipped because their stage or status label "
            "wasn't recognized, so a diagnosis on the rest could name the wrong leak. Relabel them "
            "(stage: %s; status: %s) and rerun."
            % (len(dcheck["skipped"]), dcheck["rows_read"], 100 * dcheck["skipped_share"],
               ", ".join(STAGES), ", ".join(STATUSES))))
    elif not cands:
        lines.update(status="too_few", leak=None, message=(
            "Too few resolved applications to diagnose (need at least %d resolved at a stage). "
            "To collect: log every application with channel, furthest stage and status; "
            "add posted_date and applied_date; update status when you hear back." % max(min_n, 1)))
    else:
        exp = hv.get("expected", EXPECTED)
        scored = [(rate / exp[trans_name(i)] if exp.get(trans_name(i)) else rate, rate, i, s)
                  for rate, i, s in cands]
        def describe(ratio, rate, i, s):
            return {"transition": trans_name(i), "k": s["k"], "n": s["n"], "rate": rate,
                    "expected": exp.get(trans_name(i)), "ratio_to_expected": ratio,
                    "interval_90": list(wilson(s["k"], s["n"], hv["interval_z"])),
                    "low_confidence": s["n"] < hv["low_n"],
                    "likely_cause_heuristic": LEAK_CAUSES[trans_name(i)]}

        def clear_shortfall(d):
            # Clearly below its reference: 20%+ under it, or the whole 90% interval sits under it.
            ref = d["expected"]
            return d["ratio_to_expected"] <= hv["clear_leak_ratio"] or d["interval_90"][1] < ref

        # A stage with no reference rate (a user-supplied null or 0) can't be judged against one.
        described = sorted((describe(*x) for x in scored if exp.get(trans_name(x[2]))),
                           key=lambda d: d["ratio_to_expected"])
        clear = [d for d in described if clear_shortfall(d)]
        if not described:
            lines.update(status="too_few", leak=None, message="No stage with enough data has a reference rate "
                         "to compare against. Remove the null or 0 entries from --expected.")
        elif clear:
            worst = clear[0]
            lines.update(status="leak", leak=worst)
        else:
            worst = described[0]  # every eligible stage is at or near its reference: no leak to name
            lines.update(status="no_leak", leak=None, weakest=worst)
        raw_rate, raw_i, raw_s = min(cands)
        if lines["status"] == "leak" and raw_i != STAGES.index(lines["leak"]["transition"].split("->")[0]):
            lines["lowest_raw"] = {"transition": trans_name(raw_i), "k": raw_s["k"], "n": raw_s["n"],
                                   "rate": raw_rate, "expected": exp.get(trans_name(raw_i))}
    # channel comparison on applied -> recruiter_screen; none when skipped rows make the data untrustworthy
    elig = {c: g["stages"][0] for c, g in groups.items()
            if g["stages"][0]["n"] >= max(min_n, 1) and lines["status"] != "data_problem"}
    comps = []
    for hi, a in elig.items():
        for lo, b in elig.items():
            if hi != lo and a["rate"] > 0 and (b["rate"] == 0 or a["rate"] >= hv["channel_ratio"] * b["rate"]):
                comps.append({"better": hi, "worse": lo, "better_rate": a["rate"], "better_k": a["k"],
                              "better_n": a["n"], "worse_rate": b["rate"], "worse_k": b["k"], "worse_n": b["n"],
                              "ratio": (a["rate"] / b["rate"]) if b["rate"] else None})
    lines["channel_comparison"] = comps
    return lines


def check_predictions(path, overall, hv):
    with open(path, encoding="utf-8") as fh:
        preds = json.load(fh)
    out = []
    for name, expected in preds.items():
        parts = [SYNONYMS["stage"].get(key(p)) for p in name.split("->")]
        if len(parts) != 2 or None in parts or STAGES.index(parts[1]) != STAGES.index(parts[0]) + 1:
            raise SystemExit("error: prediction key %r must look like applied->recruiter_screen" % name)
        s = overall["stages"][STAGES.index(parts[0])]
        lo, hi = wilson(s["k"], s["n"], hv["interval_z"])
        entry = {"transition": "->".join(parts), "predicted": expected, "k": s["k"], "n": s["n"],
                 "observed": s["rate"], "interval_90": [lo, hi]}
        if s["n"] == 0:
            entry["verdict"] = "no resolved data yet"
        elif expected < lo or expected > hi:
            entry["verdict"] = "SURPRISE: your prediction is outside the 90% interval of what you observed"
        else:
            entry["verdict"] = "consistent: prediction is inside the 90% interval of what you observed"
        out.append(entry)
    return out


def analyze(rows, today, stale_days, min_n, predictions_path=None, expected=None,
            no_response_days=HEURISTICS["no_response_days"], check=None):
    hv = dict(HEURISTICS)
    hv["no_response_days"] = no_response_days
    rows = [dict(r) for r in rows]
    for r in rows:
        last = last_activity(r)
        r["quiet_days"] = (today - last).days if last else None
        # A slash date that could be day- or month-first never ages a row: the guess would change the numbers.
        unsure = {d["field"] for d in r.get("unsure_dates", [])}
        used = "last_update" if r.get("last_update") else "applied_date"
        r["no_response"] = bool(r["status"] == "active" and no_response_days and r["quiet_days"] is not None
                                and r["quiet_days"] > no_response_days and used not in unsure)
    hv["expected"] = dict(EXPECTED, **(expected or {}))
    by_ch = dict(EXPECTED_APPLIED_BY_CHANNEL, **((expected or {}).get("by_channel") or {}))
    hv["expected"].pop("by_channel", None)
    hv["expected_by_channel"] = by_ch
    channels = [c for c in CHANNELS if any(r["channel"] == c for r in rows)]
    groups = {c: group_stats([r for r in rows if r["channel"] == c]) for c in channels}
    overall = group_stats(rows)
    stale = []
    for r in rows:
        # Quiet days run from last_update, or applied_date at the applied stage (see last_activity).
        if r["status"] == "active" and r["quiet_days"] is not None and (r["quiet_days"] > stale_days
                                                                         or r["no_response"]):
            stale.append({"company": r["company"], "role": r["role"], "stage": r["stage"],
                          "days_since_update": r["quiet_days"], "counted_as_no_response": r["no_response"],
                          "suggestion": ("Counted as no response. Close it as ghosted, or update last_update "
                                         "if it's still moving" if r["no_response"] else
                                         "Send one follow-up now; if nothing in a week, close it as ghosted")})
    dcheck = data_check(rows, check, no_response_days)
    report = {
        "basis": ("Conversion S->next counts only resolved rows: reached S and either advanced or are no "
                  "longer active at S. Active rows haven't had a chance to convert yet, unless they've been "
                  "quiet for over %d days: those count as no response." % no_response_days
                  if no_response_days else
                  "Conversion S->next counts only resolved rows: reached S and either advanced or are no "
                  "longer active at S. Active rows haven't had a chance to convert yet."),
        "data_check": dcheck,
        "total_rows": len(rows), "today": str(today),
        "overall": overall, "by_channel": groups,
        "speed": speed(rows, hv), "stale": stale,
        "diagnosis": None,
    }
    if hv["expected"].get("applied->recruiter_screen") is None:
        n_tot = sum(g["stages"][0]["n"] for g in groups.values())
        hv["expected"]["applied->recruiter_screen"] = (
            sum(g["stages"][0]["n"] * by_ch.get(c, 0.05) for c, g in groups.items()) / n_tot if n_tot else 0.05)
    report["diagnosis"] = diagnose(overall, groups, min_n, hv, dcheck)
    report["channel_vs_reference"] = [
        {"channel": c, "k": g["stages"][0]["k"], "n": g["stages"][0]["n"], "rate": g["stages"][0]["rate"],
         "reference": by_ch.get(c)} for c, g in groups.items() if g["stages"][0]["n"]]
    if predictions_path:
        report["predictions"] = check_predictions(predictions_path, overall, hv)
    report["heuristics"] = hv
    return report


def pct(k, n):
    return "%d/%d (%.0f%%)" % (k, n, 100.0 * k / n) if n else "0/0 (n/a)"


def stage_table(g):
    out = ["| Stage | Reached | Converted to next (resolved only) |", "|---|---|---|"]
    for s in g["stages"]:
        out.append("| %s | %d | %s |" % (s["stage"], s["reached"], pct(s["k"], s["n"]) if "n" in s else "-"))
    o = g["offers"]
    if o["total"]:
        out.append("")
        out.append("Offers: %d total, %d accepted, %d declined." % (o["total"], o["accepted"], o["declined"]))
    return out


def render_data_check(dc):
    out = ["", "## Data check", ""]
    if dc["skipped"]:
        out.append("- Skipped %d of %d rows (unrecognized stage or status): %s. Relabel and rerun."
                   % (len(dc["skipped"]), dc["rows_read"], "; ".join(
                       "line %d %s (%r, %r)" % (s["line"], s["company"], s["stage"], s["status"])
                       for s in dc["skipped"][:8]) + ("; ..." if len(dc["skipped"]) > 8 else "")))
    if dc["interpreted"]:
        out.append("- Labels interpreted: %s. Check these; relabel any row that went further or sits in "
                   "the wrong channel."
                   % "; ".join("%s %r read as %s (%d)" % (x["field"], x["raw"], x["read_as"], x["count"])
                               for x in dc["interpreted"]))
    if dc["channel_defaulted_to_other"]:
        out.append("- Channel not recognized, counted as other: %s."
                   % "; ".join("%r (%d)" % (x["raw"], x["count"]) for x in dc["channel_defaulted_to_other"]))
    if dc["unreadable_dates"]:
        out.append("- Unreadable dates (ignored): %d, e.g. %s. Use YYYY-MM-DD."
                   % (len(dc["unreadable_dates"]), "; ".join(
                       "line %d %s %r" % (d["line"], d["field"], d["raw"]) for d in dc["unreadable_dates"][:3])))
    order = dc.get("date_order")
    if order == "day":
        p = dc.get("day_proof")
        out.append("- Slash dates read day-first (%s). If that line is a typo, fix it; use YYYY-MM-DD to be safe."
                   % ("--day-first" if dc["day_first_flag"] or not p else
                      "line %d %s %r can only be day-first" % (p["line"], p["field"], p["raw"])))
    elif order == "month" and not dc["date_order_proven"]:
        out.append("- Slash dates read month-first (US), but no date in the file proves the order. If you write "
                   "dates day-first, rerun with --day-first or switch to YYYY-MM-DD.")
    elif order == "mixed":
        out.append("- Slash dates mix day-first and month-first. %d date(s) that could be either were read "
                   "month-first; they never count as no response and stay out of the speed figures, e.g. %s. "
                   "Switch to YYYY-MM-DD and rerun."
                   % (len(dc["unsure_dates"]), "; ".join("line %d %s %r" % (d["line"], d["field"], d["raw"])
                                                         for d in dc["unsure_dates"][:3]) or "none"))
    if dc["active_without_dates"]:
        out.append("- %d active row(s) have no last_update (or, at applied, no applied_date), so they can "
                   "never count as no response. Add the dates." % dc["active_without_dates"])
    if dc["presumed_no_response"]:
        out.append("- %d active row(s) quiet for over %d days count as no response at their stage "
                   "(heuristic). They are marked in the stale list below."
                   % (dc["presumed_no_response"], dc["no_response_days"]))
    if len(out) == 3:
        out.append("All %d rows read with standard labels." % dc["rows_read"])
    return out


def render_markdown(rep):
    out = ["# Application funnel", "", "_%s_" % rep["basis"], "",
           "Rows analyzed: %d of %d read (as of %s)." % (rep["total_rows"], rep["data_check"]["rows_read"],
                                                         rep["today"])]
    out += render_data_check(rep["data_check"])
    out += ["", "## Overall", ""] + stage_table(rep["overall"])
    for c, g in rep["by_channel"].items():
        out += ["", "## Channel: %s (%d row(s))" % (c, g["rows"]), ""] + stage_table(g)
    sp = rep["speed"]
    out += ["", "## Speed", ""]
    if sp["median_days"] is None:
        out.append("No rows with both posted_date and applied_date.")
    else:
        out.append("Median days posted to applied: %s (n=%d)." % (sp["median_days"], sp["n_with_dates"]))
        b = sp["buckets"]
        if b:
            out.append("Response (reached a screen) when applied within %d days: %s; later: %s."
                       % (HEURISTICS["fast_apply_days"], pct(b["fast"]["k"], b["fast"]["n"]),
                          pct(b["slow"]["k"], b["slow"]["n"])))
        else:
            out.append("Response rate by speed: too few (need %d+ resolved rows in each bucket)."
                       % HEURISTICS["min_bucket"])
    out += ["", "## Stale active rows (no update for over %d days)" % HEURISTICS["stale_days"], ""]
    if rep["stale"]:
        for s in rep["stale"]:
            out.append("- %s, %s (%s): %d days quiet. %s." % (s["company"], s["role"], s["stage"],
                                                              s["days_since_update"], s["suggestion"]))
    else:
        out.append("None.")
    d = rep["diagnosis"]
    out += ["", "## Diagnosis (heuristics, not data; min n = %d)" % d["min_n"], ""]
    if d["status"] in ("too_few", "data_problem"):
        out.append(d["message"])
    elif d["status"] == "no_leak":
        w = d["weakest"]
        conf = " Low confidence: only %d resolved rows." % w["n"] if w.get("low_confidence") else ""
        if w["ratio_to_expected"] >= 1.0:
            out.append("No leak: every stage with at least %d resolved rows converts at or above its reference. "
                       "Closest to its reference: %s, %s against ~%.0f%%.%s"
                       % (d["min_n"], w["transition"], pct(w["k"], w["n"]), 100 * w["expected"], conf))
        else:
            out.append("No clear leak: the weakest stage, %s at %s, is within %.0f%% of its ~%.0f%% reference "
                       "and inside the 90%% range of what you observed (%.0f%%-%.0f%%). That gap is noise "
                       "at this sample size.%s"
                       % (w["transition"], pct(w["k"], w["n"]), 100 * (1 - HEURISTICS["clear_leak_ratio"]),
                          100 * w["expected"], 100 * w["interval_90"][0], 100 * w["interval_90"][1], conf))
    else:
        lk = d["leak"]
        exp_txt = (" against a reference of ~%.0f%%" % (100 * lk["expected"])) if lk.get("expected") else ""
        conf = " Low confidence: only %d resolved rows." % lk["n"] if lk.get("low_confidence") else ""
        out.append("Biggest leak (furthest below what this stage normally converts): **%s**, %s%s.%s "
                   "Usual causes (heuristic): %s."
                   % (lk["transition"], pct(lk["k"], lk["n"]), exp_txt, conf, lk["likely_cause_heuristic"]))
        if d.get("lowest_raw"):
            lr = d["lowest_raw"]
            out.append("- Lowest raw rate is %s at %s, but that stage normally converts low (reference ~%.0f%%)."
                       % (lr["transition"], pct(lr["k"], lr["n"]), 100 * (lr["expected"] or 0)))
    for c in rep.get("channel_vs_reference", []) if d["status"] != "data_problem" else []:
        if c["reference"] is not None and c["n"] >= max(d["min_n"], 1):
            ratio = (c["rate"] or 0) / c["reference"]
            verdict = "about normal for this channel" if 0.6 <= ratio <= 1.6 else (
                "below what this channel usually converts" if ratio < 0.6 else "above what this channel usually converts")
            out.append("- %s applied->screen %s vs a reference of ~%.0f%%: %s."
                       % (c["channel"], pct(c["k"], c["n"]), 100 * c["reference"], verdict))
    for c in d["channel_comparison"]:
        ratio = "%.1fx" % c["ratio"] if c["ratio"] else "versus zero screens"
        out.append("- Channel gap: %s converts applied->screen at %s vs %s at %s (%s)."
                   % (c["better"], pct(c["better_k"], c["better_n"]), c["worse"],
                      pct(c["worse_k"], c["worse_n"]), ratio))
    if rep["overall"]["offers"]["declined"]:
        out.append("- You declined offer(s): usual causes are negotiation or fit (heuristic).")
    if "predictions" in rep:
        out += ["", "## Predictions vs observed (90% Wilson interval on the observed rate)", "",
                "| Transition | Predicted | Observed | 90% interval | Verdict |", "|---|---|---|---|---|"]
        for p in rep["predictions"]:
            obs = pct(p["k"], p["n"])
            out.append("| %s | %.0f%% | %s | %.0f%%-%.0f%% | %s |" % (
                p["transition"], 100 * p["predicted"], obs, 100 * p["interval_90"][0],
                100 * p["interval_90"][1], p["verdict"]))
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Diagnose your job-application funnel from a CSV tracker.")
    ap.add_argument("tracker", help="tracker CSV (not xlsx)")
    ap.add_argument("--format", choices=["markdown", "json"], default="markdown")
    ap.add_argument("--stale-days", type=int, default=HEURISTICS["stale_days"])
    ap.add_argument("--no-response-days", type=int, default=HEURISTICS["no_response_days"],
                    help="active rows quiet longer than this count as no response (0 = off)")
    ap.add_argument("--day-first", action="store_true",
                    help="read slash dates as day/month/year (default: month first unless a date proves otherwise)")
    ap.add_argument("--today", help="YYYY-MM-DD (default: today)")
    ap.add_argument("--min-n", type=int, default=HEURISTICS["min_n"])
    ap.add_argument("--expected", help="JSON of reference rates per transition, overriding the built-in heuristics")
    ap.add_argument("--predictions", help="JSON of expected rates, e.g. {\"applied->recruiter_screen\": 0.15}")
    args = ap.parse_args(argv)
    today = parse_date(args.today) if args.today else date.today()
    if today is None:
        raise SystemExit("error: --today must be YYYY-MM-DD")
    if args.no_response_days < 0 or args.stale_days < 0 or args.min_n < 0:
        raise SystemExit("error: --no-response-days, --stale-days and --min-n must be 0 or more")
    HEURISTICS["stale_days"] = args.stale_days
    check = {}
    rows, warnings = load_rows(args.tracker, check, args.day_first)
    expected = None
    if args.expected:
        with open(args.expected, encoding="utf-8") as fh:
            expected = json.load(fh)
    rep = analyze(rows, today, args.stale_days, args.min_n, args.predictions, expected,
                  args.no_response_days, check)
    rep["warnings"] = warnings
    if args.format == "json":
        print(json.dumps(rep, indent=2))
    else:
        print(render_markdown(rep), end="")
        for w in warnings:
            print("warning: " + w, file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
