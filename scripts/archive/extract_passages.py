import re, sys
from pypdf import PdfReader
A='/Users/home/Documents/02. Papers/-Data Colonialism/-corpus/BDS_Corpus_Archive/'
def body(path):
    if path.endswith('.pdf'):
        return '\n'.join((p.extract_text() or '') for p in PdfReader(A+path).pages)
    t=open(A+path,encoding='utf-8').read()
    return t.split('\n---\n',1)[1] if '\n---\n' in t else t
def around(t,pat,w=500,maxn=3):
    out=[]; last=-10**9
    for m in re.finditer(pat,t,flags=re.I):
        if m.start()-last < w: continue
        last=m.start()
        out.append(t[max(0,m.start()-w):m.end()+w].replace('\n',' ¶ '))
        if len(out)>=maxn: break
    return out
def paras(t,pat,maxn=8,maxlen=700):
    ps=[p.strip() for p in re.split(r'\n\s*\n|\n',t) if p.strip()]
    return [p[:maxlen] for p in ps if re.search(pat,p,flags=re.I)][:maxn]
JOBS={
'A':[
 ('NODE/00_OC_2026-10-03_UNHCR_001.txt','around',r'participation in registration is voluntary|right to refuse the collection|In such cases, individuals may be registered|Where the host government leads|legitimate interest in knowing|Freely given means|obligation to cooperate|prerequisite to recognition',260,8),
 ('CASE06/06_OC_2023-05-02_UNHCR_005.txt','paras',r'identit|biometric|registr|protect|assist|data|share|Government|card|refus|update',10,600),
 ('CASE06/06_OC_2026-01-20_UNHCR_006.txt','paras',r'refus|deregist|consent|biometric|pre-requisite|prerequisite|protection|share|Government|object',12,600),
 ('CASE06/06_MC_2025-06-01_Diplomat_002.txt','paras',r'UNHCR|refus|biometric|assistance|letter|families|food|ration',12,600),
],
'B':[
 ('CASE09/09_OC_2025-05-08_GHF_002.pdf','around',r'identity|eligib|vett|screen|recipient|IDF|verif|biometric|facial|data',300,8),
 ('CASE09/09_OC_2025-05-19_IsraelUN_001.pdf','paras',r'.',40,900),
 ('CASE09/09_OC_2025-08-08_USEmbassy_001.txt','around',r'screen|guarantee|Hamas members',350,4),
 ('CASE09/09_OC_2025-05-09_UNGeneva_001.txt','around',r'facial recognition',900,1),
 ('CASE09/09_MC_2025-05-28_Reuters_001.txt','paras',r'.',30,700),
],
'C':[
 ('CASE10/10_OC_2026-05-18_MOHA_001.pdf','paras',r'.',40,900),
 ('CASE10/10_OC_2026-07-23_Hansard_001.txt','around',r'menghentikan sebarang pendaftaran',1600,1),
 ('CASE10/10_OC_2026-09-30_UNHCR_004.txt','paras',r'.',30,700),
 ('CASE10/10_MC_2026-10-01_MyanmarNow_001.txt','paras',r'.',30,700),
],
'D':[
 ('CASE11/11_OC_2025-04-01_SRDRegs_001.txt','around',r'By virtue of application|biometric|identity verification',700,3),
 ('CASE11/11_OC_2025-08-25_SAnews_001.txt','paras',r'.',30,700),
 ('CASE11/11_PA_2026-08-03_OpenSecrets_001.txt','around',r'consent',450,4),
 ('CASE11/11_OC_2025-01-23_Judgment_001.txt','around',r'ulterior purpose|reasonable justification to subject|biometric',450,4),
 ('CASE11/11_MC_2024-06-19_GroundUp_002.txt','paras',r'Pieters|biometric|fraud|verif|Letsatsi|suspend',12,600),
 ('CASE12/12_MC_2023-09-28_ThePrint_001.txt','paras',r'biometric|blood|Centre|refugee|minister|said|MHA',12,600),
 ('CASE12/12_MC_2025-12-04_TheWire_001.txt','paras',r'afraid|mandate|refugee ID|assurance|consent|refus|data|biometric',12,600),
]}
for path,mode,pat,a,b in JOBS[sys.argv[1]]:
    t=body(path)
    print('\n########', path.split('/')[-1], '|', len(t.split()), 'words')
    items=around(t,pat,a,b) if mode=='around' else paras(t,pat,a,b)
    for i,x in enumerate(items,1): print(f'[{i}]', x)
