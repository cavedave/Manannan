#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch Caighdeán (Intergaelic) output for one chapter: new-orthography → spelling/.

Reads:  caibidlí/new-orthography/manannanNN.md  (grapheme layer only)
Writes: caibidlí/spelling/manannanNN.md           (same text + API spelling; authoritative for spelling/)
        caibidlí/spelling/manannanNN.pairs.tsv   (source\\ttarget tokens; may include ___MANANPH___ placeholders)
        caibidlí/spelling/manannanNN.diff.tsv    (rows where source != target)

Example:
  python3 caibidlí/conversion/fetch_caighdean_chapter.py --chapter 01

Requires network access to https://cadhan.com/api/intergaelic/3.0
(see https://github.com/kscanne/caighdean/blob/master/API.md).

old-orthography/ is unchanged by this script. Optional: old-to-new-spelling.md only affects
rebuilding new/ from old/, not this fetch.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

ROOT = HERE.parents[1]
NEW_ORTHO = ROOT / "caibidlí" / "new-orthography"
SPELLING_OUT = ROOT / "caibidlí" / "spelling"

from caighdean_api import (  # noqa: E402
    differing_pairs,
    pairs_to_tsv,
    shield_markdown,
    standardize_irish_long,
    unshield,
)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--chapter",
        required=True,
        help="Two digits, e.g. 01 (reads manannan01.md)",
    )
    args = ap.parse_args()
    ch = args.chapter.strip().zfill(2)
    src = NEW_ORTHO / f"manannan{ch}.md"
    if not src.is_file():
        print(f"Missing {src}", file=sys.stderr)
        return 1

    text = src.read_text(encoding="utf-8")
    shielded, mapping = shield_markdown(text)
    print(
        f"POSTing {src.relative_to(ROOT)} "
        f"({len(shielded.encode('utf-8'))} bytes UTF-8 after shield)..."
    )
    det, pairs = standardize_irish_long(shielded)
    det = unshield(det, mapping)
    diff = differing_pairs(pairs)

    SPELLING_OUT.mkdir(parents=True, exist_ok=True)
    md_path = SPELLING_OUT / f"manannan{ch}.md"
    tsv_path = SPELLING_OUT / f"manannan{ch}.pairs.tsv"
    diff_path = SPELLING_OUT / f"manannan{ch}.diff.tsv"

    header = (
        "<!-- spelling/: new-orthography + Cadhan Intergaelic (this file is the API layer for this chapter). "
        "old-orthography/ and new-orthography/ are not modified by the fetch script. -->\n\n"
    )
    md_path.write_text(header + det, encoding="utf-8")
    tsv_path.write_text(pairs_to_tsv(pairs), encoding="utf-8")
    diff_path.write_text(pairs_to_tsv(diff), encoding="utf-8")

    print(f"wrote {md_path.relative_to(ROOT)}")
    print(f"wrote {tsv_path.relative_to(ROOT)} ({len(pairs)} pairs)")
    print(f"wrote {diff_path.relative_to(ROOT)} ({len(diff)} differing pairs)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
