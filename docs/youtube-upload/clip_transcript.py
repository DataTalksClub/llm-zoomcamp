#!/usr/bin/env python3
"""Slice a module's ORIGINAL transcript into per-clip, clip-relative transcripts
using the chop spec — so chapter timecodes can be prepared in advance, without
waiting for YouTube to generate captions after upload.

It correctly handles multi-segment clips (where bits were cut from the middle):
each kept segment is offset by the cumulative duration of the segments before it,
so timestamps line up with the concatenated clip.

  uv run python clip_transcript.py \
    --transcript ../transcripts/module1-agents.txt \
    --spec ../module1-agents.spec \
    --out-dir captions

Then generate chapters from captions/<clip>.txt exactly as you would from a
YouTube-fetched caption file.
"""
import argparse
import re
from pathlib import Path


def parse_ts(ts: str) -> int:
    p = [int(x) for x in ts.split(":")]
    return p[0] * 60 + p[1] if len(p) == 2 else p[0] * 3600 + p[1] * 60 + p[2]


def fmt(s: int) -> str:
    h, r = divmod(s, 3600)
    m, sec = divmod(r, 60)
    return f"{h}:{m:02d}:{sec:02d}" if h else f"{m}:{sec:02d}"


def load_cues(path: Path):
    cues = []
    for line in path.read_text(encoding="utf-8").splitlines():
        mt = re.match(r"^(\d+(?::\d+)+)\s(.*)$", line)
        if mt:
            cues.append((parse_ts(mt.group(1)), mt.group(2)))
    return cues


def clip_lines(cues, segments):
    """segments: [(start,end),...] in original seconds -> [(clip_sec, text)]."""
    out, base = [], 0
    for s, e in segments:
        for t, txt in cues:
            if s <= t < e:
                out.append((base + (t - s), txt))
        base += e - s
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--transcript", type=Path, required=True)
    ap.add_argument("--spec", type=Path, required=True)
    ap.add_argument("--out-dir", type=Path, default=Path("captions"))
    args = ap.parse_args()

    cues = load_cues(args.transcript)
    args.out_dir.mkdir(parents=True, exist_ok=True)
    for line in args.spec.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, segs = line.split("|")
        segments = [tuple(int(x) for x in p.split("-")) for p in segs.split(",")]
        lines = clip_lines(cues, segments)
        (args.out_dir / f"{name}.txt").write_text(
            "\n".join(f"{fmt(t)} {txt}" for t, txt in lines) + "\n", encoding="utf-8"
        )
        end = fmt(lines[-1][0]) if lines else "0:00"
        tag = f"{len(segments)} segments" if len(segments) > 1 else "1 segment"
        print(f"{name}: {len(lines)} cues, 0:00..{end}  ({tag})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
