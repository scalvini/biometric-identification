# Textual analysis

> **Version:** 1.0
> **Last updated:** 3 October 2026

This document describes the textual analysis shown under the Textual analysis tabs of the page. It is limited to the text, which is the first of the three dimensions in Fairclough's framework, and discourse practice and social practice will be analysed in the article.

## Scope

The textual analysis was carried out on the 21 saved documents of the proposed core corpus (`corpus-tables.md`, Table 2). Section 5.2 of UNHCR's *Guidance on Registration and Identity Management* is the text of the node. Two UNHCR texts from Bangladesh document its articulation there, and a report in *The Diplomat* records the agency's response to refusal. Each of the four cases has the five positions listed in the table below.

| Position | Text |
|---|---|
| Sets the condition | The text that sets the condition |
| Runs or backs it | A text of the agency or state that runs or backs it |
| Answers contestation | The official answer to contestation |
| Refuses or contests | An institutional refusal or contestation |
| Voice of those subject to it | A text in which the people subject to the condition speak |

Three Mizoram positions still lack a saved text and appear on the page as gaps.

## Research questions

- **RQ1.** Whether agencies and governments resolve the consent dilemma when they invoke necessity, or make the people who must choose between being read and being fed responsible for its outcome.
- **RQ2.** What recognition would require of an agency or government faced with such a refusal, and whether those examined here meet that requirement.

## Excerpts

Candidate passages were located with `scripts/archive/extract_passages.py` and chosen for the features listed below. Eighty excerpts were checked word for word against the saved copies with `scripts/archive/verify_excerpts.py`. Seventy-eight were found after Unicode normalisation and the collapsing of whitespace. The other two, from the Malaysian Home Ministry PDF, were found once the spaces that text extraction inserts inside words were removed. The page uses 79 of them, because excerpt 15 is a shorter form of excerpt 63. Quotations from news reports are kept short.

## Categories

| Code | Category | Fairclough (2003) | Question asked of the text |
|---|---|---|---|
| ACT | Social actors | pp. 145 to 150 | Who acts upon whom, and who is absent from the clause? |
| NOM | Nominalisation | pp. 12 to 13, 143 to 144 | Which processes become things, and whose agency disappears with them? |
| MODD | Deontic modality | pp. 167 to 170 | Who is obliged or permitted, and by whom? |
| MODE | Epistemic modality | pp. 167 to 171 | How strongly does the text commit to what it claims? |
| EVAL | Evaluation | pp. 171 to 173 | What is presented as good or bad, and on whose authority? |
| REL | Semantic relations | pp. 89 to 91 | How are refusal and loss connected in the grammar? |
| ASM | Assumptions | pp. 55 to 58 | What must the reader already accept for the sentence to make sense? |
| REP | Reporting and intertextuality | pp. 39 to 51 | Whose words are these, and how close does the text stand to them? |
| LEG | Legitimation | pp. 98 to 100 | On what grounds is the condition justified? |
| LEX | Wording | pp. 129 to 133 | Which words name the people and the place? |

The page references were checked in the book. The Method tab lists the sub-labels used under each category, with their counts.

## Annotation

Each annotation names a span of an excerpt, a category, a sub-label and a note. `src/analysis/annotations.py` holds the annotations, and `src/analysis/build.py` checks that every span occurs in its excerpt and that spans either nest or stay apart, because a partial overlap cannot be displayed. A nested span takes its own colour on the page, and a double underline in the colour of the outer category shows that it sits inside a longer span. Notes are numbered in the order in which their markers appear in the text.

## Profiles and readings

Each document has a short textual profile that names its dominant features. Seven readings across the cases address the research questions, and each links to its evidence in the excerpts. The whole analysis is a provisional first pass, which the author has still to review.

## Term counts

The Terms tab counts twelve word families in the full saved text of each document, below the header that records its address. The counts ignore case and respect word boundaries.

| Column | English pattern | Malay addition |
|---|---|---|
| voluntary | voluntar(y, ily) | sukarela |
| consent | consent(s, ed, ing) | persetujuan |
| refuse | refus(e, es, ed, ing, al, als) | enggan, menolak, penolakan, ditolak |
| verify | verif(y, ies, ied, ying, ication, ications, iable, iably) | pengesahan, mengesahkan, disahkan, verifikasi |
| identity | identit(y, ies) | identiti |
| biometric | biometric(s) | biometrik |
| security | security | keselamatan |
| fraud | fraud and its derivatives, misuse and its derivatives | penipuan, menipu, palsu, penyalahgunaan, menyalahgunakan |
| legitimate | legitima(te, tely, cy) | sah, sahih |
| necessary | necess(ary, arily, ity, ities) | perlu, keperluan, memerlukan |
| required | requir(e, es, ed, ing, ement, ements), mandatory, compulsory, obligatory | wajib, diwajibkan, mandatori |
| protection | protect and its derivatives | perlindungan, melindungi, dilindungi |

The Hansard is counted on the passage of question 6 and its supplementary questions (2,447 words), the part of the sitting that concerns refugees. The UN Geneva file holds the whole briefing, which covers several subjects, and the Huckabee interview covers more than aid. Their rates are therefore lower than those of a text on aid alone. The Malay additions are approximate, because words such as *perlu* and *sah* have wider senses than *necessary* and *legitimate*. Web texts keep some navigation text from the page, which lowers their rates slightly.

## Glosses

The English glosses of the two Malay texts are working translations prepared with Claude for orientation. They should be checked against the original before any quotation in the article.

## Counting annotations

The Matrix tab counts annotated spans. The counts reflect what was selected for annotation as well as what the texts contain, so they serve as a guide to reading.

## Reference

Fairclough, N. (2003) *Analysing Discourse: Textual Analysis for Social Research*. London: Routledge.
