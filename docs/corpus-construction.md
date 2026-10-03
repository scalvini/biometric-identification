# Corpus construction

> **Version:** 1.0
> **Last updated:** 3 October 2026

This document is adapted from the working file DC_10 of the article project, version 1.0.

This document records how the corpus in the archive folder `BDS_Corpus_Archive` was built on 2 and 3 October 2026: which AI agents were used and for what, what the main session and the author did, and how the procedure can be repeated. It covers the folders NODE, CASE06 (two pages), CASE09, CASE10, CASE11 and CASE12. The April 2026 collection of cases 01 to 08 has its own prompts (`BDS_Corpus_Construction_Prompts.md`) and log (`BDS_Collection_Log_Session1.md`), and three of the CASE06 copies come from an earlier session on 1 October. The counts and times below come from the session's own records (the transcript and the subagent files), and the times are British Summer Time.

The corpus can be browsed in the page `index.html` of this repository. `corpus-tables.md` gives the dataset summary and the proposed core corpus. `data/corpus/archive_manifest.jsonl` lists every file with its full SHA-256, and the archive log (`ARCHIVE_LOG.md`, version 1.5), which stays with the archive, records each file with notes.

## 1. Agents used

Thirty-three helper agents ran in this working session, 21 on 2 October and 12 on 3 October. All were of the general-purpose type, spawned by the main Claude session. They worked only with web search and web page reading, and reported back in text. No agent saved, edited or deleted a file. Four agents supplied leads that entered the corpus.

| Work | Agents | When | Effort | What entered the corpus |
|---|---:|---|---|---|
| UNHCR's global texts for the node | 1 | 3 Oct, 11:47 to 12:08 | 28 searches, 133 page reads | The lead to section 5.2 of the Guidance on Registration and Identity Management, which the main session then read on the live page and saved |
| Gap searches: Gaza (actors' own texts), Malaysia (UNHCR's words), South Africa (refusal) | 3 | 3 Oct, 13:29 to 13:52 | 206 searches, 356 page reads | 37 of the 39 documents saved in the second batch came from their ranked lists |
| Second sources for the Bangladesh case | 1 | 2 Oct, 11:06 to 11:12 | 10 searches, 21 page reads | No document; its report qualified the record of the 2025 dispute |
| Ethiopia, Rwanda, Yemen and India, in two rounds of four | 8 | 3 Oct, 11:38 to 11:43 and 11:47 to 12:09 | Stopped by the author before they reported | Nothing |
| Checks on the article's theoretical sources and facts, and one independent review of a draft | 20 | 2 Oct, 08:50 to 11:48 | Literature and fact checks | Not corpus work |
| **Total** | **33** | | | |

The agents of 2 October ran on `claude-fable-5-1`, and those of 3 October, like the main session that day, on `claude-opus-5-5`, as the session files record. Three of the first five agents of 2 October ended without a usable report, and their checks were run again in the second group.

The corpus work that no agent did:

- **Case search.** The main session searched for disputes from 2021 to 2026 with a biometric condition, a recorded refusal or contestation, an institutional response and little academic work: 32 searches and 25 page reads on 3 October, 12:10 to 12:31 (section 5). The author chose the four cases.
- **Saving.** The main session saved every file after the author's approval: 79 through Chrome (text copies, plus one PDF fetched inside the UN Digital Library page) and 4 PDFs with curl on the Mac.
- **Checks and records.** The main session computed the hashes, checked 22 quotations against the saved copies, and wrote the archive log and the working log.

## 2. Division of work on 3 October

| Time | Who | What | Result |
|---|---|---|---|
| 11:35 to 13:05 | The author, with Claude's proposals | Design: UNHCR's identity-management discourse as the node, and recent disputes as cases; Ethiopia, Rwanda, Yemen and India moved to the introduction and framework | The node and the four cases |
| 11:47 to 12:08 | One agent | Read UNHCR's global texts on registration and identity management | Report with the section 5.2 lead |
| 12:10 to 12:31 | Main session | Case search (section 5) | Candidate disputes; The author chose Gaza, Malaysia, South Africa and Mizoram |
| 12:20 to 12:43 | Main session, after the author's approval | First batch saved through Chrome, and one PDF with curl | 39 files in CASE09 to CASE12 |
| 13:29 to 13:52 | Three agents | Gap searches (prompts in section 4) | Three ranked lists of texts |
| about 14:10 | Main session | Section 5.2 of the Guidance read on the live page | Wording checked word for word |
| 14:20 to 14:38 | Main session, after the author approved 42 proposed items | Second batch saved through Chrome and curl | 39 files in NODE and CASE09 to CASE11; four items not saved |
| 14:40 to 14:55 | Main session | Hashes, content checks, 22 quotations checked, logs | `ARCHIVE_LOG.md` 1.4 and `DC_Log.md` 3.32 |

On 2 October the main session saved the two UNHCR Bangladesh pages of CASE06 through Chrome, one of them from a Wayback capture because the live page had been removed.

## 3. The corpus on 3 October 2026

| Folder | Files | Saved |
|---|---:|---|
| NODE | 1 | 3 Oct, second batch |
| CASE06 Bangladesh | 5 | 3 on 1 Oct (earlier session), 2 on 2 Oct |
| CASE09 Gaza | 20 | 9 in the first batch, 11 in the second |
| CASE10 Malaysia | 28 | 13 in the first batch, 15 in the second |
| CASE11 South Africa | 20 | 8 in the first batch, 12 in the second |
| CASE12 Mizoram | 9 | first batch |
| **Total** | **83** | 78 text copies and 5 PDFs |

The text copies record the element they were taken from: the article element (42 files), the main element (21), the whole page body (14), or, for the UNHCR Guidance, the full page text including its collapsed sections (1).

Four proposed items were not saved:
- The GHF notice of 18 August 2025 on a pilot for reserving parcels. The domain ghf.org no longer resolves; a Wayback capture of 16 December 2025 exists.
- The 235sa blog "SASSA: Government's Foot in the Door".
- The NST report on UNHCR's response to the pause in registration (July 2026).
- The Wayback copy of the UNHCR Malaysia DPP notice, captured after the page's last update.

The 235sa and NST sites refuse automated access. The author can save those two and the GHF capture from his own browser.

## 4. Agent prompts, verbatim

These are the prompts given to the four agents whose reports fed the corpus. Each states what the corpus already held, which is why they differ. The Malaysia prompt reflects what was believed at the time; the agent then found the UNHCR page live at a new address.

### 4.1 The node: UNHCR's global texts (3 October, 11:47)

```text
You are helping an academic (critical discourse analysis after Norman Fairclough, communication ethics) with an article on disputes over biometric registration as a condition of humanitarian assistance, 2017 to 2026.

The argument: a "nodal discourse" of identity management, in Fairclough's sense of a discourse which "subsume[s] and articulate[s] in a particular way a great many other discourses" (Fairclough 2010, Critical Discourse Analysis, 2nd edn, p. 507), is formed in UNHCR's texts on registration and identity management (the PRIMES system was launched in 2017) and is articulated most fully in Bangladesh. There, UNHCR and the Government of Bangladesh write that "establishing and preserving identities is key to ensuring protection" (2023 notice) and that registration is "a pre-requisite" for protection and assistance, so that "refusing the processing of personal data may lead to deregistration" (2026 questions and answers). The article then traces how this nodal discourse is recontextualised in other disputes.

YOUR TASK: identify the node at the global scale. Find and READ UNHCR's own global texts (and closely related inter-agency texts) that state why registration and biometric identity management are needed, what they are for, and what follows for people who do not register or who refuse. Candidates (verify each; do not assume):
- UNHCR, Guidance on Registration and Identity Management (online, from about 2018), especially its chapters on the purpose of registration, biometrics, data protection, consent and refusal.
- UNHCR descriptions of PRIMES (Population Registration and Identity Management EcoSystem) and BIMS, including news items and the 2017 to 2019 rollout.
- UNHCR Strategy on Digital Identity and Inclusion (around 2018) and the Digital Transformation Strategy 2022 to 2026.
- UNHCR Policy on the Protection of Personal Data of Persons of Concern (2015) and the General Policy on Personal Data Protection and Privacy (2022), on consent and on what happens if a person does not consent.
- UNHCR Executive Committee Conclusion No. 91 (2001) on registration.
- The Global Compact on Refugees (2018), paragraphs on registration and documentation.
- The UNHCR and WFP joint principles or data-sharing agreements on biometrics and targeting (around 2017 to 2018), and WFP's statements on SCOPE.
- The World Bank ID4D "Principles on Identification for Sustainable Development" (2017), if UNHCR texts cite them.

For each text, find the passages where it (1) names the purposes of registration and identity management (protection, assistance, solutions, integrity, accuracy, fraud, duplication, efficiency, accountability to donors, security, inclusion); (2) presents registration or biometrics as necessary, required or a condition of assistance; (3) addresses consent, objection or refusal to registration or to biometric capture, and what follows from it; (4) cites other texts or "global standards".

Rules:
- Use WebSearch and WebFetch only. Read-only: do not download or save files, do not use curl, do not write files. If a site is declined, do not work around it; report it as a lead.
- Report only texts you actually opened and read. A page you could not open is a lead.
- Excerpts must be copied word for word from the page, inside quotation marks, at most 40 words each, with the section or paragraph number where there is one. Never paraphrase inside quotation marks and never reconstruct wording from memory.
- For each text give: title; organisation; date; URL; type; approximate length; whether a capture exists in the Internet Archive (query https://archive.org/wayback/available?url=THE_URL with WebFetch).
- Accuracy matters more than coverage. Flag every uncertainty.

Final answer (about 1,000 to 1,500 words): 1. The texts read (table). 2. Excerpts grouped by the four points above. 3. The vocabulary of the node, in the texts' own words (the terms that recur across texts). 4. What these texts say, or leave unsaid, about refusal. 5. Leads not opened.
```

### 4.2 Gaza: the actors' own texts (3 October, 13:29)

```text
You are helping an academic (critical discourse analysis) who studies disputes over biometric identification as a condition of humanitarian assistance, 2021 to 2026. One case is GAZA, May to September 2025: the US- and Israel-backed Gaza Humanitarian Foundation (GHF) distribution sites, and Israeli plans to screen aid recipients, including by facial recognition, which UN agencies refused to join.

The corpus already holds press reports (Reuters 28 May 2025, CNN 30 May 2025, NBC 28 May 2025, PassBlue 12 May 2025, ID Tech 12 and 28 May 2025), the UN Humanitarian Country Team statement of 28 May 2025, and two Skyline International reports. WHAT IS MISSING are texts written by the actors who set or defended the condition.

TASK: find and READ primary texts, in which the condition of identification, screening, vetting or facial recognition of aid recipients is stated, defended, qualified or denied, by:
- the Gaza Humanitarian Foundation: its website (for example ghf.org), press releases (also on PR Newswire or Business Wire), statements on X, FAQs, letters to OCHA or UN agencies, and its operating plan or proposal documents, including any leaked plan describing "hubs", vetting, "humanitarian bubbles" or the contractor Global Delivery Company;
- the Israeli government: COGAT (gov.il, X), the Prime Minister's Office, the Ministry of Defense, the IDF spokesperson, ministers, and Israeli statements at the UN;
- the US government: State Department briefings or statements on GHF, the US Ambassador to Israel, and envoys;
- UN agencies' own official texts that mention biometrics, facial recognition or screening, as opposed to press paraphrase: for example the transcript of the UN Geneva press briefing where UNICEF's James Elder spoke (around 9 May 2025), and OCHA, UNRWA or WFP statements or flash updates.

Rules:
- Use WebSearch and WebFetch only. Read-only: do not download or save files, do not use curl, do not write files. If a site is declined, do not work around it; report it as a lead.
- WebFetch passes pages through a summarising model, so ask it for verbatim sentences and mark every excerpt "verbatim as returned by the tool, to verify".
- Report only texts you actually opened. A page you could not open is a lead.
- For each text give: author or organisation; title; date; URL; type (official statement, press release, plan or proposal, briefing transcript, social media post); whether a capture exists in the Internet Archive (query https://archive.org/wayback/available?url=THE_URL with WebFetch); and up to four excerpts of at most 40 words each on identification, screening, vetting, facial recognition, biometrics, data or eligibility of recipients.
- Say plainly if the actors' own texts never mention facial recognition, and whether any of them denies using it.
- Accuracy matters more than coverage. Flag every uncertainty.

Final answer (at most 1,200 words): 1. Texts found, as a table with the fields above. 2. Excerpts grouped by actor. 3. What the actors' own texts say or leave unsaid about screening and facial recognition. 4. Leads not opened. 5. A ranked list of the texts most worth saving to the corpus.
```

### 4.3 Malaysia: UNHCR's words and refugees' statements (3 October, 13:30)

```text
You are helping an academic (critical discourse analysis) who studies disputes over biometric registration of refugees, 2021 to 2026. One case is MALAYSIA, 2025 to 2026: the Ministry of Home Affairs (KDN) launched its own biometric refugee registration, the Dokumen Pendaftaran Pelarian (DPP), from 1 January 2026, run with the Immigration Department and developed by MIMOS, under National Security Council Directive No. 23. In July 2026 the government ordered UNHCR to pause the registration of new refugees, and deportations to Myanmar followed in September and October 2026.

The corpus already holds the KDN media statement of 18 May 2026, ministers' statements reported by Bernama, FMT, Malay Mail and Suara Keadilan, HRW (4 May 2026), Fortify Rights (1 June 2026), DVB (13 December 2025) and Al Jazeera (2 October 2026). WHAT IS MISSING:
(1) UNHCR's own words on the DPP and on the order to pause registration. A UNHCR Malaysia help page titled "Important Update on Dokumen Pendaftaran Pelarian (DPP) Programme" (https://help.unhcr.org/malaysia/important_update_on_dokumen_pendaftaran_pelarian_dpp_programme/, also reached via refugeemalaysia.org) now returns "Page not found" and has no capture in the Wayback Machine.
(2) Refugees' own statements about registering with the DPP, especially any refusal, boycott or reluctance, and their reasons, from refugee community organisations (for example the Alliance of Chin Refugees, Rohingya Society in Malaysia, MERHROM, Myanmar Ethnic Rohingya Human Rights Organisation Malaysia) or from interviews.

TASK: find and READ:
- copies or quotations of the removed UNHCR page: try archive.today (archive.ph, archive.is), other Wayback URLs (with or without trailing slash, refugeemalaysia.org address), search-engine snippets, and NGO or community posts that quote it;
- other UNHCR texts: UNHCR Malaysia announcements (https://help.unhcr.org/malaysia/announcements/), UNHCR news pages for Malaysia, UNHCR Asia-Pacific briefing notes, and UNHCR spokespeople or the Representative quoted in Malaysian or international media (The Star, New Straits Times, Malaysiakini, CNA, Reuters, Bernama) on the DPP, data sharing, or the pause in registration;
- refugees' and community organisations' statements on registering, refusing or fearing the DPP.

Rules:
- Use WebSearch and WebFetch only. Read-only: do not download or save files, do not use curl, do not write files. If a site is declined, do not work around it; report it as a lead.
- WebFetch passes pages through a summarising model, so ask it for verbatim sentences and mark every excerpt "verbatim as returned by the tool, to verify".
- Report only texts you actually opened. A page you could not open is a lead.
- For each text give: author or organisation; title; date; URL; type; language; whether a capture exists in the Internet Archive (query https://archive.org/wayback/available?url=THE_URL with WebFetch); and up to four excerpts of at most 40 words each (Malay with an English translation in brackets).
- Accuracy matters more than coverage. Flag every uncertainty.

Final answer (at most 1,200 words): 1. Texts found (table). 2. Excerpts grouped by UNHCR, government, refugees and NGOs. 3. Whether the removed UNHCR page can be recovered, and what it said if quoted elsewhere. 4. Leads not opened. 5. A ranked list of the texts most worth saving.
```

### 4.4 South Africa: records of refusal (3 October, 13:30)

```text
You are helping an academic (critical discourse analysis, communication ethics) who studies disputes over biometric identification as a condition of assistance, 2021 to 2026. One case is SOUTH AFRICA: the South African Social Security Agency (SASSA) introduced facial verification for the Social Relief of Distress (SRD) grant (from about 2024) and made biometric enrolment (fingerprints or facial recognition through "eKYC") mandatory for all grant applications and reviews from 1 September 2025. About 68,000 grants were suspended by May 2026, with thousands of complaints about the facial system.

The corpus already holds SAnews (25 August 2025), GroundUp (27 August 2025), Cape Argus on Black Sash (2 September 2025), IOL (24 May 2026), Daily Voice (25 May 2026), Daily Maverick (24 August 2026), Bizcommunity (31 July 2024) and a Black Sash and UBI Coalition statement (24 June 2024). Those documents record exclusion and contestation by civil society. WHAT IS MISSING is any record of REFUSAL: people who declined, objected to or would not consent to biometric or facial verification (for privacy, religious, data-protection or other reasons), as opposed to people who failed to verify.

TASK: find and READ public documents showing:
(a) individuals or groups refusing or objecting to SASSA biometric or facial verification, in their own words where possible;
(b) complaints to the Information Regulator about SASSA's processing of biometric data under POPIA, and any statement, assessment or enforcement notice of the Information Regulator on SASSA biometrics or facial recognition;
(c) litigation touching the biometric or digital verification conditions (for example Black Sash, the Institute for Economic Justice, #PayTheGrants or others on the SRD regulations, 2023 to 2026), with the court's or the department's words;
(d) parliamentary questions and SASSA or Department of Social Development answers about people who decline or cannot do biometric or facial verification, and any opt-out, exemption or "alternative arrangement";
(e) SASSA's or the Department's own statements responding to objections (consent, privacy, alternatives, consequences of not enrolling).

Rules:
- Use WebSearch and WebFetch only. Read-only: do not download or save files, do not use curl, do not write files. If a site is declined, do not work around it; report it as a lead.
- WebFetch passes pages through a summarising model, so ask it for verbatim sentences and mark every excerpt "verbatim as returned by the tool, to verify".
- Report only texts you actually opened. A page you could not open is a lead.
- Distinguish clearly REFUSAL (declining, objecting, withholding consent) from EXCLUSION (failure to verify, technical problems).
- For each text give: author or organisation; title; date; URL; type; whether a capture exists in the Internet Archive (query https://archive.org/wayback/available?url=THE_URL with WebFetch); and up to four excerpts of at most 40 words each.
- Accuracy matters more than coverage. Flag every uncertainty.

Final answer (at most 1,200 words): 1. Texts found (table). 2. Excerpts grouped under (a) to (e). 3. Your plain judgement: is there a documented refusal (not only exclusion) in this case, and by whom? 4. Leads not opened. 5. A ranked list of the texts most worth saving.
```

### 4.5 Template for a further case or gap

The four prompts share one structure, which can be reused for Mizoram or any new case.

```text
You are helping an academic (critical discourse analysis) who studies disputes over biometric
identification as a condition of assistance, 2021 to 2026. One case is [CASE]: [two or three
sentences of context, with dates and the institutions involved].

The corpus already holds [list of documents with dates]. WHAT IS MISSING is [the gap].

TASK: find and READ [the kinds of primary text, and the actors who wrote them].

Rules:
- Use WebSearch and WebFetch only. Read-only: do not download or save files, do not use curl,
  do not write files. If a site is declined, do not work around it; report it as a lead.
- WebFetch passes pages through a summarising model, so ask it for verbatim sentences and mark
  every excerpt "verbatim as returned by the tool, to verify".
- Report only texts you actually opened. A page you could not open is a lead.
- For each text give: author or organisation; title; date; URL; type; language; whether a capture
  exists in the Internet Archive (query https://archive.org/wayback/available?url=THE_URL with
  WebFetch); and up to four excerpts of at most 40 words each.
- Accuracy matters more than coverage. Flag every uncertainty.

Final answer (at most 1,200 words): 1. Texts found (table). 2. Excerpts grouped by actor.
3. [The question this case must answer]. 4. Leads not opened. 5. A ranked list of the texts
most worth saving.
```

## 5. The case search by the main session

The criteria were a dispute between 2021 and 2026 in which biometric identification was a condition of assistance or status, with a recorded refusal or contestation, an institutional response, and little academic work on it. The main session ran these 32 searches on 3 October between 12:10 and 12:31 and read 25 pages; the dates in the queries are part of the queries.


1. refugees refuse biometric registration food assistance suspended 2024
2. refugees protest biometric verification exercise rations cut 2025
3. Lebanon UNHCR data sharing General Security Syrian refugees biometric 2023 refugees fear
4. Malaysia government refugee registration system biometric UNHCR takeover 2025 refugees
5. SASSA biometric verification grants suspended Black Sash 2025
6. Gaza Humanitarian Foundation facial recognition aid distribution biometric refused UN 2025
7. Egypt asylum law 2024 registration transfer from UNHCR refugees biometric concerns
8. Kenya refugees Maisha Namba digital ID integration refugee data 2025 concerns biometric
9. Thailand border camps refugees biometric registration 2025 Myanmar refugees fear
10. Afghanistan Taliban demand biometric data aid beneficiaries WFP NGOs 2024 2025
11. Kakuma Dadaab refugees protest biometric verification food 2025 WFP
12. Pakistan Afghan refugees biometric verification PoR card refuse 2024 2025 UNHCR
13. Rohingya refugees Malaysia afraid to register immigration DPP biometric 2026
14. Palestinians refuse facial recognition aid sites Gaza biometric screening fear 2025
15. SASSA facial recognition court challenge Black Sash biometric grants 2026
16. Syrian refugees Lebanon object UNHCR data sharing stopped approaching UNHCR fear deportation 2024
17. refugees refused biometric enrolment 2023 2024 camp "refused" biometrics UNHCR WFP news
18. Sudanese refugees Chad Egypt biometric registration protest food assistance 2024 2025
19. Humanitarian Country Team statement Gaza aid delivery plan May 2025 "humanitarian principles" biometric screening
20. Gaza Humanitarian Foundation facial recognition statement GHF denies or confirms biometric identification aid recipients
21. Mizoram cabinet refuses biometric data collection Myanmar refugees Ministry of Home Affairs 2023
22. SASSA media statement biometric enrolment September 2025 fraud identity verification grants
23. DVB Refugees in Malaysia face uncertain future new registration program Rohingya interview
24. "Gaza Humanitarian Foundation" "facial recognition" statement GHF spokesperson recipients identity verification
25. Mizoram biometric data Myanmar refugees 2025 Centre MHA foreigners portal collection resumed Lalduhoma
26. journal article 2026 biometric humanitarian aid Gaza Humanitarian Foundation facial recognition analysis
27. Malaysia "Dokumen Pendaftaran Pelarian" UNHCR statement 2026
28. COGAT statement aid distribution Gaza recipients identification screening May 2025 Israel facial recognition official
29. Kementerian Dalam Negeri kenyataan media Dokumen Pendaftaran Pelarian DPP biometrik 2026
30. DIPR Mizoram biometric enrolment Myanmar refugees Foreigners Identification Portal 2025 press release
31. Black Sash statement SASSA biometric enrolment facial recognition 2025 site:blacksash.org.za
32. Reuters "Palestinians rush US-backed aid centre despite concerns over checks"


## 6. Scripts

### 6.1 Save a web page as text (Chrome)

The script runs inside the page, in Claude in Chrome's JavaScript tool or in the browser console. It writes the visible text of the article, main or body element, or with `dom: true` the full text including collapsed sections, under a header that gives the doc_id, title, address, publication date from the metadata, retrieval time and the element copied. Chrome allows one automatic download per tab, so each page needs a fresh tab. Downloads land in `~/Downloads` and are moved with the script in 6.3.

```javascript
// Save the open page as a text file with a header that records its source.
// Run it in the page (Claude in Chrome's javascript tool, or the DevTools console).
// Use a fresh tab for each page: Chrome allows one automatic download per tab.
await (async () => {
  const C = {
    p: '09_OC_',       // case number and class, for example 10_MC_
    fb: '2025-08-18',  // date to use if the page metadata gives none
    s: '_GHF_001',     // _Source_NNN
    force: null,       // a complete doc_id to use regardless of metadata, or null
    dom: false,        // true copies all text in the page, including collapsed sections
    sel: null          // CSS selector of the element to copy, or null for automatic choice
  };
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  for (let i = 0; i < 20 && !document.body; i++) await sleep(250);
  if (location.protocol === 'chrome-error:') return 'The page did not load.';
  const head = document.title + ' ' + document.body.innerText.slice(0, 600);
  if (/automated user|short interruption|verify you are human|security verification|page not found/i.test(head))
    return 'A security check or a missing page. Do not interact; wait, and if the page loads, save it from a fresh tab.';
  window.scrollTo(0, document.body.scrollHeight);           // let lazy content load
  let last = -1, stable = 0;
  for (let i = 0; i < 6; i++) {
    await sleep(400);
    const L = document.body.innerText.length;
    if (L === last) { if (++stable >= 2) break; } else { stable = 0; last = L; }
  }
  window.scrollTo(0, 0);
  const metaSel = ['meta[property="article:published_time"]', 'meta[name="article:published_time"]',
    'meta[property="og:published_time"]', 'meta[name="date"]', 'meta[name="pubdate"]',
    'meta[itemprop="datePublished"]', 'meta[name="publish-date"]', 'meta[name="parsely-pub-date"]',
    'meta[name="sailthru.date"]', 'meta[name="dcterms.date"]', 'meta[name="DC.date"]'];
  let pub = null;
  for (const s of metaSel) { const m = document.querySelector(s); if (m && m.content) { pub = m.content; break; } }
  if (!pub) { const t = document.querySelector('time[datetime]'); if (t) pub = t.getAttribute('datetime'); }
  if (!pub) {
    try {
      for (const sc of document.querySelectorAll('script[type="application/ld+json"]')) {
        const j = JSON.parse(sc.textContent);
        const arr = Array.isArray(j) ? j : (j['@graph'] || [j]);
        for (const o of arr) { if (o && o.datePublished) { pub = o.datePublished; break; } }
        if (pub) break;
      }
    } catch (e) {}
  }
  const mod = (document.querySelector('meta[property="article:modified_time"]') || {}).content || null;
  const d = (pub && /^\d{4}-\d{2}-\d{2}/.test(pub)) ? pub.slice(0, 10) : C.fb;
  const docId = C.force || (C.p + d + C.s);
  let el, en;                                                // the element to copy
  if (C.sel && document.querySelector(C.sel)) { el = document.querySelector(C.sel); en = C.sel; }
  else {
    const arts = [...document.querySelectorAll('article')].filter(a => a.innerText.length > 1500);
    if (arts.length === 1) { el = arts[0]; en = 'article'; }
    else if (document.querySelector('main') && document.querySelector('main').innerText.length > 800) { el = document.querySelector('main'); en = 'main'; }
    else { el = document.body; en = 'body'; }
  }
  const W = n0 => {                                          // all DOM text, for collapsed sections
    let o = '';
    for (const n of n0.childNodes) {
      if (n.nodeType === 3) o += n.nodeValue;
      else if (n.nodeType === 1) {
        const t = n.tagName;
        if (/^(SCRIPT|STYLE|NOSCRIPT|SVG|IFRAME)$/.test(t)) continue;
        if (/cookie/i.test((n.id || '') + ' ' + (typeof n.className === 'string' ? n.className : ''))) continue;
        const b = /^(P|DIV|LI|UL|OL|H[1-6]|TR|TABLE|SECTION|ARTICLE|BLOCKQUOTE|BR|DT|DD|FIGCAPTION|HEADER|FOOTER|ASIDE|NAV|DETAILS|SUMMARY)$/.test(t);
        if (b) o += '\n'; o += W(n); if (b) o += '\n';
      }
    }
    return o;
  };
  const text = C.dom
    ? W(el).replace(/[ \t ]+/g, ' ').split('\n').map(s => s.trim()).join('\n').replace(/\n{3,}/g, '\n\n').trim()
    : el.innerText;
  const how = C.dom ? `DOM text of the <${en}> element, including collapsed sections, whitespace normalised`
                    : `innerText of the <${en}> element, saved verbatim from the browser`;
  const content = `doc_id: ${docId}\ntitle: ${document.title}\nurl: ${location.href}\npublished_meta: ${pub || 'not found'}\n` +
                  `modified_meta: ${mod || 'not found'}\nretrieved: ${new Date().toISOString()}\ncopy: ${how}\n---\n` + text;
  let sha = 'n/a';
  if (window.crypto && crypto.subtle) {
    const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(content));
    sha = [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
  }
  const a = document.createElement('a');
  a.href = URL.createObjectURL(new Blob([content], { type: 'text/plain;charset=utf-8' }));
  a.download = docId + '.txt'; document.body.appendChild(a); a.click(); a.remove();
  return JSON.stringify({ docId, element: en, chars: text.length, sha256: sha, published: pub });
})()
```

### 6.2 PDFs

Four PDFs were downloaded with curl on the Mac. The UN Digital Library serves its files only to a browser, so S/2025/313 was fetched inside its record page.

```bash
A="$HOME/Documents/02. Papers/-Data Colonialism/-corpus/BDS_Corpus_Archive"
cd "$A" || exit 1
curl -fsSL -m 90 -o "CASE09/09_OC_2025-05-08_GHF_002.pdf" \
  "https://static-cdn.toi-media.com/www/uploads/2025/05/Gaza-Humanitarian-Foundation-Memo.pdf"
curl -fsSL -m 90 -o "CASE10/10_OC_2026-05-18_MOHA_001.pdf" \
  "https://www.moha.gov.my/utama/images/Kenyataan%20Media/MEI_2026/18_MEI_2026_KENYATAAN_MEDIA_LAWATAN_KERJA_YB_MENTERI_DALAM_NEGERI_KE_PUSAT_PENGASINGAN_KHAS_PELARIAN_DAN_PEMOHON_SUAKA_BIDOR_PERAK.pdf"
curl -fsSL -m 90 -o "CASE11/11_PA_2023-09-xx_BlackSash_002.pdf" \
  "https://blacksash.org.za/wp-content/uploads/2023/09/Bowmans_BlackSash_POPI.pdf"
curl -fsSL -m 90 -o "CASE11/11_PA_2025-02-xx_IEJ_001.pdf" \
  "https://iej.org.za/wp-content/uploads/2025/03/South-Africa-SRD-exclusions_WEB.pdf"
file CASE*/*.pdf
```

```javascript
// Run on the record page https://digitallibrary.un.org/record/4082957 once it has loaded.
await (async () => {
  const r = await fetch('https://digitallibrary.un.org/record/4082957/files/S_2025_313-EN.pdf', { credentials: 'include' });
  const b = await r.blob();
  const magic = String.fromCharCode(...new Uint8Array(await b.slice(0, 5).arrayBuffer()));
  if (magic !== '%PDF-') return 'Not a PDF (HTTP ' + r.status + ')';
  const a = document.createElement('a');
  a.href = URL.createObjectURL(b); a.download = '09_OC_2025-05-19_IsraelUN_001.pdf';
  document.body.appendChild(a); a.click(); a.remove();
  return 'Saved ' + b.size + ' bytes';
})()
```

### 6.3 Move, hash and list

```bash
#!/bin/bash
# Move downloaded copies into their folders, then list SHA-256, size and path of today's files.
shopt -s nullglob
A="$HOME/Documents/02. Papers/-Data Colonialism/-corpus/BDS_Corpus_Archive"
cd "$HOME/Downloads" || exit 1
mkdir -p "$A/NODE"
for f in 00_*; do mv -n "$f" "$A/NODE/"; done
for c in 06 09 10 11 12; do
  mkdir -p "$A/CASE$c"
  for f in ${c}_OC_* ${c}_MC_* ${c}_CS_* ${c}_PA_*; do mv -n "$f" "$A/CASE$c/"; done
done
cd "$A" || exit 1
find NODE CASE* -type f -newermt "$(date +%Y-%m-%d)" | sort | while read -r f; do
  printf "%s\t%s\t%s\n" "$(shasum -a 256 "$f" | cut -c1-64)" "$(stat -f %z "$f")" "$f"
done
```

### 6.4 Check quotations against the saved copies

This script checked the 22 quotations of 3 October. The excerpts of the textual analysis were checked later with `scripts/archive/verify_excerpts.py`, and the files themselves can be checked against the manifest with `scripts/archive/check_hashes.py` (see `data-and-scripts.md`).

```python
#!/usr/bin/env python3
"""Check that quotations appear word for word in the saved copies.
Usage: python3 check_quotes.py quotes.tsv
Each line of quotes.tsv: path<TAB>quotation. Needs pypdf for PDFs."""
import re, sys, unicodedata
from pypdf import PdfReader

def norm(s):
    s = unicodedata.normalize('NFKC', s)
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), (' ', ' ')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', s).lower()

def text(path):
    if path.endswith('.pdf'):
        return ' '.join((p.extract_text() or '') for p in PdfReader(path).pages)
    return open(path, encoding='utf-8').read()

cache = {}
for line in open(sys.argv[1], encoding='utf-8'):
    if '\t' not in line:
        continue
    path, quote = line.rstrip('\n').split('\t', 1)
    if path not in cache:
        cache[path] = norm(text(path))
    print(('OK   ' if norm(quote) in cache[path] else 'MISS ') + path + ' | ' + quote[:70])
```

## 7. Conventions

- **doc_id.** `[case]_[class]_[YYYY-MM-DD]_[Source]_[NNN]`, as defined in Prompt A of the April 2026 collection. NODE files use the case number 00.
- **Classes**, as defined in Prompt A: OC, organisational communications (press releases, programme descriptions, executive statements); MC, media coverage; CS, civil society reports (reports, open letters, legal filings and policy briefs of advocacy organisations); PA, policy and governance documents (audits, regulatory rulings, parliamentary testimony, court opinions, UNHCR data protection policies, contracts).
- **Dates.** The publication date from the page metadata, else from the text, else from the address. Prompt A uses the first of January when only the year is known.
- **Header** of each text copy: doc_id, title, url, published_meta, modified_meta (second batch only), retrieved (UTC), copy. The text follows a line of three hyphens.
- **Log.** Each file is recorded in `ARCHIVE_LOG.md` with its title, date and the first 16 characters of its SHA-256. The status "Saved" means not yet read in full.

## 8. Deviations to settle

These were found while writing this file and have not been corrected, because renaming changes the doc_id line inside each file and therefore its hash.

1. **Civil society texts filed as PA (11 files).** Prompt A classes them as CS: 09_PA_2025-05-15_Skyline_001, 09_PA_2025-09-10_Skyline_002, 10_PA_2026-05-04_HRW_001, 10_PA_2026-06-01_FortifyRights_001, 10_PA_2026-07-23_Amnesty_001, 10_PA_2026-07-30_MERHROM_001, 11_PA_2023-09-xx_BlackSash_002, 11_PA_2024-06-24_BlackSash_001, 11_PA_2024-07-30_UBICoalition_001, 11_PA_2025-02-xx_IEJ_001 and 11_PA_2026-08-03_OpenSecrets_001.
2. **Governance texts filed as OC (6 files).** Prompt A classes them as PA: 00_OC_2026-10-03_UNHCR_001, 10_OC_2026-07-23_Hansard_001, 11_OC_2025-01-23_Judgment_001, 11_OC_2025-04-01_SRDRegs_001, 11_OC_2025-07-01_PMG_001 and 11_OC_2025-09-17_PMG_002.
3. **Borderline (2 files).** The UNHCR Malaysia privacy notice (10_OC_2026-07-09_UNHCR_003) and Israel's letter to the Security Council (09_OC_2025-05-19_IsraelUN_001) could be PA.
4. **Month-only dates (2 files).** 11_PA_2023-09-xx_BlackSash_002 and 11_PA_2025-02-xx_IEJ_001 use xx for the day. By analogy with Prompt A, they would become 2023-09-01 and 2025-02-01.
5. **Undated pages (2 files).** 00_OC_2026-10-03_UNHCR_001 and 10_OC_2026-10-03_UNHCR_002 carry the retrieval date.
6. **Wayback copies.** 10_MC_2025-12-13_DVB_001 (live site down) and 06_OC_2023-05-02_UNHCR_005 (page removed) were saved from Wayback captures. On the afternoon of 3 October such copies were left to the author instead. One rule should be chosen.
7. **Page count (corrected).** Version 1.4 of the archive log gave the GHF memo 38 pages, the figure that the `file` command reports. The PDF reader and the page tree both count 14, and version 1.5 of the log corrects it.

The tables in `corpus-tables.md` and the page count each file under the class that Prompt A gives.

## 9. Reproducing the corpus

**What can be reproduced.** The saved copies and their hashes are the corpus of record. Anyone can check that a file is unchanged by recomputing its SHA-256 and comparing it with `ARCHIVE_LOG.md`. The procedure can be repeated with the prompts and scripts above. The outputs cannot be repeated exactly: search results change, pages move or disappear (ghf.org no longer exists, and the UNHCR Malaysia notice changed address), and language models do not return the same text twice. A new run therefore reproduces the procedure and the criteria, not the same set of files.

**Prompt for a new session.** This prompt is reconstructed from the steps above. The original work proceeded step by step in conversation, with the author's decisions at each stage.

```text
You are working with Dr Marco Scalvini on the corpus of a critical discourse analysis article on
biometric identification as a condition of assistance, 2021 to 2026. You have web search and web
reading, Claude in Chrome, and a shell on Marco's Mac. The archive is
~/Documents/02. Papers/-Data Colonialism/-corpus/BDS_Corpus_Archive, with ARCHIVE_LOG.md.

Design. The node is UNHCR's identity-management discourse (Guidance on Registration and Identity
Management, section 5.2), articulated most fully in Bangladesh (CASE06). The cases trace its
recontextualisation: Gaza 2025 (CASE09), Malaysia 2025 to 2026 (CASE10), South Africa 2024 to 2026
(CASE11), and Mizoram, India, 2023 to 2026 (CASE12). Case documents must date from the last five
years.

1. For each case, run one read-only search agent with the template in section 4.5 of
   docs/corpus-construction.md, stating what the corpus holds and what is missing.
2. From the agents' ranked lists, propose the documents to save, giving for each the doc_id,
   the source and the size. Wait for Marco's approval before saving anything.
3. Save each approved web page with the script in section 6.1, one fresh tab per page, and each
   PDF with curl (section 6.2). Never complete or bypass a CAPTCHA or an interactive check. If a
   site refuses automated access, leave the page for Marco to save from his own browser. Move any
   error or check page that was downloaded by mistake to the Trash.
4. Move the files into their folders and list their hashes (section 6.3). Add a section to
   ARCHIVE_LOG.md with one row for each file, and raise its version.
5. Check every quotation you report against the saved copies (section 6.4). Mark any other
   excerpt "to verify".
6. Record the run in DC_Log.md: the agents (number, task, effort), the searches, Marco's
   decisions, the files saved and not saved, and the checks.
```

## 10. Rules followed during collection

- Agents searched and read only; every file was saved by the main session after the author approved the list, with the filename, source and size given beforehand.
- No CAPTCHA or interactive check was completed. Two pages showed a security check that finished by itself in the browser; nothing was clicked, and each page was saved again from a fresh tab.
- Sites that refuse automated access were not approached by other means; those pages are left for the author to save himself.
- Excerpts returned by agents were treated as unverified until found word for word in the saved copies.
- Every saved file has a SHA-256 in the archive log, and the files discarded during saving (an error page and two security-check pages) are in the Trash, not in the archive.
