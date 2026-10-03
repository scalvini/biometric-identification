#!/bin/bash
# Download the four PDFs of 3 October 2026 into the archive, as run on the author's Mac.
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
