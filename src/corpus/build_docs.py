"""Build data/corpus/docs.json, the records shown in the corpus part of the page.

Reads data/corpus/records.jsonl (one array per saved file: doc_id, folder, type, page title,
address, retrieval time, element copied, bytes, first 16 characters of the SHA-256, words,
pages) and adds display titles, sources, positions in the core corpus, notes and class
corrections. Run from the repository root: python3 src/corpus/build_docs.py
"""
import json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
rows=[json.loads(l) for l in open(ROOT / 'data' / 'corpus' / 'records.jsonl', encoding='utf-8')]

CASES={'NODE':('node','Node: UNHCR guidance'),'CASE06':('bd','Bangladesh, instance of the node'),
       'CASE09':('gaza','Gaza'),'CASE10':('my','Malaysia'),'CASE11':('za','South Africa'),'CASE12':('mz','Mizoram, India')}
SOURCE={'UNHCR':'UNHCR','Diplomat':'The Diplomat','RefIntl':'Refugees International','IDTechWire':'ID Tech','PassBlue':'PassBlue',
 'NBC':'NBC News','Reuters':'Reuters (Stabroek News copy)','CNN':'CNN','UNHCT':'UN Humanitarian Country Team','GHF':'Gaza Humanitarian Foundation',
 'UNGeneva':'UN Geneva','UNNews':'UN News','UNifeed':'UNifeed','OCHA':'OCHA','IsraelUN':'Permanent Mission of Israel to the UN',
 'UNSpokesperson':'Spokesperson for the UN Secretary-General','USEmbassy':'US Embassy Jerusalem','Skyline':'Skyline International',
 'MalayMail':'Malay Mail','Bernama':'Bernama','FMT':'Free Malaysia Today','DVB':'DVB (Wayback copy)','SuaraKeadilan':'Suara Keadilan',
 'MerdekaTimes':'The Merdeka Times','DailyMaverick':'Daily Maverick','AP':'AP (Click2Houston copy)','TheStar':'The Star',
 'MyanmarNow':'Myanmar Now','AlJazeera':'Al Jazeera','MOHA':'Ministry of Home Affairs, Malaysia','Hansard':'Parliament of Malaysia, Dewan Negara',
 'HRW':'Human Rights Watch','FortifyRights':'Fortify Rights','Amnesty':'Amnesty International Malaysia','MERHROM':'MERHROM (in The Sun)',
 'GroundUp':'GroundUp','Bizcommunity':'Bizcommunity','Context':'Context (Thomson Reuters Foundation)','CapeArgus':'Cape Argus','IOL':'IOL',
 'DailyVoice':'Daily Voice','Judgment':'High Court, Gauteng Division (SAFLII)','SRDRegs':'Minister of Social Development (GN R2042)',
 'PMG':'Parliamentary Monitoring Group','SAnews':'SAnews','SASSA':'SASSA (gov.za)','BlackSash':'Black Sash','UBICoalition':'UBI Coalition (in GroundUp)',
 'IEJ':'Institute for Economic Justice','OpenSecrets':'Open Secrets','ThePrint':'ThePrint','Scroll':'Scroll','DeccanHerald':'Deccan Herald',
 'MorungExpress':'Morung Express','Organiser':'Organiser','TheWire':'The Wire','NewsMill':'NewsMill','ShillongTimes':'The Shillong Times'}
# Daily Maverick copy of Reuters for the Malaysia item
SOURCE_OVR={'10_MC_2026-09-01_DailyMaverick_001':'Reuters (Daily Maverick copy)'}

PDF={'09_OC_2025-05-08_GHF_002':('Gaza Humanitarian Foundation (GHF): Safe, Transparent Aid for Gaza (overview memo)','https://static-cdn.toi-media.com/www/uploads/2025/05/Gaza-Humanitarian-Foundation-Memo.pdf'),
 '09_OC_2025-05-19_IsraelUN_001':('Letter dated 19 May 2025 from the Permanent Representative of Israel to the United Nations addressed to the President of the Security Council (S/2025/313)','https://digitallibrary.un.org/record/4082957/files/S_2025_313-EN.pdf'),
 '10_OC_2026-05-18_MOHA_001':('Kenyataan media: lawatan kerja Menteri Dalam Negeri ke Pusat Pengasingan Khas Pelarian dan Pemohon Suaka Bidor, Perak','https://www.moha.gov.my/utama/images/Kenyataan%20Media/MEI_2026/18_MEI_2026_KENYATAAN_MEDIA_LAWATAN_KERJA_YB_MENTERI_DALAM_NEGERI_KE_PUSAT_PENGASINGAN_KHAS_PELARIAN_DAN_PEMOHON_SUAKA_BIDOR_PERAK.pdf'),
 '11_PA_2023-09-xx_BlackSash_002':('The Protection of Personal Information of Social Grant Beneficiaries (Bowmans and Black Sash)','https://blacksash.org.za/wp-content/uploads/2023/09/Bowmans_BlackSash_POPI.pdf'),
 '11_PA_2025-02-xx_IEJ_001':('Systemic exclusion from a South African social assistance transfer: Drivers, impacts, and who is most at risk (AFD Research Papers No. 340)','https://iej.org.za/wp-content/uploads/2025/03/South-Africa-SRD-exclusions_WEB.pdf')}

TITLE_OVR={
 '00_OC_2026-10-03_UNHCR_001':'Guidance on Registration and Identity Management, section 5.2: Registration as an Identity Management Process',
 '09_OC_2025-05-09_UNGeneva_001':'UN Geneva press briefing, 9 May 2025 (teleprompter transcript)',
 '09_OC_2025-05-09_UNGeneva_002':'UN Geneva press briefing, 9 May 2025 (summary)',
 '09_OC_2025-05-09_UNifeed_001':'Geneva / Gaza aid update (UNifeed soundbites)',
 '09_OC_2025-05-19_UNSpokesperson_001':'Daily press briefing by the Office of the Spokesperson for the Secretary-General, 19 May 2025',
 '09_OC_2025-05-04_UNHCT_002':'Statement by the Humanitarian Country Team on principled aid delivery in Gaza',
 '09_OC_2025-05-28_UNHCT_001':'Statement by the Humanitarian Country Team on Gaza',
 '09_OC_2025-05-28_OCHA_001':'Briefing to journalists by Jonathan Whittall, Head of OCHA oPt',
 '10_OC_2026-07-23_Hansard_001':'Dewan Negara Hansard, sitting of 23 July 2026',
 '10_OC_2026-10-03_UNHCR_002':'UNHCR Malaysia home page, with "Looking Ahead: Towards a Comprehensive Asylum System"',
 '10_OC_2026-01-02_UNHCR_001':'Important update on Dokumen Pendaftaran Pelarian (DPP) Programme',
 '10_OC_2026-07-09_UNHCR_003':'Privacy Notice, UNHCR Malaysia help site',
 '11_PA_2026-08-03_OpenSecrets_001':'Digital Profiteers (Part Two): The banks and the costs of verifying social grant recipients',
 '11_OC_2025-04-01_SRDRegs_001':'Regulations Relating to COVID-19 Social Relief of Distress, 2022 (GN R2042), version of 1 April 2025',
 '11_OC_2025-01-23_Judgment_001':'Institute for Economic Justice and Another v Minister of Social Development and Others [2025] ZAGPPHC 29',
 '11_OC_2025-07-01_PMG_001':'Question NW3803 to the Minister of Social Development, with reply',
 '11_OC_2025-09-17_PMG_002':'Portfolio Committee: DSD Q1 2025/26 Performance; SASSA Biometric Verification Process',
 '10_MC_2025-11-25_Bernama_001':'Kerajaan Laksana Sistem DPP Urus Pelarian Mulai 1 Jan 2026',
 '10_MC_2026-06-20_Bernama_002':'Refugees Must Respect Malaysian Laws In Exchange For Protection, Says UNHCR',
 '10_PA_2026-07-23_Amnesty_001':'Refugee protection cannot be paused during transition to DPP system',
 '11_MC_2026-05-25_DailyVoice_001':"SASSA's face palm: facial recognition tech linked to the suspension of 68 000 grants",
}
SUFFIXES=[' – The Diplomat',' - UNHCR Bangladesh',' - Refugees International',' - ID Tech',' - PassBlue',' - Stabroek News',' | CNN',
 ' - Question of Palestine',' - U.S. Embassy Jerusalem',' | Malay Mail',' | FMT',' - DVB',' - The Merdeka Times',' | The Star',' | Refugees | Al Jazeera',
 ' | UNHCR',' | UN News',' | Human Rights Watch',' - Fortify Rights',' | GroundUp',' | Context by TRF',' | SAnews',' | South African Government',
 ' - Black Sash',' | MorungExpress | morungexpress.com',' - The Wire',' | The Shillong Times',' - Amnesty Malaysia',' | PMG']
def clean(t):
    t=t.replace(' ',' ').strip()
    changed=True
    while changed:
        changed=False
        for s in SUFFIXES:
            if t.endswith(s): t=t[:-len(s)].rstrip(); changed=True
    if t.startswith('Skyline International :: '): t=t[len('Skyline International :: '):]
    if t.startswith('BERNAMA - '): t=t[len('BERNAMA - '):]
    return t

# proposed core: (case key, position, note)
CORE={
 '00_OC_2026-10-03_UNHCR_001':('node','standard','UNHCR\'s global standard. Participation in registration is voluntary; individuals may refuse biometrics on legitimate grounds and be registered by alternative methods. Footnote 5 leaves the right to object to government policy where the host government leads registration.'),
 '06_OC_2023-05-02_UNHCR_005':('node','articulation','The Bangladesh notice of the registration update, which presents establishing and preserving identities as key to protection.'),
 '06_OC_2026-01-20_UNHCR_006':('node','articulation','Joint Government and UNHCR questions and answers on data processing, which state that refusing processing may lead to deregistration.'),
 '06_MC_2025-06-01_Diplomat_002':('node','response','Reports UNHCR\'s defence of biometric enrolment after registered families refused it in 2025: the one documented reply of an agency to refusal by the people themselves.'),
 '09_OC_2025-05-08_GHF_002':('gaza','sets','GHF\'s overview memo: aid "without regard to identity", with no eligibility requirements.'),
 '09_OC_2025-05-19_IsraelUN_001':('gaza','runs','Israel\'s letter to the Security Council ("strict oversight"), with Fletcher\'s letter annexed, which claims the UN\'s own "verification measures".'),
 '09_OC_2025-08-08_USEmbassy_001':('gaza','answers','The US Ambassador answers criticism of screening at the distribution sites (CBS interview transcript).'),
 '09_OC_2025-05-09_UNGeneva_001':('gaza','contests','UNICEF objects to facial recognition as a precondition of aid, used to screen beneficiaries "for intelligence and military purposes".'),
 '09_MC_2025-05-28_Reuters_001':('gaza','voice','Palestinians at the first GHF centre describe hunger and fear in their own words.'),
 '10_OC_2026-05-18_MOHA_001':('my','sets','Home Ministry statement: the DPP records identity and biometrics under National Security Council Directive No. 23, to strengthen monitoring and enforcement.'),
 '10_OC_2026-01-02_UNHCR_001':('my','runs','UNHCR notice: the first phase covers people in immigration detention; readers are sent to the Ministry\'s channels "For official updates".'),
 '10_OC_2026-07-23_Hansard_001':('my','answers','The Deputy Minister tells the Senate that UNHCR has been directed to stop registering refugees while the DPP is restructured.'),
 '10_OC_2026-09-30_UNHCR_004':('my','contests','UNHCR asks whether decisions to return to Myanmar were "genuinely free and informed".'),
 '10_MC_2026-10-01_MyanmarNow_001':('my','voice','Myanmar nationals describe fear of arrest and doubt that signed returns are voluntary.'),
 '11_OC_2025-04-01_SRDRegs_001':('za','sets','Regulation 4(2): applying for the grant counts as consent to the processing of the applicant\'s information.'),
 '11_OC_2025-08-25_SAnews_001':('za','runs','SASSA announces compulsory biometric enrolment from September 2025; applications without biometric data go into review.'),
 '11_PA_2026-08-03_OpenSecrets_001':('za','answers','A SASSA official on consent: "if you don\'t consent, we can\'t assess you".'),
 '11_OC_2025-01-23_Judgment_001':('za','contests','The High Court finds the database verification unreasonable and used "with an ulterior purpose of excluding eligible SRD grant applicants".'),
 '11_MC_2024-06-19_GroundUp_002':('za','voice','A beneficiary asks why identity must be verified again after bank checks.'),
 '12_MC_2023-09-28_ThePrint_001':('mz','contests','The Mizoram government refuses the Centre\'s order to collect biometrics of Myanmar refugees, calling them "our blood" (as reported).'),
 '12_MC_2025-12-04_TheWire_001':('mz','voice','Refugees at Zokhawthar say they are "afraid to refuse the mandate".'),
}
NOTES={
 '09_OC_2025-05-09_UNGeneva_002':'UN Geneva\'s summary of the same briefing. It keeps UNICEF\'s concern and drops the intelligence and military purposes.',
 '09_OC_2025-05-09_UNNews_001':'UN News keeps UNICEF\'s wording on screening and monitoring "for intelligence and military purposes".',
 '09_OC_2025-05-28_UNHCT_001':'The humanitarian agencies state that they will not take part in any scheme that undermines humanitarian principles.',
 '09_OC_2025-05-04_UNHCT_002':'The humanitarian agencies reject delivery through Israeli hubs under "conditions set by the Israeli military".',
 '09_OC_2025-05-28_OCHA_001':'OCHA calls the scheme "surveillance-based rationing".',
 '10_OC_2026-10-03_UNHCR_002':'UNHCR welcomes the DPP as a "nationally owned approach" and says it remains committed to supporting its implementation.',
 '10_OC_2026-07-09_UNHCR_003':'UNHCR Malaysia privacy notice, "last updated on 9 July 2026"; its list of recipients of personal data is to be checked against the DPP.',
 '10_MC_2026-06-20_Bernama_002':'UNHCR\'s Representative is reported welcoming the DPP as strengthening national security through verified identity and biometrics.',
 '11_OC_2025-07-01_PMG_001':'The Minister\'s written reply: biometric verification "is compulsory for all new SRD applications".',
 '11_OC_2025-09-17_PMG_002':'Committee report: facial biometrics introduced for people with unreadable fingerprints or missing fingers.',
 '11_OC_2026-01-27_SASSA_001':'SASSA Mpumalanga offers office help to grant recipients without a smartphone or data.',
 '11_PA_2024-07-30_UBICoalition_001':'The UBI Coalition objects that applicants must consent to sharing information with "any government or private institution".',
 '12_MC_2026-03-02_ShillongTimes_001':'Official framing of the enrolment as documentation and coordination alongside humanitarian assistance (as reported).',
}
CHECKED=set(['00_OC_2026-10-03_UNHCR_001','09_OC_2025-05-09_UNGeneva_001','09_OC_2025-05-09_UNGeneva_002','09_OC_2025-05-09_UNNews_001',
 '09_OC_2025-05-08_GHF_002','09_OC_2025-05-19_IsraelUN_001','09_OC_2025-05-28_OCHA_001','09_OC_2025-05-28_UNHCT_001','09_OC_2025-05-04_UNHCT_002',
 '10_OC_2026-10-03_UNHCR_002','10_MC_2026-06-20_Bernama_002','10_OC_2026-07-23_Hansard_001','10_MC_2026-10-01_MyanmarNow_001','10_MC_2026-09-30_TheStar_001',
 '10_OC_2026-01-02_UNHCR_001','10_OC_2026-09-30_UNHCR_004','10_OC_2026-07-09_UNHCR_003','11_OC_2025-04-01_SRDRegs_001','11_PA_2026-08-03_OpenSecrets_001',
 '11_OC_2025-07-01_PMG_001','11_OC_2025-09-17_PMG_002','11_OC_2025-01-23_Judgment_001','11_PA_2024-07-30_UBICoalition_001','12_MC_2025-12-04_TheWire_001'])
READ_FULL=set(['06_MC_2025-06-01_Diplomat_002','06_MC_2025-06-07_Diplomat_001','06_OC_2023-05-02_UNHCR_005','06_OC_2026-01-20_UNHCR_006','06_PA_2025-05-22_RefIntl_001','10_OC_2026-01-02_UNHCR_001'])
TO_CS=set(['09_PA_2025-05-15_Skyline_001','09_PA_2025-09-10_Skyline_002','10_PA_2026-05-04_HRW_001','10_PA_2026-06-01_FortifyRights_001','10_PA_2026-07-23_Amnesty_001',
 '10_PA_2026-07-30_MERHROM_001','11_PA_2023-09-xx_BlackSash_002','11_PA_2024-06-24_BlackSash_001','11_PA_2024-07-30_UBICoalition_001','11_PA_2025-02-xx_IEJ_001','11_PA_2026-08-03_OpenSecrets_001'])
TO_PA=set(['00_OC_2026-10-03_UNHCR_001','10_OC_2026-07-23_Hansard_001','11_OC_2025-01-23_Judgment_001','11_OC_2025-04-01_SRDRegs_001','11_OC_2025-07-01_PMG_001','11_OC_2025-09-17_PMG_002'])
BORDER={'10_OC_2026-07-09_UNHCR_003':'PA','09_OC_2025-05-19_IsraelUN_001':'PA'}
APPROX={'00_OC_2026-10-03_UNHCR_001':'Undated living guidance; the date is the retrieval date.',
 '10_OC_2026-10-03_UNHCR_002':'Undated page; the date is the retrieval date.',
 '11_PA_2023-09-xx_BlackSash_002':'Undated booklet; the upload folder is September 2023.',
 '11_PA_2025-02-xx_IEJ_001':'February 2025 on the cover; 14 March 2025 on the IEJ page (to check).',
 '09_OC_2025-05-08_GHF_002':'Undated memo; the earliest known copy was uploaded on 8 May 2025.',
 '11_OC_2025-04-01_SRDRegs_001':'Regulations of 2022; the date is that of the consolidated version.'}
out=[]
for r in rows:
    did,folder,typ,title,url,retr,copy,b,sha,words,pages=r
    m=re.match(r'^(\d\d)_([A-Z]{2})_(\d{4}-\d\d-(?:\d\d|xx))_([A-Za-z]+)_(\d{3})$',did)
    case,cls,date,src,seq=m.groups()
    ck,cname=CASES[folder]
    if did in PDF: title,url=PDF[did]
    disp=TITLE_OVR.get(did) or clean(title)
    if retr.startswith('2026-10-01'): batch='b1'
    elif retr.startswith('2026-10-02'): batch='b2'
    elif did in ('10_MC_2025-12-13_DVB_001','10_OC_2026-05-18_MOHA_001') or retr.startswith('2026-10-03T11'): batch='b3'
    else: batch='b4'
    d=dict(id=did,folder=folder,ck=ck,case=cname,cls=cls,date=date,src=SOURCE_OVR.get(did,SOURCE.get(src,src)),title=disp,raw=title.replace(' ',' '),
           url=url,retr=retr if not did.startswith('10_MC_2025-12-13_DVB') else '2026-10-03 (Wayback capture of 2026-07-03)',copy=copy,bytes=b,sha=sha,words=words,pages=pages,
           batch=batch,read=did in READ_FULL,checked=did in CHECKED)
    if did in CORE: d['core']=CORE[did][1]; d['note']=CORE[did][2]
    elif did in NOTES: d['note']=NOTES[did]
    if did in TO_CS: d['conv']='CS'
    if did in TO_PA: d['conv']='PA'
    if did in BORDER: d['convb']=BORDER[did]
    if did in APPROX: d['approx']=APPROX[did]
    if did=='06_PA_2025-05-22_RefIntl_001': d['convnote']='Class set by the April 2026 collection; under its own definitions a Refugees International report would be CS.'
    out.append(d)
json.dump(out,open(ROOT / 'data' / 'corpus' / 'docs.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(out),'docs;', sum(1 for d in out if 'core' in d),'core;', sum(1 for d in out if 'conv' in d),'class deviations')
from collections import Counter
print(Counter(d['batch'] for d in out)); print(Counter(d['ck'] for d in out)); print(Counter(d['cls'] for d in out))
for d in out[:3]+out[40:42]: print(d['id'],'|',d['title'],'|',d['src'])
