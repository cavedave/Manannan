# Old → new orthography pipeline

**Source of truth:** [`../old-orthography/`](../old-orthography/) — fix transcription and page markers there only.

**Generated output:** [`../new-orthography/`](../new-orthography/) — recreate with the script below; avoid hand-editing for anything the pipeline can redo.

## Regenerate all chapters

From the repository root:

```bash
python3 caibidlí/conversion/build_new_orthography.py
```

This runs **step 1 (grapheme pass):** dotted lenition letters (ḃ ċ …) → Roman `bh`, `ch`, … — see [`grapheme_pass.py`](grapheme_pass.py). Only `manannan00.md`–`manannan15.md` are copied (not `*.annotated.md` or other side files).

Optional **step 2 (small approved word list):** whole-word replacements from [`../old-to-new-spelling.md`](../old-to-new-spelling.md):

```bash
python3 caibidlí/conversion/build_new_orthography.py --spelling
```

Add rows to that markdown table as you approve pairs; re-run with `--spelling` when you want them applied. Longer entries are applied before shorter ones.

## What is not automated yet

- Full **An Caighdeán** lexical normalisation (beyond the small table).
- **Proofreading** and PDF alignment — still human work on `old-orthography/`.
