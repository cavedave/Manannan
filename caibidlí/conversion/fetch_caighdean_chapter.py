#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fetch Caighdeán (Intergaelic) output for one chapter: new-orthography → spelling/.

Reads:  caibidlí/new-orthography/manannanNN.md  (grapheme layer only)
Writes: caibidlí/spelling/manannanNN.md           (same text + API spelling; authoritative for spelling/)
        caibidlí/spelling/manannanNN.pairs.tsv   (local only; gitignored)
        caibidlí/spelling/manannanNN.diff.tsv    (local only; gitignored)

Examples:
  python3 caibidlí/conversion/fetch_caighdean_chapter.py --chapter 01
  python3 caibidlí/conversion/fetch_caighdean_chapter.py --all --delay 5 --chapter-delay 15
  python3 caibidlí/conversion/fetch_caighdean_chapter.py --all --only-missing --delay 6

Requires network access to https://cadhan.com/api/intergaelic/3.0
(see https://github.com/kscanne/caighdean/blob/master/API.md).

On HTTP errors, bad JSON, empty token lists, or network failure, the script exits
with a non-zero status and does not continue to further chapters (--all).

old-orthography/ is unchanged by this script. Optional: old-to-new-spelling.md only affects
rebuilding new/ from old/, not this fetch.
"""

from __future__ import annotations

import argparse
import sys
import time
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


def list_chapter_ids() -> list[str]:
    ids: list[int] = []
    for p in NEW_ORTHO.glob("manannan*.md"):
        stem = p.stem
        if not stem.startswith("manannan"):
            continue
        suffix = stem[len("manannan") :]
        if suffix.isdigit():
            ids.append(int(suffix))
    return [f"{n:02d}" for n in sorted(ids)]


def write_chapter(ch: str, det: str, pairs: list[tuple[str, str]]) -> None:
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


def fetch_chapter(
    ch: str,
    *,
    delay_between_requests_sec: float,
    timeout: int,
) -> None:
    src = NEW_ORTHO / f"manannan{ch}.md"
    if not src.is_file():
        raise FileNotFoundError(f"Missing {src}")

    text = src.read_text(encoding="utf-8")
    shielded, mapping = shield_markdown(text)
    print(
        f"POSTing chapter {ch} {src.relative_to(ROOT)} "
        f"({len(shielded.encode('utf-8'))} bytes UTF-8 after shield)..."
    )
    det, pairs = standardize_irish_long(
        shielded,
        timeout=timeout,
        delay_between_requests_sec=delay_between_requests_sec,
    )
    det = unshield(det, mapping)
    write_chapter(ch, det, pairs)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument(
        "--chapter",
        help="Two digits, e.g. 01 (reads manannan01.md)",
    )
    g.add_argument(
        "--all",
        action="store_true",
        help="Process every manannanNN.md under new-orthography (sorted by number).",
    )
    ap.add_argument(
        "--only-missing",
        action="store_true",
        help="With --all, skip chapters that already have spelling/manannanNN.md.",
    )
    ap.add_argument(
        "--delay",
        type=float,
        default=5.0,
        metavar="SEC",
        help="Seconds to wait between successive API requests (default: 5). Applies between byte-chunks and between chapters.",
    )
    ap.add_argument(
        "--chapter-delay",
        type=float,
        default=12.0,
        metavar="SEC",
        help="Extra seconds to wait after finishing one chapter before starting the next, when using --all (default: 12).",
    )
    ap.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="Per-request socket timeout in seconds (default: 120).",
    )
    args = ap.parse_args()

    delay_req = max(0.0, args.delay)
    delay_ch = max(0.0, args.chapter_delay)

    try:
        if args.chapter is not None:
            ch = args.chapter.strip().zfill(2)
            fetch_chapter(
                ch,
                delay_between_requests_sec=delay_req,
                timeout=args.timeout,
            )
            return 0

        prior_completed = False
        for ch in list_chapter_ids():
            out_md = SPELLING_OUT / f"manannan{ch}.md"
            if args.only_missing and out_md.is_file():
                print(f"skip chapter {ch} (already exists: {out_md.relative_to(ROOT)})")
                continue
            if prior_completed:
                gap = delay_req + delay_ch
                if gap > 0:
                    print(f"waiting {gap:.1f}s before chapter {ch}...")
                    time.sleep(gap)
            fetch_chapter(
                ch,
                delay_between_requests_sec=delay_req,
                timeout=args.timeout,
            )
            prior_completed = True
    except Exception as e:
        print(f"Stopped: {e}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
