#!/usr/bin/env python3
"""Check that every excerpt appears word for word in its saved copy.

Usage:
    python3 verify_excerpts.py ARCHIVE_DIR data/analysis/excerpts.jsonl

Each line of the excerpts file is a JSON array [index, relative_path, excerpt].
The text of a saved web copy starts after the header line '---'. PDFs are read
with pypdf. Both sides are normalised with Unicode NFKC, and runs of whitespace
are collapsed to one space. If an excerpt is still not found, the check is
repeated with all spaces removed, because PDF text extraction can insert spaces
inside words. The script prints one line for each excerpt (exact, despaced or
missing) and a summary, and exits with status 1 if any excerpt is missing.
Needs pypdf (pip install pypdf).
"""
import json
import re
import sys
import unicodedata
from pathlib import Path


def body(path):
    if path.suffix == '.pdf':
        from pypdf import PdfReader
        return '\n'.join((p.extract_text() or '') for p in PdfReader(str(path)).pages)
    text = path.read_text(encoding='utf-8')
    return text.split('\n---\n', 1)[1] if '\n---\n' in text else text


def norm(s):
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', s))


def find(text, quote):
    if quote in text:
        return 'exact'
    if quote.replace(' ', '') in text.replace(' ', ''):
        return 'despaced'
    return 'missing'


def main(archive, excerpts):
    root = Path(archive)
    cache = {}
    counts = {'exact': 0, 'despaced': 0, 'missing': 0}
    for line in open(excerpts, encoding='utf-8'):
        if not line.strip():
            continue
        index, rel, quote = json.loads(line)
        if rel not in cache:
            cache[rel] = norm(body(root / rel))
        how = find(cache[rel], norm(quote))
        counts[how] += 1
        print(f'{how:9} {index:3} {rel} | {quote[:60]}')
    print('summary', counts)
    return 1 if counts['missing'] else 0


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
