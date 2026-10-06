# BDS Corpus Archive Log

> **Version:** 1.6
> **Last updated:** 6 October 2026

This folder holds saved copies of corpus documents, with one subfolder per case. Each copy is the page text as displayed in Chrome and saved by the browser. Each file starts with a header that gives the corpus doc_id, the URL and the retrieval time. File names follow the corpus doc_id, even where the corpus date is wrong, so that each copy maps to its record.

## Case 06, sources from 2025

| doc_id | Title | Author | Published | Copy | Status |
|---|---|---|---|---|---|
| 06_MC_2025-06-07_Diplomat_001 | No Fingerprint, No Food | Shafiur Rahman | 7 June 2025 | Saved | Read in full |
| 06_MC_2025-06-01_Diplomat_002 | UNHCR Defends Biometric Enrollment Push for Rohingya Refugees | Shafiur Rahman | 12 June 2025 | Saved | Read in full |
| 06_PA_2025-05-22_RefIntl_001 | A Closing Window | Daniel P. Sullivan and Lucky Karim | 22 May 2025 | Saved as web text. The report PDF is linked from the page and was not downloaded. | Read in full |
| 06_MC_2025-06-13_BiometricUpdate_002 | UNHCR biometric verification standoff leaves 400 refugee families off food aid list | Not checked | June 2025 | None | Not read. The site is not allowed in the Chrome extension. |

## Case 06, UNHCR pages saved on 2 October 2026

| doc_id | Title | Published | Copy | Status |
|---|---|---|---|---|
| 06_OC_2023-05-02_UNHCR_005 | Registration Update Exercise Notice | Not stated. The notice gives 2 May 2023 as the start of the exercise. The earliest capture in the Wayback Machine is dated 23 December 2023. | Saved from the Wayback Machine capture of 12 March 2026, because the live address now returns "Page not found" | Read in full |
| 06_OC_2026-01-20_UNHCR_006 | Frequently Asked Questions on Improved Data Processing Modalities between the Government of Bangladesh and UNHCR | 20 January 2026, modified 13 April 2026, according to the public page record of the site | Saved from the live page | Read in full |

Both doc_ids are new, because neither page is in the corpus collection. The class OC follows the corpus convention for organisational communications.

1. The notice is no longer published. Its address returned HTTP 404 on 2 October 2026 at 09:48 UTC, with and without the final slash. The page record of the site lists no published page under that name, and the parent page (id 259) answers "not allowed".
2. The Wayback Machine holds 16 captures of the notice with status 200, from 23 December 2023 to 12 March 2026. It holds captures with status 404 dated 29 March 2026 and 8 May 2026. The page was therefore taken down between 12 and 29 March 2026.
3. The wording of the notice did not change while it was online. The text of the main element is identical in all 16 captures (same SHA-1 after whitespace normalisation).
4. The questions and answers page is still published. Its address contains "registration-update__trashed" because its parent page is the notice.
5. Each file was written by the browser and then moved here. The SHA-256 of the notice file as downloaded was 811a283c5f67a39176b22edbc3f706af6757742aac99fd37f6413f65779bb184. One header line was then corrected, because the Wayback page reports the capture time as the current time. The retrieved line now gives the real time, and the file hash is e194ee88a9711131e17e83f7e327c61c74f9268009f01d263338448c455c3bc4. The text below the header is unchanged. The SHA-256 of the questions and answers file is 98eac551eacb12f9037197339c23e31e3597d5b2068e17ed72751705d209e999.
6. A web reading tool still returned the text of the notice on 2 October 2026 although the page was gone. A summary from such a tool is not proof that a page is online.

## Corrections to the corpus record

1. Diplomat_002 was published on 12 June 2025. The corpus record says 1 June.
2. Both Diplomat pieces are by Shafiur Rahman, a journalist who also publishes the Rohingya Refugee News newsletter. The corpus record lists staff as the author.
3. The UNHCR letter of 17 March 2025 is reported in indirect speech. The corpus note presents the wording as a quotation. The letter itself is not in the corpus.
4. The registration update for registered refugees is dated 2 May 2023 in the UNHCR notice saved as 06_OC_2023-05-02_UNHCR_005. The corpus places the exercise in 2025. Rations stopped in March 2025.

## What the documents confirm

1. The new identity cards do not carry the word Rohingya. Diplomat_002 reports that the UNHCR letter confirmed this. Diplomat_001 attributes the omission to the position of the Bangladesh government.
2. The letter of 17 March 2025 was signed by the UNHCR Head of Operations in Cox's Bazar. It is reported to say that people without biometric registration cannot receive assistance.
3. The community sent a complaint to four UN Special Rapporteurs. Before that it held a sit-in on 3 March and sent letters to the authorities on 27 April.
4. The number of families is given as about 400 in one piece and as 300 to 400 in the other. The first piece adds a figure of at least 2,000 people.
5. A UNHCR spokesperson is reported to link biometrics to donor confidence at a time of underfunding.
6. The Refugees International report documents the aid cuts of early 2025. It also reports that new arrivals gained limited access to food only after biometric registration was allowed.

## What changes for the paper

1. The families who refused are long-registered refugees in the Nayapara and Kutupalong registered camps. Many arrived in the early 1990s and hold documents from 1991 and 1992. The dispute is about a biometric update that would replace those documents. It is not a renewal for people who arrived in 2017.
2. The families say they were first told the exercise was voluntary and that they received no consent forms in their own language. The submitted paper says they had adequate information.
3. UNHCR disputes the account. It is reported to say that it found no specific protection risks and that the families kept access to other services.
4. The record of the 2025 dispute rests on one journalist. It needs a second source. The letter of 17 March 2025 should also be obtained.

## Sources found on 2 October 2026 and not yet saved

None of the sources below has been saved. The Radio Free Asia piece was read in full through a web reading tool on 2 October 2026. The others were seen through a web summary. The two UNHCR pages that stood in this table in version 1.1 are now saved and listed above.

| Source | Address | What it adds |
|---|---|---|
| UNHCR Bangladesh, questions and answers on the continuous registration exercise | https://help.unhcr.org/bangladesh/support-in-bangladesh/faq-registration/ | It describes continuous registration as voluntary and names two databases, one for registered refugees and one for later arrivals. |
| Rohingya Refugee News, 28 August 2025 | https://www.rohingyarefugee.news/p/bangladesh-biometric-mandate-ration-cuts-rohingya | It reports a letter from the UNHCR Inspector General and an email from the World Food Programme. It reports a sixth month without rations. The author is the journalist who wrote the Diplomat pieces. |
| Radio Free Asia, 26 November 2018 | https://www.rfa.org/english/news/myanmar/rohingya-refugees-protest-strike-11262018154627.html | The strike of 2018 and its two demands. |
| Associated Press via NPR, 1 April 2026 | https://www.npr.org/2026/04/01/nx-s1-5769798/food-assistance-slashed-rohingya-refugees-bangladesh-camps | The move to tiered rations from 1 April 2026. |

## Still to do

1. Save the third UNHCR page, the questions and answers on the continuous registration exercise. This needs a go-ahead, because saving a copy is a download. The other two pages were saved on 2 October 2026.
2. Read and save the Biometric Update piece. The site has to be allowed in the Chrome extension, or the piece opened by hand.
3. Obtain the letter of 17 March 2025. The notice is now saved from the Wayback Machine, because UNHCR took the page down in March 2026.
4. Find a second source for the 2025 dispute that does not depend on the same journalist.
5. Decide whether to save the Refugees International PDF.
6. The Diplomat allows two free articles a month, so further media sources may need library access.

## Cases 09 to 12, saved on 3 October 2026

Marco approved the new cases and the saving of these copies on 3 October 2026. The corpus now covers disputes from 2021 to 2026, and the earlier cases of Ethiopia, Rwanda, Yemen and India leave the corpus. Each text file was written by Chrome from the page as displayed (the innerText of the article, main or body element, as the header states) and then moved here. Each header gives the doc_id, the title, the address, the date found in the page metadata, the retrieval time and the element copied. The SHA-256 below is that of the file as stored. The status "Saved" meant saved and not yet read in full. Since version 1.6 of 6 October 2026, every saved document is marked as read in full.


### CASE09, Gaza, 2025

| doc_id | Title | Published (page metadata) | SHA-256 (first 16) | Status |
|---|---|---|---|---|
| 09_MC_2025-05-12_IDTechWire_001 | UNICEF Rejects Israel's Facial Recognition Plan for Gaza Aid Distribution - ID Tech | 2025-05-12T14:34:20+00:00 | 59d03ad2a44c533d | Read in full |
| 09_MC_2025-05-12_PassBlue_001 | 'Weaponizing Aid': New Plan Calls for Private Contractors to Take Over From UN in Gaza - PassBlue | 2025-05-12T12:52:01-04:00 | eba056055730d98e | Read in full |
| 09_MC_2025-05-28_IDTechWire_002 | Palestinians Reportedly Flock to Gaza Aid Centers Despite Biometric Screening Effort - ID Tech | 2025-05-28T15:38:13+00:00 | 7615a36125cb0ef1 | Read in full |
| 09_MC_2025-05-28_NBC_001 | How Gaza's new U.S.-backed aid system works and what it means for the people there | 2025-05-28T08:54:34.035Z | b07f0f4529dac490 | Read in full |
| 09_MC_2025-05-28_Reuters_001 | Palestinians rush US-backed aid centre despite concerns over checks - Stabroek News | 2025-05-28T06:06:37+00:00 | 89582e38695e8148 | Read in full |
| 09_MC_2025-05-30_CNN_001 | Gaza Humanitarian Foundation isn’t screening recipients — despite being established to keep supplies from Hamas / CNN | 2025-05-30T15:44:30.198Z | be7ef0ba13db8931 | Read in full |
| 09_OC_2025-05-28_UNHCT_001 | Statement by the Humanitarian Country Team of the Occupied Palestinian Territory – on Gaza / United Nations in Palestine | not found | e658fc112d6bb59c | Read in full |
| 09_PA_2025-05-15_Skyline_001 | Skyline International :: Biometrics-for-food: a dangerous shift from humanitarian relief to coercive surveillance | not found | e3c9191cfdc90e95 | Read in full |
| 09_PA_2025-09-10_Skyline_002 | Skyline International :: The Price of a Meal: Forced Biometric Surveillance and Military Control of Humanitarian Aid in Gaza | not found | 2f4e3a3f9662307a | Read in full |

### CASE10, Malaysia, 2025 to 2026

| doc_id | Title | Published (page metadata) | SHA-256 (first 16) | Status |
|---|---|---|---|---|
| 10_MC_2025-07-08_MalayMail_001 | Malaysia cites UNHCR data-sharing delays in move to launch own refugee registration system / Malay Mail | 2025-07-08 14:37:44 | 6b6ecb7d2955d9fb | Read in full |
| 10_MC_2025-11-25_Bernama_001 | BERNAMA - Kerajaan Laksana Sistem DPP Urus Pelarian Mulai 1 Jan 2026 | 25/11/2025 06:48 PM | 60bbd766dbe47368 | Read in full |
| 10_MC_2025-11-25_FMT_001 | Govt to launch refugee registration system on Jan 1 / FMT | 2025-11-25T12:28:27Z | 2e0d476ffd72acbb | Read in full |
| 10_MC_2025-12-13_DVB_001 | Refugees in Malaysia face uncertain future with new registration program - DVB | 2025-12-13T23:00:00+00:00 | 857b87a707bf9ec4 | Read in full |
| 10_MC_2026-04-06_SuaraKeadilan_001 | Pelarian didaftar dalam sistem biometrik, kawal selia lebih sistematik - Saifuddin | 2026-04-06T08:27:33.215Z | f259072ec999703c | Read in full |
| 10_MC_2026-05-05_FMT_003 | Rights group raises concerns over new refugee registration system / FMT | 2026-05-05T01:23:11Z | c2022bc9e22817fe | Read in full |
| 10_MC_2026-06-11_FMT_005 | KDN laksana pendaftaran status pelarian / FMT | 2026-06-11T11:13:16Z | a3b48eac226402a1 | Read in full |
| 10_MC_2026-07-21_FMT_002 | Data Dokumen Pendaftaran Pelarian dijangka diperoleh akhir tahun, kata Saifuddin / FMT | 2026-07-21T06:13:30Z | 67bfe434e7387efb | Read in full |
| 10_MC_2026-07-23_FMT_004 | Malaysia arah UNHCR henti sementara pendaftaran pelarian / FMT | 2026-07-23T05:08:46Z | baf643eca847305b | Read in full |
| 10_MC_2026-10-02_AlJazeera_001 | ‘They are crying’: Refugees in Malaysia in fear amid Myanmar deportation / Refugees / Al Jazeera | 2026-10-02T08:14:18Z | 45c0e18d765e14ed | Read in full |
| 10_OC_2026-05-18_MOHA_001 | Kenyataan media, lawatan kerja Menteri Dalam Negeri ke PPKPPS Bidor (Ministry of Home Affairs media statement), PDF downloaded from moha.gov.my | 18 May 2026 (stated in the text) | 699b3e7c8f11d3f7 | Read in full |
| 10_PA_2026-05-04_HRW_001 | Malaysia: New Refugee Registration System Raises Concerns / Human Rights Watch | 2026-05-04T19:00:00-0400 | 86776b919a1928a2 | Read in full |
| 10_PA_2026-06-01_FortifyRights_001 | Malaysia: New Refugee Registration Scheme Must Protect Rights - Fortify Rights | 2026-06-01T13:46:32+00:00 | 0c29d0810cba541e | Read in full |

### CASE11, South Africa, 2024 to 2026

| doc_id | Title | Published (page metadata) | SHA-256 (first 16) | Status |
|---|---|---|---|---|
| 11_MC_2024-07-31_Bizcommunity_001 | Beneficiaries are still battling with Sassa’s new biometric system | 2024-07-31T10:58+02:00 | 5d7bd3e7a0d2fef0 | Read in full |
| 11_MC_2025-08-27_GroundUp_001 | SASSA to bring in biometrics for all social grant applications from September / GroundUp | 2025-08-27T04:50:00+02:00 | f88acd16ac0efae1 | Read in full |
| 11_MC_2025-09-02_CapeArgus_001 | SASSA's biometric enrolment: Black Sash voices readiness concerns | 1756791000000 | 0258b08735a86793 | Read in full |
| 11_MC_2026-05-24_IOL_001 | SASSA’s biometric rollout leaves thousands without grants amid fraud crackdown | 1779602400000 | bf4ea64640e2d0b9 | Read in full |
| 11_MC_2026-05-25_DailyVoice_001 | SASSA’S FACE PALM - Facial recognition tech linked to the suspension of 68 000 grants | 1779705420000 | 24a57d9c970f60f2 | Read in full |
| 11_MC_2026-08-24_DailyMaverick_001 | Sassa grant reviews strand beneficiaries in systemic chaos | 2026-08-24T22:03:28.000Z | f4546a9c82068a68 | Read in full |
| 11_OC_2025-08-25_SAnews_001 | SASSA to introduce biometric enrolment in September / SAnews | 2025-08-25T11:11:21+02:00 | 8190f95995f907b7 | Read in full |
| 11_PA_2024-06-24_BlackSash_001 | Universal Basic Income Coalition is concerned about the apparent deepening of digital hurdles to accessing the SRD Grant - Black Sash | 2024-06-24T11:25:25+00:00 | ceefc88db168cd84 | Read in full |

### CASE12, Mizoram, India, 2023 to 2026

| doc_id | Title | Published (page metadata) | SHA-256 (first 16) | Status |
|---|---|---|---|---|
| 12_MC_2023-09-28_ThePrint_001 | ‘Our blood:’ Mizoram won’t collect biometric data of Myanmar refugees as ordered by Centre | 2023-09-28T09:25:08+00:00 | 96aec3e2f4bfddd5 | Read in full |
| 12_MC_2023-09-29_Scroll_001 | Mizoram refuses to follow Centre’s directive to collect biometric data of Myanmar refugees | 2023-09-29T15:58:00+05:30 | 0ef2271d85bda54a | Read in full |
| 12_MC_2024-02-29_DeccanHerald_001 | Mizoram not to collect biometric data of Myanmar, Bangladesh refugees: CM | 2024-02-29T15:45:48+05:30 | f02350408aa5391a | Read in full |
| 12_MC_2024-06-19_MorungExpress_001 | Mizoram agrees to record biometric details of 34,000 Myanmar refugees, awaits MHA directions / MorungExpress / morungexpress.com | not found | 848609c47d56a03e | Read in full |
| 12_MC_2025-08-01_Organiser_001 | Biometric tracking begins for illegal migrants in Mizoram | 2025-08-01T12:00:51+00:00 | 1cb359027726e973 | Read in full |
| 12_MC_2025-08-10_DeccanHerald_002 | After initial hesitancy, Mizoram govt starts collecting biometrics of Myanmar refugees | 2025-08-10T21:57:44+05:30 | 7cff99af4b3cadc1 | Read in full |
| 12_MC_2025-12-04_TheWire_001 | Fear, Mistrust Grow as India Collects Biometrics From Myanmar Refugees - The Wire | 2025-12-04T10:46:29+05:30 | e79e78c81f0b3c51 | Read in full |
| 12_MC_2025-12-15_NewsMill_001 | Mizoram completes biometric enrolment of 70% Myanmar refugees | 2025-12-15T08:37:16+05:30 | 16840b9ea11727e9 | Read in full |
| 12_MC_2026-03-02_ShillongTimes_001 | Biometric enrolment of over 97 pc of Myanmar refugees completed so far in Mizoram / The Shillong Times | 2026-03-02T18:55:27+05:30 | c9c5fd640c0e9ba2 | Read in full |

Corrections made on saving. Two files were first named with a fallback date because the page metadata gave none. The Morung Express report is dated 19 June 2024 in its text, and the Skyline International report is dated 10 September 2025. Both files and their doc_id lines were renamed. The DVB opinion piece (13 December 2025) was saved from the Wayback Machine capture of 3 July 2026, because the live site returned a 504 error. The UNHCR Malaysia page "Important Update on Dokumen Pendaftaran Pelarian (DPP) Programme" now returns "Page not found" and has no capture in the Wayback Machine. (Superseded: see note 4 of the section for the afternoon of 3 October 2026.)

## Node and cases 09 to 11, saved on the afternoon of 3 October 2026

Marco approved on 3 October 2026 the saving of the documents found by three further searches on Gaza, Malaysia and South Africa, and of the UNHCR guidance page that the paper treats as the node. The method is the one described for the morning's copies, with three differences. The node page hides most of its text behind expandable headings, so its copy is the DOM text of the whole page, including the collapsed sections, with whitespace normalised. The PDFs were downloaded with curl, except S/2025/313, which the UN Digital Library serves only to a browser and which was fetched in Chrome from the record page. Where the page metadata gave no date, the date in the doc_id was taken from the text or the address, as the table states.

### NODE, UNHCR guidance

| doc_id | Title | Published | SHA-256 (first 16) | Status |
|---|---|---|---|---|
| 00_OC_2026-10-03_UNHCR_001 | Registration as an Identity Management Process (Guidance on Registration and Identity Management, section 5.2) | Not stated. The guidance is a living online text, so the doc_id carries the retrieval date | 5bbaba196cc79357 | Read in full. The passages on voluntary participation, the right to refuse biometrics, footnote 5 and "freely given" consent were checked on the live page |

### CASE09, Gaza, additions

| doc_id | Title | Published (page metadata) | SHA-256 (first 16) | Status |
|---|---|---|---|---|
| 09_OC_2025-05-04_UNHCT_002 | Statement by the Humanitarian Country Team of the Occupied Palestinian Territory on principled aid delivery in Gaza (OCHA oPt) | 2025-05-04T12:00:00Z | 998d0f94660661c7 | Read in full |
| 09_OC_2025-05-08_GHF_002 | Gaza Humanitarian Foundation (GHF): Safe, Transparent Aid for Gaza, PDF of 14 pages, Times of Israel copy | Undated. The earliest known copy was uploaded on 8 May 2025 | 7c05ae34a7baa841 | Read in full |
| 09_OC_2025-05-09_UNGeneva_001 | UN Geneva Press Briefing, 9 May 2025 (teleprompter transcript) | 2025-05-09 12:55:00 | 00fd2ac28cfdd962 | Read in full |
| 09_OC_2025-05-09_UNGeneva_002 | UN Geneva Press Briefing, 9 May 2025 (summary) | 2025-05-09T14:37:51Z | a3fb96c93df4f0bd | Read in full |
| 09_OC_2025-05-09_UNNews_001 | Gaza: UN agencies reject Israeli plan to use aid as 'bait' (UN News) | 2025-05-09T08:28:11-04:00 | 600c814a7a9d5d5f | Read in full |
| 09_OC_2025-05-09_UNifeed_001 | GENEVA / GAZA AID UPDATE (UNifeed) | 2025-05-09T12:00:00Z | 7960952c99e6fea1 | Read in full |
| 09_OC_2025-05-13_OCHA_002 | UN Relief Chief calls on Security Council to act decisively to prevent genocide in Gaza (UNISPAL) | 2025-05-13T13:36:00+00:00 | 83212e586c4d71d6 | Read in full |
| 09_OC_2025-05-19_IsraelUN_001 | Letter dated 19 May 2025 from the Permanent Representative of Israel to the United Nations addressed to the President of the Security Council (S/2025/313), PDF | 19 May 2025 (stated in the title) | 30444981415d4a63 | Read in full |
| 09_OC_2025-05-19_UNSpokesperson_001 | Daily Press Briefing by the Office of the Spokesperson for the Secretary-General, 19 May 2025 | 2025-05-19T00:00:00-04:00 | 4eb86b8f4eeb53a5 | Read in full |
| 09_OC_2025-05-28_OCHA_001 | Briefing to journalists by Jonathan Whittall, Head of OCHA OPT | 2025-05-28T12:00:00Z | 7c8e8131defac5e7 | Read in full |
| 09_OC_2025-08-08_USEmbassy_001 | Ambassador Huckabee's Interview with CBS News (U.S. Embassy Jerusalem) | 2025-08-08T06:49:53+00:00 | 6da8d3ae125e48d4 | Read in full |

### CASE10, Malaysia, additions

| doc_id | Title | Published (page metadata) | SHA-256 (first 16) | Status |
|---|---|---|---|---|
| 10_MC_2026-06-20_Bernama_002 | Refugees Must Respect Malaysian Laws In Exchange For Protection, Says UNHCR (Bernama) | 20/06/2026 02:52 PM | 564a7e78524047aa | Read in full |
| 10_MC_2026-07-24_MerdekaTimes_001 | Pendaftaran pelarian baharu dibeku, UNHCR terus runding dengan kerajaan (The Merdeka Times) | 2026-07-24T10:06:37+00:00 | 8fd79d5d4d4657fa | Read in full |
| 10_MC_2026-07-30_MalayMail_002 | Home Ministry starts refugee checks as Malaysia prepares to send back 5,000 Myanmar nationals (Malay Mail) | 2026-07-30 16:24:43 | 43c208cbb22028d8 | Read in full |
| 10_MC_2026-09-01_DailyMaverick_001 | UNHCR says it has no role in Malaysia's planned repatriation of Myanmar refugees, warns country is still unsafe (Reuters, Daily Maverick copy) | 2026-09-01T11:07:26.000Z | 2b26231269a43211 | Read in full |
| 10_MC_2026-09-29_AP_001 | Malaysia begins Myanmar repatriations despite safety warnings by UN and rights groups (AP, Click2Houston copy) | 2026-09-29T06:30:55Z | b34d1e1456fac9cc | Read in full |
| 10_MC_2026-09-30_TheStar_001 | Man claiming to be MERHROM president charged over unregistered organisation (The Star) | 2026-09-30T20:07:00.000Z | aec216454b8a23a9 | Read in full |
| 10_MC_2026-10-01_MyanmarNow_001 | Myanmar nationals in Malaysia fear arrest and forced return (Myanmar Now) | 2026-10-01T11:30:12+00:00 | 349f5dc754763cc7 | Read in full |
| 10_OC_2026-01-02_UNHCR_001 | Important update on Dokumen Pendaftaran Pelarian (DPP) Programme (UNHCR Malaysia help site) | Not found. The page states 2 January 2026 | f7c63f2df81544fd | Read in full |
| 10_OC_2026-07-09_UNHCR_003 | Privacy Notice (UNHCR Malaysia help site) | Not found. The text states that it was "last updated on 9 July 2026" | 0cd6c45aea14d8f5 | Read in full |
| 10_OC_2026-07-23_Hansard_001 | Digital Hansard, Dewan Negara, sitting of 23 July 2026 (Parliament of Malaysia) | Not found. The address gives the sitting date | 1df05d60854c47bc | Read in full |
| 10_OC_2026-09-30_UNHCR_004 | UNHCR concerned by returns from Malaysia to Myanmar amid ongoing conflict (UNHCR press release) | 2026-09-30T09:22:46+0200 | 44be7dc62c75dd40 | Read in full |
| 10_OC_2026-09-30_UNNews_001 | Malaysia: UN agency urges safeguards after refugees returned to Myanmar (UN News) | 2026-09-30T06:13:21-04:00 | 871902165a3f75ef | Read in full |
| 10_OC_2026-10-03_UNHCR_002 | UNHCR Malaysia home page, including the section "Looking Ahead: Towards a Comprehensive Asylum System" | Not stated. The doc_id carries the retrieval date | e45cbbfff91aeac8 | Read in full |
| 10_PA_2026-07-23_Amnesty_001 | Refugee protection cannot be paused during transition to DPP system (Amnesty International Malaysia) | 2026-07-23T11:29:37+00:00 | f022b5404cbec5b9 | Read in full |
| 10_PA_2026-07-30_MERHROM_001 | MERHROM urgent appeal to the Malaysian government to halt the deportation of 5000 stateless Rohingya to Myanmar (The Sun) | 2026-07-30T14:19:00+08:00 | 09c06c588ec476ec | Read in full |

### CASE11, South Africa, additions

| doc_id | Title | Published (page metadata) | SHA-256 (first 16) | Status |
|---|---|---|---|---|
| 11_MC_2024-06-19_GroundUp_002 | SASSA's new ID verification process sparks alarm (GroundUp) | 2024-06-19T16:41:45+02:00 | 22887ad2182ba345 | Read in full |
| 11_MC_2025-06-30_Context_001 | How is South Africa's welfare algorithm failing the poor? (Context, Thomson Reuters Foundation) | 2025-06-30 | c79edb9d46bbb8c2 | Read in full |
| 11_MC_2026-01-28_GroundUp_003 | State is blocking access to SASSA grants, argue activists (GroundUp) | 2026-01-28T12:33:11+02:00 | ef94c0d54a70d8e9 | Read in full |
| 11_OC_2025-01-23_Judgment_001 | Institute for Economic Justice and Another v Minister of Social Development and Others [2025] ZAGPPHC 29 (SAFLII) | 23 January 2025 (stated in the title) | 45b8e3c4e493c80d | Read in full |
| 11_OC_2025-04-01_SRDRegs_001 | Regulations Relating to COVID-19 Social Relief of Distress, 2022, GN R2042, version of 1 April 2025 (LawLibrary) | The address gives the version date | 97e264471344640c | Read in full |
| 11_OC_2025-07-01_PMG_001 | Question NW3803 to the Minister of Social Development (PMG) | 01 July 2025 (stated on the page) | a16badcbddc94a5f | Read in full |
| 11_OC_2025-09-17_PMG_002 | DSD Q1 2025/26 Performance; SASSA Biometric Verification Process; with Deputy Minister (PMG committee report) | 17 September 2025 (stated on the page) | 021370f59840c236 | Read in full |
| 11_OC_2026-01-27_SASSA_001 | SASSA on beneficiaries with no tools of trade to do biometric identity verification (gov.za, a statement by SASSA Mpumalanga) | 2026-01-27T12:00:00Z | b50b8645b97d1282 | Read in full |
| 11_PA_2023-09-xx_BlackSash_002 | The Protection of Personal Information of Social Grant Beneficiaries (Bowmans and Black Sash), PDF of 58 pages | Undated. The upload folder is 2023/09 | ba0f5a60cd3f88ca | Read in full |
| 11_PA_2024-07-30_UBICoalition_001 | SASSA's fraud management system is fraught with danger (UBI Coalition, GroundUp) | 2024-07-30T09:31:03+02:00 | 64add1c640c8a6b7 | Read in full |
| 11_PA_2025-02-xx_IEJ_001 | Systemic exclusion from a South African social assistance transfer: Drivers, impacts, and who is most at risk (Howson, Baduza, Setambule and Khumalo, AFD Research Papers No. 340), PDF of 116 pages | February 2025 on the cover | 80bdea7785d7c478 | Read in full |
| 11_PA_2026-08-03_OpenSecrets_001 | Digital Profiteers (Part Two): The banks and the costs of verifying social grant recipients (Open Secrets) | 2026-08-03T14:45:01+00:00 | 8183aab71a0d8b6a | Read in full |

### Not saved

1. GHF, "Announcing New Pilot For Families to Reserve Aid Parcels" (18 August 2025). The domain ghf.org no longer resolves (DNS error NXDOMAIN on 3 October 2026 at 13:21 UTC). The Wayback Machine holds a capture of 16 December 2025. Marco can save it from his own browser.
2. 235sa, "SASSA: Government's Foot in the Door". The site refuses automated access. Marco can save it from his own browser.
3. NST, "UNHCR says refugee processing follows standards, welcomes closer ties with Putrajaya" (July 2026). The site refuses automated access. Marco can save it from his own browser.
4. The Wayback capture of 12 June 2026 of the UNHCR Malaysia DPP notice at refugeemalaysia.org. It postdates the last update that a search report gives for the page (22 May 2026, still to check), so it cannot show the January wording.

### Notes

1. Three downloads were discarded and moved to the Trash: the DNS error page for ghf.org and two security-check pages, shown by unhcr.org and by lawlibrary.org.za before the pages loaded. The checks completed without any action, and each page was then saved again from a fresh tab.
2. The Dewan Negara Hansard is published as digital text, not as a PDF, so it was saved as text.
3. The UNHCR press release of 30 September 2026 was found as the source of the UN News story and saved with it. UN News is classed OC, as in CASE09.
4. The note at the end of the morning section, that the UNHCR Malaysia DPP notice returned "Page not found" and had no Wayback capture, is superseded. The notice is live at a new dated address and is saved as 10_OC_2026-01-02_UNHCR_001. It refers readers to two Facebook pages of the Ministry of Home Affairs "For official updates".
5. Twenty-two quotations used in the report to Marco of 3 October were found verbatim in the saved copies, after whitespace and quotation marks were normalised. The UN Geneva summary (09_OC_2025-05-09_UNGeneva_002) does not contain the word "intelligence", whereas the transcript (09_OC_2025-05-09_UNGeneva_001) and UN News (09_OC_2025-05-09_UNNews_001) contain "screen and monitor beneficiaries for intelligence and military purposes".
6. The GHF memo (09_OC_2025-05-08_GHF_002) has 14 pages, as the PDF reader and the page tree both count. Version 1.4 gave 38, the figure that the file command reports.
