# Biometric Identification

> **Version:** 1.0
> **Last updated:** 3 October 2026

This repository holds the corpus archive and the textual analysis for a study of biometric identification as a condition of assistance, by Dr Marco Scalvini (University of the Arts London). The study is a critical discourse analysis, in which UNHCR's identity-management guidance is read as the node, and Bangladesh as the place where that guidance is articulated most fully. Four disputes from 2023 to 2026, in Gaza, Malaysia, South Africa and Mizoram (India), are read as its recontextualisations. The textual analysis was carried out on the 21 saved core texts, at the first of the three dimensions in Norman Fairclough's framework.

The article is in preparation, and the textual analysis is a provisional first pass.

## The page

`index.html` is a single self-contained page that opens in any browser. Its tabs form two groups.

| Group | Tabs |
|---|---|
| Corpus | Ledger, Timeline, Core corpus, Dataset, Corpus construction |
| Textual analysis | Texts, Matrix, Across cases, Terms, Method |

A record in the corpus opens its textual analysis, and each analysed document opens its record. The page loads its fonts from Google Fonts and uses system fonts when it is offline.

## Contents

| Path | What it holds |
|---|---|
| `index.html` | The page, as a complete HTML document |
| `build/artifact.html` | The same page as published to claude.ai, which adds its own document head |
| `data/corpus/` | The records of the 83 saved files, with the size and full SHA-256 of each file |
| `data/analysis/` | The 80 verified excerpts, the term counts and the built analysis data |
| `src/` | The two page templates, the annotations and the build scripts |
| `scripts/collection/` | The scripts used to save, download, hash and check the corpus |
| `scripts/archive/` | The scripts that check the archive and the excerpts against the saved files |
| `prompts/` | The prompts given to the search agents, and the queries of the case search |
| `docs/` | The documentation listed below |
| `build.sh` | Rebuilds the data and the page |
| `robots.txt` | Asks crawlers not to index a website built from this repository |

## The corpus

| Group | Saved documents | In the core corpus |
|---|---:|---:|
| Node: UNHCR guidance | 1 | 1 |
| Bangladesh (instance of the node) | 5 | 3 |
| Gaza | 20 | 5 |
| Malaysia | 28 | 5 |
| South Africa | 20 | 5 |
| Mizoram, India | 9 | 2 |
| **Total** | **83** | **21** |

The saved texts are not in this repository, because most of them are under copyright. The author holds them, and `data/corpus/archive_manifest.jsonl` gives the size and SHA-256 of every file, checked on 3 October 2026, so that any copy can be verified. The doc_id format and the document classes follow Prompt A of the April 2026 collection, which is included in `docs/archive/`.

## The textual analysis

Seventy-nine excerpts, each checked word for word against the saved copies, carry 247 annotated spans in ten categories taken from Fairclough's *Analysing Discourse* (2003). Each document has a textual profile, and seven readings across the cases address the article's two research questions. The term counts show how twelve word families are distributed across the 21 texts. `docs/textual-analysis.md` describes the method and its limits.

## Documentation

| File | Content |
|---|---|
| `docs/corpus-construction.md` | How the corpus was built on 2 and 3 October 2026, with the agents, prompts, queries, scripts and conventions |
| `docs/corpus-tables.md` | The dataset by case and class, and the proposed core corpus |
| `docs/textual-analysis.md` | The scope, categories, procedure and limits of the textual analysis |
| `docs/data-and-scripts.md` | The data files, the rebuild and the checks against the archive |
| `docs/archive/ARCHIVE_LOG.md` | The archive log, version 1.5, copied unchanged from the archive folder |
| `docs/archive/BDS_Corpus_Construction_Prompts.md` | The prompts of the April 2026 collection for an earlier design of the project, copied unchanged. Its Prompt A defines the doc_id and the classes used here |

## Rebuilding and checking

```bash
./build.sh
```

The build needs Python 3.9 or later and no other package. It rewrites `data/corpus/docs.json`, `data/analysis/payload.json`, `build/artifact.html` and `index.html`, and it stops if any annotated span is missing from its excerpt.

With the archive folder and pypdf (`pip install pypdf`), three scripts check the archive itself.

```bash
A="path/to/BDS_Corpus_Archive"
python3 scripts/archive/check_hashes.py "$A" data/corpus/archive_manifest.jsonl
python3 scripts/archive/verify_excerpts.py "$A" data/analysis/excerpts.jsonl
python3 scripts/archive/count_terms.py "$A" data/analysis/excerpts.jsonl > /tmp/terms.json
```

On 3 October 2026 they reported 83 files unchanged and 78 excerpts found exactly. The other 2 excerpts, from a PDF, were found once the spaces that text extraction inserts inside words were removed, and the term counts were identical to `data/analysis/terms.json`.

## Use of AI

The corpus was collected and the page was built in working sessions with Claude, a model by Anthropic, under the author's direction. Search agents read web pages and reported back in text. Every file was saved after the author's approval, and every quotation was checked against the saved copies. `docs/corpus-construction.md` records the agents and their prompts, and the glosses of the two Malay texts are working translations prepared with Claude.

## Copyright and indexing

The excerpts are short quotations for criticism and review, and copyright in them remains with their authors and publishers. The code and the documentation are © 2026 Marco Scalvini, and no licence is granted at present. The `robots.txt` file and the `noindex` tag in `index.html` ask search engines not to index a website built from this repository. They do not govern the repository pages on github.com, which GitHub serves under its own rules.

## Citation

`CITATION.cff` gives the citation details.
