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
