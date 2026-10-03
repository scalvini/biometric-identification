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
