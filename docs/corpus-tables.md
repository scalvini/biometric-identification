# Corpus tables

> **Version:** 1.0
> **Last updated:** 3 October 2026

This document is adapted from the working file DC_11 of the article project, version 1.1.

These two tables describe the corpus as it stood on 3 October 2026. Table 1 summarises the dataset of 83 saved documents by case and class. Table 2 lists the proposed core corpus for close analysis: one text for each position in each case, plus four texts for the node. The classes follow the definitions of the April 2026 collection (`BDS_Corpus_Construction_Prompts.md`). Seventeen files carry another class in their file name, and both tables count them under the class those definitions give (note 3).

## Table 1. Dataset by case and document class

| Case | Documents | OC | MC | CS | PA | Dates of the documents | Language | In the core |
|---|---:|---:|---:|---:|---:|---|---|---:|
| Node: UNHCR guidance | 1 | 0 | 0 | 0 | 1 | Undated; current text retrieved in October 2026 | English | 1 |
| Bangladesh (instance of the node) | 5 | 2 | 2 | 1 | 0 | May 2023 to January 2026 | English | 3 |
| Gaza | 20 | 12 | 6 | 2 | 0 | May to September 2025 | English | 5 |
| Malaysia | 28 | 6 | 17 | 4 | 1 | July 2025 to October 2026 | English; Malay (8) | 5 |
| South Africa | 20 | 2 | 9 | 5 | 4 | September 2023 to August 2026 | English | 5 |
| Mizoram, India | 9 | 0 | 9 | 0 | 0 | September 2023 to March 2026 | English | 2 |
| **Total** | **83** | **22** | **43** | **12** | **6** | **May 2023 to October 2026** | | **21** |

*Notes.* OC, organisational communications; MC, media coverage; CS, civil society reports; PA, policy and governance documents. Five documents are PDFs, and the other 78 are web texts saved from the browser with a header that records the address and the time of retrieval. The last column counts the documents proposed for the core corpus in Table 2. Every file is listed with its full SHA-256 in `data/corpus/archive_manifest.jsonl`.

## Table 2. Proposed core corpus

| Case | Position | Document | Date | Class | doc_id |
|---|---|---|---|---|---|
| Node | Standard | UNHCR, *Guidance on Registration and Identity Management*, section 5.2, "Registration as an Identity Management Process" | Undated (retrieved 3 Oct 2026) | PA | 00_OC_2026-10-03_UNHCR_001 |
| Node | Articulation | UNHCR Bangladesh, "Registration Update Exercise Notice" | 2 May 2023 | OC | 06_OC_2023-05-02_UNHCR_005 |
| Node | Articulation | Government of Bangladesh and UNHCR, "Frequently Asked Questions on Improved Data Processing Modalities" | 20 Jan 2026 | OC | 06_OC_2026-01-20_UNHCR_006 |
| Node | Response to refusal | *The Diplomat* (Shafiur Rahman), "UNHCR Defends Biometric Enrollment Push for Rohingya Refugees" | 12 Jun 2025 | MC | 06_MC_2025-06-01_Diplomat_002 |
| Gaza | Sets the condition | Gaza Humanitarian Foundation, "Safe, Transparent Aid for Gaza" (overview memo) | Undated (first copy 8 May 2025) | OC | 09_OC_2025-05-08_GHF_002 |
| Gaza | Runs or backs it | Permanent Representative of Israel, letter to the President of the Security Council (S/2025/313), with Fletcher's letter annexed | 19 May 2025 | OC | 09_OC_2025-05-19_IsraelUN_001 |
| Gaza | Answers contestation | US Embassy Jerusalem, "Ambassador Huckabee's Interview with CBS News" | 8 Aug 2025 | OC | 09_OC_2025-08-08_USEmbassy_001 |
| Gaza | Refuses or contests | UN Geneva press briefing, teleprompter transcript (UNICEF) | 9 May 2025 | OC | 09_OC_2025-05-09_UNGeneva_001 |
| Gaza | Voice of those subject to it | Reuters, "Palestinians rush US-backed aid centre despite concerns over checks" | 28 May 2025 | MC | 09_MC_2025-05-28_Reuters_001 |
| Malaysia | Sets the condition | Ministry of Home Affairs, media statement on the Minister's visit to the Bidor centre | 18 May 2026 | OC | 10_OC_2026-05-18_MOHA_001 |
| Malaysia | Runs or backs it | UNHCR Malaysia, "Important update on Dokumen Pendaftaran Pelarian (DPP) Programme" | 2 Jan 2026 | OC | 10_OC_2026-01-02_UNHCR_001 |
| Malaysia | Answers contestation | Dewan Negara Hansard, sitting of 23 July 2026 | 23 Jul 2026 | PA | 10_OC_2026-07-23_Hansard_001 |
| Malaysia | Refuses or contests | UNHCR, "UNHCR concerned by returns from Malaysia to Myanmar amid ongoing conflict" | 30 Sep 2026 | OC | 10_OC_2026-09-30_UNHCR_004 |
| Malaysia | Voice of those subject to it | *Myanmar Now*, "Myanmar nationals in Malaysia fear arrest and forced return" | 1 Oct 2026 | MC | 10_MC_2026-10-01_MyanmarNow_001 |
| South Africa | Sets the condition | Minister of Social Development, SRD Regulations (GN R2042 of 2022), regulation 4(2) | 2022 (version of 1 Apr 2025) | PA | 11_OC_2025-04-01_SRDRegs_001 |
| South Africa | Runs or backs it | SAnews, "SASSA to introduce biometric enrolment in September" | 25 Aug 2025 | OC | 11_OC_2025-08-25_SAnews_001 |
| South Africa | Answers contestation | Open Secrets, "Digital Profiteers (Part Two)", with a SASSA official on consent | 3 Aug 2026 | CS | 11_PA_2026-08-03_OpenSecrets_001 |
| South Africa | Refuses or contests | High Court, *Institute for Economic Justice v Minister of Social Development* [2025] ZAGPPHC 29 | 23 Jan 2025 | PA | 11_OC_2025-01-23_Judgment_001 |
| South Africa | Voice of those subject to it | GroundUp, "SASSA's new ID verification process sparks alarm" | 19 Jun 2024 | MC | 11_MC_2024-06-19_GroundUp_002 |
| Mizoram | Sets the condition | Ministry of Home Affairs (Delhi), directive on biometrics of Myanmar nationals | 2023 | PA | *Not yet found* |
| Mizoram | Runs or backs it | Government of Mizoram, statement on the enrolment | 2025 | OC | *Not yet found* |
| Mizoram | Answers contestation | Lok Sabha or Rajya Sabha answer on the enrolment | 2023 to 2026 | PA | *Not yet found* |
| Mizoram | Refuses or contests | ThePrint, "'Our blood:' Mizoram won't collect biometric data of Myanmar refugees as ordered by Centre" (the state government's refusal, as reported) | 28 Sep 2023 | MC | 12_MC_2023-09-28_ThePrint_001 |
| Mizoram | Voice of those subject to it | *The Wire* (Myanmar Now report), "Fear, Mistrust Grow as India Collects Biometrics From Myanmar Refugees" | 4 Dec 2025 | MC | 12_MC_2025-12-04_TheWire_001 |

*Notes.*

1. The five positions are: the text that sets the condition; the agency or state that runs or backs it; the official answer to contestation; an institutional refusal or contestation; and a text in which the people subject to the condition speak. The node has three positions of its own: the standard, its articulation in Bangladesh, and the response of an agency to refusal by the people themselves.
2. Twenty-one documents are saved. Three Mizoram texts are still to be found, and the GHF notice of 18 August 2025 on a pilot for reserving parcels is still to be saved. Once saved, that notice joins the Gaza row "Sets the condition", because it is the one GHF text that describes the identification of recipients.
3. The class column applies the April 2026 definitions. Five core documents carry another class in their file names: the UNHCR guidance, the Hansard, the SRD regulations and the judgment are filed as OC and counted as PA, and Open Secrets is filed as PA and counted as CS. The file names are unchanged until the author decides on renaming.
4. *The Diplomat* published "UNHCR Defends Biometric Enrollment Push" on 12 June 2025. The doc_id keeps the date of the corpus record (1 June), as the archive log explains.
5. The other 62 documents form the context corpus. They serve to trace intertextual chains, for example UNICEF's objection as rendered by UN News and by the UN Geneva summary, and to check dates and facts.
