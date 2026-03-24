# Old-Orthography Chapter Workflow

Use this checklist for each chapter (`manannanXX.md`) against its source PDF.

## 1) Setup

- [ ] Open chapter markdown file.
- [ ] Open source chapter PDF.
- [ ] Confirm chapter number and output file path.

## 2) Page Markers

- [ ] Add page markers in markdown at true page breaks: `[l.xx]: #`.
- [ ] Keep page marker numbering sequential and unique.
- [ ] Human check marker positions before further edits.

## 3) First Cleanup Pass (Conservative)

- [ ] Remove obvious scan header/footer junk.
- [ ] Fix obvious punctuation spacing noise (for example space before `, . ; : ? !`).
- [ ] Keep old orthography; do not modernize spelling.
- [ ] Preserve paragraph/dialogue structure unless clearly broken by OCR.
- [ ] Find tokens ending with a stray hyphen before a space or punctuation (for example `ḃí-`, `coille-`) — usually a line-break or OCR artifact; merge with the next chunk or remove the hyphen after checking the PDF.

## 4) Pattern Scans

- [ ] Scan for `ii` patterns (possible OCR artifacts).
- [ ] Scan for mid-word capital `L`.
- [ ] Scan for mid-word capitals: `Ḃ Ċ Ḋ Ḟ Ġ Ṁ Ṗ Ṡ Ṫ`.
- [ ] Scan for stray trailing hyphens (see step 3) and for hyphenated line-wrap splits that should be one word (project style: rejoin hyphenated words where the PDF has a normal word).

## 5) Human Approval Gate

- [ ] Propose replacements from pattern scans.
- [ ] Get human accept/reject before applying each replacement group.
- [ ] Apply only approved changes.

## 6) Final Verification

- [ ] Re-run the same scans to confirm fixes are complete.
- [ ] Re-check page marker placement and sequence.
- [ ] Do final read-through for OCR leftovers and formatting consistency.
- [ ] Quick grep for words ending in `-` (before space) to catch any remaining `ḃí-`-style artifacts.

## 7) Learn-As-We-Go Log

- [ ] If a recurring OCR issue appears, add it to `AGREED_FIXES.md`.
- [ ] Keep each new agreed fix concise: `pattern -> fix` with a short note.

## 8) Git Hygiene and Publish

- [ ] Review diff for chapter file only.
- [ ] Commit chapter file with clear message.
- [ ] Push to `main` only after final human confirmation.
- [ ] Do not commit temporary extraction files (for example `*_extracted.txt`).

## Candidate File Rule (Default)

- Default: edit the chapter file directly (no candidate copy required).
- Use a `_candidate` file only when the chapter is messy/high-risk or when requested.
