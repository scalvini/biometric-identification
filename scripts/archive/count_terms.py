#!/usr/bin/env python3
"""Count twelve word families in each core document and print the counts as JSON.

Usage:
    python3 count_terms.py ARCHIVE_DIR data/analysis/excerpts.jsonl > data/analysis/terms.json

The documents are those named in the excerpts file, in order of first mention.
Counts run over the saved text below the header line '---' (PDFs through pypdf),
after Unicode NFKC normalisation, ignoring case and respecting word boundaries.
The two Malay documents add Malay equivalents to each pattern. The Hansard is
counted on the passage of question 6 and its supplementary questions only.
Needs pypdf (pip install pypdf).
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

EN = [('voluntary', r'voluntar(?:y|ily)'), ('consent', r'consent(?:s|ed|ing)?'),
      ('refuse', r'refus(?:e|es|ed|ing|al|als)'),
      ('verify', r'verif(?:y|ies|ied|ying|ication|ications|iable|iably)'),
      ('identity', r'identit(?:y|ies)'), ('biometric', r'biometrics?'), ('security', r'security'),
      ('fraud', r'fraud\w*|misus\w*'), ('legitimate', r'legitima(?:te|tely|cy)'),
      ('necessary', r'necess(?:ary|arily|ity|ities)'),
      ('required', r'requir(?:e|es|ed|ing|ement|ements)|mandatory|compulsory|obligatory'),
      ('protection', r'protect\w*')]
MS = {'voluntary': r'sukarela', 'consent': r'persetujuan', 'refuse': r'enggan|menolak|penolakan|ditolak',
      'verify': r'pengesahan|mengesahkan|disahkan|verifikasi', 'identity': r'identiti',
      'biometric': r'biometrik', 'security': r'keselamatan',
      'fraud': r'penipuan|menipu|palsu|penyalahgunaan|menyalahgunakan', 'legitimate': r'sah|sahih',
      'necessary': r'perlu|keperluan|memerlukan', 'required': r'wajib|diwajibkan|mandatori',
      'protection': r'perlindungan|melindungi|dilindungi'}
MALAY = {'10_OC_2026-05-18_MOHA_001', '10_OC_2026-07-23_Hansard_001'}


def body(path):
    if path.suffix == '.pdf':
        from pypdf import PdfReader
        return '\n'.join((p.extract_text() or '') for p in PdfReader(str(path)).pages)
    text = path.read_text(encoding='utf-8')
    return text.split('\n---\n', 1)[1] if '\n---\n' in text else text


def norm(s):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', s))


def main(archive, excerpts):
    root = Path(archive)
    paths = []
    for line in open(excerpts, encoding='utf-8'):
        if line.strip():
            rel = json.loads(line)[1]
            if rel not in paths:
                paths.append(rel)
    out = {}
    for rel in paths:
        doc = Path(rel).stem
        raw = body(root / rel)
        seg = None
        if doc == '10_OC_2026-07-23_Hansard_001':
            start = raw.find('Dipersilakan Yang Berhormat Senator Puan Rita Sarimah')
            end = start + re.search(r'\n\s*7\. ', raw[start:]).start()
            raw, seg = raw[start:end], 'q6'
        text = norm(raw)
        counts = []
        for key, pattern in EN:
            p = pattern if doc not in MALAY else '(?:' + pattern + '|' + MS[key] + ')'
            counts.append(len(re.findall(r'\b(?:' + p + r')\b', text, flags=re.I)))
        out[doc] = {'words': len(text.split()), 'counts': counts, 'malay': doc in MALAY, 'seg': seg}
    print(json.dumps({'terms': [k for k, _ in EN], 'docs': out}, ensure_ascii=True))


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
