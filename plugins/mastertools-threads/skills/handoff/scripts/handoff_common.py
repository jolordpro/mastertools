"""Shared helpers for the handoff scripts: the handoff folder, the thread tree, thread folders, the fence.

The thread tree comes from the desktop app's session records
(~/Library/Application Support/Claude/claude-code-sessions/<account>/<org>/local_*.json).
Each record has `title`, `cliSessionId` (the transcript id), `isArchived`, `lastActivityAt`, `cwd`,
and for a thread started by another one, `spawnedFrom.sessionId`. Records of every account on
this machine are read, so a new account can see the old account's tree.
"""
import glob, json, os, re, socket, time

HOME = os.path.expanduser("~")
RECORDS = os.path.join(HOME, "Library", "Application Support", "Claude", "claude-code-sessions")
CONFIG = os.path.join(HOME, ".config", "handoff")
ID_FILE = ".thread-id"


def handoff_dir(arg=None):
    """The handoff folder: the argument, $HANDOFF_DIR, ~/.config/handoff/dir, this script's folder if it holds INDEX.md, ~/.claude/handoffs."""
    if arg:
        return os.path.expanduser(arg)
    if os.environ.get("HANDOFF_DIR"):
        return os.path.expanduser(os.environ["HANDOFF_DIR"])
    cfg = os.path.join(CONFIG, "dir")
    if os.path.isfile(cfg):
        line = open(cfg, encoding="utf-8").read().strip()
        if line:
            return os.path.expanduser(line)
    here = os.path.dirname(os.path.abspath(__file__))
    if os.path.isfile(os.path.join(here, "INDEX.md")):
        return here
    return os.path.join(HOME, ".claude", "handoffs")


def find_transcript(tid):
    hits = glob.glob(os.path.join(HOME, ".claude", "projects", "*", tid + ".jsonl"))
    return max(hits, key=os.path.getmtime) if hits else None


def load_threads():
    """transcript id -> thread dict. Threads without a desktop record are left out (look them up by transcript)."""
    by_local, threads = {}, {}
    for f in glob.glob(os.path.join(RECORDS, "*", "*", "local_*.json")):
        try:
            d = json.load(open(f, encoding="utf-8"))
        except (OSError, ValueError):
            continue
        tid = d.get("cliSessionId")
        if not tid:
            continue
        sp = d.get("spawnedFrom") or {}
        t = dict(id=tid, local=d.get("sessionId", ""), title=(d.get("title") or "").strip() or tid[:8],
                 archived=bool(d.get("isArchived")), last=(d.get("lastActivityAt") or 0) / 1000,
                 cwd=d.get("cwd") or d.get("originCwd") or "", parent_local=sp.get("sessionId"),
                 parent_title=sp.get("title"), account=f.split(os.sep)[-3], children=[])
        old = threads.get(tid)
        if old is None or t["last"] >= old["last"]:
            threads[tid] = t
        by_local[t["local"]] = tid
    for t in threads.values():
        t["parent"] = by_local.get(t["parent_local"])
    for t in sorted(threads.values(), key=lambda x: x["last"]):
        if t["parent"] in threads:
            threads[t["parent"]]["children"].append(t["id"])
    return threads


def resolve(threads, key):
    """Accept a transcript id, a local_ id, or a unique title fragment."""
    if key in threads:
        return key
    for t in threads.values():
        if t["local"] == key:
            return t["id"]
    hits = [t["id"] for t in threads.values() if key.lower() in t["title"].lower()]
    return hits[0] if len(hits) == 1 else None


def subtree(threads, tid, depth=0):
    yield tid, depth
    for c in threads[tid]["children"]:
        yield from subtree(threads, c, depth + 1)


def safe_name(title):
    name = re.sub(r"[/:\\\x00-\x1f]+", "-", title).strip(" .-")
    return (name or "untitled")[:80]


def read_ids(folder):
    """Transcript ids in a folder's .thread-id, the original thread first. A resumed thread adds its id on a new line."""
    try:
        return [l.strip() for l in open(os.path.join(folder, ID_FILE), encoding="utf-8") if l.strip()]
    except OSError:
        return []


def add_id(folder, tid):
    if tid not in read_ids(folder):
        with open(os.path.join(folder, ID_FILE), "a", encoding="utf-8") as f:
            f.write(tid + "\n")


def thread_folders(root):
    """folder -> its transcript ids (original first), for every folder under root that holds a .thread-id file."""
    out = {}
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        if ID_FILE in filenames:
            ids = read_ids(dirpath)
            if ids:
                out[dirpath] = ids
    return out


def id_folders(root):
    """transcript id -> folder. Every id in a folder's .thread-id maps to that folder."""
    out = {}
    for folder, ids in thread_folders(root).items():
        for tid in ids:
            out.setdefault(tid, folder)
    return out


RESUMED_LINK = re.compile(r"\((local_[0-9A-Za-z-]{4,})\)")


def resume_links(root, threads):
    """transcript id -> old folder, from the (local_…) session ids handoff-resume writes into each old folder's RESUMED.md."""
    by_local = {t["local"]: tid for tid, t in threads.items() if t["local"]}
    out = {}
    for folder in thread_folders(root):
        try:
            text = open(os.path.join(folder, "RESUMED.md"), encoding="utf-8").read()
        except OSError:
            continue
        for short in RESUMED_LINK.findall(text):
            hits = [tid for local, tid in by_local.items() if local.startswith(short)]
            if len(hits) == 1:
                out.setdefault(hits[0], folder)
    return out


def folder_for(root, threads, tid, create=True, _known=None):
    """The thread's folder. An existing folder (found by .thread-id) always wins, so renames never move it.
    A thread resumed from an older one (listed in that folder's RESUMED.md) shares the older thread's folder.
    Otherwise a new folder goes inside its parent's folder, named by title."""
    known = _known if _known is not None else id_folders(root)
    if tid in known:
        return known[tid]
    linked = resume_links(root, threads).get(tid)
    if linked:
        if create:
            add_id(linked, tid)
            known[tid] = linked
        return linked
    t = threads.get(tid)
    title = t["title"] if t else tid[:8]
    parent = t.get("parent") if t else None
    base = folder_for(root, threads, parent, create, known) if parent in threads else root
    path = os.path.join(base, safe_name(title))
    if os.path.exists(path) and tid not in read_ids(path):
        path += f" ({tid[:8]})"
    if create:
        os.makedirs(path, exist_ok=True)
        add_id(path, tid)
        known[tid] = path
    return path


ENTRY = re.compile(r"^## (\d{4}-\d\d-\d\d \d\d:\d\d) · (.*?) · (.*?) · transcript ([0-9a-f]{8})", re.M)


def changelog(folder):
    """Entries in the folder's CHANGELOG.md and CHANGELOG-ARCHIVE.md: (epoch, account, title, transcript id prefix, text)."""
    out = []
    for name in ("CHANGELOG-ARCHIVE.md", "CHANGELOG.md"):
        try:
            text = open(os.path.join(folder, name), encoding="utf-8").read()
        except OSError:
            continue
        marks = list(ENTRY.finditer(text))
        for i, m in enumerate(marks):
            end = marks[i + 1].start() if i + 1 < len(marks) else len(text)
            try:
                when = time.mktime(time.strptime(m.group(1), "%Y-%m-%d %H:%M"))
            except ValueError:
                continue
            out.append((when, m.group(2), m.group(3), m.group(4), text[m.start():end].strip()))
    return sorted(out)


def last_handoff(folder, tid):
    """When this thread last wrote to its folder: its newest changelog entry, else HANDOFF.md if it is the folder's
    original thread, else None (a resumed thread's whole transcript is new since the last handoff)."""
    own = [e[0] for e in changelog(folder) if tid.startswith(e[3])]
    if own:
        return max(own)
    ids = read_ids(folder)
    hf = os.path.join(folder, "HANDOFF.md")
    if ids and ids[0] == tid and os.path.isfile(hf):
        return os.path.getmtime(hf)
    return None


def account_label(account):
    """A friendly name for an account folder id, from lines like `e37733af = Personal` in ~/.config/handoff/accounts."""
    p = os.path.join(CONFIG, "accounts")
    if account and os.path.isfile(p):
        for line in open(p, encoding="utf-8"):
            key, _, name = line.partition("=")
            if key.strip() and account.startswith(key.strip()) and name.strip():
                return name.strip()
    return f"account {account[:8]}" if account else "account unknown"


def fence_lines():
    p = os.path.join(CONFIG, "fence")
    if not os.path.isfile(p):
        return []
    return [l.strip() for l in open(p, encoding="utf-8") if l.strip() and not l.startswith("#")]


def fence_terms():
    """Strict fence terms in ~/.config/handoff/fence (plain lines). A matching thread is regulated: nothing is copied."""
    return [l for l in fence_lines() if not l.lower().startswith("private:")]


def private_terms():
    """`private: <term>` lines in ~/.config/handoff/fence. A matching thread keeps its full handoff in its project
    folder; the handoff folder gets only POINTER.md."""
    return [l.split(":", 1)[1].strip() for l in fence_lines() if l.lower().startswith("private:") and l.split(":", 1)[1].strip()]


def _hay(thread, extra_paths):
    return " ".join([thread.get("title", ""), thread.get("cwd", ""), *extra_paths]).lower() if thread else " ".join(extra_paths).lower()


def fenced(thread, extra_paths=()):
    hay = _hay(thread, extra_paths)
    return next((term for term in fence_terms() if term.lower() in hay), None)


def private(thread, extra_paths=()):
    """The private term a thread matches, unless a strict fence term matches too (strict wins)."""
    if fenced(thread, extra_paths):
        return None
    hay = _hay(thread, extra_paths)
    return next((term for term in private_terms() if term.lower() in hay), None)


def private_folder(thread, create=False):
    """Where a private thread's full handoff lives: <project>/.handoff-private/<title>, with a .gitignore so git never
    picks it up. A thread with no project folder (none, or the home folder) uses ~/.claude/handoffs-private/<title>."""
    cwd = os.path.realpath(thread.get("cwd") or "") if thread.get("cwd") else ""
    if cwd and os.path.isdir(cwd) and cwd != os.path.realpath(HOME):
        base = os.path.join(cwd, ".handoff-private")
    else:
        base = os.path.join(HOME, ".claude", "handoffs-private")
    path = os.path.join(base, safe_name(thread.get("title") or thread.get("id", "")[:8]))
    if create:
        os.makedirs(path, exist_ok=True)
        ignore = os.path.join(base, ".gitignore")
        if not os.path.exists(ignore):
            open(ignore, "w").write("*\n")
        if thread.get("id"):
            add_id(path, thread["id"])
    return path


SHARED_HANDOFF_FILES = ("HANDOFF.md", "SUMMARY.md", "CHANGELOG.md", "CHANGELOG-ARCHIVE.md", "RESUME-PROMPT.md", "AUTO-DIGEST*.md")


def private_leftovers(folder, local):
    """For a private thread: a warning when handoff files still sit in its shared folder. Never deletes or moves them."""
    left = sorted({os.path.basename(p) for pat in SHARED_HANDOFF_FILES for p in glob.glob(os.path.join(glob.escape(folder), pat))})
    if not left:
        return None
    return f"⚠ private thread has files in _HANDOFF: move them to {local} ({', '.join(left)} in {folder})"


def pointer_text(thread, transcript, term=None, folder=None, warning=None):
    if folder:
        return (f"# {thread['title']}\n\nPrivate thread (matches \"private: {term}\" in ~/.config/handoff/fence). "
                f"Its full handoff stays in its project folder, on this machine:\n`{folder}`\n"
                f"Transcript: `{transcript}`\n" + (f"\n{warning}\n" if warning else ""))
    return (f"# {thread['title']}\n\nFenced thread (matches \"{term}\" in ~/.config/handoff/fence). Nothing from it is copied here.\n"
            f"Resume from its local transcript with the digest script, on this machine only:\n`{transcript}`\n")


# Secrets. Every script that writes transcript-derived text passes it through redact().
REDACTED = "[REDACTED]"
_Q = "[\"'*_`]*"
# A label's separator: `:`, `=`, `is` or `is:`, then optional bold or quote marks and spaces.
_SEP = r"(\s*(?:[:=]|\bis\b:?)\s*)" + _Q + r"\s*"
# Words that say where a password lives, or what state it is in, rather than what it is.
_NOT_VALUE = (r"(?!\[|(?:none|n/?a|in|on|is|from|stored|see|kept|lives?|saved|manager|keychain|1password|vault|redacted|"
              r"required|reset|changed|set|wrong|correct|incorrect|now|the|same|still|not|expired|missing|empty|ok|"
              r"true|false|yes|no)\b)")
SECRET_RULES = [
    # A block with no END line runs to the next blank line or the end of the text.
    ("private key", re.compile(r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----.*?(?:-----END [A-Z0-9 ]*PRIVATE KEY-----|(?=\n[ \t]*\n)|\Z)", re.S), None),
    ("password", re.compile(r"(?i)(?<![A-Za-z])(passwords?|passwd|passcodes?|passphrase|pass|pw)" + _Q + _SEP + _NOT_VALUE +
                            r"([^\s\"'`,;)\]]{3,})"), 3),
    ("PIN", re.compile(r"(?i)(?<![A-Za-z])(pin(?:\s*code)?)" + _Q + _SEP + r"(\d{4,8})\b"), 3),
    ("labelled key", re.compile(r"(?i)(?<![A-Za-z])([a-z_]*(?:api[ _-]?key|access[ _-]?key|secret|token|auth|credential)s?)" + _Q +
                                r"(\s*[:=]\s*)" + _Q + r"\s*" + _NOT_VALUE + r"([A-Za-z0-9+/=_.~-]{8,})"), 3),
    ("bearer token", re.compile(r"(?i)(\bBearer)(\s+)([A-Za-z0-9._~+/=-]{12,})"), 3),
    ("basic auth", re.compile(r"(?i)(authorization\s*:\s*basic)(\s+)([A-Za-z0-9+/=]{6,})"), 3),
    ("URL password", re.compile(r"(\b[a-z][a-z0-9+.-]*://[^\s:/@]+:)([^\s@/]+)(?=@)"), 2),
    ("password flag", re.compile(r"(?i)(--pass(?:word|wd)?)(=|\s+)['\"]?(?!-)([^\s'\"]+)"), 3),
    ("password flag", re.compile(r"(\bsshpass\s+-p)(\s*)['\"]?([^\s'\"]+)"), 3),
    ("password flag", re.compile(r"(\b(?:mysql|mysqldump|mysqladmin|mariadb)\b[^\n|;&]*?\s-p)()([^\s'\"]+)"), 3),
    ("password flag", re.compile(r"(\bcurl\b[^\n|;&]*?\s(?:-u|--user)\s+['\"]?[^\s:'\"]+:)()([^\s'\"]+)"), 3),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{5,}\.eyJ[A-Za-z0-9_-]{5,}\.[A-Za-z0-9_-]{5,}"), None),
    ("API key", re.compile(r"\bsk-[A-Za-z0-9_-]{16,}"), None),
    ("GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})"), None),
    ("Slack token", re.compile(r"\bxox[abposre]-[A-Za-z0-9-]{10,}"), None),
    ("AWS key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"), None),
    ("Google key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"), None),
]


def redact_words():
    """Literals from ~/.config/handoff/redact, one per line (# comments), redacted wherever they appear."""
    p = os.path.join(CONFIG, "redact")
    try:
        return [l.rstrip("\n") for l in open(p, encoding="utf-8") if l.strip() and not l.startswith("#")]
    except OSError:
        return []


def _sub(rule, group, text):
    if group is None:
        return rule.sub(REDACTED, text)
    return rule.sub(lambda m: m.group(0)[:m.start(group) - m.start(0)] + REDACTED if m.group(group) != REDACTED else m.group(0), text)


def redact(text):
    """Text with passwords, keys, tokens, private keys and the user's listed words replaced by [REDACTED]."""
    if not text:
        return text
    for word in sorted(redact_words(), key=len, reverse=True):
        text = text.replace(word.strip(), REDACTED)
    for _, rule, group in SECRET_RULES:
        text = _sub(rule, group, text)
    return text


def secret_hits(text):
    """(line number, kind) for each secret shape in text. Never returns the value."""
    hits = []
    words = [w.strip() for w in redact_words()]
    for i, line in enumerate(text.splitlines(), 1):
        if any(w and w in line for w in words):
            hits.append((i, "listed word"))
        for kind, rule, group in SECRET_RULES:
            if kind == "private key":
                continue
            if any(group is None or m.group(group) != REDACTED for m in rule.finditer(line)):
                hits.append((i, kind))
    for m in SECRET_RULES[0][1].finditer(text):
        hits.append((text.count("\n", 0, m.start()) + 1, "private key"))
    return sorted(set(hits))


# Two Macs: each folder records the host and handoff home that last wrote it.
HOST_FILE = ".written-by"


def host_name():
    return socket.gethostname().split(".")[0] or "unknown host"


def stamp_host(folder, root):
    try:
        with open(os.path.join(folder, HOST_FILE), "w", encoding="utf-8") as f:
            f.write(f"{host_name()}\t{root}\t{time.strftime('%Y-%m-%d %H:%M')}\n")
    except OSError:
        pass


def other_host(folder):
    """(host, handoff home, time) when another Mac wrote this folder last, else None."""
    try:
        cells = open(os.path.join(folder, HOST_FILE), encoding="utf-8").readline().rstrip("\n").split("\t")
    except OSError:
        return None
    if cells and cells[0] and cells[0] != host_name():
        return (cells + ["", "", ""])[:3]
    return None


def nested_children(root, folder):
    """Thread folders whose nearest enclosing thread folder is `folder` (their first transcript id, folder path)."""
    out = []
    for f, ids in thread_folders(root).items():
        if not f.startswith(folder + os.sep):
            continue
        up = os.path.dirname(f)
        while up != folder and not os.path.isfile(os.path.join(up, ID_FILE)):
            up = os.path.dirname(up)
        if up == folder:
            out.append((ids[0], f))
    return sorted(out, key=lambda x: x[1])


def age(ts):
    if not ts:
        return "unknown"
    d = (time.time() - ts) / 86400
    return f"{d * 24:.0f}h ago" if d < 1 else f"{d:.0f}d ago"
