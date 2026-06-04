#!/usr/bin/env bash
# Generic lesson-clip chopper.
# Usage: chop.sh <source-video> <out-dir> <spec-file> <filename-prefix>
# Spec lines: clipname|start1-end1[,start2-end2,...]   (integer seconds)
#   - multiple comma-separated ranges are concatenated into one clip
#   - lines starting with # are ignored
# Every clip is re-encoded (frame-accurate) with YouTube loudnorm applied.
set -euo pipefail

FFMPEG="/c/Users/alexey/bin/ffmpeg.exe"
SRC="$1"; OUT="$2"; SPEC="$3"; PREFIX="$4"
LN="loudnorm=I=-14:TP=-1.5:LRA=11"
VOPTS=(-c:v libx264 -preset faster -crf 23 -pix_fmt yuv420p)
AOPTS=(-c:a aac -b:a 192k)
mkdir -p "$OUT"

while IFS= read -r line || [ -n "$line" ]; do
  line="${line%$'\r'}"
  [ -z "$line" ] && continue
  case "$line" in \#*) continue ;; esac

  name="${line%%|*}"
  segs="${line#*|}"
  IFS=',' read -ra parts <<< "$segs"
  out="$OUT/$PREFIX-$name.mp4"

  if [ "${#parts[@]}" -eq 1 ]; then
    s="${parts[0]%-*}"; e="${parts[0]#*-}"; dur=$(awk "BEGIN{print $e - $s}")
    echo "=== $PREFIX-$name  (${s}s +${dur}s) ==="
    "$FFMPEG" -hide_banner -loglevel error -y -ss "$s" -i "$SRC" -t "$dur" \
      -af "$LN" "${VOPTS[@]}" "${AOPTS[@]}" "$out"
  else
    fc=""; maps=""; i=0
    for p in "${parts[@]}"; do
      s="${p%-*}"; e="${p#*-}"
      fc+="[0:v]trim=start=${s}:end=${e},setpts=PTS-STARTPTS[v${i}];"
      fc+="[0:a]atrim=start=${s}:end=${e},asetpts=PTS-STARTPTS[a${i}];"
      maps+="[v${i}][a${i}]"
      i=$((i + 1))
    done
    fc+="${maps}concat=n=${#parts[@]}:v=1:a=1[v][a];[a]${LN}[ao]"
    echo "=== $PREFIX-$name  (${#parts[@]} segments) ==="
    "$FFMPEG" -hide_banner -loglevel error -y -i "$SRC" -filter_complex "$fc" \
      -map "[v]" -map "[ao]" "${VOPTS[@]}" "${AOPTS[@]}" "$out"
  fi
done < "$SPEC"
echo "DONE: $PREFIX"
