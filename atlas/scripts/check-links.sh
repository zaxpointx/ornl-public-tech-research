#!/bin/sh
set -eu
for f in README.md projects/*.md; do
  grep -oE 'https?://[^)]+' "$f" | while read -r url; do
    code=$(curl -L -s -o /dev/null -w '%{http_code}' --max-time 20 "$url" || true)
    case "$code" in 2*|3*) echo "PASS $code $url";; *) echo "WARN $code $url";; esac
  done
done
