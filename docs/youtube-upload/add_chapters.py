#!/usr/bin/env python3
"""Append generated chapter timecodes to each video's description.

Reads the manifest (base descriptions), rename-state.json (file -> videoId),
and chapters/<short>.txt (e.g. chapters/l05-search.txt), then rebuilds each
description as <base>\n\nChapters:\n<chapter lines> and pushes it via
videos.update. Rebuilding from the manifest base each time keeps it idempotent.

  uv run --with google-api-python-client --with google-auth-oauthlib \
    python add_chapters.py            # use --dry-run to preview
"""
import argparse
import json
import re
from pathlib import Path

from rename import get_service  # reuse the cached-token auth
from googleapiclient.errors import HttpError


def load_json(p: Path):
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def short_name(stem: str) -> str:
    m = re.search(r"l\d+.*$", stem)  # module1-rag-l05-search -> l05-search
    return m.group(0) if m else stem


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--client-secret", type=Path, default=Path("client_secret.json"))
    ap.add_argument("--token", type=Path, default=Path("token.json"))
    ap.add_argument("--manifest", type=Path, default=Path("part1-manifest.json"))
    ap.add_argument("--state", type=Path, default=Path("rename-state.json"))
    ap.add_argument("--chapters-dir", type=Path, default=Path("chapters"))
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    cfg = load_json(args.manifest)
    state = load_json(args.state)
    yt = get_service(args.client_secret, args.token)
    tags = cfg.get("tags", [])

    for v in cfg["videos"]:
        f = v["file"]
        stem = Path(f).stem
        vid = state.get(f, {}).get("videoId")
        chap = args.chapters_dir / f"{short_name(stem)}.txt"
        if not vid:
            print(f"skip (no videoId in state): {f}"); continue
        if not chap.exists():
            print(f"skip (no chapters file): {chap}"); continue

        chapters = chap.read_text(encoding="utf-8").strip()
        desc = v["description"].rstrip() + "\n\nChapters:\n" + chapters + "\n"
        print(f"{v['title']}  ({vid})  [{len(chapters.splitlines())} chapters]")
        if args.dry_run:
            print("    " + chapters.replace("\n", "\n    "));  continue
        try:
            yt.videos().update(part="snippet", body={
                "id": vid,
                "snippet": {
                    "title": v["title"],
                    "description": desc,
                    "tags": tags,
                    "categoryId": cfg.get("categoryId", "27"),
                    "defaultLanguage": cfg.get("defaultLanguage", "en"),
                },
            }).execute()
            print("    chapters added")
        except HttpError as e:
            print(f"    ERROR: {e}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
