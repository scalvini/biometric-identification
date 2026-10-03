# Interface guide

> **Version:** 1.0
> **Last updated:** 3 October 2026

This document describes the two interfaces through which the project is published. The page presents the corpus and the textual analysis in a web browser, and the repository on GitHub holds the page together with the data, scripts, prompts and documentation from which it is built. Sections 1 to 5 explain how to read the page, and section 6 explains how to use the repository. Sections 7 to 9 describe how the page is built from its sources, and how it is published and kept up to date. The README gives an overview of the study, and `data-and-scripts.md` describes the formats of the data files and the build scripts.

| Interface | Address |
|---|---|
| The page | https://scalvini.eu/biometric-identification/ |
| The repository | https://github.com/scalvini/biometric-identification |

## 1. Opening the page

The page is a single file, `index.html`, which contains both its data and its code, so it opens in any current browser without a server or an installation. A copy downloaded from the repository opens in the same way from the computer's own disk, also without an internet connection. When it is online, the page loads its fonts from Google Fonts, and when it is offline it uses the fonts of the system. The page makes no other request to the internet, and the only setting that it keeps in the browser is the measure chosen in the Terms tab.

In this document, to select an element means to click it or, on a touch screen, to tap it. On a narrow screen, such as that of a phone, the tabs wrap onto several lines, and the filters of the Texts tab are folded under the heading "Filters", which opens when it is selected.

### Links to a tab

The address bar shows the name of the open tab after the sign #, so a copied address reopens the page on the same tab. The address https://scalvini.eu/biometric-identification/#texts, for example, opens the Texts tab, and the table below gives the name of each tab. The page reads this name when it opens, and it shows the Ledger when the name is not recognised. Links made with the earlier name of the Corpus construction tab still open that tab.

| Tab | Name after # |
|---|---|
| Ledger | `ledger` |
| Timeline | `timeline` |
| Core corpus | `core` |
| Dataset | `dataset` |
| Corpus construction | `construction` |
| Texts | `texts` |
| Matrix | `matrix` |
| Across cases | `readings` |
| Terms | `terms` |
| Method | `method` |

## 2. The parts of the page

The top of the page gives the title of the archive and a summary of the study. Below the summary, a coloured bar divides the 83 saved documents by case, and its legend gives the number of documents in each case, whose colour stays the same on every tab. The figures under the legend count the saved documents, the documents of the core corpus, those read in full, the PDFs, the documents not saved, the excerpts analysed and the annotations.

The tabs are arranged in two rows, of which the Corpus row presents the archive of saved documents and the Textual analysis row presents the close reading of the 21 core documents. While a Textual analysis tab is open, a band under the tabs states that the analysis is a provisional first pass and holds the key of the ten categories. Selecting a category in the key opens the Texts tab with that category alone.

### The record panel

Each saved document has a record, which opens in a panel on the right of the page. The record panel opens from a row of the Ledger, a mark of the Timeline, a row of the Core corpus table or the button "Open the record" in the Texts tab. It closes with its Close button, or when the page outside the panel is selected. A note on the document, where there is one, appears above the fields listed below.

| Field | Content |
|---|---|
| doc_id | The identifier of the document, with a Copy button that places it on the clipboard |
| Source | The organisation or outlet that published the document |
| Date | The date of publication, with a note where the date is approximate |
| Class | The document class, with a note where the file name carries another class or where the class is borderline |
| Core | For a document of the core corpus, its position and the button "Open its textual analysis" |
| Status | Whether the document was read in full, or a quotation from it was checked in the copy |
| Address | The address from which the document was saved, which opens in a new browser tab |
| Saved | The batch in which the file was saved |
| Retrieved | The time of retrieval in UTC, or for a PDF a reference to the archive log |
| Copy | The part of the web page that was copied, or the PDF file |
| Size | The size of the file, with its number of words and of pages |
| SHA-256 | The first 16 characters of the hash of the saved file, whose full value is in `data/corpus/archive_manifest.jsonl` |
| Page title | The title of the page as it was saved |

### Keyboard

The page can be used from the keyboard alone, with the keys listed below.

| Key | Effect |
|---|---|
| Tab | Moves through the controls, rows and marks of the page, and reaches the open tab |
| Left and right arrows | On the open tab, open the previous or the next tab across both rows |
| Enter | Opens the selected row, mark or cell |
| Space | Opens the selected row of the Ledger or mark of the Timeline |
| Escape | Closes the record panel and returns to the element from which it was opened |

## 3. The Corpus tabs

### 3.1 Ledger

The Ledger lists the 83 saved documents, one row for each, and selecting a row opens its record. A row gives the date of publication, the case, the class, the title, the source and the doc_id. The labels at the end of the row give the position of the document in the core corpus, and show whether it was read in full or a quotation from it was checked. An asterisk after a date marks an approximate date, and a dashed box around a class marks a file whose name carries another class.

The controls above the list act as described below. Several cases or classes selected together widen the list, and each further control narrows it, while the line above the list gives the number of documents shown.

| Control | Effect |
|---|---|
| Search | Shows the documents whose title, source, doc_id or note contains the words typed |
| Sort | Orders the list from the oldest document, from the newest, or by case and then by date |
| Reset | Clears every control and restores the order from the oldest document |
| Case | Shows the documents of the cases selected |
| Class | Shows the documents of the classes selected, whose full names appear when the pointer rests on their codes |
| Saved | Shows the files saved in one batch |
| Core corpus only | Shows the 21 documents of the core corpus |
| Class to settle | Shows the files whose class differs from the one in their name, or whose class is borderline |

### 3.2 Timeline

The Timeline places each saved document by its date of publication, on one line for each case, from 2023 to 2026. A ring around a mark identifies a document of the core corpus, and a hollow mark shows that the date of the document is approximate. An undated page takes its retrieval date, and a date known only to the month is placed in the middle of that month. Marks that fall close together are moved above or below the line of their case, so that each remains visible. Resting the pointer on a mark shows the date and title of the document with its source, and selecting the mark opens its record.

### 3.3 Core corpus

This tab gives Table 2, the proposed core corpus, in which each case has one row for each position, and selecting the row of a saved document opens its record. Rows in grey italics are positions still without a saved text, and their last column gives the state of the search for each text. The notes under the table define the positions, and `corpus-tables.md` reproduces the table.

### 3.4 Dataset

This tab gives Table 1, which counts the saved documents of each case by class and gives the range of their dates and their languages. The last column of the table gives the number of documents of each case in the core corpus. Two smaller tables count the files by the batch in which they were saved and by the part of the web page that was copied.

### 3.5 Corpus construction

This tab summarises how the corpus was built on 2 and 3 October 2026. It lists the agents that ran in the working sessions, with their effort and what entered the corpus from their reports, and it gives the steps of 3 October in order of time. Two further tables list the documents that could not be saved, with the reason for each, and the conventions still to settle. `corpus-construction.md` records the full procedure, with the prompts and the scripts.

## 4. The Textual analysis tabs

### 4.1 Texts

The Texts tab presents the 79 analysed excerpts of the 21 core documents, grouped by case. The heading of each document gives its case, position, title, date, class, language and doc_id, with the button "Open the record" and a bar that divides its annotations by category. Under the heading, "Voice" states who speaks in the text, and "Textual profile" names the dominant features of the text.

Highlights in the colour of their category mark the annotated spans of each excerpt, and a small number after each span refers to a note below the excerpt, with the notes numbered within each excerpt. Below the excerpt, a gloss gives a working translation where the text is in Malay, and "Context" states where the excerpt stands in its document. Each note gives the category code, the sub-label, the words of the span and the comment. Resting the pointer on a highlight, or selecting it, marks its note, and the same action on a note marks its highlight. On a narrow screen, the selection of a highlight also scrolls the page to its note.

A span nested inside a longer one takes the colour of its own category, and a double underline in the colour of the longer span's category shows the nesting. Positions without a saved text appear as "Not yet found" while every category is selected and the search is empty. The filters on the left act as described below, and the line above the documents gives the number of excerpts and documents shown.

| Control | Effect |
|---|---|
| Case | Shows one case, or all cases |
| Categories | Shows or hides the highlights of each category, and All or None selects every category or none. While only some categories are selected, an excerpt that carries none of them is hidden |
| Search | Shows the excerpts whose text, gloss or context, whose document's title or voice, or whose notes in the selected categories contain the words typed |
| Show | Shows or hides the document profiles, the glosses of the Malay texts and the notes under the excerpts |
| Jump to | Opens a chosen document, with every case and category selected and the search cleared |

### 4.2 Matrix

The Matrix counts the annotated spans of each document in each of the ten categories, with totals for each document and for each category. A darker cell holds a higher count, and a dot marks a category without spans. Selecting a number opens the Texts tab at that document with that category alone. The rows "Not yet found" list the Mizoram positions that still lack a saved text, so that the gaps remain visible.

### 4.3 Across cases

This tab presents seven readings across the cases, numbered R1 to R7, each labelled with the research question or questions on which it bears. Under each reading, a row of buttons names the documents and quotes the words on which the reading rests. Selecting a button opens the Texts tab at the excerpt concerned, with every category selected, and the quoted words stay highlighted for a few seconds.

### 4.4 Terms

The Terms tab counts twelve word families in the full saved text of each core document. The buttons "Per 1,000 words" and "Counts" switch between rates and raw counts, and the browser keeps the choice for the next visit. The shading of a cell compares the documents within its column, so it shows in which documents each term is concentrated. A label under the name of a document marks a choice made in counting it, and resting the pointer on a cell gives the count and the number of words. The notes and the table of patterns below the counts state how each family was counted, and `textual-analysis.md` gives the rules in full.

### 4.5 Method

The Method tab gives one card for each of the ten categories, with the code and name of the category and its page reference in *Analysing Discourse* (Fairclough 2003). Each card then gives the definition of the category, the question that it asks of a text, and the sub-labels used on the page with their counts. The notes under the cards state the scope and the status of the analysis, and they explain how the excerpts were checked, how the highlights and glosses should be read and what the counts measure.

## 5. From a reading to the archive

The page connects each step of the analysis to the evidence on which it rests, so that a claim can be followed back to the saved file. A reading in the Across cases tab opens, through its buttons, the excerpts that support it. Each excerpt was checked word for word against the saved copy of its document. The button "Open the record" gives the address and the time of retrieval of that copy, with the first characters of its SHA-256. The full hash in `data/corpus/archive_manifest.jsonl` identifies the saved file. With the scripts described in the README, a holder of a copy of the archive can therefore confirm that the copy is the file from which the excerpt was taken. In the other direction, the record of a core document opens its analysis through the button "Open its textual analysis".

## 6. The repository on GitHub

The front page of the repository lists its folders and files, and the README appears below them. GitHub shows Markdown files, such as those in `docs/`, as formatted text, and it shows data files and scripts as code with line numbers. It shows `index.html` as code too, because GitHub displays the source of a file, while the page itself opens at its own address. The Raw button of a file shows the file without GitHub's layout, and the download button beside it saves the file.

The link to the commits, at the top of the list of files, opens the history of the repository, with the date and message of each change and the lines that it changed. The History button of a file opens the changes made to that file alone, and the commits made in working sessions with Claude name Claude in their message.

The green Code button offers Download ZIP, which saves the whole repository as one archive, and opening `index.html` in the unpacked folder shows the page. With git installed, the command below copies the repository together with its history.

```bash
git clone https://github.com/scalvini/biometric-identification.git
```

GitHub reads `CITATION.cff` and shows the link "Cite this repository" in the About box on the right of the front page, which gives the citation in APA and BibTeX formats. The saved texts of the corpus are not in the repository, for the reason that the README gives.

## 7. Where each part of the page comes from

`build.sh` builds the page from the sources listed below, and `data-and-scripts.md` describes their formats. Each part of the page is changed in its source and never in `index.html`, because the next build replaces `index.html`.

| Part of the page | Source |
|---|---|
| Title, summary, tab names, the band of the Textual analysis tabs and the footer | `src/assemble.py` |
| The records shown in the Ledger, the Timeline and the record panel | `data/corpus/records.jsonl`, with the titles, sources, core positions, notes and class corrections in `src/corpus/build_docs.py` |
| The rows without a saved text in Core corpus, the dates and languages in Table 1, the tables of Corpus construction and the notes under the tables | `src/corpus/template.html` |
| The excerpts | `data/analysis/excerpts.jsonl` |
| Voices, profiles, contexts, glosses, annotations, readings, categories and the positions without a saved text | `src/analysis/annotations.py` |
| Term counts | `data/analysis/terms.json`, written by `scripts/archive/count_terms.py` |
| Introductions and notes of the Textual analysis tabs, the labels of the Terms tab and the table of patterns | `src/analysis/template.html` |
| Layout, colours and behaviour | The two templates, which `src/assemble.py` joins |

The positions without a saved text are listed twice, in `src/corpus/template.html` for the Core corpus tab and in `src/analysis/annotations.py` for the Texts and Matrix tabs, so a change to them is made in both files.

## 8. Publishing

GitHub Pages publishes the page from the root folder of the main branch, as set under Settings and then Pages in the repository. The author's user site on GitHub, `scalvini.github.io`, uses the domain scalvini.eu, so GitHub serves the page of this repository at scalvini.eu/biometric-identification/. Each push to the main branch publishes the page again, in a run that the Actions tab of the repository lists as "pages build and deployment" and that usually ends within a few minutes. The empty file `.nojekyll` tells GitHub Pages to publish the files as they are, without processing them with Jekyll. GitHub Pages also serves the other files of the repository at their paths under the same address, as plain files, and the README explains where the noindex tag and `robots.txt` take effect.

The file `build/artifact.html` holds the same page as published on claude.ai, where Claude adds its own document head. That copy is visible only to the author unless the author shares it, and it changes only when it is published again from a new build.

## 9. Updating the page

A change to the page follows the steps below.

1. Change the source of the part concerned, as listed in section 7.
2. Run `./build.sh` from the root of the repository. The build stops with a message if an annotated span does not occur in its excerpt or overlaps another span in part.
3. Open `index.html` in a browser and check the tabs that the change concerns.
4. Raise the version number and the date of each document whose content changed, and correct the counts in the README where they changed.
5. Commit the changes and push them to the main branch, which publishes the page again.
6. Publish `build/artifact.html` again, in a session with Claude, to the copy on claude.ai, so that the two copies remain identical.
7. Open the address of the page and reload it, because a browser can show the earlier version for a few minutes.

Steps 2 and 5 use the commands below.

```bash
./build.sh
git add -A
git commit -m "State the change"
git push origin main
```

### Checking that the page matches its sources

A build of an unchanged copy of the repository writes `index.html` and `build/artifact.html` again byte for byte, so that `git status` then reports no change. A build with Python 3.13 on 3 October 2026 reproduced both files exactly, and any reader can therefore confirm that the published page was built from the data and the annotations in the repository. The README describes the further checks against the saved archive, which need a copy of the archive folder.
