# Project backlog

Items to pick up after the old-orthography transcription pass is complete.

## Orthography & language tooling

- [x] **Regenerate new orthography from old (mechanical):** run `python3 caibidlí/conversion/build_new_orthography.py` — see [caibidlí/conversion/README.md](caibidlí/conversion/README.md). Edit [old-orthography](caibidlí/old-orthography/) only; re-run the script instead of duplicating fixes in [new-orthography](caibidlí/new-orthography/).
- [ ] **Convert spelling** to modern Irish (An Caighdeán / new orthography), using a clear repeatable pipeline (extend `build_new_orthography.py --spelling` and [old-to-new-spelling.md](caibidlí/old-to-new-spelling.md); add rules as needed).  
  - Context: [Universal Dependencies — UD_Irish-Cadhan](https://github.com/UniversalDependencies/UD_Irish-Cadhan) is a small pre-standard Irish treebank and documents the usual approach (standardize → modern tools); useful reference for tooling and evaluation, not a drop-in converter for this text.
- [ ] **Spell-check pass**: run the (modernised) text through a **modern Irish spell checker** and review flagged tokens (many will be names, dialect, or intentional forms).

## See also

- [README.md](README.md) — overall plan  
- [caibidlí/old-orthography/WORKFLOW.md](caibidlí/old-orthography/WORKFLOW.md) — current chapter workflow  
- [caibidlí/conversion/README.md](caibidlí/conversion/README.md) — old → new regeneration pipeline  
