# Manannán

*[Manannán](https://www.isfdb.org/cgi-bin/pl.cgi?584553)* written in 1940 by [Máiréad Ní Ghráda](https://www.dib.ie/biography/ni-ghrada-mairead-a6187). An Irish-language young adult sci-fi space travel book. Contains one of the first uses of a [mecha](https://en.wikipedia.org/wiki/Mecha) outside of Japan and the first mention of a [gravity assist](https://en.wikipedia.org/wiki/Gravity_assist) in literature. 

The book has never been reprinted or translated. This digitisation project aims to make the book more accessible and widely read. The text used the old [Irish orthography](https://en.wikipedia.org/wiki/Irish_orthography) (dot over the letter = h after the letter, etc.).

![Manannán cover](assets/manannan.jpg)

## Clár an Leabhair (Table of Contents)

| #  | Chapter | Original | Modern | Pages | PDF |
|----|---------|----------|--------|-------|-----|
|    | Cover | — | — |  | [PNG](assets/manannan.png) |
| 0  | Front matter | [Front matter](caibidlí/old-orthography/manannan00.md) | — | 1–8 | [PDF](caibidlí/manannan00.pdf) |
| 1  | A Planet No Human Eye Had Ever Seen Before | [Pláinéid ná Feaca Súil Duine riaṁ](caibidlí/old-orthography/manannan01.md "A Planet No Human Eye Had Ever Seen Before") | [Pláinéid nach bhFaca Súil Duine riamh](caibidlí/spelling/manannan01.md "A Planet No Human Eye Had Ever Seen Before") | 9–17 | [PDF](caibidlí/manannan01.pdf) |
| 2  | The View through the Telescope | [An Raḋarc tríd an gCiandracán](caibidlí/old-orthography/manannan02.md "The View through the Telescope") | — | 18–30 | [PDF](caibidlí/manannan02.pdf) |
| 3  | The Journey to Manannán | [An Turas go Manannán](caibidlí/old-orthography/manannan03.md "The Journey to Manannán") | — | 31–43 | [PDF](caibidlí/manannan03.pdf) |
| 4  | Manannán | [Manannán](caibidlí/old-orthography/manannan04.md "Manannán") | — | 44–52 | [PDF](caibidlí/manannan04.pdf) |
| 5  | The People of Manannán | [Muintear Manannáin](caibidlí/old-orthography/manannan05.md "The People of Manannán") | — | 53–67 | [PDF](caibidlí/manannan05.pdf) |
| 6  | The Cráidhmí | [Na ‘Cráiḋmí’](caibidlí/old-orthography/manannan06.md "The Cráidhmí") | — | 68–75 | [PDF](caibidlí/manannan06.pdf) |
| 7  | The High-Master | [An tÁrd-Ṁáiġistir](caibidlí/old-orthography/manannan07.md "The High-Master") | — | 76–86 | [PDF](caibidlí/manannan07.pdf) |
| 8  | The Prison | [An Priosún](caibidlí/old-orthography/manannan08.md "The Prison") | — | 87–97 | [PDF](caibidlí/manannan08.pdf) |
| 9  | The Night in the Woods | [Oiḋċe sa Ċoill](caibidlí/old-orthography/manannan09.md "The Night in the Woods") | — | 98–109 | [PDF](caibidlí/manannan09.pdf) |
| 10 | The Engine | [An tInneall](caibidlí/old-orthography/manannan10.md "The Engine") | — | 110–123 | [PDF](caibidlí/manannan10.pdf) |
| 11 | The Night of all Nights | [Oiḋċe ṫar Oiḋċeanta](caibidlí/old-orthography/manannan11.md "The Night of all Nights") | — | 124–136 | [PDF](caibidlí/manannan11.pdf) |
| 12 | Lugh of the Long Arm | [‘Luġ Láṁ-ḟada’](caibidlí/old-orthography/manannan12.md "Lugh of the Long Arm") | — | 137–150 | [PDF](caibidlí/manannan12.pdf) |
| 13 | The Fight with the Cráidhmí | [An Tróid leis na ‘Cráiḋmí’](caibidlí/old-orthography/manannan13.md "The Fight with the Cráidhmí") | — | 151–165 | [PDF](caibidlí/manannan13.pdf) |
| 14 | Revenge | [Díoġaltas](caibidlí/old-orthography/manannan14.md "Revenge") | — | 166–177 | [PDF](caibidlí/manannan14.pdf) |
| 15 | The Escape | [An tÉalóḋ](caibidlí/old-orthography/manannan15.md "The Escape") | — | 178–188 | [PDF](caibidlí/manannan15.pdf) |

**Original** — [`caibidlí/old-orthography/`](caibidlí/old-orthography/): PDF-faithful transcription (old orthography). **Modern** — [`caibidlí/spelling/`](caibidlí/spelling/): same text after a [grapheme pass](caibidlí/conversion/build_new_orthography.py) to [`caibidlí/new-orthography/`](caibidlí/new-orthography/) and then the [Cadhan Intergaelic](https://cadhan.com/) standardiser (chapters show a link when `spelling/manannanNN.md` exists; others are pending).

## How to Help

Read the **Modern** (spelling-corrected) version linked in the table of contents above ([`caibidlí/spelling/`](caibidlí/spelling/)). If you find errors, say so in **chat** (here or wherever we are talking) and the text will be updated from that. If you are comfortable with Git, a **pull request** with edits is welcome too. Corrections are especially welcome from Irish speakers.

## Plan
1. Accurate transcription of the PDF in old orthography
2. Adapt to new orthography and An Caighdeán Oifigiúil — see **[TODO.md](TODO.md)** for next steps (spelling conversion, [UD_Irish-Cadhan](https://github.com/UniversalDependencies/UD_Irish-Cadhan) as reference context, modern spell-check pass)

## Old-orthography chapter workflow

Step-by-step checklist for proofreading each chapter against its PDF (page markers, OCR scans, human approval gates, and git hygiene):

- **[WORKFLOW.md](caibidlí/old-orthography/WORKFLOW.md)** — repeatable chapter checklist
- **[AGREED_FIXES.md](caibidlí/old-orthography/AGREED_FIXES.md)** — recurring OCR / transcription fixes to apply consistently

## Errors

Errors are where the extract makes a spelling error. Do not worry about the page numbers and book name being present. These are easy to take out later and help keep track of where we are in the book for combining the text together later.

## Formatting

We are lightly formatting the text files in [Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github) format. 

* Keep original line breaks to make it easier to compare side by side with PDF
* Rejoin words that were hyphenated
* Leave a blank line between paragraphs
* Remove spaces between punctuation and words e.g. `“ An mar sin é ? ” arsa an garsún` becomes `“An mar sin é?” arsa an garsún`.

Mark page numbers  with a reference like this `[l.31]: #` for *leathanach 31*. This is a Markdown reference that will be hidden if the text is converted to HTML or ePUB. Leave a blank line before the page number reference. By convention, a blank line *after* the page number reference means that the following text is a new paragraph; no blank line after means that the following text runs on from the previous page. We are not currently using these references but they are useful to keep track when editing and would allow us to include print edition page numbers in output formats.


## Contents of This Repo

### Text layers (`caibidlí/`)

- **Old** — [`caibidlí/old-orthography/`](caibidlí/old-orthography/): transcription from the PDF, aiming to match the printed text as closely as possible (including old Irish orthography).
- **New** — [`caibidlí/new-orthography/`](caibidlí/new-orthography/): same text after replacing old-style characters with modern equivalents (mechanical / grapheme pass from Old).
- **Spell** — [`caibidlí/spelling/`](caibidlí/spelling/): starting from New, spelling updated using suggestions from the [caighdean](https://github.com/kscanne/caighdean) engine (via Cadhan [Intergaelic](https://cadhan.com/api/intergaelic/3.0); see [API.md](https://github.com/kscanne/caighdean/blob/master/API.md)), plus **reader-submitted fixes** applied on top where the automatic output is wrong.

Chapter PDFs live under `caibidlí/` (e.g. `manannan01.pdf`). Conversion scripts are in [`caibidlí/conversion/`](caibidlí/conversion/) (e.g. [`build_new_orthography.py`](caibidlí/conversion/build_new_orthography.py), [`fetch_caighdean_chapter.py`](caibidlí/conversion/fetch_caighdean_chapter.py)).

### Assets

- **Manannán_pages_1-20.pdf** — PDF, pages 1–20 (the full 188-page scan exceeds GitHub’s file size limit)
- **Manannán_09-13.txt** — Extracted and corrected text, pages 9–13
- **Manannán_13-18.txt** — Extracted and corrected text, pages 13–18
- **Manannán_15-20_tg.txt** — pages 15–20
- **Manannán.jpg** — JPEG of the cover
- **Manannán.png** — lossless high-resolution PNG of the cover

Pages 9–18 overlap with the opening of the first chapter; page 13 appears in more than one extract as a transition.

### epub

- Scripts and files to build an EPUB
