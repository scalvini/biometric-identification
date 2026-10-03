# Gemini/Claude Prompts for Corpus Construction

Two prompts below. Prompt A builds the full working corpus (including copyrighted materials for personal research use). Prompt B prepares the public deposit version for Harvard Dataverse.

---

## PROMPT A — Working Corpus Construction (Full, Including Copyrighted Materials)

Use this prompt with Claude (web search enabled) or Gemini. Run one case at a time. Paste the case-specific search block at the end.

---

**PROMPT A — CORPUS COLLECTION SESSION**

I am building an empirical corpus for a paper on corporate data infrastructures and data colonialism for *Big Data & Society*. The corpus collects publicly available documents for eight cases of corporate data practice in humanitarian, crisis, and development contexts, organised across four data practices (Analytics, Connectivity, Cloud Infrastructure, Identification) plus one contrast case (Data Labour).

For each case I need four types of documents:

**1. ORGANISATIONAL COMMUNICATIONS (OC):** press releases, CSR reports, programme descriptions, partnership announcements, blog posts, and executive statements from the corporate actor or its institutional partners that frame the data practice in beneficial terms (care, inclusion, connectivity, protection, efficiency, evidence-based decision-making). These are the primary texts through which the legitimating vocabulary is produced.

**2. MEDIA COVERAGE (MC):** news articles, editorials, op-eds, and investigative reporting from English-language outlets (The Guardian, NYT, Washington Post, The Intercept, Wired, MIT Technology Review, The New Humanitarian, Devex, TIME, Al Jazeera, Vice, HuffPost, Context News, Die Zeit English, The Register, TechCrunch, etc.) that report on the data practice. I need BOTH favourable coverage (ratifying the legitimating vocabulary) AND critical coverage (contesting it).

**3. CIVIL SOCIETY REPORTS (CS):** reports, open letters, legal filings, and policy briefs from advocacy organisations (Privacy International, Access Now, Human Rights Watch, Amnesty International, ACLU, EFF, The Engine Room, EDRi, NYU CHRGJ, Foxglove, No Tech for Apartheid, etc.) that contest the corporate actor's data practice.

**4. POLICY AND GOVERNANCE DOCUMENTS (PA):** internal audits, GDPR enforcement decisions, parliamentary testimony, ICJ opinions, regulatory rulings, World Bank frameworks, UNHCR data protection policies, and contract documents (leaked or published) that provide institutional and regulatory context.

---

### For EACH document found, provide ALL of the following fields:

| Field | What to provide |
|---|---|
| doc_id | Format: [CaseNum]_[DocClass]_[YYYY-MM-DD]_[Source]_[NNN]. Example: 02_MC_2024-04-10_TIME_001 |
| case_num | Two-digit case number (01–08) |
| case_name | Case name |
| data_practice | Analytics, Connectivity, Cloud, Identification, or Data Labour |
| doc_class | OC, MC, CS, or PA |
| date | Publication date (YYYY-MM-DD). If only year is known, use YYYY-01-01 |
| source | Publishing organisation or outlet |
| author | Author name(s) if identified |
| title | Full document title |
| url | Original URL (full, clickable) |
| local_format | pdf (if saveable as PDF) or web (if web-only) |
| deposit_status | full_text (if openly available OC/CS/PA) or metadata_only (if copyrighted MC or paywalled) |
| copyright_status | open (corporate press release, open-license CS report), restricted (paywalled news), or unclear |
| analytical_note | 2–3 sentences explaining why this document matters for the article's argument about data colonialism and legitimating discourse. Be specific. Name the legitimating vocabulary used or the contestation ground raised. |

---

### Search thoroughly. For each document type:

**For OC:** Search the corporate actor's press room, blog, and partner announcements. Search for CSR/impact reports. Search for executive speeches and conference presentations. Use multiple queries.

**For MC:** Search news outlets individually. Try at least 4–6 different search queries per case, varying keywords. Search for both favourable and critical coverage. Search specialist outlets (The New Humanitarian, Devex, Context News) as well as general outlets. Prioritise investigative reporting and original sources over aggregated content.

**For CS:** Search the websites of Privacy International, Access Now, HRW, Amnesty, ACLU, EFF, The Engine Room, EDRi, and any case-specific advocacy organisations. Search for open letters and coalition statements.

**For PA:** Search for audit reports, regulatory decisions, parliamentary testimony, and leaked contract documents. Search government and institutional websites.

---

### After searching, produce:

1. **A numbered document list** with all fields above in table format
2. **A CSV-formatted block** I can paste directly into my corpus_metadata.csv spreadsheet
3. **A gap assessment** identifying which document types are underrepresented for this case and suggesting follow-up searches

---

### Case-specific search blocks

Paste ONE of these at the end of the prompt for each session:

**CASE 01 — Palantir–WFP/UNHCR:**
Search for: Palantir WFP partnership, Palantir UNHCR, WFP SCOPE biometric database, WFP SCOPE audit 2017, WFP SCOPE audit 2021, Palantir humanitarian, Palantir ICE immigration, civil society open letter WFP Palantir 65 signatories, Responsible Data community WFP, Privacy International Palantir, Amnesty International Palantir ICE, Access Now Palantir. Date range: 2018–2026.

**CASE 02 — Google/Amazon Project Nimbus:**
Search for: Project Nimbus Google Amazon Israel, Project Nimbus contract, Google Cloud Israel government, No Tech for Apartheid, Google employee protest Nimbus, Google fired employees Nimbus, Project Nimbus Ministry of Defence, Project Nimbus human rights, BSR Google Nimbus consultant, No Azure for Apartheid Microsoft, Abolitionist Law Center Nimbus, ICJ advisory opinion corporations occupation. Date range: 2021–2026.

**CASE 03 — Meta/Facebook Free Basics:**
Search for: Facebook Free Basics India, Internet.org launch, Free Basics Africa, Save the Internet India net neutrality, TRAI differential pricing ruling 2016, Zuckerberg Free Basics Times of India, Andreessen anti-colonialism tweet, Free Basics digital colonialism, Free Basics zero-rating, WhatsApp data colonialism Global South, Facebook Free Basics 32 countries Africa. Date range: 2013–2026.

**CASE 04 — SpaceX Starlink:**
Search for: Starlink Ukraine activation, Musk Starlink humanitarian, Starlink Crimea geofencing, SpaceX Pentagon Starlink funding, Starlink sovereign dependency Ukraine, Starlink disaster response, Starlink humanitarian marketing, Walter Isaacson Starlink Musk decision. Date range: 2022–2026.

**CASE 05 — Microsoft Azure / Cloud Sovereignty:**
Search for: Microsoft AI for Humanitarian Action, Microsoft Azure UNHCR, Microsoft Azure humanitarian, CLOUD Act data sovereignty, Microsoft French Senate testimony data sovereignty 2025, AWS European Sovereign Cloud, cloud sovereignty Global South, UN agencies cloud hosting Azure AWS, No Azure for Apartheid, Microsoft sovereign cloud criticism, AWS Bahrain drone strike data centre 2026. Date range: 2018–2026.

**CASE 06 — UNHCR Rohingya Biometrics:**
Search for: UNHCR Rohingya biometric registration Bangladesh, Rohingya data shared Myanmar, Human Rights Watch Rohingya data consent, UNHCR Smart Card Rohingya, Rohingya biometric food aid cut 2025, Access Now UNHCR biometrics Jordan, IrisGuard refugee iris scan, Engine Room Rohingya biometrics, Rohingya ejajot consent, UNHCR data protection policy. Date range: 2017–2026.

**CASE 07 — World Bank ID4D / Aadhaar:**
Search for: World Bank ID4D digital identity, ID4D Aadhaar model, Aadhaar exclusion deaths India, NYU CHRGJ digital road to hell, Access Now open letter World Bank digital ID, Beware of Aadhaar 2025 statement, SDG 16.9 legal identity, Aadhaar National Register Citizens Assam, Reetika Khera Aadhaar, Jean Drèze Aadhaar, ID4D Malawi Kenya Uganda. Date range: 2016–2026.

**CASE 08 — Sama/Meta Content Moderation:**
Search for: Sama Meta content moderation Kenya, Sama ethical AI, Daniel Motaung content moderator, TIME Billy Perrigo content moderation investigation, Foxglove Sama lawsuit, Sama dignified digital work, content moderation labour Global South, Meta content moderation outsourcing Nairobi, Sama ended Meta contract 2023, content moderation data colonialism. Date range: 2019–2026.

---
---

## PROMPT B — Harvard Dataverse Deposit Preparation

Use this prompt with Claude (computer use) or as a manual checklist. Run AFTER the working corpus is complete.

---

**PROMPT B — PREPARE PUBLIC CORPUS FOR HARVARD DATAVERSE**

I have a complete working corpus for my *Big Data & Society* article in the folder `BDS_Corpus/`. The corpus contains approximately [N] documents across eight cases and four data practices. I now need to prepare a public deposit version for Harvard Dataverse that complies with copyright requirements and research data management standards.

---

### Step 1 — Copyright audit

Review every file in `BDS_Corpus/`. Apply the following rules:

**DEPOSIT AS FULL-TEXT PDF (copy to deposit folder):**
- Organisational communications (OC) published on corporate websites, blogs, and press rooms. These are published for public distribution and typically carry no redistribution restriction.
- Civil society reports (CS) published under open licenses (CC BY, CC0) or distributed freely for public advocacy. Most reports from Privacy International, Access Now, Human Rights Watch, Amnesty International, The Engine Room, NYU CHRGJ, and EDRi fall into this category.
- Policy documents (PA) published by governments, international organisations, or regulatory bodies for public access. This includes World Bank publications, UNHCR policy documents, GDPR enforcement decisions, ICJ opinions, and parliamentary testimony transcripts.
- Academic articles (AC) published open access.

**CONVERT TO METADATA-ONLY (do NOT copy PDF to deposit folder):**
- All media coverage (MC) regardless of current paywall status. News organisations retain copyright. Record the full metadata in corpus_metadata.csv.
- Any OC, CS, or PA document where redistribution rights are unclear. When in doubt, metadata-only.
- Academic articles behind paywalls.

For metadata-only entries, the CSV record must include: doc_id, case_num, case_name, data_practice, doc_class, date, source, author, title, url, and an analytical_summary of no more than 50 words.

---

### Step 2 — Build deposit folder structure

Create the following structure:

```
BDS_Corpus_Dataverse/
├── README.md
├── CODEBOOK.md
├── corpus_metadata.csv
├── collection_log.csv
│
├── 01_Palantir_WFP_UNHCR/
│   ├── OC/
│   ├── CS/
│   └── PA/
│
├── 02_Google_Amazon_ProjectNimbus/
│   ├── OC/
│   ├── CS/
│   └── PA/
│
├── 03_Meta_FreeBasics/
│   ├── OC/
│   ├── CS/
│   └── PA/
│
├── 04_SpaceX_Starlink/
│   ├── OC/
│   ├── CS/
│   └── PA/
│
├── 05_Microsoft_Azure_CloudSovereignty/
│   ├── OC/
│   ├── CS/
│   └── PA/
│
├── 06_UNHCR_Rohingya_Biometrics/
│   ├── OC/
│   ├── CS/
│   └── PA/
│
├── 07_WorldBank_ID4D_Aadhaar/
│   ├── OC/
│   ├── CS/
│   └── PA/
│
└── 08_Sama_Meta_ContentModeration/
    ├── OC/
    ├── CS/
    └── PA/
```

Note: No MC/ folders in the deposit version. Media coverage exists only as metadata rows in corpus_metadata.csv.

---

### Step 3 — Update corpus_metadata.csv

Ensure every document in the working corpus has a row in the CSV. The deposit_status column must reflect the copyright audit:
- `full_text` for documents deposited as PDFs
- `metadata_only` for documents recorded as metadata only

Add a column `dataverse_filepath` recording the path within the deposit folder for full_text items, and "N/A" for metadata_only items.

---

### Step 4 — Write README.md

Use this template:

```markdown
# BDS Data Colonialism Corpus

## Overview
This dataset supports the article "[TITLE]" published in 
Big Data & Society.

It contains [N] publicly available documents collected across 
four data practices of corporate data infrastructure in 
humanitarian, crisis, and development contexts (Analytics, 
Connectivity, Cloud Infrastructure, Identification) and 
eight cases, plus one contrast case (Data Labour).

## Contents
- corpus_metadata.csv: Document-level metadata for all [N] items
- CODEBOOK.md: Analytical categories used in framework analysis
- collection_log.csv: Systematic search strategy documentation
- Case folders: Full-text documents organised by case and document type

## Cases

| # | Case | Data Practice | Corporate Actor |
|---|------|--------------|-----------------|
| 01 | Palantir–WFP/UNHCR | Analytics | Palantir Technologies |
| 02 | Google/Amazon Project Nimbus | Analytics | Google, Amazon |
| 03 | Meta Free Basics | Connectivity | Meta/Facebook |
| 04 | SpaceX Starlink | Connectivity | SpaceX |
| 05 | Microsoft Azure / CLOUD Act | Cloud Infrastructure | Microsoft, AWS |
| 06 | UNHCR Rohingya Biometrics | Identification | UNHCR, IrisGuard |
| 07 | World Bank ID4D / Aadhaar | Identification | World Bank, UIDAI |
| 08 | Sama/Meta Content Moderation | Data Labour (contrast) | Sama, Meta |

## Document Types
- OC: Organisational Communications
- MC: Media Coverage (metadata-only due to copyright)
- CS: Civil Society and Advocacy Reports
- PA: Policy and Governance Documents

## File Naming Convention
[CaseNum]_[DocClass]_[YYYY-MM-DD]_[Source]_[BriefDescription].pdf

## Collection Period
[start date] to [end date]

## Copyright Note
This corpus contains only non-copyrighted or openly licensed 
materials as full-text PDFs. Organisational communications 
published for public distribution, openly licensed civil 
society reports, and public policy documents are deposited 
as full-text files. Media coverage is recorded as 
metadata-only entries (title, date, source, URL, analytical 
summary) in corpus_metadata.csv due to copyright restrictions.
Researchers can retrieve media articles through institutional 
database access (e.g., Nexis UK) using the search strings 
documented in collection_log.csv.

## Analytical Framework
Framework analysis (Ritchie and Spencer, 1994). Four coding 
dimensions: legitimating vocabulary, subject position 
production, dependency chain indicators, and contestation 
dynamics. Full definitions in CODEBOOK.md.

## Contact
[Your name]
[Your email]
[Your ORCID]
University of the Arts London / London School of Economics

## License
CC BY 4.0 (Creative Commons Attribution)

## Related Publication
[Paper title]
[Journal: Big Data & Society]
[DOI once assigned]
```

---

### Step 5 — Write CODEBOOK.md

Use this template, adapted from the theoretical framework:

```markdown
# BDS Data Colonialism Corpus — Analytical Codebook

## Analytical Framework
Framework analysis (Ritchie and Spencer, 1994). Categories 
established theoretically prior to analysis, with additional 
categories added during first-stage coding.

## Coding Dimensions

### 1. Legitimating Vocabulary
1.1 Care language (dignity, protection, saving lives, 
    alleviating suffering, humanitarian)
1.2 Inclusion language (connectivity, access, bridging 
    the digital divide, legal identity for all)
1.3 Efficiency language (evidence-based, data-driven, 
    optimisation, scalability, innovation)
1.4 Development language (empowerment, capacity building, 
    sustainable development, SDG alignment)
1.5 Security language (protection, verification, 
    fraud prevention, accountability)

### 2. Subject Position Production
2.1 Subject position named (beneficiary, user, data subject, 
    rights-bearing person, consumer, worker)
2.2 Agency afforded or foreclosed (can the subject contest 
    the terms of the data relationship?)
2.3 Consent structure (informed consent, coerced consent, 
    structural impossibility of refusal)
2.4 Reversibility (can the subject withdraw from the 
    data relationship? Is the data deletable?)

### 3. Dependency Chain Indicators
3.1 Infrastructure reliance (does this data practice depend 
    on infrastructure from another practice in the corpus?)
3.2 Data flow directionality (where does data move? 
    Global South to North? Local to corporate?)
3.3 Jurisdictional exposure (whose law governs the data? 
    US CLOUD Act? GDPR? Host country? None?)
3.4 Lock-in mechanisms (contractual, technical, or 
    structural barriers to switching or withdrawal)

### 4. Contestation Dynamics
4.1 Source of contestation (civil society, employees, 
    affected communities, regulators, media)
4.2 Grounds of contestation (privacy, consent, sovereignty, 
    human rights, labour rights, colonial critique)
4.3 Corporate response to contestation (silence, denial, 
    discursive absorption, reprisal, withdrawal)
4.4 Outcome of contestation (regulation, ban, contract 
    termination, continuation, expansion)

## Cross-Cutting Codes
CC.1 North-South directionality of data flows
CC.2 Consent paradox indicators
CC.3 Infrastructure persistence (does the data practice 
     outlast its original rationale?)
CC.4 Vocabulary of care markers per data practice
```

---

### Step 6 — Harvard Dataverse deposit

**Create a new dataset on Harvard Dataverse** (https://dataverse.harvard.edu/).

**Metadata fields:**

| Field | Value |
|---|---|
| Title | Data Colonialism Corpus: Corporate Data Infrastructures in Humanitarian, Crisis, and Development Contexts (2013–2026) |
| Author | [Your name], ORCID: [Your ORCID] |
| Affiliation | University of the Arts London; London School of Economics |
| Contact email | [Your email] |
| Description | This dataset contains the empirical corpus supporting "[paper title]," published in Big Data & Society. The corpus comprises [N] publicly available documents collected across four data practices of corporate data infrastructure (Analytics, Connectivity, Cloud Infrastructure, Identification) and eight cases. Document types include organisational communications, media coverage metadata, civil society reports, and policy and governance documents. All documents are publicly available materials collected between [dates]. The corpus is organised by data practice and case, with a metadata spreadsheet providing document-level information and a codebook defining the analytical categories applied during framework analysis. A data collection log records the systematic search strategy. For full methodological details, see the associated publication. |
| Subject | Social Sciences |
| Keywords | data colonialism, technocolonialism, digital colonialism, humanitarian technology, corporate data infrastructure, data justice, biometric registration, cloud sovereignty, platform connectivity, data labour, Big Data Society |
| Related publication | IsSupplementTo; [BDS paper DOI once assigned] |
| License | CC BY 4.0 |
| Deposit type | Dataset |

**Files to upload:**
1. `BDS_Corpus_Dataverse.zip` (the entire deposit folder as a ZIP archive)
2. `README.md` (individually, for browser preview)
3. `CODEBOOK.md` (individually, for browser preview)
4. `corpus_metadata.csv` (individually, for browser preview and download)
5. `collection_log.csv` (individually, for browser preview)

**Embargo option:** If you want to embargo the dataset until publication, set the embargo date when creating the dataset. Update the data availability statement in the manuscript accordingly.

---

### Step 7 — Data availability statement for BDS manuscript

Insert before the references:

> The empirical corpus supporting this analysis is publicly available at [DOI] via Harvard Dataverse. The corpus contains organisational communications, media coverage metadata, civil society reports, and policy documents for all eight cases across four data practices. Full-text documents are provided where copyright permits. Metadata records with original URLs are provided for copyrighted media sources.

If embargoed:

> The empirical corpus supporting this analysis will be made publicly available at [DOI] via Harvard Dataverse upon publication.
