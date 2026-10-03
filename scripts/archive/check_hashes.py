#!/usr/bin/env python3
"""Check that every file of the archive is present and unchanged.

Usage:
    python3 check_hashes.py ARCHIVE_DIR data/corpus/archive_manifest.jsonl

Recomputes the SHA-256 and the size of each file listed in the manifest and
compares them with the recorded values. Prints the files that are missing or
changed, and a summary. Exits with status 1 if any file fails the check.
"""
import hashlib
import json
import sys
from pathlib import Path


def main(archive, manifest):
    root = Path(archive)
    ok, failed = 0, []
    for line in open(manifest, encoding='utf-8'):
        if not line.strip():
            continue
        rec = json.loads(line)
        path = root / rec['folder'] / rec['file']
        if not path.exists():
            failed.append((rec['doc_id'], 'missing'))
            continue
        data = path.read_bytes()
        if len(data) != rec['bytes'] or hashlib.sha256(data).hexdigest() != rec['sha256']:
            failed.append((rec['doc_id'], 'changed'))
            continue
        ok += 1
    for doc_id, why in failed:
        print(why, doc_id)
    print(f'{ok} files unchanged, {len(failed)} missing or changed')
    return 1 if failed else 0


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
