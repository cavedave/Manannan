#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regenerate caibidlí/new-orthography/*.md from caibidlí/old-orthography/*.md.

  python3 caibidlí/conversion/build_new_orthography.py

Step 1 (default): grapheme pass only — ponc letters → h digraphs (grapheme_pass.py).
Optional: --spelling applies whole-word rows from caibidlí/old-to-new-spelling.md
(table columns Old | New), longest-first.

From repo root after fixing old-orthography, re-run this script.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

ROOT = HERE.parents[1]
OLD_DIR = ROOT / "caibidlí" / "old-orthography"
NEW_DIR = ROOT / "caibidlí" / "new-orthography"
SPELLING_MD = ROOT / "caibidlí" / "old-to-new-spelling.md"

from grapheme_pass import apply_clo_to_roman  # noqa: E402


def _load_spelling_pairs(path: Path) -> list[tuple[str, str]]:
    if not path.is_file():
        return []
    text = path.read_text(encoding="utf-8")
    pairs: list[tuple[str, str]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip("|").split("|")]
        if len(parts) < 2:
            continue
        old_w, new_w = parts[0], parts[1]
        if old_w.lower() == "old" or not old_w or not new_w:
            continue
        pairs.append((old_w, new_w))
    pairs.sort(key=lambda x: len(x[0]), reverse=True)
    return pairs


def _apply_spelling_whole_words(text: str, pairs: list[tuple[str, str]]) -> str:
    for old_w, new_w in pairs:
        pat = re.compile(
            r"(?<![\w\d'])"
            + re.escape(old_w)
            + r"(?![\w\d'])",
            re.IGNORECASE,
        )
        text = pat.sub(new_w, text)
    return text


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--spelling",
        action="store_true",
        help="Apply whole-word pairs from old-to-new-spelling.md after grapheme pass",
    )
    ap.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions only; do not write files",
    )
    args = ap.parse_args()

    if not OLD_DIR.is_dir():
        print(f"Missing directory: {OLD_DIR}", file=sys.stderr)
        return 1

    pairs = _load_spelling_pairs(SPELLING_MD) if args.spelling else []
    NEW_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(OLD_DIR.glob("manannan[0-9][0-9].md"))
    if not files:
        print(f"No manannan*.md under {OLD_DIR}", file=sys.stderr)
        return 1

    for src in files:
        raw = src.read_text(encoding="utf-8")
        out = apply_clo_to_roman(raw)
        if pairs:
            out = _apply_spelling_whole_words(out, pairs)
        dest = NEW_DIR / src.name
        if args.dry_run:
            print(f"would write {dest} ({len(out)} chars)")
        else:
            dest.write_text(out, encoding="utf-8")
            print(f"wrote {dest.relative_to(ROOT)}")

    print(
        "Done. Grapheme pass applied."
        + (" Spelling table applied." if pairs else " (Use --spelling to apply old-to-new-spelling.md.)")
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
