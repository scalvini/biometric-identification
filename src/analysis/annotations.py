# Level-1 (textual) annotations for the 21 saved core texts.
# Excerpts are referenced by index into quotes.jsonl (verified against the archive copies).
# Annotation tuple: (code, span, sub-label, note[, occurrence index])

def A(code, span, sub, note, k=None):
    d = {"c": code, "s": span, "sub": sub, "n": note}
    if k is not None:
        d["k"] = k
    return d

def X(q, v, a, gl=None):
    d = {"q": q, "v": v, "a": a}
    if gl:
        d["gl"] = gl
    return d

GROUPS = [
    {"k": "node", "name": "Node: UNHCR guidance", "short": "Node"},
    {"k": "bd", "name": "Bangladesh (node instance)", "short": "Bangladesh"},
    {"k": "gaza", "name": "Gaza", "short": "Gaza"},
    {"k": "my", "name": "Malaysia", "short": "Malaysia"},
    {"k": "za", "name": "South Africa", "short": "South Africa"},
    {"k": "mz", "name": "Mizoram, India", "short": "Mizoram"},
]

CATS = [
    {"c": "ACT", "name": "Social actors", "ref": "2003, pp. 145 to 150",
     "def": "How people and institutions are included or excluded, activated or passivated, named or classified, and made specific or generic.",
     "ask": "Who acts upon whom, and who is absent from the clause?"},
    {"c": "NOM", "name": "Nominalisation", "ref": "2003, pp. 12 to 13, 143 to 144",
     "def": "Processes represented as nouns, which can remove the agent and the time of the process from the clause.",
     "ask": "Which processes become things, and whose agency disappears with them?"},
    {"c": "MODD", "name": "Deontic modality", "ref": "2003, pp. 167 to 170",
     "def": "Commitment to obligation or permission, expressed through modal verbs and through adjectives and nouns such as ‘required’ or ‘pre-requisite’.",
     "ask": "Who is obliged or permitted, and by whom?"},
    {"c": "MODE", "name": "Epistemic modality", "ref": "2003, pp. 167 to 171",
     "def": "Commitment to truth, ranging from categorical assertion to hedged or attributed claims.",
     "ask": "How strongly does the text commit to what it claims?"},
    {"c": "EVAL", "name": "Evaluation", "ref": "2003, pp. 171 to 173",
     "def": "Evaluative statements and attributes, together with affective mental processes such as fear or concern.",
     "ask": "What is presented as good or bad, and on whose authority?"},
    {"c": "REL", "name": "Semantic relations", "ref": "2003, pp. 89 to 91",
     "def": "Relations between clauses and sentences, such as reason, consequence, purpose, condition, contrast and time.",
     "ask": "How are refusal and loss connected in the grammar?"},
    {"c": "ASM", "name": "Assumptions", "ref": "2003, pp. 55 to 58",
     "def": "What the text takes as given. Fairclough separates assumptions about existence and about what is the case from assumptions about value.",
     "ask": "What must the reader already accept for the sentence to make sense?"},
    {"c": "REP", "name": "Reporting and intertextuality", "ref": "2003, pp. 39 to 51",
     "def": "How other voices enter the text, whether quoted, paraphrased, left unattributed or held at a distance by scare quotes.",
     "ask": "Whose words are these, and how close does the text stand to them?"},
    {"c": "LEG", "name": "Legitimation", "ref": "2003, pp. 98 to 100",
     "def": "Justification by authority, by utility, by moral value or by narrative, following Van Leeuwen’s strategies as Fairclough presents them.",
     "ask": "On what grounds is the condition justified?"},
    {"c": "LEX", "name": "Wording", "ref": "2003, pp. 129 to 133",
     "def": "Choices of vocabulary and naming that identify a discourse and classify people and places.",
     "ask": "Which words name the people and the place?"},
]

DOCS = []

# ---------------------------------------------------------------- NODE
DOCS.append({
 "id": "00_OC_2026-10-03_UNHCR_001", "g": "node", "pos": "Standard", "cls": "PA", "lang": "English",
 "short": "UNHCR guidance §5.2",
 "title": "UNHCR, Guidance on Registration and Identity Management, section 5.2, ‘Registration as an Identity Management Process’",
 "date": "Undated (retrieved 3 Oct 2026)",
 "voice": "UNHCR operational guidance addressed to registration staff. Several sentences tell the interviewer what to say to the person being registered.",
 "profile": "The section makes the individual the grammatical holder of a right to refuse and defines consent as a genuine choice without adverse consequences. The same list places an obligation to cooperate beside the reminder of voluntariness. In a footnote, the guidance then assigns the requirement to share data, together with the right to object, to government policy wherever a government leads registration.",
 "ex": [
  X(0, "Guidance to staff, in the list headed ‘Rights and obligations of individuals’.", [
   A("ACT", "Individuals", "Generic, passivated", "People appear as a generic class and as the object of reminding, while the staff member who reminds them stays implicit in the passive."),
   A("MODD", "should", "Median obligation", "The median deontic ‘should’ places the duty to remind on staff, which makes voluntariness something the interviewer must state."),
   A("NOM", "participation in registration", "Process as noun", "The nominalisation turns the act of registering into a state that can carry the attribute ‘voluntary’, with no agency named as the one asking."),
   A("MODE", "is voluntary", "Categorical assertion", "The unmodalised present asserts voluntariness as a fact about registration, the attribute that the Bangladesh notice replaces with ‘required’ in the same frame."),
  ]),
  X(59, "Guidance to staff, the next item in the same list.", [
   A("MODD", "their obligation to cooperate", "Obligation as noun", "Placed directly after the reminder of voluntariness, the obligation appears as a noun that the individual possesses, and the agency that demands cooperation is left unstated."),
   A("ASM", "truthful and complete responses", "Propositional", "The demand for truthful and complete answers presupposes that answers could be otherwise, an assumption that the verification texts in the cases make explicit."),
  ]),
  X(1, "Guidance to staff, same list.", [
   A("ACT", "Individuals have the right to refuse", "Activated holder of a right", "The individual is the activated holder of a right to refuse, and the node is the only text in the core corpus where refusal belongs to the person as a right."),
   A("NOM", "the collection of their biometrics", "Process as noun", "The nominalisation names the collecting without a collector, so the right is directed at a process whose agent is absent."),
   A("ASM", "on legitimate grounds related to his or her specific personal situation", "Propositional", "The qualification assumes that refusal needs grounds and that someone other than the person judges their legitimacy, locating those grounds in individual circumstances."),
   A("LEX", "legitimate", "Recurrent attribute", "The same adjective qualifies the host government’s ‘interest in knowing who is on its territory’ a few paragraphs later."),
  ]),
  X(60, "Guidance to staff, the sentence that follows the right to refuse.", [
   A("ASM", "This does not alter their right to international protection", "Presupposition", "The assurance presupposes that a reader might expect refusal to affect protection, which is the link that the operational texts go on to make."),
   A("MODE", "does not alter", "Categorical negative", "A categorical negative in the present tense guarantees that refusal leaves protection intact, with no condition attached."),
   A("LEX", "of concern to UNHCR", "Institutional category", "The phrase keeps the refuser inside the agency’s mandate category, so refusal leaves the person’s institutional status unchanged."),
  ]),
  X(2, "Guidance to staff, the sentence after the assurance.", [
   A("MODD", "may be registered", "Low, permission", "The low modal ‘may’ permits registration without biometrics and leaves the decision with the operation."),
   A("ACT", "alternative methods identified", "Suppressed agent", "The elliptical passive leaves open who identifies the alternatives and who bears the work of finding them."),
   A("REL", "to ensure they can access rights, assistance and solutions", "Purpose", "The purpose relation ties refusal to continued access, the relation that the Bangladesh notice and FAQ replace with consequence."),
  ]),
  X(3, "Footnote 5 of the section.", [
   A("REL", "Where the host government leads registration procedures", "Conditional", "The conditional clause names the case in which the guidance defers to a government, the arrangement found in Bangladesh and Malaysia."),
   A("MODD", "the requirement to share personal data including biometrics", "Obligation as noun", "The obligation to share is a noun with no stated source, so the requirement exists in the sentence before any agent imposes it."),
   A("LEX", "(and the related right to object)", "Bracketed right", "The right to object appears in brackets as an appendage of the requirement, a typographic subordination of the person’s right."),
   A("MODE", "may be determined", "Possibility, agent suppressed", "The modal passive leaves open both whether and by whom the matter is decided."),
   A("REL", "not UNHCR policy", "Contrastive", "The closing contrast removes the agency’s own policy from the case, so the footnote marks the point where the node’s standard stops applying."),
  ]),
  X(4, "Content the interviewer ‘should further explain’ to the person when seeking consent to share data.", [
   A("ACT", "The host government", "Activated institution", "The government is the activated holder of an interest, the grammatical role the individual holds as bearer of a right to refuse."),
   A("EVAL", "legitimate", "Evaluative attribute", "The attribute evaluates the government’s interest positively, using the adjective that elsewhere restricts the individual’s grounds for refusal."),
   A("NOM", "knowing who is on its territory", "Process as noun", "Knowledge of presence is nominalised as the object of the interest, a phrase the 2026 FAQ from Bangladesh restates as ‘authorities know who has arrived on their territory’."),
  ]),
  X(5, "Guidance on consent to share personal information.", [
   A("LEX", "Freely given means that", "Definition", "The definitional frame fixes the meaning of consent inside the guidance and makes the definition available for citation by other texts."),
   A("ACT", "the individual has a genuine choice and is able to refuse or withdraw", "Activated", "The individual is the subject of every process in the definition, holding the choice and performing refusal or withdrawal."),
   A("ASM", "genuine", "Value assumption", "The attribute ‘genuine’ presupposes that a choice can exist in name only, the possibility that UNICEF later calls an ‘impossible choice’."),
   A("REL", "without adverse consequences", "Consequence, negated", "The phrase detaches refusal from loss, the relation that the Bangladesh texts and the South African texts reverse."),
  ]),
 ]})

# ---------------------------------------------------------------- BANGLADESH
DOCS.append({
 "id": "06_OC_2023-05-02_UNHCR_005", "g": "bd", "pos": "Articulation", "cls": "OC", "lang": "English",
 "short": "UNHCR Bangladesh notice, 2023",
 "title": "UNHCR Bangladesh, ‘Registration Update Exercise Notice’",
 "date": "2 May 2023",
 "voice": "UNHCR Bangladesh notice addressed to registered refugees in the camps, setting out the registration update exercise.",
 "profile": "The notice keeps the node’s nominalisation ‘participation’ and gives it the attribute ‘required’, then states the loss of all future assistance as a certain consequence of absence. The agencies that enrol and inactivate disappear behind agentless passives, while people appear as eligible persons or as persons who fail to show up.",
 "ex": [
  X(6, "Notice, the paragraph after the stated purpose of the exercise.", [
   A("LEX", "Biometrics", "Subject of the passive", "The subject of the passive is ‘biometrics’, so the body’s measurements occupy the place of the person being enrolled."),
   A("ACT", "will be enrolled", "Suppressed agent", "The agentless passive with ‘will’ presents enrolment as scheduled fact and leaves the enrolling agencies unnamed."),
   A("ACT", "all individuals 5 years and above", "Generic, classified by age", "People are classified by age alone, so children from the age of five enter the clause as subjects of enrolment."),
   A("REL", "given that", "Reason", "The connective presents its reason as already granted, so the reader receives the justification as common ground."),
   A("NOM", "establishing and preserving identities", "Process as noun", "Two gerunds name identity work without an agent who establishes or preserves."),
   A("LEG", "is key to ensuring protection and solutions for refugees", "Rationalisation", "Enrolment is legitimated by its utility for protection, an instrumental claim stated categorically."),
  ]),
  X(7, "Notice, under the heading ‘ATTENDANCE’.", [
   A("NOM", "Participation in the exercise", "Process as noun", "The node’s nominalisation returns in the same grammatical position, which makes the comparison with ‘participation in registration is voluntary’ direct."),
   A("MODD", "is required", "High obligation", "The deontic ‘required’, which Fairclough (2003, p. 170) gives as a marker of obligation, takes the place of ‘voluntary’ and names no requiring agency."),
   A("ACT", "all eligible persons", "Generic class", "The obligation falls on a generic class defined by eligibility, which the notice itself determines."),
  ]),
  X(8, "Notice, under ‘ATTENDANCE’.", [
   A("ACT", "Persons who fail to show up", "Activated in a failure", "The relative clause defines people by a failure, which makes absence their own act and the first link in the sequence."),
   A("ACT", "will be inactivated", "Suppressed agent", "The agentless passive states deactivation of the record as certain and leaves the deactivating agency unnamed."),
   A("REL", "and they will not benefit from any assistance in future", "Consequence", "The coordinated clause attaches a permanent loss of assistance to absence, the consequence relation that the node’s definition of consent excludes."),
   A("MODE", "any assistance in future", "Categorical, unlimited", "The quantifier ‘any’ and the phrase ‘in future’ give the loss no limit in scope or time."),
  ]),
 ]})

DOCS.append({
 "id": "06_OC_2026-01-20_UNHCR_006", "g": "bd", "pos": "Articulation", "cls": "OC", "lang": "English",
 "short": "GoB and UNHCR FAQ, 2026",
 "title": "Government of Bangladesh and UNHCR, ‘Frequently Asked Questions on Improved Data Processing Modalities’",
 "date": "20 Jan 2026",
 "voice": "Question and answer page published by UNHCR in the names of the Government of Bangladesh and UNHCR.",
 "profile": "The FAQ sets protection beside the state’s knowledge of arrivals as purposes of equal rank. Refusal returns as a nominalised subject that ‘may lead’, through further nominalisations, to deregistration and the end of protection, with the deciding agencies absent from the chain.",
 "ex": [
  X(9, "Opening answer of the FAQ.", [
   A("NOM", "Registration and identification", "Process as noun", "Two nominalisations occupy the subject position and do the helping, so no agency appears as the one who registers or identifies."),
   A("ACT", "people who need protection can be recognized and supported", "Passivated", "People are the passivated objects of recognition and support, defined by their need."),
   A("REL", "and that authorities know who has arrived on their territory", "Additive, equivalence", "The coordinating ‘and’ gives the authorities’ knowledge of arrivals the same rank as protection, restating the node’s ‘legitimate interest in knowing who is on its territory’."),
  ]),
  X(10, "FAQ, same answer.", [
   A("MODD", "Refugees’ obligations", "Obligation as noun", "Obligation is nominalised and attributed to refugees as its possessors, which makes compliance a property of refugee status."),
   A("LEG", "under international refugee law", "Authorisation", "The duties are legitimated by the authority of international law, which the answer invokes in general terms."),
   A("LEX", "a duty to provide accurate information", "Data as duty", "Supplying data becomes a legal duty, a wording close to the node’s ‘obligation to cooperate and give truthful and complete responses’."),
  ]),
  X(11, "FAQ, inside the reason clause that describes registration as a joint process of UNHCR and the Government of Bangladesh.", [
   A("MODD", "a pre-requisite", "Condition as noun", "The noun states a condition without a modal verb, so obligation appears as a property of registration itself."),
   A("NOM", "the GoB’s protection and assistance", "Process as noun, owned", "Protection and assistance are nominalised and owned by the government, which becomes their sole source in this clause."),
  ]),
  X(12, "FAQ, the main clause after the reason clause.", [
   A("NOM", "refusing the processing of personal data", "Gerund subject", "The refuser is absorbed into a gerund and the refused process is itself nominalised, so refusal appears as an event with no person in it."),
   A("MODE", "may lead to", "Possibility", "Epistemic ‘may’ softens a causal chain whose links are all nominalised, which lowers commitment while keeping the chain."),
   A("NOM", "deregistration", "Outcome as noun", "The outcome is named without a deregistering agent."),
   A("REL", "as a result", "Consequence", "The explicit marker links refusal to the end of protection, the reverse of ‘without adverse consequences’ in the node."),
   A("NOM", "the discontinuation of protection and assistance", "Outcome as noun", "A second nominalised outcome completes the chain, again with no agent who discontinues."),
   A("MODE", "depending on the circumstances", "Hedge", "The closing hedge leaves the deciding criteria unstated."),
  ]),
 ]})

DOCS.append({
 "id": "06_MC_2025-06-01_Diplomat_002", "g": "bd", "pos": "Response to refusal", "cls": "MC", "lang": "English",
 "short": "The Diplomat, 2025",
 "title": "The Diplomat (Shafiur Rahman), ‘UNHCR Defends Biometric Enrollment Push for Rohingya Refugees’",
 "date": "12 Jun 2025",
 "voice": "News report on refugee families who refused enrolment, with UNHCR’s written replies quoted and paraphrased.",
 "profile": "The report places the families’ refusal and the loss of food aid in a temporal sequence and keeps the agency of the cut-off implicit. The quoted replies legitimate enrolment by global standards and by the agency’s mandate, and they report an assessment of risk that has no named assessor.",
 "ex": [
  X(61, "Lead sentence. The subject is ‘Around 300 to 400 Rohingya refugee families’ in the Nayapara and Kutupalong registered camps.", [
   A("ACT", "have been cut off", "Suppressed agent", "The journalist’s agentless passive leaves the agency that cut off food aid unnamed in the lead sentence."),
   A("REL", "after", "Temporal", "A temporal connective places refusal before loss and leaves the causal link for the reader to infer."),
   A("ACT", "refusing to participate in a biometric data collection drive", "Activated refusers", "The families are the implied agents of refusal, the only clause in the core excerpts where people are reported as having refused."),
   A("LEX", "drive", "Campaign noun", "The noun ‘drive’ presents enrolment as a campaign."),
  ]),
  X(62, "Journalist paraphrasing UNHCR’s letter of 17 March, signed by its Head of Operations in Cox’s Bazar.", [
   A("REP", "The letter stated that", "Indirect", "The agency’s letter reaches the reader in indirect speech, so its wording is the journalist’s paraphrase."),
   A("MODD", "no humanitarian assistance could be provided", "Negated possibility", "The negated ‘could’ with an agentless passive presents exclusion as an impossibility, with no provider named."),
   A("ACT", "those not biometrically registered", "Classified by absence", "People are classified by a negative property, their absence from the biometric register."),
  ]),
  X(13, "UNHCR spokesperson, written reply quoted directly.", [
   A("NOM", "The use of biometrics", "Process as noun", "The nominalisation ‘use’ removes both the users and the persons whose biometrics are used."),
   A("LEG", "aligns with global standards for identity management", "Authorisation", "Conformity with unnamed global standards legitimates the practice by external authority."),
   A("MODD", "is essential for UNHCR to fulfill its mandate", "Necessity", "The adjective ‘essential’ grounds necessity in the agency’s mandate, so the institution’s needs justify the condition."),
  ]),
  X(14, "UNHCR statement, quoted. The journalist adds that the claim concerned ‘suspending distributions’.", [
   A("ACT", "were identified", "Suppressed agent", "The agentless passive reports an assessment with no named assessor and no stated method."),
   A("MODE", "specific", "Hedge", "The qualifier narrows the claim to ‘specific’ risks, which leaves general risk unaddressed."),
  ]),
 ]})

# ---------------------------------------------------------------- GAZA
DOCS.append({
 "id": "09_OC_2025-05-08_GHF_002", "g": "gaza", "pos": "Sets the condition", "cls": "OC", "lang": "English",
 "short": "GHF memo, 2025",
 "title": "Gaza Humanitarian Foundation, ‘Safe, Transparent Aid for Gaza’ (overview memo)",
 "date": "Undated (first copy 8 May 2025)",
 "voice": "The foundation’s own overview memo, written in the first person plural and in lists of activities and inputs.",
 "profile": "The memo names need as its only criterion and mentions identity in order to deny that it counts. Its own lists of activities and inputs include data collection on access and real-time tracking in nominal form, with the collectors and the tracked persons left unnamed.",
 "ex": [
  X(63, "Memo, section on operations. The preceding sentence states that the IDF will not be stationed at the sites.", [
   A("ACT", "Aid will be distributed", "Suppressed agent", "The agentless passive with ‘will’ leaves the distributor implicit in a sentence about the foundation’s own operation."),
   A("LEX", "without regard to identity, origin, or affiliation", "Denied criterion", "The memo names identity in order to deny that it counts, while its list of activities includes data collection on access."),
   A("MODE", "There will be no eligibility requirements", "Categorical negative", "A categorical negative prediction rules out any condition of access."),
   A("LEG", "purely based on need", "Moral evaluation", "Need appears as the sole criterion, a legitimation drawn from humanitarian principle."),
  ]),
  X(16, "Memo, list of ‘Activities’.", [
   A("ACT", "Collect data", "Suppressed agent", "The bare verb in a list omits both the collector and the persons whose data is collected."),
   A("LEX", "access", "Monitored item", "Access is an object of data collection, which leaves open whether the data concern numbers or persons.", 0),
   A("LEX", "recipient feedback", "Naming", "People are named by their relation to aid, as ‘recipients’ whose feedback becomes data."),
  ]),
  X(64, "Memo, list of inputs.", [
   A("NOM", "real-time tracking and reporting", "Process as noun", "The nominalised ‘tracking’ leaves open what or whom the technology tracks."),
  ]),
  X(17, "Memo, statement of values.", [
   A("ACT", "We", "Exclusive we", "The organisational ‘we’ activates the foundation as a moral agent."),
   A("LEG", "based solely on necessity", "Moral evaluation", "Necessity here names the recipients’ need and serves as the sole stated criterion."),
   A("EVAL", "without discrimination or bias", "Evaluation by denial", "Neutrality is asserted through the denial of two negative qualities."),
  ]),
  X(18, "Memo, after the statement that perimeter security will be provided by ‘experienced professionals’.", [
   A("ACT", "the Israeli Defense Forces (IDF)", "Passivated institution", "The army is the passivated object of stationing, and the authority that stations it is unnamed."),
   A("MODE", "will not be stationed", "Categorical negative", "A categorical future negative states the army’s absence as certain."),
   A("LEX", "SDS locations", "Technical naming", "The initialism abbreviates the memo’s ‘safe, neutral aid distribution sites’, so the evaluation is built into the name of the sites."),
  ]),
 ]})

DOCS.append({
 "id": "09_OC_2025-05-19_IsraelUN_001", "g": "gaza", "pos": "Runs or backs it", "cls": "OC", "lang": "English",
 "short": "Israel letter S/2025/313",
 "title": "Permanent Representative of Israel, letter to the President of the Security Council (S/2025/313), with Fletcher’s letter annexed",
 "date": "19 May 2025",
 "voice": "Security Council document with two letters. Annex I is Ambassador Danny Danon to Tom Fletcher, and annex II is Fletcher to Danon, dated 16 May 2025.",
 "profile": "Danon’s letter presents aid as a resumption granted by cabinet approval and justified by looting that it presupposes. Fletcher’s reply speaks of verification measures against theft by Hamas, so both letters share the premise that aid and its recipients must be checked.",
 "ex": [
  X(19, "Danny Danon, annex I, after ‘That is why, after careful deliberation,’.", [
   A("LEG", "the Israeli Security Cabinet has approved", "Authorisation", "Aid depends on the approval of an activated state authority, which legitimates the arrangement by its institutional standing."),
   A("NOM", "the resumption of aid entry", "Process as noun", "Stacked nominalisations present the end of a stoppage without naming who stopped aid from entering."),
   A("ACT", "specific agencies", "Unnamed but specified", "The agencies are marked as specific and yet remain unnamed in the letter."),
   A("NOM", "strict oversight", "Process as noun", "Control appears as a nominalised and intensified quality of the arrangement."),
   A("REL", "to prevent", "Purpose", "The purpose relation legitimates oversight by the harm it prevents."),
   A("ASM", "Hamas’ continued looting of humanitarian resources", "Existential and propositional", "The nominal group presupposes that looting by Hamas exists and continues, so the claim enters the letter as given."),
  ]),
  X(20, "Tom Fletcher, Under-Secretary-General for Humanitarian Affairs, annex II.", [
   A("ACT", "We", "Exclusive we", "The UN’s ‘we’ claims the capacity to deliver."),
   A("EVAL", "solid", "Evaluative attribute", "The attribute asserts the reliability of the UN’s plans."),
   A("LEX", "verification measures", "Shared term", "The UN coordinator also uses the vocabulary of verification, so the premise of checking appears on both sides of the exchange."),
   A("ASM", "aid does not get stolen by Hamas", "Propositional", "The purpose clause accepts the possibility of theft by Hamas that the Israeli letter presupposes."),
  ]),
 ]})

DOCS.append({
 "id": "09_OC_2025-08-08_USEmbassy_001", "g": "gaza", "pos": "Answers contestation", "cls": "OC", "lang": "English",
 "short": "Huckabee interview, CBS",
 "title": "US Embassy Jerusalem, ‘Ambassador Huckabee’s Interview with CBS News’",
 "date": "8 Aug 2025",
 "voice": "Interview transcript published by the US Embassy, with the CBS reporter’s questions and Ambassador Huckabee’s answers.",
 "profile": "The exchange turns on the reporter’s presupposition that recipients might be members of Hamas. The ambassador concedes that no guarantee is possible, then asserts an agentless screening and narrows its purpose to weapons, which leaves the question of identity unanswered.",
 "ex": [
  X(65, "CBS reporter, question to the ambassador.", [
   A("ACT", "we", "Inclusive we", "The reporter’s ‘we’ places questioner and audience among those entitled to know who receives aid."),
   A("ACT", "those people", "Distal reference", "Recipients appear as ‘those people’, held at a distance by the demonstrative."),
   A("ASM", "aren’t from Hamas", "Propositional", "The question presupposes that recipients may belong to Hamas and that their affiliation should be known."),
  ]),
  X(21, "Ambassador Huckabee, answer.", [
   A("ACT", "You", "Generic you", "Generic ‘you’ extends the impossibility to anyone who might attempt a guarantee."),
   A("MODE", "can’t absolutely guarantee", "Negated certainty", "The negated modal with an intensifier concedes that recipients cannot be cleared."),
   A("ASM", "that they’re not", "Accepted presupposition", "The elliptical clause takes over the reporter’s presupposition without restating it."),
  ]),
  X(66, "CBS reporter, follow-up.", [
   A("MODE", "zero", "Categorical", "The numeral ‘zero’ states the absence with full commitment."),
   A("LEX", "verification process", "Frame term", "The reporter makes verification the measure of adequate aid, the frame within which the ambassador then answers."),
  ]),
  X(22, "Ambassador Huckabee, answer.", [
   A("MODE", "Look, no,", "Counter-assertion", "The discourse markers signal disagreement before the claim and raise its assertive force."),
   A("NOM", "a screening", "Process as noun", "Screening is named as a noun, without its agent or its object."),
   A("ACT", "that is done", "Suppressed agent", "The agentless passive repeats the absence of a screener."),
  ]),
  X(23, "Ambassador Huckabee, after the reporter asks ‘What is that screening?’.", [
   A("REL", "to make sure", "Purpose", "The purpose clause redefines the screening as a check for weapons, so the answer moves from identity to objects."),
   A("ACT", "they’re", "Pronoun reference", "Recipients remain an undifferentiated ‘they’."),
  ]),
 ]})

DOCS.append({
 "id": "09_OC_2025-05-09_UNGeneva_001", "g": "gaza", "pos": "Refuses or contests", "cls": "OC", "lang": "English",
 "short": "UN Geneva briefing, UNICEF",
 "title": "UN Geneva press briefing, teleprompter transcript (UNICEF)",
 "date": "9 May 2025",
 "voice": "James Elder for UNICEF, speaking at the briefing. The transcript has no speaker labels, so the speaker is identified from the briefing summary and the surrounding remarks in the same file.",
 "profile": "UNICEF’s objection is carried by an institutional ‘we’ and by affective and moral evaluation. Recipients appear as passivated ‘beneficiaries’, and the evaluation ‘impossible choice’ names the absence of the genuine choice that the node’s definition of consent requires.",
 "ex": [
  X(67, "James Elder (UNICEF), on the distribution plan.", [
   A("MODE", "appears", "Appearance", "The evidential ‘appears’ lowers commitment to a claim about the plan’s design."),
   A("ACT", "designed", "Implied agent", "The participle implies a designer who remains unnamed."),
   A("REL", "to reinforce control over life sustaining items", "Purpose", "The purpose attributed to the plan is control over goods needed for life."),
   A("EVAL", "as a pressure tactic", "Negative evaluation", "The phrase evaluates the plan as coercive."),
  ]),
  X(24, "James Elder (UNICEF). The repetition ‘as a as a’ is in the transcript.", [
   A("ACT", "we", "Institution as objector", "The objecting subject is UNICEF’s ‘we’, so the contestation belongs to an institution."),
   A("EVAL", "are very concerned", "Affective process", "An affective mental process, intensified by ‘very’, carries the objection (Fairclough 2003, p. 173)."),
   A("NOM", "the proposal", "Process as noun", "The nominalisation leaves the author of the plan unnamed."),
   A("MODD", "precondition", "Condition as noun", "The noun names the conditionality to which the speaker objects."),
  ]),
  X(25, "James Elder (UNICEF), the next sentence.", [
   A("LEG", "against all humanitarian principles", "Moral evaluation", "The objection appeals to principle, and the universal ‘all’ raises its commitment."),
   A("ACT", "beneficiaries", "Passivated", "Beneficiaries are the passivated objects of screening and monitoring, with the screener unnamed."),
   A("REL", "for intelligence and military purposes", "Purpose", "The purpose phrase names the uses that the speaker attributes to the screening."),
  ]),
  X(26, "James Elder (UNICEF). The subject is ‘the use of humanitarian aid as a bait to force displacement’.", [
   A("MODE", "will create", "Prediction", "A categorical prediction presents the outcome as certain."),
   A("EVAL", "impossible choice", "Negative evaluation", "The evaluation names a choice in name only, the opposite of the ‘genuine choice’ in the node’s definition of consent."),
   A("NOM", "displacement and death", "Outcomes as nouns", "Two nominalisations name the alternatives without naming who displaces or who dies."),
  ]),
 ]})

DOCS.append({
 "id": "09_MC_2025-05-28_Reuters_001", "g": "gaza", "pos": "Voice of those subject to it", "cls": "MC", "lang": "English",
 "short": "Reuters, 28 May 2025",
 "title": "Reuters, ‘Palestinians rush US-backed aid centre despite concerns over checks’",
 "date": "28 May 2025",
 "voice": "Reuters report, saved from Stabroek News, with direct speech from Abu Ahmed, 55, a father of seven, and reported speech from humanitarian groups.",
 "profile": "The report attributes the checks to Israel through indirect speech and gives agency to nominalised states of desperation and concern. In direct speech the father’s hunger and fear share one concessive sentence, and the reported condition requires ‘anyone’ to ‘submit’.",
 "ex": [
  X(68, "Lead sentence. The main clause reports that thousands of Palestinians rushed a distribution site.", [
   A("NOM", "desperation for food overcoming concern", "States as actors", "Two nominalised states act as participants, so the clause attributes the decision to go to desperation and concern."),
   A("LEX", "biometric and other checks", "Open category", "The vague ‘other checks’ widens the category beyond biometrics."),
   A("REP", "Israel said it would employ", "Indirect", "The checks are attributed to Israel through reported speech, which reports the statement without quoting it."),
  ]),
  X(27, "Abu Ahmed, 55, a father of seven, direct speech.", [
   A("REL", "As much as I want to go", "Concessive", "The concessive frame sets desire against fear inside one sentence."),
   A("REL", "because I am hungry and my children are hungry", "Reason", "The reason clause grounds the wish to go in hunger, his own and his children’s."),
   A("EVAL", "I am afraid", "Affective process", "Fear is the speaker’s stated state, and the sentence contains no clause of refusal."),
  ]),
  X(28, "Reported speech attributed to ‘Humanitarian groups briefed on the foundation’s plans’.", [
   A("ACT", "anyone accessing aid", "Generic", "The generic ‘anyone’ extends the condition to every recipient."),
   A("MODD", "will have to", "High obligation", "The deontic ‘have to’ marks the condition as compulsory."),
   A("LEX", "submit", "Subordination", "The verb ‘submit’ positions the recipient as subordinate to the technology."),
  ]),
 ]})

# ---------------------------------------------------------------- MALAYSIA
DOCS.append({
 "id": "10_OC_2026-05-18_MOHA_001", "g": "my", "pos": "Sets the condition", "cls": "OC", "lang": "Malay",
 "short": "MOHA statement, Bidor",
 "title": "Ministry of Home Affairs, media statement on the Minister’s visit to the Bidor centre",
 "date": "18 May 2026",
 "voice": "Ministry press statement in Malay, written in the third person about the working visit of the Minister of Home Affairs, Datuk Seri Saifuddin Nasution bin Ismail.",
 "profile": "The ministry names the government by its MADANI brand and evaluates refugee management as ‘terkawal’ (controlled) and ‘berperikemanusiaan’ (humane) in one series. Legitimation runs through a National Security Council directive and ‘valid data’, while people appear as migrants and as detainees who have been entered as data.",
 "ex": [
  X(69, "Name of the centre in the statement’s first paragraph.", [
   A("LEX", "Pengasingan", "Naming of place", "‘Pengasingan’ means separation or isolation, so the place where the programme runs is named as a place that separates refugees."),
  ], gl="Special Separation Centre for Refugees and Asylum Seekers (PPKPPS), Bidor"),
  X(29, "Statement, paragraph 1.", [
   A("LEX", "Kerajaan MADANI", "Branded actor", "The government names itself by its political brand, so the programme is attributed to a branded administration."),
   A("ACT", "mengurus pelarian dan pemohon suaka", "Passivated", "‘Mengurus’ (managing) makes refugees and asylum seekers the objects of administration."),
   A("EVAL", "tersusun, terkawal dan berperikemanusiaan", "Evaluative series", "The series joins ‘terkawal’ (controlled) to ‘berperikemanusiaan’ (humane), so control and care are evaluated together as qualities of one approach."),
  ], gl="The DPP Programme is a new approach of the MADANI Government to managing refugees and asylum seekers in a more orderly, controlled and humane manner"),
  X(30, "Statement, end of paragraph 1.", [
   A("LEG", "selaras dengan Arahan Majlis Keselamatan Negara No. 23", "Authorisation", "The programme is legitimated by a security directive, which places refugee management within national security."),
   A("ASM", "tanpa menjejaskan aspek keselamatan serta kedaulatan negara", "Propositional", "The clause ‘without compromising’ presupposes that refugee management could threaten security and sovereignty."),
  ], gl="in line with National Security Council Directive No. 23 (Revision 2023), without compromising the security and sovereignty of the nation."),
  X(31, "Statement, paragraph 2, after ‘Pelaksanaan program ini’ (the implementation of this programme).", [
   A("ACT", "Kerajaan merekod", "Activated recorder", "The government is the activated recorder, so this text names the agency that holds the data."),
   A("LEX", "migran yang memerlukan perlindungan sementara", "Naming of people", "People are ‘migrants’ who need ‘temporary protection’, although the programme’s own name speaks of refugees (‘pelarian’)."),
   A("REL", "sekali gus", "Consequence", "The connective ‘sekali gus’ (thereby) presents monitoring and enforcement as results of recording."),
   A("NOM", "pemantauan, penguatkuasaan dan perancangan dasar", "Processes as nouns", "Nominalised monitoring and enforcement name state capacities without stating whom they are directed at."),
   A("LEG", "berasaskan data yang sahih", "Rationalisation", "‘Valid data’ legitimates the programme by its utility for policy."),
  ], gl="enables the Government to record the identity and biometric information of migrants who need temporary protection, thereby strengthening the capacity for monitoring, enforcement and policy planning based on valid data."),
  X(70, "Statement, paragraph 3.", [
   A("ACT", "tahanan", "Classified as detainees", "People are counted as ‘tahanan’ (detainees), so detention defines them at the moment of registration."),
   A("LEX", "didatakan", "Word formation, agent suppressed", "The passive verb is formed on the noun ‘data’ and names no agent, so detainees become the objects of a process named after data."),
  ], gl="So far, a total of 4,010 detainees have been entered as data"),
 ]})

DOCS.append({
 "id": "10_OC_2026-01-02_UNHCR_001", "g": "my", "pos": "Runs or backs it", "cls": "OC", "lang": "English",
 "short": "UNHCR Malaysia notice",
 "title": "UNHCR Malaysia, ‘Important update on Dokumen Pendaftaran Pelarian (DPP) Programme’",
 "date": "2 Jan 2026",
 "voice": "UNHCR Malaysia web notice in English, addressed to refugees.",
 "profile": "The agency presents itself as a recipient of information and relays the government’s plan without naming its source. It evaluates legitimacy by place, so registration inside detention becomes the legitimate form, and it refers readers to the ministry for official information.",
 "ex": [
  X(32, "Notice, opening sentence under ‘Registration’.", [
   A("REP", "UNHCR has been informed that", "Unattributed source", "The agentless ‘has been informed’ relays the plan without naming the informant and casts UNHCR as a recipient of information."),
   A("ACT", "the Government’s", "Possessive attribution", "The possessive assigns the programme to the government."),
   A("ACT", "individuals currently held in immigration detention centres", "Passivated", "Individuals are the objects of registering and of being held, and the holding authority is unnamed."),
  ]),
  X(33, "Notice, second sentence.", [
   A("MODD", "Please note", "Demand", "The imperative addresses refugees directly with a demand for attention."),
   A("LEX", "OUTSIDE", "Typographic emphasis", "Capitals stress location, so detention becomes the place of legitimate registration."),
   A("EVAL", "is not legitimate", "Evaluative statement", "The agency evaluates legitimacy by location, which implies that registration inside detention is the legitimate form."),
  ]),
  X(34, "Notice, third sentence, followed by links to the ministry’s Facebook pages.", [
   A("LEX", "official", "Authority marker", "The attribute ‘official’ assigns authority to the ministry’s updates."),
   A("REP", "please refer to the Ministry of Home Affairs social media channels", "Referral", "The notice sends readers to the ministry’s channels, so the government becomes the authoritative source on the programme."),
  ]),
 ]})

DOCS.append({
 "id": "10_OC_2026-07-23_Hansard_001", "g": "my", "pos": "Answers contestation", "cls": "PA", "lang": "Malay",
 "short": "Dewan Negara Hansard",
 "title": "Dewan Negara Hansard, sitting of 23 July 2026",
 "date": "23 Jul 2026",
 "voice": "Deputy Minister of Foreign Affairs, Dato Lukanisman bin Awang Sauni, answering question 6 from Senator Rita Sarimah anak Patrick Insol and the supplementary questions that followed.",
 "profile": "The deputy minister speaks as a government ‘kita’ (we) that instructs UNHCR and lists expulsion among ‘long-term solutions’. His answer presupposes card misuse by Rohingya refugees and limits humane acceptance to the present. It also denies that finding resettlement places is the government’s responsibility.",
 "ex": [
  X(35, "Deputy minister, after ‘melalui keputusan Kabinet’ (through a Cabinet decision).", [
   A("ACT", "kita", "Exclusive we, government", "The government’s ‘kita’ (we) is the activated agent that instructs.", 0),
   A("MODD", "mengarahkan", "Directive", "‘Mengarahkan’ (instructed) makes UNHCR the recipient of a government directive, which reverses the node’s position of the agency as the setter of standards."),
   A("NOM", "sebarang pendaftaran pelarian", "Process as noun", "Registration is nominalised and quantified by ‘sebarang’ (any), so the instruction covers all registration."),
   A("ACT", "yang kita perkenalkan", "Ownership", "The relative clause claims the programme as the government’s own (‘that we introduced’)."),
  ], gl="we have also instructed UNHCR to stop any registration of refugees at this time, as we are in the process of restructuring the DPP programme that we introduced."),
  X(36, "Deputy minister, the third of ‘tiga penyelesaian jangka panjang’ (three long-term solutions), after repatriation and resettlement.", [
   A("LEX", "pemindahan ataupun pengusiran", "Recontextualised category", "Expulsion is listed as a ‘long-term solution’, the place that local integration holds among UNHCR’s durable solutions."),
   A("MODD", "tindakan mandatori", "High obligation", "The borrowed ‘mandatori’ marks expulsion as obligatory action."),
   A("REL", "akibat", "Consequence", "‘Akibat’ (as a result of) attaches expulsion to the person’s act."),
   A("NOM", "pelanggaran undang-undang tempatan", "Act as noun", "The violation is nominalised, and ‘local law’ echoes the Bangladesh FAQ on ‘adherence to local laws’."),
  ], gl="transfer or expulsion as mandatory action resulting from violations of local law."),
  X(37, "Deputy minister, after ‘kad DPP itu adalah sangat-sangat penting’ (the DPP card is very, very important).", [
   A("EVAL", "tidak ingin melihat", "Affective process", "A negated desiderative (‘do not wish to see’) states the government’s stance as a wish."),
   A("ACT", "pelarian-pelarian khususnya Rohingya ini", "Classified, ethnic", "The reduplicated plural and the demonstrative ‘ini’ (these) single out the Rohingya as a group."),
   A("ASM", "menyalahgunakan kad UNHCR", "Propositional", "The clause presupposes misuse of UNHCR cards by refugees, which justifies the government’s own card."),
  ], gl="Since we do not wish to see these refugees, particularly the Rohingya, misusing the existing UNHCR cards."),
  X(71, "Deputy minister, closing an answer to a supplementary question.", [
   A("LEG", "Demi kemanusiaan", "Moral evaluation", "Acceptance is legitimated by humanity, and ‘ketika ini’ (at this time) limits it to the present."),
   A("REL", "tetapi", "Contrastive", "The contrastive ‘tetapi’ (but) sets humanity against the welfare of citizens."),
   A("MODD", "kena", "Obligation", "‘Kena’ (must) expresses an obligation that runs to citizens."),
   A("ACT", "rakyat kita", "In-group", "‘Rakyat kita’ (our people) separates citizens from refugees through the possessive."),
  ], gl="For the sake of humanity we accept Rohingya refugees at this time, but we must think of the welfare of our people"),
  X(72, "Deputy minister, after saying that resettlement is ‘tanggungjawab UNHCR’ (UNHCR’s responsibility).", [
   A("MODD", "Bukan tanggungjawab Kerajaan Malaysia", "Responsibility denied", "The negated noun of responsibility assigns the task of resettlement to UNHCR, named in the previous sentence."),
   A("NOM", "penempatan Rohingya ini", "Process as noun", "Resettlement is nominalised with the Rohingya as its object."),
  ], gl="It is not the responsibility of the Government of Malaysia to find a third country for the resettlement of these Rohingya."),
 ]})

DOCS.append({
 "id": "10_OC_2026-09-30_UNHCR_004", "g": "my", "pos": "Refuses or contests", "cls": "OC", "lang": "English",
 "short": "UNHCR on returns",
 "title": "UNHCR, ‘UNHCR concerned by returns from Malaysia to Myanmar amid ongoing conflict’",
 "date": "30 Sep 2026",
 "voice": "UNHCR press release with direct quotations from Edem Wosornu, Assistant High Commissioner for Protection.",
 "profile": "UNHCR attributes voluntariness to the authorities in reported speech and questions it with low commitment, grounding its doubt in a lack of access. It then restates the standard as a high deontic ‘must’ with no named addressee and places valid assessment outside detention.",
 "ex": [
  X(38, "Edem Wosornu, direct quotation.", [
   A("REL", "While", "Contrastive", "The contrastive ‘while’ sets the authorities’ claim against the fact of detention."),
   A("REP", "authorities say", "Indirect, attributed", "The claim of voluntariness is attributed to unnamed ‘authorities’, which marks it as theirs and lowers the speaker’s commitment to it (Fairclough 2003, p. 171)."),
   A("ACT", "those returned had been held", "Passivated, agent suppressed", "Returnees appear only as objects of return and detention, and the detaining authority is unnamed."),
  ]),
  X(39, "Edem Wosornu, direct quotation.", [
   A("MODE", "raises serious questions", "Questioning", "The speaker questions voluntariness without asserting coercion, a lower commitment than a categorical claim."),
   A("NOM", "decisions to return", "Process as noun", "Return is nominalised as ‘decisions’, which keeps the frame of individual choice."),
   A("LEX", "genuinely free and informed", "Consent vocabulary", "The phrase restates the guidance’s ‘Freely given’ and ‘genuine choice’ and applies them to return."),
  ]),
  X(73, "Edem Wosornu, direct quotation.", [
   A("ACT", "UNHCR", "Activated institution", "The agency is the subject of a negated process, so the text states the limit of its own knowledge."),
   A("MODE", "did not have access", "Grounds for uncertainty", "The negative statement explains the low commitment of the previous sentence."),
  ]),
  X(40, "Press release narrative, after ‘UNHCR urges Malaysia to ensure’.", [
   A("MODD", "must", "High obligation", "High deontic ‘must’ restates voluntariness as an obligation addressed to no named agent."),
   A("ACT", "assessed", "Suppressed agent", "The agentless ‘assessed’ leaves open who assesses."),
   A("LEX", "outside detention settings", "Condition of place", "The phrase places valid assessment outside detention, while UNHCR Malaysia’s notice placed legitimate registration inside it."),
  ]),
 ]})

DOCS.append({
 "id": "10_MC_2026-10-01_MyanmarNow_001", "g": "my", "pos": "Voice of those subject to it", "cls": "MC", "lang": "English",
 "short": "Myanmar Now",
 "title": "Myanmar Now, ‘Myanmar nationals in Malaysia fear arrest and forced return’",
 "date": "1 Oct 2026",
 "voice": "News report with direct speech from James Bawi Thang Bik, chair of the Kuala Lumpur-based Alliance of Chin Refugees.",
 "profile": "The report places ‘voluntarily’ in scare quotes at the end of a chain of agentless passives. The community leader marks the authorities’ statement as a claim and names detention centres as prisons. He rejects the inference from a signature to voluntariness.",
 "ex": [
  X(42, "Journalist’s narrative. The subject is Myanmar nationals ‘lacking legal documentation’.", [
   A("ACT", "being arrested, detained,", "Suppressed agents", "Agentless passives present arrest and detention as things done to people, with no authority named."),
   A("REP", "“voluntarily”", "Scare quotes", "Scare quotes mark ‘voluntarily’ as the authorities’ word and distance the report from it."),
  ]),
  X(74, "James Bawi Thang Bik, direct speech.", [
   A("REP", "They always claim", "Reporting verb", "The verb ‘claim’ marks the authorities’ statement as contestable, and ‘always’ marks it as repeated."),
   A("REL", "but", "Contrastive", "The contrast sets the claim against what cannot be known."),
   A("MODE", "we don’t know", "Stated uncertainty", "The speaker states a limit of knowledge, the same ground UNHCR gives for its doubt."),
   A("LEX", "prisons", "Naming of place", "Detention centres are named ‘prisons’."),
  ]),
  X(41, "James Bawi Thang Bik, direct speech.", [
   A("REL", "Just because", "Reason, rejected", "The speaker rejects the causal inference from signature to voluntariness."),
   A("EVAL", "a piece of paper", "Diminishing evaluation", "The phrase diminishes the document that the authorities treat as proof of consent."),
  ]),
 ]})

# ---------------------------------------------------------------- SOUTH AFRICA
DOCS.append({
 "id": "11_OC_2025-04-01_SRDRegs_001", "g": "za", "pos": "Sets the condition", "cls": "PA", "lang": "English",
 "short": "SRD Regulations, reg. 4(2)",
 "title": "Minister of Social Development, SRD Regulations (GN R2042 of 2022), regulation 4(2)",
 "date": "2022 (version of 1 Apr 2025)",
 "voice": "Regulation made by the Minister of Social Development. Legal text.",
 "profile": "The regulation turns the act of applying into consent, so the applicant is the grammatical subject of consenting while the text supplies the consent. Necessity appears twice without a named judge, and disclosure extends to an open class of institutions.",
 "ex": [
  X(43, "Regulation 4(2), headed ‘Date of application and consent by applicant to information sharing’.", [
   A("REL", "By virtue of application", "Deemed ground", "The nominalised act of applying is the ground from which consent follows, so applying counts as consenting."),
   A("ACT", "an applicant consents", "Activated, deemed", "The applicant is the grammatical subject of consenting, although the regulation produces the consent."),
   A("MODD", "when necessary", "Necessity, judge unnamed", "Necessity is stated without saying who judges it."),
   A("NOM", "collecting, verifying, using and disclosing", "Processes as nouns", "A series of gerunds names the data processes, with the Agency as their implied agent."),
  ]),
  X(44, "Regulation 4(2)(d), the last item in the list of bodies.", [
   A("ACT", "any other government or private institution", "Open class", "The open category extends disclosure beyond the bodies named in the list."),
   A("MODD", "considered necessary", "Necessity, judge unnamed", "The agentless ‘considered’ leaves the judge of necessity unnamed."),
  ]),
 ]})

DOCS.append({
 "id": "11_OC_2025-08-25_SAnews_001", "g": "za", "pos": "Runs or backs it", "cls": "OC", "lang": "English",
 "short": "SAnews on SASSA",
 "title": "SAnews, ‘SASSA to introduce biometric enrolment in September’",
 "date": "25 Aug 2025",
 "voice": "Government news agency report of a SASSA statement.",
 "profile": "The government news service reports compulsion as an announcement and legitimates enrolment by its purpose of making recipients verifiably authentic. Applicants appear as applications and clients, and missing data leads automatically to review through agentless passives.",
 "ex": [
  X(45, "Opening sentence.", [
   A("REP", "has announced that", "Indirect", "The government news service reports SASSA’s announcement in indirect speech and takes no distance from it."),
   A("MODD", "mandatory", "High obligation", "The deontic adjective attaches compulsion to enrolment."),
   A("NOM", "Beneficiary Biometric Enrolment", "Named programme", "Capitalisation turns the process into a named programme in which beneficiaries become a modifier."),
  ]),
  X(75, "Third paragraph. The subject is the agency ‘ramping up efforts to improve its systems’.", [
   A("LEX", "root out", "Verb of removal", "The verb ‘root out’ presents fraud as embedded and in need of removal."),
   A("ASM", "any fraudulent elements", "Existential", "The phrase assumes that fraudulent elements exist, without saying who they are."),
  ]),
  X(46, "Third paragraph, after ‘Moreover,’.", [
   A("EVAL", "a strategic move", "Positive evaluation", "Enrolment is evaluated as strategy."),
   A("LEG", "to ensure", "Rationalisation", "The purpose relation legitimates enrolment by its utility."),
   A("ACT", "every grant recipient", "Generic", "Every recipient becomes the object of verification."),
   A("ASM", "verifiably authentic", "Propositional", "The phrase assumes that a recipient’s authenticity is open to doubt until verified."),
  ]),
  X(47, "Later paragraph, after the list of expected benefits.", [
   A("ACT", "Applications", "Impersonal", "Applicants appear as ‘applications’, an impersonal representation (Fairclough 2003, p. 146)."),
   A("REL", "without biometric data", "Condition", "The prepositional phrase works as a condition, so missing data triggers review."),
   A("ACT", "will be immediately put into the review cycle", "Suppressed agent", "The agentless passive with ‘immediately’ presents the consequence as automatic."),
   A("LEX", "the client", "Naming", "Grant recipients are named ‘clients’, a term from commercial service."),
   A("MODD", "the need to capture biometrics", "Obligation as noun", "The nominalised ‘need’ states the obligation without its source."),
  ]),
 ]})

DOCS.append({
 "id": "11_PA_2026-08-03_OpenSecrets_001", "g": "za", "pos": "Answers contestation", "cls": "CS", "lang": "English",
 "short": "Open Secrets, SASSA official",
 "title": "Open Secrets, ‘Digital Profiteers (Part Two)’, with a SASSA official on consent",
 "date": "3 Aug 2026",
 "voice": "Civil society investigation quoting Brenton van Vrede, SASSA Executive Grants Manager, from a 2025 interview, in answer to a question on informed consent.",
 "profile": "The official places responsibility for informed consent on whether the person reads the terms. Conditionals and negated possibility make consent the only route to assessment, and the agency’s refusal to assess appears as an incapacity (‘we can’t’).",
 "ex": [
  X(76, "Brenton van Vrede, answering whether the forms provide informed consent.", [
   A("REL", "It really depends on whether", "Conditional", "Informed consent is made conditional on the applicant’s reading."),
   A("ACT", "the person reads it", "Activated, responsible", "The person is the activated reader, so responsibility for being informed falls on the applicant."),
  ]),
  X(48, "Brenton van Vrede, after comparing applicants with ‘most of us’ when ‘we want something’.", [
   A("MODD", "There’s no way you can proceed", "Impossibility", "Negated possibility closes every route except acceptance."),
   A("REL", "if you don’t accept", "Conditional", "The conditional makes acceptance the condition of proceeding."),
   A("LEX", "the T&C’s", "Consumer genre", "The consumer form of terms and conditions frames an application for a social grant."),
  ]),
  X(49, "Brenton van Vrede, end of the answer.", [
   A("EVAL", "might not sound fair", "Conceded evaluation", "Low epistemic ‘might’ with ‘sound’ concedes unfairness as an appearance only."),
   A("REL", "but…", "Contrastive", "The contrast sets fairness aside in favour of the condition."),
   A("REL", "if you don’t consent", "Conditional", "The conditional makes consent the condition of assessment."),
   A("MODD", "we can’t assess you", "Negated ability", "The negated ‘can’ presents the agency’s refusal to assess as an incapacity, with ‘we’ as the agency."),
  ]),
 ]})

DOCS.append({
 "id": "11_OC_2025-01-23_Judgment_001", "g": "za", "pos": "Refuses or contests", "cls": "PA", "lang": "English",
 "short": "IEJ v Minister, High Court",
 "title": "High Court, Institute for Economic Justice v Minister of Social Development [2025] ZAGPPHC 29",
 "date": "23 Jan 2025",
 "voice": "Judgment of the High Court, Gauteng Division, Pretoria, delivered by Twala J.",
 "profile": "The court adopts the state’s term ‘safeguards’ and evaluates it against reasonableness and fairness with high deontic commitment. It classifies beneficiaries as poor and vulnerable and attributes an exclusionary purpose to verification, so the purpose relation that legitimates the condition in SASSA’s texts becomes the ground of the court’s finding against it.",
 "ex": [
  X(77, "Paragraph 94.", [
   A("EVAL", "It cannot be right", "Negated evaluation", "A negated evaluation with high commitment judges the regulations as wrong."),
   A("REL", "that are intended to reduce the number of people who are eligible", "Purpose attributed", "The court reads the safeguards by their purpose, which it names as reducing eligibility."),
  ]),
  X(51, "Paragraph 94, closing sentence.", [
   A("LEX", "The safeguards", "Adopted term", "The court takes over the state’s word ‘safeguards’ and makes it the object of evaluation."),
   A("MODD", "must", "High obligation", "High deontic ‘must’ binds the safeguards to legal standards."),
   A("EVAL", "reasonable and fair", "Evaluative standard", "The attributes come from administrative law and set the measure for the rest of the judgment."),
  ]),
  X(50, "Paragraph 95.", [
   A("LEG", "There is no reasonable justification", "Legitimation refused", "The court denies the legitimation that the state offers for the online process."),
   A("ACT", "to subject its potential beneficiaries", "Passivated", "Beneficiaries are the objects of ‘subject’, a verb that marks the process as imposed."),
   A("ACT", "who are mainly poor and vulnerable members of society", "Classified", "The relative clause classifies beneficiaries by poverty and vulnerability, which ties the evaluation to the people affected."),
  ]),
  X(52, "Paragraph 125.", [
   A("REL", "therefore", "Consequence", "The conclusion follows from the preceding reasoning on database checks."),
   A("EVAL", "unreasonable and unfair", "Negative evaluation", "The negative attributes answer the standard ‘reasonable and fair’ of paragraph 94."),
   A("ACT", "is used", "Backgrounded agent", "The agentless ‘is used’ backgrounds the agency, which the context identifies as SASSA."),
   A("REL", "with an ulterior purpose of excluding eligible SRD grant applicants", "Purpose attributed", "The court attributes an exclusionary purpose to verification, the relation that SASSA’s texts use to legitimate it."),
  ]),
 ]})

DOCS.append({
 "id": "11_MC_2024-06-19_GroundUp_002", "g": "za", "pos": "Voice of those subject to it", "cls": "MC", "lang": "English",
 "short": "GroundUp, 2024",
 "title": "GroundUp, ‘SASSA’s new ID verification process sparks alarm’",
 "date": "19 Jun 2024",
 "voice": "News report with direct speech from Lerverch Pieters, an SRD grant recipient, and from Paseka Letsatsi, SASSA spokesperson.",
 "profile": "The agency’s justification appears in reported speech as a purpose of fighting fraud. The recipient’s question challenges the necessity of a repeated check, and the spokesperson answers with a categorical prediction that grants will remain suspended.",
 "ex": [
  X(78, "Article summary at the head of the report.", [
   A("REP", "says", "Indirect", "The agency’s justification is reported indirectly in the article’s summary."),
   A("ACT", "has been introduced", "Suppressed agent", "The agentless passive leaves the introducing authority implicit."),
   A("LEG", "to fight fraud", "Rationalisation", "Fraud prevention legitimates the process by its purpose."),
  ]),
  X(53, "Lerverch Pieters, direct speech. The journalist notes that his grant is paid into his bank account.", [
   A("ACT", "have been done", "Suppressed agent", "The recipient also uses an agentless passive for the checks."),
   A("ACT", "they", "Undifferentiated other", "‘They’ names the agency as an unspecified other."),
   A("MODD", "need", "Necessity questioned", "The question challenges the necessity that the agency claims."),
   A("LEX", "again", "Repetition", "‘Again’ frames the verification as redundant."),
  ]),
  X(54, "Paseka Letsatsi, asked what will happen to recipients who do not complete the verification.", [
   A("ACT", "Their grants", "Possessors", "Recipients appear only as the possessors of grants."),
   A("MODE", "will remain suspended", "Categorical prediction", "A categorical prediction with an agentless participle states the consequence as a continuing state."),
  ]),
 ]})

# ---------------------------------------------------------------- MIZORAM
DOCS.append({
 "id": "12_MC_2023-09-28_ThePrint_001", "g": "mz", "pos": "Refuses or contests", "cls": "MC", "lang": "English",
 "short": "ThePrint, 2023",
 "title": "ThePrint, ‘“Our blood”: Mizoram won’t collect biometric data of Myanmar refugees as ordered by Centre’ (the state government’s refusal, as reported)",
 "date": "28 Sep 2023",
 "voice": "News report by Isaac Zoramsanga on the state government’s decision, with Minister Lalruatkima’s statement to the media.",
 "profile": "The report activates the state, named as ‘Mizoram’, as the agent of refusal and grounds the refusal in a predicted harm. The central instruction appears in the minister’s reported speech, which makes the hierarchy between centre and state explicit.",
 "ex": [
  X(55, "Opening sentence, datelined Aizawl.", [
   A("ACT", "Mizoram has decided not to collect", "Institution as refuser", "The state, named as ‘Mizoram’, is the activated agent of refusal."),
   A("REL", "as it would lead to discrimination", "Reason", "The reason clause grounds the refusal in a predicted harm."),
   A("MODE", "would", "Hypothetical", "The hypothetical ‘would’ frames discrimination as the expected result of collection."),
  ]),
  X(56, "Reported speech after ‘Lalruatkima told the media that’.", [
   A("ACT", "the Union Ministry of Home Affairs", "Activated authority", "The Union ministry is the activated agent of the instruction, so the hierarchy between centre and state is explicit."),
   A("REP", "had instructed", "Indirect, backshifted", "The past perfect marks indirect speech, so the directive reaches the reader through the minister’s report."),
  ]),
 ]})

DOCS.append({
 "id": "12_MC_2025-12-04_TheWire_001", "g": "mz", "pos": "Voice of those subject to it", "cls": "MC", "lang": "English",
 "short": "The Wire, 2025",
 "title": "The Wire (Myanmar Now report), ‘Fear, Mistrust Grow as India Collects Biometrics From Myanmar Refugees’",
 "date": "4 Dec 2025",
 "voice": "Report with direct speech from Siamliana, a pseudonym in the report, a 57-year-old resident, and a quotation from the former chief minister Zoramthanga.",
 "profile": "The report carries the central ‘mandate’ through local leaders to residents. In direct speech the resident’s refusal appears only as the object of fear, while the former chief minister’s kinship vocabulary places refugees inside the political community.",
 "ex": [
  X(79, "Journalist’s narrative.", [
   A("ACT", "village council leaders", "Activated carriers", "Local leaders are the activated carriers of the central instruction."),
   A("MODD", "mandate", "Obligation as noun", "The deontic noun comes from the national government and arrives through local leaders."),
   A("LEX", "residents", "Naming of people", "People are named ‘residents’, a term that places them in the village."),
  ]),
  X(57, "Siamliana (pseudonym), direct speech.", [
   A("MODE", "We do not know", "Stated uncertainty", "The speaker states a lack of knowledge about the purpose of the enrolment."),
   A("REL", "but", "Contrastive", "The contrast sets that uncertainty against fear."),
   A("EVAL", "we are afraid to refuse the mandate", "Affective process", "Refusal appears as the object of fear, so the person’s refusal remains a possibility only."),
  ]),
  X(58, "Former chief minister Zoramthanga, quoted by the report.", [
   A("NOM", "discrimination", "Process as noun", "The nominalisation evaluates the collection as harmful without naming who would discriminate."),
   A("ACT", "of our blood and kindred brothers and sisters", "In-group by kinship", "Kinship vocabulary includes the refugees in the speaker’s own group."),
  ]),
 ]})

MISSING = [
 {"g": "mz", "pos": "Sets the condition", "title": "Ministry of Home Affairs (Delhi), directive on biometrics of Myanmar nationals", "date": "2023", "cls": "PA"},
 {"g": "mz", "pos": "Runs or backs it", "title": "Government of Mizoram, statement on the enrolment", "date": "2025", "cls": "OC"},
 {"g": "mz", "pos": "Answers contestation", "title": "Lok Sabha or Rajya Sabha answer on the enrolment", "date": "2023 to 2026", "cls": "PA"},
]

# ---------------------------------------------------------------- READINGS (provisional)
READINGS = [
 {"id": "r1", "title": "Implementing texts leave out who decides loss", "rq": "RQ1",
  "p": [
   "In the texts that set or run the condition, the processes that decide loss appear as agentless passives or nominalisations. Examples are ‘will be inactivated’, ‘deregistration’, ‘will be immediately put into the review cycle’ and ‘didatakan’. The Diplomat repeats the pattern when it reports that families ‘have been cut off’ from food aid.",
   "People appear as generic or negatively defined classes, in the implementing texts and in reports of them, for example ‘all eligible persons’, ‘every grant recipient’, ‘anyone accessing aid’ and ‘those not biometrically registered’.",
   "Agents appear when a text contests the condition or when a government speaks in its own name. ThePrint makes ‘the Union Ministry of Home Affairs’ the instructing agent, and in the Senate the government’s ‘kita’ (we) instructs UNHCR in the first person.",
  ],
  "ev": [[8, "will be inactivated"], [12, "deregistration"], [61, "have been cut off"], [70, "didatakan"], [47, "will be immediately put into the review cycle"], [7, "all eligible persons"], [46, "every grant recipient"], [28, "anyone accessing aid"], [62, "those not biometrically registered"], [56, "the Union Ministry of Home Affairs"], [35, "mengarahkan"]]},
 {"id": "r2", "title": "From ‘voluntary’ to ‘required’", "rq": "RQ1",
  "p": [
   "The node states that ‘participation in registration is voluntary’ and permits registration without biometrics with ‘may’. The Bangladesh notice keeps the nominalisation and changes its attribute to ‘required’. The same move appears as ‘mandatory’ in the SASSA announcement and as ‘tindakan mandatori’ in the Senate, and the Reuters report gives it as ‘will have to’.",
   "The node itself contains both terms of this shift. Its list places ‘their obligation to cooperate’ next to voluntariness, and in a footnote the guidance assigns ‘the requirement to share personal data’ to government policy wherever a government leads registration.",
  ],
  "ev": [[0, "participation in registration"], [0, "is voluntary"], [2, "may be registered"], [7, "Participation in the exercise"], [7, "is required"], [45, "mandatory"], [36, "tindakan mandatori"], [28, "will have to"], [59, "their obligation to cooperate"], [3, "the requirement to share personal data including biometrics"]]},
 {"id": "r3", "title": "Loss attached to the person’s act", "rq": "RQ1",
  "p": [
   "The node detaches refusal from loss with ‘without adverse consequences’. The implementing texts attach loss to the person’s act through relations of consequence and condition. The examples run from ‘Persons who fail to show up will be inactivated’ in Bangladesh to ‘if you don’t consent, we can’t assess you’ in South Africa.",
   "In these clauses the person’s act is the first link of the chain, while the deciding agency is absent or appears as an incapacity. This is the textual form of the responsibility that RQ1 asks about, because the person who must choose becomes the grammatical cause of the outcome.",
  ],
  "ev": [[5, "without adverse consequences"], [8, "Persons who fail to show up"], [8, "and they will not benefit from any assistance in future"], [12, "as a result"], [47, "without biometric data"], [49, "if you don’t consent"], [49, "we can’t assess you"], [54, "will remain suspended"], [36, "akibat"], [76, "the person reads it"]]},
 {"id": "r4", "title": "Institutions refuse, people fear", "rq": "RQ2",
  "p": [
   "Refusal is the person’s own act in two texts only, the node’s ‘right to refuse’ and the report in The Diplomat of families ‘refusing to participate’. In the contesting texts the refuser is an institution, as in ‘Mizoram has decided not to collect’, UNICEF’s ‘we are very concerned’, UNHCR’s ‘raises serious questions’ and the court’s ‘unreasonable and unfair’.",
   "In the voices of those subject to the condition, refusal appears as fear, in ‘we are afraid to refuse the mandate’. It also appears as a question about necessity, in ‘why do they need to verify your identity again?’. For RQ2, recognition would have to answer refusal by persons, and these texts rarely make such refusal the act of a grammatical subject.",
  ],
  "ev": [[1, "Individuals have the right to refuse"], [61, "refusing to participate in a biometric data collection drive"], [55, "Mizoram has decided not to collect"], [24, "are very concerned"], [39, "raises serious questions"], [52, "unreasonable and unfair"], [27, "I am afraid"], [57, "we are afraid to refuse the mandate"], [53, "need"]]},
 {"id": "r5", "title": "Consent words against verification words", "rq": "RQ1, RQ2",
  "p": [
   "The vocabulary of consent recurs in the contesting texts. UNHCR’s ‘genuinely free and informed’ restates the guidance, and the Chin community leader denies that a signature makes return ‘voluntary’.",
   "The implementing texts speak of verification and fraud, in ‘verification measures’, ‘verifiably authentic’, ‘fraudulent elements’ and ‘menyalahgunakan kad UNHCR’ (misusing UNHCR cards). Where consent appears on the implementing side, the SRD regulation deems it from the act of applying, and the Terms tab gives the distribution of both vocabularies across the 21 documents.",
  ],
  "ev": [[39, "genuinely free and informed"], [5, "Freely given means that"], [41, "Just because"], [20, "verification measures"], [46, "verifiably authentic"], [75, "any fraudulent elements"], [37, "menyalahgunakan kad UNHCR"], [43, "By virtue of application"]]},
 {"id": "r6", "title": "Tensions inside the UN system", "rq": "RQ2",
  "p": [
   "UN texts both contest the condition and adopt its premise. In Gaza, UNICEF objects on 9 May 2025 to plans ‘to screen and monitor beneficiaries’. On 16 May the Emergency Relief Coordinator promises ‘verification measures to ensure that aid does not get stolen by Hamas’.",
   "In Malaysia, UNHCR’s January notice treats registration ‘OUTSIDE of detention facilities’ as illegitimate, while UNHCR’s September release requires that decisions to return be ‘assessed outside detention settings’. In Bangladesh, the guidance’s ‘without adverse consequences’ stands beside the joint FAQ’s ‘discontinuation of protection and assistance’.",
  ],
  "ev": [[25, "beneficiaries"], [20, "verification measures"], [33, "OUTSIDE"], [33, "is not legitimate"], [40, "outside detention settings"], [5, "without adverse consequences"], [12, "the discontinuation of protection and assistance"]]},
 {"id": "r7", "title": "Who counts as ‘our people’", "rq": "RQ2",
  "p": [
   "Speakers in the Malaysian Senate and in Mizoram use collective pronouns to exclude or to include refugees. In the Senate, ‘rakyat kita’ (our people) separates citizens from refugees whose acceptance holds only ‘ketika ini’ (at this time).",
   "In Mizoram, the former chief minister calls the refugees people ‘of our blood and kindred brothers and sisters’ and names collection as discrimination against them. In the Huckabee interview, the reporter’s ‘we’ and ‘those people’ place recipients outside the community that is entitled to know.",
  ],
  "ev": [[71, "rakyat kita"], [71, "Demi kemanusiaan"], [58, "of our blood and kindred brothers and sisters"], [58, "discrimination"], [65, "we"], [65, "those people"]]},
]
