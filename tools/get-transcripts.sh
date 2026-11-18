#!/usr/bin/env bash
# Run on your own computer from the Isidore repo folder:  bash tools/get-transcripts.sh
# Needs yt-dlp:  pip install yt-dlp   (or: brew install yt-dlp)
# Saves English captions to source/youtube/, one file per video, pausing between videos.
set -u
cd "$(dirname "$0")/.."
mkdir -p source/youtube
grep -oE 'https://[^ ]+' tools/priority-videos.txt | while read -r url; do
  id="${url##*=}"
  if ls source/youtube/*"[$id]"* >/dev/null 2>&1; then echo "have $id"; continue; fi
  echo "getting $id"
  yt-dlp --skip-download --write-auto-subs --write-subs --sub-langs en --sub-format vtt \
    -o "source/youtube/%(upload_date)s %(title)s [%(id)s].%(ext)s" "$url" || echo "failed $id"
  sleep 30
done
echo "Done. Now: git add source/youtube && git commit -m 'Add Dodgy transcripts' && git push"
