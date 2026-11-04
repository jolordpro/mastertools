#!/usr/bin/env python3
"""scan_postings.py - pull live job postings straight from employers' public job-board APIs.

Why: a career advisor should work from raw postings (title, posted pay range, date, URL),
not from digested salary summaries. This script needs only Python 3.8+ (standard library).
No logins, no secrets, public JSON endpoints only.

Sources (board spec on the command line / "type" in boards.json):
  greenhouse:{token}                         e.g. greenhouse:figma
  ashby:{org}                                e.g. ashby:openai
  lever:{company}                            e.g. lever:spotify
  eightfold:{host}:{domain}                  e.g. eightfold:explore.jobs.netflix.net:netflix.com
  workday:{tenant}:{wdN}:{site}              e.g. workday:adobe:wd5:external_experienced

Examples:
  python3 scan_postings.py                                   # all boards in boards.json, markdown
  python3 scan_postings.py --boards ashby:openai lever:spotify --min-pay 200000
  python3 scan_postings.py --format json --out run.json --save-raw raw/   # reproducible run
  python3 scan_postings.py --from-dir raw/ --format csv                    # offline replay

Saved raw files (--save-raw writes them, --from-dir reads them), one per board:
  greenhouse_{token}.json  ashby_{org}.json  lever_{company}.json
  eightfold_{host}_{domain}.json  workday_{tenant}_{site}.json
Search-style sources (eightfold, workday) and greenhouse also keep a "_details" key holding the
per-job detail responses fetched for title-matched jobs only. Boards without a saved file are skipped.

Pay: structured API fields are used when present (pay_basis=structured), otherwise the pay range is
parsed from the posting text (parsed_text), otherwise pay fields stay empty (none). Never invented.
"""
import argparse
import csv
import html
import io
import json
import os
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
TIMEOUT = 20
HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_TITLE = r"\b(motion|animat\w*|design technologist|creative technologist|prototyp\w*)\b"
# Server-side search queries for sources that need one (eightfold, workday); title regex filters after.
SEARCH_QUERIES = ["motion", "animation", "creative technologist", "design technologist", "prototype"]
DEFAULT_TERMS = ("After Effects, Cinema 4D, Redshift, Houdini, Blender, Unreal, Unity, Rive, Lottie, "
                 "SwiftUI, Jetpack Compose, Framer, ProtoPie, Origami, Figma, JavaScript, React, GSAP, "
                 "Three.js, WebGL, shader, prototype, motion system, design system, tokens, spring, "
                 "accessibility, reduced motion, AI, generative, live, broadcast, sports, brand, campaign, "
                 "product, UI, interaction, 3D, real-time, MOGRT, expressions, toolkit, template").split(", ")
HOURS_PER_YEAR = 2080
# Titles dropped by default: engineering and ops roles that share words like "animation" or
# "prototyping", and studio names inside titles ("..., Animation Studios"). --exclude-title "" keeps all.
DEFAULT_EXCLUDE = (r"\b(engineer\w*|technician|programmer|developer|scientist|researcher|recruiter|"
                   r"counsel|accountant|analyst)\b|^(?!.*\b(motion|animators?)\b).*\banimation stu\w*os\b")


class TitleFilter:
    """Include regex minus exclude regex, with the .search() interface the fetchers expect."""

    def __init__(self, include, exclude=""):
        self.include = re.compile(include, re.I)
        self.exclude = re.compile(exclude, re.I) if exclude else None

    def search(self, title):
        if self.exclude and self.exclude.search(title or ""):
            return None
        return self.include.search(title or "")


# ---------------------------------------------------------------- network
def http_json(url, data=None):
    """GET (or POST when data is a dict) and parse JSON. One retry on failure."""
    headers = {"User-Agent": UA, "Accept": "application/json"}
    body = None
    if data is not None:
        body = json.dumps(data).encode()
        headers["Content-Type"] = "application/json"
    last = None
    for _ in range(2):
        try:
            req = urllib.request.Request(url, data=body, headers=headers)
            with urllib.request.urlopen(req, timeout=TIMEOUT) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001 - captured per board by the caller
            last = e
    raise last


# ---------------------------------------------------------------- text helpers
def to_text(s):
    """HTML (possibly HTML-escaped HTML) -> plain text with collapsed whitespace."""
    if not s:
        return ""
    if "&lt;" in s and "<" not in s:
        s = html.unescape(s)
    s = re.sub(r"(?i)<\s*(br|/p|/li|/div|/h\d|/tr)\b[^>]*>", " ", s)
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


_LEVELS = [("Intern", r"\bintern(ship)?\b"), ("Junior", r"\b(junior|jr\.?|entry[- ]level)\b"),
           ("Head", r"\bhead of\b"), ("Director", r"\bdirector\b"), ("Principal", r"\bprincipal\b"),
           ("Staff", r"\bstaff\b"), ("Manager", r"\bmanager\b"), ("Lead", r"\blead\b"),
           ("Senior", r"\b(senior|sr\.?)(?=\W|$)"), ("Mid", r"\bmid(-level)?\b")]


def level_hint(title):
    for name, rx in _LEVELS:
        if re.search(rx, title or "", re.I):
            return name
    return "None"


def term_regex(term):
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(term) + r"(?![A-Za-z0-9])", re.I)


def find_terms(text, terms):
    return [t for t in terms if term_regex(t).search(text)]


# ---------------------------------------------------------------- pay parser
_CUR = r"(?:USD|CAD|EUR|GBP|AUD|US\$|C\$|\$|£|€)"
_NUM = r"\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?"


def _amt(i):
    return (r"(?:(?P<c%d>%s)\s?)?(?P<n%d>%s)\s?(?P<k%d>[kK])?(?!\w)(?!,\d)(?!\.\d)" % (i, _CUR, i, _NUM, i))


_RANGE = re.compile(_amt(1) + r"\s*(?:-|\bto\b)\s*" + _amt(2) + r"(?:\s?(?P<t>USD|CAD|EUR|GBP|AUD)\b)?", re.I)
_CODES = {"$": "USD", "US$": "USD", "USD": "USD", "C$": "CAD", "CAD": "CAD", "£": "GBP", "GBP": "GBP",
          "€": "EUR", "EUR": "EUR", "AUD": "AUD"}
_NOT_PAY = re.compile(r"bonus|equity|stock|rsu|relocat|stipend|commission|funding|raised", re.I)


def _interval(before, after):
    if re.search(r"(/\s?h(ou)?r|per hour|an hour|hourly)", after, re.I) or re.search(r"hourly|per hour", before, re.I):
        return "hour"
    if re.search(r"(/\s?mo\b|per month|monthly|a month)", after, re.I):
        return "month"
    return "year"


def parse_pay(text):
    """Find pay ranges in free text. Returns dict(min,max,currency,interval,text) or None.

    Several ranges (location zones) -> widest min..max of the most common currency/interval group,
    all snippets listed in `text`. Requires a currency marker so '2020-2024' or '401(k)' never count.
    """
    t = re.sub(r"[‐-―−]", "-", text or "")
    found = []
    for m in _RANGE.finditer(t):
        cur = m.group("c1") or m.group("c2") or m.group("t")
        if not cur:
            continue
        a, b = float(m.group("n1").replace(",", "")), float(m.group("n2").replace(",", ""))
        ka, kb = m.group("k1"), m.group("k2")
        if kb and not ka and a < b:
            ka = kb  # "$150-200k"
        a, b = a * (1000 if ka else 1), b * (1000 if kb else 1)
        before, after = t[max(0, m.start() - 30):m.start()], t[m.end():m.end() + 30]
        if _NOT_PAY.search(before):
            continue
        interval = _interval(before, after)
        if a > b:
            continue
        ok = {"hour": 7 <= a and b <= 2000, "month": 1500 <= a and b <= 200000,
              "year": 20000 <= a and b <= 5000000}[interval]
        if not ok:
            continue
        snippet = t[max(0, m.start() - 25):m.end() + 15].strip()
        found.append((_CODES.get(cur.upper(), "USD"), interval, a, b, snippet))
    if not found:
        return None
    groups = {}
    for f in found:
        groups.setdefault((f[0], f[1]), []).append(f)
    key = max(groups, key=lambda k: (len(groups[k]), k[1] == "year"))
    g = groups[key]
    snippets = " | ".join(x[4] for x in g)
    return {"min": min(x[2] for x in g), "max": max(x[3] for x in g), "currency": key[0], "interval": key[1],
            "text": snippets[:160]}


def annual(value, interval):
    if value is None:
        return None
    return value * {"hour": HOURS_PER_YEAR, "month": 12}.get(interval, 1)


def _interval_word(s):
    s = (s or "").lower()
    return "hour" if "hour" in s else "month" if "month" in s else "year"


# ---------------------------------------------------------------- normalizer
def make_record(company, source, title, location, remote, date, date_kind, url, pay, text, terms):
    pay = pay or {}
    remote, remote_ev = remote if isinstance(remote, tuple) else (remote, "")
    pmin, pmax = pay.get("min"), pay.get("max")
    return {
        "company": company, "source": source, "title": (title or "").strip(), "level_hint": level_hint(title),
        "location": (location or "").strip(), "remote": remote, "remote_evidence": remote_ev, "date": date, "date_kind": date_kind, "url": url,
        "pay_min": pmin, "pay_max": pmax, "pay_currency": pay.get("currency"), "pay_interval": pay.get("interval"),
        "pay_basis": pay.get("basis", "none") if pay else "none", "pay_text": (pay.get("text") or "")[:160] or None,
        "terms": find_terms((title or "") + " \n " + text, terms),
        "_pay_max_annual": annual(pmax, pay.get("interval")),
    }


def pay_from_text(text):
    p = parse_pay(text)
    if p:
        p["basis"] = "parsed_text"
    return p


def iso_date(v):
    """ISO string / epoch seconds / epoch ms -> YYYY-MM-DD or None."""
    try:
        if isinstance(v, (int, float)) or (isinstance(v, str) and v.isdigit()):
            n = float(v)
            n = n / 1000 if n > 1e11 else n
            return datetime.fromtimestamp(n, timezone.utc).strftime("%Y-%m-%d")
        if v:
            return str(v)[:10]
    except Exception:  # noqa: BLE001
        pass
    return None


_TEXT_ONSITE = re.compile(
    r"(\b(?:\d|one|two|three|four|five)\s+days?\s+(?:a|per|each|in)\s+(?:week\s+)?(?:in|at)?\s*(?:the\s+)?office"
    r"|\bhybrid (?:work )?(?:model|schedule|role|position)\b"
    r"|\b(?:role|position|job) is (?:primarily |currently )?(?:based|located) (?:in|at) [A-Z]"
    r"|\bin[- ]office (?:\d|days|requirement|presence))", re.I)
_TEXT_REMOTE = re.compile(r"\b(?:(?:role|position|job) is (?:fully |100% )?remote|fully remote|remote[- ]first"
                          r"|work remotely|remote within)\b", re.I)


def _evidence(text, m):
    return re.sub(r"\s+", " ", text[max(0, m.start() - 35):m.end() + 60]).strip()[:120]


def remote_flag(location, hint=None, text="", flag=None, weak_hint=False):
    """Decide remote -> (True | False | 'conflict' | 'unknown', evidence <=120 chars).

    Structured evidence: `flag` (an isRemote boolean), `hint` (workplace type string), a 'remote' in the
    location. It is then checked against the posting text (in-office days, 'based in <City>', 'fully remote').
    'conflict' means structured and text (or two structured fields) disagree. weak_hint: the hint is a
    default-ish field (Netflix work_location_option) that a remote location text outranks.
    """
    h = (hint or "").lower().replace("-", "")
    loc_remote = "remote" in (location or "").lower()
    s_remote = bool(flag) or h == "remote" or loc_remote
    s_onsite = h in ("onsite", "hybrid")
    if weak_hint and loc_remote:
        s_onsite = False
    on, rem = _TEXT_ONSITE.search(text or ""), _TEXT_REMOTE.search(text or "")
    if s_remote and s_onsite:
        ev = "fields disagree: isRemote=%s workplaceType=%s" % (flag, hint)
        return "conflict", (ev + "; text: " + _evidence(text, on) if on else ev)[:120]
    if s_remote:
        if on and not rem:
            return "conflict", "flag says remote; text: " + _evidence(text, on)
        return True, ("isRemote flag" if flag else "workplaceType" if h == "remote" else "location") + (
            "; text: " + _evidence(text, rem) if rem else "")
    if s_onsite:
        if rem and not on:
            return "conflict", "workplaceType=%s; text: %s" % (hint, _evidence(text, rem))
        return False, "workplaceType=%s" % hint
    if on and not rem:
        return False, "text: " + _evidence(text, on)
    if rem and not on:
        return True, "text: " + _evidence(text, rem)
    return "unknown", ""


# ---------------------------------------------------------------- per-source: fetch raw, then normalize
def fetch_greenhouse(spec, title_re, get=http_json):
    base = "https://boards-api.greenhouse.io/v1/boards/%s" % spec["token"]
    raw = get(base + "/jobs?content=true")
    raw["_details"] = {}
    for j in raw.get("jobs", []):  # single-job endpoint exposes structured pay_input_ranges; matched jobs only
        if title_re.search(j.get("title", "")):
            try:
                raw["_details"][str(j["id"])] = get("%s/jobs/%s?pay_transparency=true" % (base, j["id"]))
            except Exception:  # noqa: BLE001 - fall back to parsing the content text
                pass
    return raw


def norm_greenhouse(spec, raw, title_re, terms):
    out, seen = [], raw.get("jobs", [])
    for j in seen:
        if not title_re.search(j.get("title", "")):
            continue
        d = (raw.get("_details") or {}).get(str(j.get("id")), {})
        text = to_text(j.get("content") or d.get("content"))
        pay = None
        ranges = [r for r in (d.get("pay_input_ranges") or []) if r.get("min_cents") and r.get("max_cents")]
        if ranges:
            lo, hi = min(r["min_cents"] for r in ranges) / 100, max(r["max_cents"] for r in ranges) / 100
            pay = {"min": lo, "max": hi, "currency": ranges[0].get("currency_type", "USD"), "interval": "year",
                   "basis": "structured",
                   "text": "; ".join("%s %s-%s %s" % (r.get("title", "").strip(), r["min_cents"] // 100,
                                                       r["max_cents"] // 100, r.get("currency_type", ""))
                                     for r in ranges)}
        else:
            pay = pay_from_text(text)
        loc = (j.get("location") or {}).get("name", "")
        pub = j.get("first_published")
        out.append(make_record(spec["company"], "greenhouse", j["title"], loc, remote_flag(loc, text=text),
                               iso_date(pub or j.get("updated_at")), "published" if pub else "updated",
                               j.get("absolute_url"), pay, text, terms))
    return out, len(seen)


def fetch_ashby(spec, title_re, get=http_json):
    return get("https://api.ashbyhq.com/posting-api/job-board/%s?includeCompensation=true" % spec["token"])


def _ashby_pay(job):
    comp = job.get("compensation") or {}
    comps = list(comp.get("summaryComponents") or [])
    for tier in comp.get("compensationTiers") or []:
        comps += tier.get("components") or []
    sal = [c for c in comps if c.get("compensationType") == "Salary" and c.get("minValue") is not None
           and c.get("maxValue") is not None]
    if sal:
        return {"min": min(c["minValue"] for c in sal), "max": max(c["maxValue"] for c in sal),
                "currency": sal[0].get("currencyCode", "USD"), "interval": _interval_word(sal[0].get("interval")),
                "basis": "structured", "text": comp.get("compensationTierSummary") or ""}
    return pay_from_text(comp.get("compensationTierSummary") or "")


def norm_ashby(spec, raw, title_re, terms):
    out, seen = [], raw.get("jobs", [])
    for j in seen:
        if not title_re.search(j.get("title", "")):
            continue
        text = j.get("descriptionPlain") or to_text(j.get("descriptionHtml"))
        pay = _ashby_pay(j) or pay_from_text(text)
        loc = j.get("location", "")
        rem = remote_flag(loc, j.get("workplaceType"), text, j.get("isRemote"))
        out.append(make_record(spec["company"], "ashby", j["title"], loc, rem, iso_date(j.get("publishedAt")),
                               "published", j.get("jobUrl"), pay, text, terms))
    return out, len(seen)


def fetch_lever(spec, title_re, get=http_json):
    return {"postings": get("https://api.lever.co/v0/postings/%s?mode=json" % spec["token"])}


def norm_lever(spec, raw, title_re, terms):
    posts = raw["postings"] if isinstance(raw, dict) else raw
    out = []
    for j in posts:
        if not title_re.search(j.get("text", "")):
            continue
        lists = " ".join("%s %s" % (x.get("text", ""), to_text(x.get("content"))) for x in j.get("lists") or [])
        text = " ".join([j.get("descriptionPlain") or "", lists, j.get("additionalPlain") or ""])
        sr = j.get("salaryRange")
        if sr and sr.get("min") is not None and sr.get("max") is not None:
            pay = {"min": sr["min"], "max": sr["max"], "currency": sr.get("currency", "USD"),
                   "interval": _interval_word(sr.get("interval")), "basis": "structured",
                   "text": "salaryRange %s-%s %s" % (sr["min"], sr["max"], sr.get("currency", ""))}
        else:
            pay = pay_from_text(text)
        loc = (j.get("categories") or {}).get("location", "")
        out.append(make_record(spec["company"], "lever", j["text"], loc, remote_flag(loc, j.get("workplaceType"), text),
                               iso_date(j.get("createdAt")), "created", j.get("hostedUrl"), pay, text, terms))
    return out, len(posts)


def fetch_eightfold(spec, title_re, get=http_json):
    base = "https://%s/api/apply/v2/jobs" % spec["host"]
    merged, details = {}, {}
    for q in SEARCH_QUERIES:
        r = get("%s?domain=%s&query=%s&num=50&start=0" % (base, spec["domain"], urllib.request.quote(q)))
        for p in r.get("positions", []):
            merged[p["id"]] = p
    for pid, p in merged.items():
        if title_re.search(p.get("name", "")):
            try:
                details[str(pid)] = get("%s/%s?domain=%s" % (base, pid, spec["domain"]))
            except Exception:  # noqa: BLE001
                pass
    return {"positions": list(merged.values()), "_details": details}


def norm_eightfold(spec, raw, title_re, terms):
    out, seen = [], raw.get("positions", [])
    for p in seen:
        if not title_re.search(p.get("name", "")):
            continue
        d = (raw.get("_details") or {}).get(str(p["id"]), {})
        text = to_text(d.get("job_description") or p.get("job_description"))
        loc = p.get("location", "")
        hint = p.get("work_location_option")
        created, posted = iso_date(p.get("t_create")), _eightfold_posted(d)
        rec = make_record(spec["company"], "eightfold", p["name"], loc, remote_flag(loc, hint, text, weak_hint=True),
                          posted or created, "posted" if posted else "created", p.get("canonicalPositionUrl"),
                          pay_from_text(text), text, terms)
        rec["date_created"] = created
        out.append(rec)
    return out, len(seen)


def _eightfold_posted(detail):
    """Netflix's public posting date (custom_JD.data_fields.posting_date, MM-DD-YYYY). t_create can predate it by weeks."""
    v = ((detail.get("custom_JD") or {}).get("data_fields") or {}).get("posting_date")
    v = v[0] if isinstance(v, list) and v else v
    m = re.match(r"(\d{2})-(\d{2})-(\d{4})$", str(v or "").strip())
    return "%s-%s-%s" % (m.group(3), m.group(1), m.group(2)) if m else None


def _wd_base(spec):
    return "https://%s.%s.myworkdayjobs.com" % (spec["tenant"], spec["wd"])


def fetch_workday(spec, title_re, get=http_json):
    base = _wd_base(spec)
    api = "%s/wday/cxs/%s/%s" % (base, spec["tenant"], spec["site"])
    merged, details = {}, {}
    for q in SEARCH_QUERIES:
        r = get(api + "/jobs", {"appliedFacets": {}, "limit": 20, "offset": 0, "searchText": q})
        for p in r.get("jobPostings", []):
            merged[p["externalPath"]] = p
    for path, p in merged.items():
        if title_re.search(p.get("title", "")):
            try:
                details[path] = get(api + path)
            except Exception:  # noqa: BLE001
                pass
    return {"jobPostings": list(merged.values()), "_details": details}


def norm_workday(spec, raw, title_re, terms, today=None):
    out, seen = [], raw.get("jobPostings", [])
    today = today or datetime.now(timezone.utc)
    for p in seen:
        if not title_re.search(p.get("title", "")):
            continue
        info = (raw.get("_details") or {}).get(p["externalPath"], {}).get("jobPostingInfo", {})
        text = to_text(info.get("jobDescription"))
        date, kind = info.get("startDate"), "posted"
        if not date:  # list view only has "Posted 22 Days Ago"
            m = re.search(r"(\d+)\+? Days? Ago", p.get("postedOn", ""))
            n = 0 if "today" in p.get("postedOn", "").lower() else int(m.group(1)) if m else None
            date, kind = ((today - timedelta(days=n)).strftime("%Y-%m-%d"), "posted (approx)") if n is not None \
                else (None, "unknown")
        loc = info.get("location") or p.get("locationsText", "")
        out.append(make_record(spec["company"], "workday", p["title"], loc, remote_flag(loc, text=text), date, kind,
                               _wd_base(spec) + "/" + spec["site"] + p["externalPath"],
                               pay_from_text(text), text, terms))
    return out, len(seen)


SOURCES = {"greenhouse": (fetch_greenhouse, norm_greenhouse), "ashby": (fetch_ashby, norm_ashby),
           "lever": (fetch_lever, norm_lever), "eightfold": (fetch_eightfold, norm_eightfold),
           "workday": (fetch_workday, norm_workday)}


# ---------------------------------------------------------------- boards
def parse_board(s):
    p = s.split(":")
    t = p[0]
    if t in ("greenhouse", "ashby", "lever") and len(p) == 2:
        d = {"type": t, "token": p[1]}
    elif t == "eightfold" and len(p) == 3:
        d = {"type": t, "host": p[1], "domain": p[2]}
    elif t == "workday" and len(p) == 4:
        d = {"type": t, "tenant": p[1], "wd": p[2], "site": p[3]}
    else:
        raise ValueError("bad board spec: %s" % s)
    return d


def board_label(b):
    return "%s:%s" % (b["type"], ":".join(str(b[k]) for k in ("token", "host", "domain", "tenant", "wd", "site") if k in b))


def raw_name(b):
    keys = {"eightfold": ("host", "domain"), "workday": ("tenant", "site")}.get(b["type"], ("token",))
    return "%s_%s.json" % (b["type"], "_".join(b[k] for k in keys))


def default_company(b):
    return b.get("company") or (b.get("token") or b.get("tenant") or b.get("domain", "").split(".")[0]).title()


def scan_board(b, title_re, terms, from_dir=None, save_raw=None):
    """Returns dict(board, ok, records, seen, error). Never raises."""
    b = dict(b, company=default_company(b))
    label = board_label(b)
    try:
        fetch, norm = SOURCES[b["type"]]
        if from_dir:
            path = os.path.join(from_dir, raw_name(b))
            if not os.path.exists(path):
                return {"board": label, "ok": None, "records": [], "seen": 0, "error": "no saved file"}
            with open(path, encoding="utf-8") as f:
                raw = json.load(f)
            captured = datetime.fromtimestamp(os.path.getmtime(path), timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        else:
            captured = None
            raw = fetch(b, title_re)
            if save_raw:
                os.makedirs(save_raw, exist_ok=True)
                with open(os.path.join(save_raw, raw_name(b)), "w", encoding="utf-8") as f:
                    json.dump(raw, f)
        recs, seen = norm(b, raw, title_re, terms)
        return {"board": label, "ok": True, "records": recs, "seen": seen, "error": None, "captured_at": captured}
    except Exception as e:  # noqa: BLE001 - one failing board never kills the run
        return {"board": label, "ok": False, "records": [], "seen": 0, "error": "%s: %s" % (type(e).__name__, e)}


# ---------------------------------------------------------------- run + filter
def run(boards, title_re, terms, from_dir=None, save_raw=None, workers=8):
    with ThreadPoolExecutor(workers) as ex:
        results = list(ex.map(lambda b: scan_board(b, title_re, terms, from_dir, save_raw), boards))
    return results


def apply_filters(recs, min_pay=None, require_pay=False, remote_only=False, since=None):
    out = []
    for r in recs:
        if remote_only and r["remote"] not in (True, "conflict"):
            continue
        if since and r["date"] and r["date"] < since:
            continue
        if min_pay is not None:
            a = r["_pay_max_annual"]
            if a is None:
                if require_pay:
                    continue
            elif a < min_pay:
                continue
        elif require_pay and r["pay_max"] is None:
            continue
        out.append(r)
    return out


def sort_records(recs):
    return sorted(recs, key=lambda r: (r["_pay_max_annual"] is None, -(r["_pay_max_annual"] or 0), r["company"], r["title"]))


def term_counts(recs, terms):
    return {t: sum(1 for r in recs if t in r["terms"]) for t in terms}


def term_employers(recs, terms):
    """Distinct employers mentioning each term, so one company's many postings can't skew the read."""
    return {t: len({r["company"] for r in recs if t in r["terms"]}) for t in terms}


# ---------------------------------------------------------------- output
def fmt_pay(r):
    if r["pay_max"] is None:
        return "-"
    sym = {"USD": "$", "GBP": "£", "EUR": "€"}.get(r["pay_currency"], "")
    unit = {"hour": "/hr", "month": "/mo", "year": ""}.get(r["pay_interval"], "")
    s = "%s%s-%s%s %s" % (sym, format(r["pay_min"], ",.0f"), sym, format(r["pay_max"], ",.0f"), r["pay_currency"])
    s += unit
    if r["pay_interval"] != "year":
        s += " (~%s annualized)" % format(r["_pay_max_annual"], ",.0f")
    return s


def public(r):
    return {k: v for k, v in r.items() if not k.startswith("_")}


def render_md(payload, recs, counts, annualized_note):
    L = []
    ok = [b for b in payload["boards_ok"]]
    L.append("# Job posting scan")
    L.append("")
    if "data_captured" in payload:
        span = payload["data_captured"] or ["unknown", "unknown"]
        L.append("- Replayed at (UTC): %s, from saved files; cite the capture time, not this" % payload["run_at"])
        L.append("- Data captured (UTC): %s" % (span[0] if span[0] == span[1] else "%s to %s" % tuple(span)))
    else:
        L.append("- Run at (UTC): %s" % payload["run_at"])
    L.append("- Boards scanned OK: %d (%s)" % (len(ok), ", ".join(
        "%s %d/%d" % (b["board"], b["matched"], b["seen"]) for b in ok)))
    L.append("- Boards failed: %d%s" % (len(payload["errors"]), "".join(
        "\n  - %s: %s" % (e["board"], e["error"]) for e in payload["errors"])))
    if payload.get("boards_missing"):
        L.append("- Boards with no saved file: %d (%s)" % (len(payload["boards_missing"]), ", ".join(payload["boards_missing"])))
    L.append("- Matched postings: %d" % len(recs))
    if annualized_note:
        L.append("- `--min-pay` compared hourly/monthly pay annualized (hour x 2,080 h; month x 12); currency not converted.")
    L += ["", "## Postings (pay_max descending; no-pay last)", "",
          "| Company | Title | Level | Location | Remote | Pay (posted) | Basis | Date | URL |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in sort_records(recs):
        L.append("| %s | %s | %s | %s | %s | %s | %s | %s (%s) | %s |" % (
            r["company"], r["title"].replace("|", "/"), r["level_hint"], r["location"].replace("|", "/"),
            str(r["remote"]).lower(), fmt_pay(r), r["pay_basis"], r["date"] or "?", r["date_kind"], r["url"]))
    emp = term_employers(recs, list(counts))
    n_emp = len({r["company"] for r in recs}) or 1
    L += ["", "## Term frequency (matched postings mentioning term)", "",
          "Read the Employers column first: one company posting many similar roles inflates Postings.", "",
          "| Term | Postings | Share | Employers (of %d) |" % n_emp, "|---|---|---|---|"]
    n = len(recs) or 1
    for t, c in sorted(counts.items(), key=lambda x: (-emp[x[0]], -x[1])):
        L.append("| %s | %d | %d%% | %d |" % (t, c, round(100.0 * c / n), emp[t]))
    L += ["", "## Known caveats", "",
          "- A posted range is not an offer; it is the employer's stated band, and offers can land outside it.",
          "- Greenhouse `updated_at` is not the posting date; `first_published` is used when present, else the date is marked updated.",
          "- Ranges may be multi-zone (location tiers); the widest min..max is shown and all ranges are in `pay_text` (json/csv).",
          "- remote=conflict means the structured flag and the posting text disagree (see remote_evidence in json/csv); `--remote-only` keeps those rows.",
          "- Pay parsed from free text (pay_basis=parsed_text) can mis-read bonus/OTE figures; check the posting.",
          "- Workday dates without a detail record are approximated from 'Posted N Days Ago'.",
          "- Term counts are word-boundary matches on title + description; zero matches on a board is a finding, not an error."]
    return "\n".join(L) + "\n"


def render_csv(recs):
    cols = ["company", "source", "title", "level_hint", "location", "remote", "remote_evidence", "date", "date_kind", "date_created", "url",
            "pay_min", "pay_max", "pay_currency", "pay_interval", "pay_basis", "pay_text", "terms"]
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(cols)
    for r in sort_records(recs):
        w.writerow([";".join(r[c]) if c == "terms" else r.get(c) for c in cols])
    return buf.getvalue()


# ---------------------------------------------------------------- CLI
def load_boards(args):
    if args.boards:
        return [parse_board(s) for s in args.boards]
    path = args.boards_file or os.path.join(HERE, "boards.json")
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    return data["boards"] if isinstance(data, dict) else data


def load_terms(args):
    if args.terms_file:
        with open(args.terms_file, encoding="utf-8") as f:
            return [t.strip() for t in re.split(r"[,\n]", f.read()) if t.strip()]
    if args.terms:
        return [t.strip() for t in args.terms.split(",") if t.strip()]
    return DEFAULT_TERMS


def main(argv=None):
    ap = argparse.ArgumentParser(description="Scan public job-board APIs for matching postings.")
    ap.add_argument("--boards", nargs="+", help="board specs, e.g. greenhouse:figma ashby:openai")
    ap.add_argument("--boards-file")
    ap.add_argument("--title", default=DEFAULT_TITLE, help="title regex, case-insensitive")
    ap.add_argument("--exclude-title", default=DEFAULT_EXCLUDE,
                    help="title regex to drop (default drops engineering/ops titles); \"\" keeps all")
    ap.add_argument("--min-pay", type=float)
    ap.add_argument("--require-pay", action="store_true", help="drop postings without pay")
    ap.add_argument("--remote-only", action="store_true")
    ap.add_argument("--since", help="YYYY-MM-DD; drop postings with an older known date")
    ap.add_argument("--terms")
    ap.add_argument("--terms-file")
    ap.add_argument("--from-dir", help="read saved raw responses instead of the network")
    ap.add_argument("--save-raw", help="write raw responses here")
    ap.add_argument("--format", choices=["md", "csv", "json"], default="md")
    ap.add_argument("--out")
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args(argv)

    title_re = TitleFilter(args.title, args.exclude_title)
    terms = load_terms(args)
    results = run(load_boards(args), title_re, terms, args.from_dir, args.save_raw, args.workers)
    recs = [r for res in results for r in res["records"]]
    recs = apply_filters(recs, args.min_pay, args.require_pay, args.remote_only, args.since)
    counts = term_counts(recs, terms)
    payload = {
        "run_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "boards_ok": [{"board": x["board"], "seen": x["seen"], "matched": len(x["records"])}
                      for x in results if x["ok"]],
        "errors": [{"board": x["board"], "error": x["error"]} for x in results if x["ok"] is False],
        "postings": [public(r) for r in sort_records(recs)],
        "term_counts": counts,
        "term_employers": term_employers(recs, terms),
    }
    if args.from_dir:  # replay: the data's age is the files' capture time, not now
        caught = sorted(x["captured_at"] for x in results if x.get("captured_at"))
        payload["data_captured"] = [caught[0], caught[-1]] if caught else None
        payload["boards_missing"] = [x["board"] for x in results if x["ok"] is None]
    if args.format == "json":
        out = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    elif args.format == "csv":
        out = render_csv(recs)
    else:
        out = render_md(payload, recs, counts, args.min_pay is not None)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out)
    else:
        sys.stdout.write(out)
    return 0 if payload["boards_ok"] or not payload["errors"] else 2


if __name__ == "__main__":
    sys.exit(main())
