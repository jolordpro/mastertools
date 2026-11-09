#!/usr/bin/env python3
"""Check a handoff folder for secrets before a handoff finishes: passwords, PINs, API keys and tokens, private keys,
and the words listed in ~/.config/handoff/redact. Every file counts, AUTO-DIGEST included.

Usage: handoff_secrets.py <folder> [<folder> ...] [--fix]
Prints file:line and the kind of secret, never the value. Exit 1 when any are found.
--fix replaces each one with [REDACTED] in place, then checks again.
"""
import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from handoff_common import redact, secret_hits  # noqa: E402

MAX_BYTES = 20_000_000


def files(folder):
    if os.path.isfile(folder):
        yield folder
        return
    for d, dirs, names in os.walk(folder):
        dirs[:] = [x for x in dirs if x != ".git"]
        for n in names:
            yield os.path.join(d, n)


def text_of(path):
    try:
        if os.path.getsize(path) > MAX_BYTES:
            return None
        with open(path, encoding="utf-8") as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return None


def main():
    fix = "--fix" in sys.argv
    folders = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not folders:
        sys.exit(__doc__)
    found = 0
    for folder in folders:
        for path in files(os.path.expanduser(folder)):
            text = text_of(path)
            if not text:
                continue
            hits = secret_hits(text)
            if hits and fix:
                tmp = path + ".redact-tmp"
                with open(tmp, "w", encoding="utf-8") as f:
                    f.write(redact(text))
                os.replace(tmp, path)
                hits = secret_hits(redact(text))
            for line, kind in hits:
                found += 1
                print(f"{path}:{line}: {kind}")
    if found:
        print(f"\n{found} secret{'s' if found != 1 else ''} found. Replace each with where it lives (Keychain, 1Password, .env), "
              f"or rerun with --fix.")
        sys.exit(1)
    print("No secrets found.")


if __name__ == "__main__":
    main()
