# Data and scripts

> **Version:** 1.0
> **Last updated:** 3 October 2026

This document describes the data files and the scripts of the repository.

## Data files

### data/corpus/records.jsonl

Each line is a JSON array for one saved file, with eleven fields in the order below. `src/corpus/build_docs.py` reads it.

| Position | Field |
|---:|---|
| 1 | doc_id |
| 2 | folder |
| 3 | type, txt or pdf |
| 4 | page title |
| 5 | address |
| 6 | retrieval time |
| 7 | element copied |
| 8 | size in bytes |
| 9 | first 16 characters of the SHA-256 |
| 10 | words |
| 11 | pages |

### data/corpus/archive_manifest.jsonl

One JSON object for each saved file, with doc_id, folder, file, type, bytes, sha256 (full), retrieved and url. The hashes and sizes were recomputed from the archive on 3 October 2026. `scripts/archive/check_hashes.py` reads it.

### data/corpus/docs.json

The records shown in the corpus part of the page, built by `src/corpus/build_docs.py`.

| Field | Meaning |
|---|---|
| id, folder, ck, case | doc_id, archive folder, case key and case name |
| cls, conv, convb, convnote | Class in the file name, the class that Prompt A gives where it differs, a borderline alternative, and a note |
| date, approx | Date in the doc_id, and a note where the date is approximate |
| src, title, raw | Source, display title and the page title as saved |
| url, retr, copy | Address, retrieval time and the element copied |
| bytes, sha, words, pages | Size, first 16 characters of the SHA-256, words and pages |
| batch | When the file was saved (b1 to b4) |
| read, checked | Read in full, or a quotation checked in the copy |
| core, note | Position in the core corpus, and a note on the document |

### data/analysis/excerpts.jsonl

Each line is a JSON array for one excerpt, with the fields below. The file is identical to the one checked against the archive with `scripts/archive/verify_excerpts.py`.

| Position | Field |
|---:|---|
| 1 | index |
| 2 | path in the archive |
| 3 | text of the excerpt |

### data/analysis/terms.json

This file holds the output of `scripts/archive/count_terms.py`, with the names of the twelve columns and, for each document, the number of words and the twelve counts. It also records whether Malay patterns were added and which passage was counted, with null where the whole text was counted.

### data/analysis/payload.json

The data of the textual analysis, built by `src/analysis/build.py`.

| Key | Content |
|---|---|
| groups | The six groups of the corpus |
| cats | The ten categories with their page references, definitions and questions |
| docs | The 21 documents with position, class, language, title, voice, profile, term counts and excerpts. Each excerpt carries its text, context, gloss where the text is in Malay, and its annotations with start, end, category, sub-label and note |
| missing | The three Mizoram positions without a saved text |
| readings | The seven readings across the cases, with their evidence as excerpt and span |
| terms, stats | The term names, and the numbers of documents, excerpts and annotations |

## Building the page

`build.sh` runs the scripts in the table below, in order.

| Step | Script | Writes |
|---:|---|---|
| 1 | `src/corpus/build_docs.py` | `data/corpus/docs.json`, from `records.jsonl` |
| 2 | `src/analysis/build.py` | `data/analysis/payload.json`, after checking the annotations in `src/analysis/annotations.py` against `excerpts.jsonl` |
| 3 | `src/assemble.py` | `build/artifact.html` and `index.html`, after joining `src/corpus/template.html` and `src/analysis/template.html` with both data sets |

`build/artifact.html` is identical, byte for byte, to the page published to claude.ai on 3 October 2026. `index.html` holds the same content in a complete HTML document with a robots `noindex` tag.

## Scripts used for the corpus

| Script | Use |
|---|---|
| `scripts/collection/save_page.js` | Saves the open web page as a text file with a header that records its doc_id, address, metadata date, retrieval time and the element copied. It runs in the page, through Claude in Chrome or the browser console |
| `scripts/collection/fetch_un_pdf.js` | Fetches S/2025/313 inside its UN Digital Library record page, which serves the PDF only to a browser |
| `scripts/collection/download_pdfs.sh` | Downloads the four other PDFs with curl |
| `scripts/collection/move_and_hash.sh` | Moves downloaded copies into their folders and lists SHA-256, size and path |
| `scripts/collection/check_quotes.py` | Checks quotations against the saved copies, as used for 22 quotations on 3 October 2026 |
| `scripts/archive/extract_passages.py` | Prints passages around chosen patterns in the 21 core documents, as used to locate candidate excerpts |
| `scripts/archive/verify_excerpts.py` | Checks that every excerpt appears in its saved copy |
| `scripts/archive/count_terms.py` | Counts the twelve word families |
| `scripts/archive/check_hashes.py` | Checks every archive file against the manifest |

The two shell scripts in `scripts/collection/` and `scripts/archive/extract_passages.py` keep the archive path of the author's Mac, because they are the versions that were run. The Python checks take their files as arguments, and the two JavaScript files run inside the page in the browser.

## Prompts

`prompts/` holds the four prompts given to the search agents, whose reports were used to build the corpus, and the 32 queries of the case search. It also holds the template for a further case and a prompt reconstructed for a new session. `docs/corpus-construction.md` gives the context of each.
