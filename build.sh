#!/usr/bin/env bash
# Rebuild the data and the page from the sources. Needs Python 3.9 or later and no other packages.
set -euo pipefail
cd "$(dirname "$0")"
python3 src/corpus/build_docs.py
python3 src/analysis/build.py
python3 src/assemble.py
