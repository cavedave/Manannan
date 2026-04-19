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

## Spelling layer (new → Cadhan API → `spelling/`)

From the repo root, one chapter (network required):

```bash
python3 caibidlí/conversion/fetch_caighdean_chapter.py --chapter 01 --delay 5
```

All chapters, skipping ones already in `spelling/`, with pauses between requests and between chapters (polite to the server):

```bash
python3 caibidlí/conversion/fetch_caighdean_chapter.py --all --only-missing --delay 5 --chapter-delay 15
```

On HTTP errors, empty API responses, or bad JSON, the script exits and does not continue. Chunk size is capped in [`caighdean_api.py`](caighdean_api.py) so POST bodies stay under server limits.

## What is not automated yet

- **Proofreading** and PDF alignment — still human work on `old-orthography/`.
