# -*- coding: utf-8 -*-
"""Call Cadhan Intergaelic / Irish standardizer HTTP API (stdlib only).

API: https://github.com/kscanne/caighdean/blob/master/API.md
"""

from __future__ import annotations

import json
import re
import urllib.error
import urllib.parse
import urllib.request

API_URL = "https://cadhan.com/api/intergaelic/3.0"
MAX_REQUEST_BYTES = 15000

_MARK_LINE = re.compile(r"^\[l\.(\d+)\]:\s*#\s*$")
# Markdown line that is only hashes and whitespace (no title text) — still shield.
_BLANK_HEADING_LINE = re.compile(r"^#+\s*$")


def _is_hashes_only(s: str) -> bool:
    return bool(s) and all(c == "#" for c in s)


def unescape_token(s: str) -> str:
    return s.replace("\\n", "\n").replace("\\t", "\t")


def shield_markdown(text: str) -> tuple[str, dict[str, str]]:
    """Replace only lines the API reliably mangles: page markers and blank # lines.

    Real headings such as ``# Pláinéid …`` are left unchanged so they are
    standardised with the rest of the text.
    """
    mapping: dict[str, str] = {}
    n = 0
    out_chunks: list[str] = []
    for line in text.splitlines(keepends=True):
        bare = line[:-1] if line.endswith("\n") else line
        if _MARK_LINE.match(bare) or _BLANK_HEADING_LINE.match(bare):
            n += 1
            key = f"___MANANPH_{n:05d}___"
            mapping[key] = bare + "\n"
            out_chunks.append(key + "\n")
        else:
            out_chunks.append(line)
    return "".join(out_chunks), mapping


def unshield(text: str, mapping: dict[str, str]) -> str:
    for key in sorted(mapping.keys(), key=len, reverse=True):
        text = text.replace(key + "\n", mapping[key])
        text = text.replace(key, mapping[key].rstrip("\n"))
    return text


def standardize_irish(teacs: str, timeout: int = 120) -> list[tuple[str, str]]:
    data = urllib.parse.urlencode({"teacs": teacs, "foinse": "ga"}).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=data,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        raise RuntimeError(
            f"Caighdeán API HTTP {e.code}: "
            f"{e.read().decode('utf-8', errors='replace')[:500]}"
        ) from e
    raw = json.loads(body)
    out: list[tuple[str, str]] = []
    for item in raw:
        if isinstance(item, (list, tuple)) and len(item) == 2:
            out.append((str(item[0]), str(item[1])))
        else:
            raise ValueError(f"Unexpected pair shape: {item!r}")
    return out


def detokenize_target(pairs: list[tuple[str, str]]) -> str:
    if not pairs:
        return ""
    bits: list[str] = []
    for i, (s_raw, t_raw) in enumerate(pairs):
        s = unescape_token(s_raw)
        t = unescape_token(t_raw)
        if i == 0:
            bits.append(t)
            continue
        s_prev = unescape_token(pairs[i - 1][0])
        add_space = True
        if s.startswith("\n") or s_prev.endswith("\n"):
            add_space = False
        elif s and s[0] in ".,;:!?)]}»…":
            add_space = False
        elif s_prev.endswith("(") or s_prev.endswith("["):
            add_space = False
        elif not s.strip():
            add_space = False
        elif s_prev and s_prev[-1] in "\"\u201d\u2019" and s and s[0].isalpha():
            # Closing straight/curly quote before a word (e.g. …,” as …).
            add_space = True
        elif s_prev.endswith(",") and s and s[0] == '"':
            add_space = False
        elif s_prev.endswith(",") and s and s[0].isalpha():
            add_space = True
        elif s_prev and s_prev[-1] in ".!?;:" and s and s[0].isalpha():
            add_space = True
        elif s_prev and s_prev[-1] in "([{«":
            add_space = False
        elif _is_hashes_only(s_prev) and s and s[0].isalpha():
            # ATX markdown: ``#`` / ``##`` token run before title word.
            add_space = True
        if add_space and bits and not bits[-1].endswith("\n"):
            prev_out = bits[-1]
            if s and s[0].isalnum():
                if prev_out[-1].isalnum() or prev_out[-1] in "'’-":
                    bits.append(" ")
                elif prev_out[-1] in "\"'.!?;:)]}\"»\u201d\u2019":
                    bits.append(" ")
                elif _is_hashes_only(prev_out):
                    bits.append(" ")
        bits.append(t)
    return "".join(bits)


def chunk_by_bytes(text: str, max_bytes: int = MAX_REQUEST_BYTES) -> list[str]:
    lines = text.splitlines(keepends=True)
    chunks: list[str] = []
    cur: list[str] = []
    cur_sz = 0
    for line in lines:
        b = len(line.encode("utf-8"))
        if cur_sz + b > max_bytes and cur:
            chunks.append("".join(cur))
            cur = [line]
            cur_sz = b
        else:
            cur.append(line)
            cur_sz += b
    if cur:
        chunks.append("".join(cur))
    return chunks


def standardize_irish_long(text: str, timeout: int = 120) -> tuple[str, list[tuple[str, str]]]:
    chunks = chunk_by_bytes(text)
    all_pairs: list[tuple[str, str]] = []
    det_parts: list[str] = []
    for ch in chunks:
        pairs = standardize_irish(ch, timeout=timeout)
        all_pairs.extend(pairs)
        det_parts.append(detokenize_target(pairs))
    return "".join(det_parts), all_pairs


def differing_pairs(pairs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    return [(s, t) for s, t in pairs if s != t]


def pairs_to_tsv(pairs: list[tuple[str, str]]) -> str:
    lines = ["source\ttarget"]
    for s, t in pairs:
        lines.append(
            s.replace("\t", " ").replace("\n", "\\n")
            + "\t"
            + t.replace("\t", " ").replace("\n", "\\n")
        )
    return "\n".join(lines) + "\n"
