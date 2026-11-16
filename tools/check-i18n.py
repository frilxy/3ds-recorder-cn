#!/usr/bin/env python3
"""Checks the Chinese texts against i18n.h.

Chinese lives in app/source/i18n_zh.c, one entry per key of the STRINGS(X) list. A key added
upstream (or renamed) would otherwise only show up as English text on a console, so this runs in
CI: every key needs a Chinese text, no entry may name a key that is gone, and the printf
conversions (%s, %u, ...) must match the English text they translate.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "app" / "source"
CONVERSION = re.compile(r"%[-+ #0-9.]*(?:l|ll|h|hh|z|j|t)?[diouxXeEfgGaAcspn%]")

# X(S_KEY, "English", "Українська")
ENTRY = re.compile(r'X\((S_\w+),\s*"((?:[^"\\]|\\.)*)"')


def unescape(text: str) -> str:
    return text.replace('\\n', '\n').replace('\\"', '"').replace("\\\\", "\\")


def conversions(text: str) -> list[str]:
    return sorted(c for c in CONVERSION.findall(text) if c != "%%")


def main() -> int:
    strings = ENTRY.findall((SRC / "i18n.h").read_text(encoding="utf-8"))
    zh_text = (SRC / "i18n_zh.c").read_text(encoding="utf-8")
    zh = dict(re.findall(r'\[(S_\w+)\]\s*=\s*"((?:[^"\\]|\\.)*)"', zh_text))

    keys = [key for key, _ in strings]
    problems: list[str] = []

    for key in keys:
        if zh.get(key) is None:
            problems.append(f"{key}: no Chinese text")

    for key in zh:
        if key not in keys:
            problems.append(f"{key}: Chinese text for a key i18n.h does not have")

    for key, english in strings:
        if key not in zh:
            continue
        want, have = conversions(unescape(english)), conversions(unescape(zh[key]))
        if want != have:
            problems.append(f"{key}: conversions {want} vs {have} in the Chinese text")

    if problems:
        print("\n".join(problems))
        print(f"\n{len(problems)} problem(s) in app/source/i18n_zh.c", file=sys.stderr)
        return 1

    print(f"{len(keys)} keys, all translated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
