# -*- coding: utf-8 -*-
"""Grapheme pass: Irish seanchló (ponc séimhithe) → Roman lenition (h digraphs).

Used as step 1 when building new-orthography from old-orthography.  No spelling /
Caighdeán normalisation here — only letter-shape mapping.
"""

from __future__ import annotations

# Order: single-codepoint dotted letters → two-character Roman forms.
_CLO_TO_ROMAN: tuple[tuple[str, str], ...] = (
    ("ḃ", "bh"),
    ("Ḃ", "Bh"),
    ("ċ", "ch"),
    ("Ċ", "Ch"),
    ("ḋ", "dh"),
    ("Ḋ", "Dh"),
    ("ḟ", "fh"),
    ("Ḟ", "Fh"),
    ("ġ", "gh"),
    ("Ġ", "Gh"),
    ("ṁ", "mh"),
    ("Ṁ", "Mh"),
    ("ṗ", "ph"),
    ("Ṗ", "Ph"),
    ("ṡ", "sh"),
    ("Ṡ", "Sh"),
    ("ṫ", "th"),
    ("Ṫ", "Th"),
)


def apply_clo_to_roman(text: str) -> str:
    """Replace dotted lenition letters with standard Irish Roman digraphs."""
    for dotted, roman in _CLO_TO_ROMAN:
        text = text.replace(dotted, roman)
    return text
